
from __future__ import print_function
import httplib2
import os
from pprint import pprint

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime

import time
from time import strftime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

from twilio.rest import TwilioRestClient

def sendSMS(txt,subject,body,txt2):
    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "ACb6cafa55f004c423ea15a648e125821f"
    auth_token  = "12369dc0952d77177afea415a2eef011"
    client = TwilioRestClient(account_sid, auth_token)

    if body:
        message = client.messages.create(to="+14088405448",
                                 from_="+12014821965", body=[" \n"+subject+body+txt+txt2])
    else:
        message = client.messages.create(to="+14088405448",
                                         from_="+12014821965", body=[" \n"+subject+txt+txt2])
    print("Message sent")


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming events')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=2, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    '''Time right now'''
    

    i=0
    
    if not events:
        print('No upcoming events found.')
    for event in events:
        '''Start time code'''
        start = event['start'].get('dateTime', event['start'].get('date','description'))
        syear = start[0:4]
        smonth = start[5:7]
        sday=start[8:10]
        shour=start[11:13]
        sminute=start[14:16]
        shour=int(shour)
        am = True
        if shour > 12:
            shour = shour-12
            am = False
        shour = str(shour)

        '''End Time code'''
        am2=True
        end = event['end'].get('dateTime',event['end'].get('date'))
        eyear = end[0:4]
        emonth = end[5:7]
        eday=end[8:10]
        ehour=end[11:13]
        eminute=end[14:16]
        ehour=int(ehour)
        if ehour > 12:
            ehour = ehour-12
            am2 = False
        ehour = str(ehour)

        if am2 ==True:
            ToD = "am"
        else:
            ToD = "pm"

        description = event.get('description')
        date = event['start'].get('date','description')
        title = event['summary']
        location = event.get('location')
        woop = start
        if event['reminders']['useDefault'] == False:
            reminder = event['reminders']['overrides'][0]['minutes']
        else:
            reminder = "No Reminder"
        print(reminder)
        starting ="\nStarts: "+smonth+"/"+sday+"/"+syear+" "+shour+":"+sminute+ToD
        ending ="\nEnds: "+emonth+"/"+eday+"/"+eyear+" "+ehour+":"+eminute+ToD+"\n"
        title="\nEvent: "+title
        
        '''Print code for testing'''
        print("")
        print(starting)
        print(title)
        if description:
            description ="\nDescription: \n" + description
            print(description)
        if location:
            location ="\nLocation: " + location
            print(location)
        print(ending)
        print(datetime.datetime.now())
        print(" ")

        '''Make sure you change the phone # before testing the txt part'''
        #sendSMS(starting,title,description,ending)


if __name__ == '__main__':
    main()