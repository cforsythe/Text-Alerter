'''GitHub link
https://github.com/Louis-Romero/projectThree.git

Team 94
Christopher Forsythe
Marilyn Florek
Louis Romero

Summary:  This program will grab a user's 10 upcoming events through the use of Google Calendar API and alert them through SMS using TWilio API.
Text based navigation has also been set up through the use of Google Maps Directions API and our messaging response system.
A GUI has also been set up for the developer to see how many text messages have been sent in 24 hours.'''

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
from twilio.rest import TwilioRestClient
import clock #forTimeChecking

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

    listOfReminderTimes = []
    listOfTitle = []
    listOfStarting = []
    listOfDescription = []
    listOfEnding = []
    counterOfEvents = 0
    listOfNumberEvents = []
    listOfHour = []
    listOfDates = []
    go = True
    flag = False

    """Shows basic usage of the Google Calendar API.

        Creates a Google Calendar API service object and outputs a list of the next
        10 events on the user's calendar.
        """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('\nGETTING THE UPCOMING EVENTS\n')
    eventsResult = service.events().list(calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,orderBy='startTime').execute()
    events = eventsResult.get('items', [])

	#Time right now
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

        time = str(datetime.datetime.now())
        time = time[0:10]
        eventDate=syear+"-"+smonth+"-"+sday

        if shour:
            shour=int(shour)
        else:
            shour=0

        if sminute:
            sminute=sminute
        else:
            sminute=10

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
        if ehour:
            ehour=int(ehour)
        else:
            ehour=11
            am2=False
        if eminute:
            eminute = eminute
        else:
            eminute = 59

        if ehour > 12:
            ehour = ehour-12
            am2 = False
            ehour = str(ehour)

        if (am2 ==True) or (am ==True):
            ToD = " AM"
        else:
            ToD = " PM"

        description = event.get('description')
        date = event['start'].get('date','description')
        title = event['summary']
        location = event.get('location')
        woop = start

        starting ="START: "+str(shour)+":"+str(sminute)+str(ToD)
        ending ="ENDS: "+str(ehour)+":"+str(eminute)+str(ToD)
        title="EVENT: "+title

        useHoursMinutes = False
        time = str(datetime.datetime.now())
        time = time[11:16]
        counterOfEvents = counterOfEvents + 1

        if event['reminders']['useDefault'] == False:
            minutesBeforeReminder = int(event['reminders']['overrides'][0]['minutes'])
            hoursReminder = int(shour)
            minutesReminder = int(sminute)
        else:
            minutesBeforeReminder = 0
            hoursReminder=int(shour)
            minutesReminder=int(sminute)

        if(minutesBeforeReminder >= 60):
            useHoursMinutes = True
            hoursBeforeReminder = minutesBeforeReminder / 60
            minutesBeforeReminder = (minutesBeforeReminder % 60)
            print("minutes b4 reminder", minutesBeforeReminder)
        if(minutesBeforeReminder >= minutesReminder):
            minutesReminder = minutesReminder + 60
            hoursReminder = hoursReminder-1

        if(useHoursMinutes):
            useHoursMinutes = False
            minutesReminder = minutesReminder - minutesBeforeReminder
            hoursReminder = hoursReminder - hoursBeforeReminder
        else:
            minutesReminder = minutesReminder - minutesBeforeReminder
        print("the tod is ", ToD)
        print("the shour ", shour)
        print("the sminute ", sminute)
        print("minutes reminder", minutesReminder)
        if ToD==" AM" and shour == 0:
            hoursReminder = 0
            minutesReminder = minutesReminder
            flag = True

        if(minutesReminder <= 10):
            if str(minutesReminder)=="00":
                minutesReminder=30
            if(ToD == " PM"):
                hoursReminder=hoursReminder
                hoursReminder = abs(hoursReminder)
                timeToBeReminded = str(hoursReminder+12)+":0"+ str(minutesReminder)
                if hoursReminder==0:
                    hoursReminder=12
            elif(flag):
                timeToBeReminded = str(hoursReminder)+"0:"+ str(minutesReminder)
                flag = False
            elif shour >= 10:
                if shour==12 and ToD==" AM":
                    hoursReminder=shour
                    minutesReminder=str(minutesReminder)
                    minutesReminder="00"
            	timeToBeReminded = str(hoursReminder)+":"+ str(minutesReminder)
            else:
                timeToBeReminded = "0" + str(hoursReminder)+":"+ str(minutesReminder)

        else:
            #Hour Reminder
            if minutesReminder==60:
                minutesReminder=str(minutesReminder)
                minutesReminder="00"
            if(ToD == " PM"):
                hoursReminder=hoursReminder
                hoursReminder=abs(hoursReminder)
                timeToBeReminded = str(hoursReminder+12)+":"+ str(minutesReminder)
                if hoursReminder==0:
                    hoursReminder=12
            elif (flag):
                timeToBeReminded = "0"+str(hoursReminder)+"0:"+ str(minutesReminder)
                flag = False
            elif shour > 10:
                if shour==12 and ToD==" AM":
                    hoursReminder = shour
                    minutesReminder=str(minutesReminder)
                    minutesReminder="00"
            	timeToBeReminded = str(hoursReminder)+":"+ str(minutesReminder)
            else:
                timeToBeReminded = "0" + str(hoursReminder)+":"+ str(minutesReminder)



        listOfReminderTimes.append(timeToBeReminded)
        listOfStarting.append(starting)
        listOfTitle.append(title)
        listOfDescription.append(description)
        listOfEnding.append(ending)
        listOfDates.append(eventDate)

        '''Print code for testing'''
        print(starting)
        print(title)
        if description:
            description ="Description: " + description
            print(description)

        elif (str(event.get('description')) == "None"):
            description = "No Description Entered"
            print(description)
        if location:
            location ="Location: " + location
            print(location)
        print(ending)

        print(" ")

        print (minutesBeforeReminder)
        #print("Minutes to be reminded before Event", minutesBeforeReminder)
        print("calculated time ", timeToBeReminded + ToD)

        print ("the counterOfEvents ", counterOfEvents)
        listOfNumberEvents.append(counterOfEvents)
        print(" ")
    else:
        reminder = "\n\nNo Reminder"

    clock.alerter(listOfReminderTimes, listOfDates, listOfStarting, listOfTitle, listOfDescription, listOfEnding, counterOfEvents)

if __name__ == '__main__':
    main()
