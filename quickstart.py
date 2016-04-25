#http://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
from __future__ import print_function
import httplib2
import os
from pprint import pprint

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from twilio.rest import TwilioRestClient
import datetime
import time
from time import strftime

currentTime = datetime.datetime.now()
print (str(currentTime))


def sendSMS(subject, body, txt, txt2):

    account_sid = "AC6720dab93f0bfd755e38d5194e80889a"
    auth_token  = "cd0a979c74fdecb33d478f3ef2eca1bb"
    client = TwilioRestClient(account_sid, auth_token)

    if body:
        message = client.messages.create(to="+18317103519",
                                 from_="+12014821837", body=[" \n"+str(subject)+str(body)+str(txt)+str(txt2)])
    else:
        message = client.messages.create(to="+18317103519",
                                         from_="+12014821837", body=[" \n"+str(subject)+str(txt)+str(txt2)])
    print("Message sent")

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
    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(

        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
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
        #date.strftime('%m/%d/%Y')
        title = event['summary']
        location = event.get('location')
        woop = start
            #reminder = event['reminders']['overrides'][0]['minutes']
        '''^^^ The line above works but only for the first event and I'm not sure why'''
        #reminder = event['reminders']
        i+=i

        starting ="\nStarts: "+smonth+"/"+sday+"/"+syear+" "+shour+":"+sminute+ToD
        ending ="\nEnds: "+emonth+"/"+eday+"/"+eyear+" "+ehour+":"+eminute+ToD+"\n"
        title="\nEvent: "+title
        
        '''Print code for testing'''
        print("")
        #print(reminder)
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
        sendSMS(starting,title,description,ending)

if __name__ == '__main__':
    main()