'''GitHub link
https://github.com/Louis-Romero/projectThree.git

Team 94
Christopher Forsythe
Marilyn Florek
Louis Romero

Summary:  This program will grab a user's 10 upcoming events through the use of Google Calendar API and alert them through SMS using TWilio API.  
Text based navigation has also been set up through the use of Google Maps Directions API and our messaging response system.  
A GUI has also been set up for the developer to see how many text messages have been sent in 24 hours.'''

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

#Louis' Authenticating information
def sendLouisSMS(date, subject, body, txt, txt2):

    account_sid = "AC6720dab93f0bfd755e38d5194e80889a"
    auth_token  = "cd0a979c74fdecb33d478f3ef2eca1bb"
    client = TwilioRestClient(account_sid, auth_token)

    if body:
        message = client.messages.create(to="+18317103519",
                                 from_="+12014821837", body=["\nEvent "+" Date: "+str(date)+" \n"+str(subject) +"\n"+str(body) +"\n"+str(txt)+"\nDescription: "+str(txt2)+"\n"])
    else:
        message = client.messages.create(to="+18317103519",
                                         from_="+12014821837", body=["\nEvent "+" Date: "+str(date)+" \n"+str(subject)+"\n"+str(txt)+"\nDescription: "+str(txt2)+"\n"])
    print("Message sent")

#Christopher's Authenticating information
def sendChristopherSMS(date,subject,body,txt,txt2):
    account_sid = "AC8f945e03fc773f6bdc7853a22ff48bf5"
    auth_token  = "84c198d180304aad6a42ab455d50b8aa"
    client = TwilioRestClient(account_sid, auth_token)

    if body:
        message = client.messages.create(to="+12099183937",
                                 from_="+12014821669", body=["\nEvent "+" Date: "+str(date)+" \n"+str(subject) +"\n"+str(body) +"\n"+str(txt)+"\nDescription: "+str(txt2)+"\n"])
    else:
        message = client.messages.create(to="++12099183937",
                                         from_="+12014821669", body=["\nEvent "+" Date: "+str(date)+" \n"+str(subject)+"\n"+str(txt)+"\nDescription: "+str(txt2)+"\n"])
    print("Message sent")

#Marilyn's Authenticating information
def sendMarilynSMS(date,subject,body,txt,txt2):
    account_sid = "ACb6cafa55f004c423ea15a648e125821f"
    auth_token  = "12369dc0952d77177afea415a2eef011"
    client = TwilioRestClient(account_sid, auth_token)

    if body:
        message = client.messages.create(to="+14088405448",
                                 from_="+12014821965", body=["\nEvent "+" Date: "+str(date)+" \n"+str(subject) +"\n"+str(body) +"\n"+str(txt)+"\nDescription: "+str(txt2)+"\n"])
    else:
        message = client.messages.create(to="+14088405448",
                                         from_="+12014821965", body=["\nEvent "+" Date: "+str(date)+" \n"+str(subject)+"\n"+str(txt)+"\nDescription: "+str(txt2)+"\n"])
    print("Message sent")