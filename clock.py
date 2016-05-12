'''GitHub link
https://github.com/Louis-Romero/projectThree.git

Team 94
Christopher Forsythe
Marilyn Florek
Louis Romero

Summary:  This program will grab a user's 10 upcoming events through the use of Google Calendar API and alert them through SMS using TWilio API.  
Text based navigation has also been set up through the use of Google Maps Directions API and our messaging response system.  
A GUI has also been set up for the developer to see how many text messages have been sent in 24 hours.'''

import quickstart
import datetime
import messageSender
import time

#outputFile is where data about the number of textes sent in 24 hours will be stored
outputFile = open('flatFileDatabase.txt', 'a')
counterOfMessages = 0


def alerter(listReminderTimes, listDates, listStarting, listTitle, listDescription, listEnding, numElements):
	
	#currentTime gets current time and stores it as a string
    currentTime = str(datetime.datetime.now())
    #The currentTime string is now parsed for compairson
    currentDate = currentTime[0:10]
    currentTime = currentTime[11:16]
    getStuckInLoop = False
    shouldSendMessage = False
    indexNeeded = 0
	
    #This loop compares the current time to the reminder times of each event grabbed for Google calendar
    #If there is a match shouldSendMessage is made to True
    for ix in range(0, len(listReminderTimes)):
        print("current time ", currentTime, "reminder time ", listReminderTimes[ix], "List Starting", str(listDates[ix]))
        if(currentTime == listReminderTimes[ix] and str(currentDate)==str(listDates[ix])):
            indexNeeded = ix
            shouldSendMessage = True
            global counterOfMessages
            counterOfMessages = counterOfMessages + 1
            orderedPair = str(listReminderTimes[ix][0:2]) + "," + str(counterOfMessages) + "\n"
            outputFile.write(orderedPair)
			#print( "the hour", listReminderTimes[ix][0:2])

			
    #This if statment is necessary when shouldSendMessage becomes true because it the sends text message to the user
    if(shouldSendMessage):
        messageSender.sendLouisSMS(str(listDates[indexNeeded]), listTitle[indexNeeded], listStarting[indexNeeded], listEnding[indexNeeded], listDescription[indexNeeded])
        print("Message sent!")
        shouldSendMessage = False
        getStuckInLoop = True
        #A timer is used here make the application light on the hardware
        time.sleep(55)

	#This while loop is necessarry to prevent messages from being sent multiple times when only one is needed
    while(getStuckInLoop):
        currentTime = str(datetime.datetime.now())
        currentTime = currentTime[11:16]
        #print("stuck in loop")
        #print("the time", currentTime)
        #print ("the reminder time ", listReminderTimes[indexNeeded])
        if(currentTime != listReminderTimes[indexNeeded]):
			getStuckInLoop = False

	
    #A timer is used here make the application light on the hardware
    time.sleep(30)
    quickstart.main()