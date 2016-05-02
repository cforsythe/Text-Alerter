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
                                 from_="+12014821837", body=[" \n"+str(subject) +"\n"+str(body) +"\n"+str(txt)+"\n"+str(txt2)+"\n"])
    else:
        message = client.messages.create(to="+18317103519",
                                         from_="+12014821837", body=[" \n"+str(subject)+"\n"+str(txt)+"\n"+str(txt2)+"\n"])
    print("Message sent")

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None