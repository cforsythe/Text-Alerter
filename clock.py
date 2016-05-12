import quickstart
import datetime
import messageSender
import time


counterOfMessages = 0
counterOfMessagesList = []
hourOfMessagesList = []
outputFile = open('flatFileDatabase.txt', 'a')

def alerter(listReminderTimes, listDates, listStarting, listTitle, listDescription, listEnding, numElements):
	
	
    print("Beginning of function")
	#while(True):
    currentTime = str(datetime.datetime.now())
    currentDate = currentTime[0:10]
    currentTime = currentTime[11:16]
    getStuckInLoop = False
    shouldSendMessage = False
    indexNeeded = 0
	
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

			

    if(shouldSendMessage):
        messageSender.sendLouisSMS(str(listDates[indexNeeded]), listTitle[indexNeeded], listStarting[indexNeeded], listEnding[indexNeeded], listDescription[indexNeeded])
        print("Message sent!")
        shouldSendMessage = False
        getStuckInLoop = True
		#time.sleep(55)

	
    while(getStuckInLoop):
        currentTime = str(datetime.datetime.now())
        currentTime = currentTime[11:16]
        print("stuck in loop")
        print("the time", currentTime)
        print ("the reminder time ", listReminderTimes[indexNeeded])
        if(currentTime != listReminderTimes[indexNeeded]):
			getStuckInLoop = False

	

	#time.sleep(30)
    quickstart.main()

    print("End of function")