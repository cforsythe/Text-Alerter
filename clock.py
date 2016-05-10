import quickstart
import datetime
import messageSender

def alerter(listReminderTimes, listStarting, listTitle, listDescritption, listEnding, numElements):
	shouldShiftLeft = False
	print("Beginning of function")
	#while(True):
	time = str(datetime.datetime.now())
	time = time[11:16]
	getStuckInLoop = False
	shouldSendMessage = False

	#for 0 in range(0, numElements):
    #print(time , listReminderTimes[0])
	if(time == listReminderTimes[0]):
		shouldSendMessage = True

	if(shouldSendMessage):
		messageSender.sendLouisSMS(listTitle[0], listStarting[0], listEnding[0], listDescritption[0])
		#print("Message sent!")
		shouldSendMessage = False
		getStuckInLoop = True

	while(getStuckInLoop):
		time = str(datetime.datetime.now())
		time = time[11:16]
		print("stuck in loop")
		print("the time", time)
		print ("the reminder time ", listReminderTimes[0])
		if(time != listReminderTimes[0]):
			getStuckInLoop = False



	quickstart.main()
        
	print("End of function")
