import quickstart
import datetime
import messageSender

def alerter(listReminderTimes, listStarting, listTitle, listDescritption, listEnding, numElements):
	shouldShiftLeft = False
	print("Beginning of function")
	while(True):
		time = str(datetime.datetime.now())
		time = time[11:16]
		for ix in range(0, numElements):
			#print(time , listReminderTimes[ix])
			if(time == listReminderTimes[ix]):
				print("alert")
				if(numElements == 1):
					messageSender.sendSMS(listTitle[ix], listStarting[ix], listEnding[ix], listDescritption[ix])
					numElements = numElements - 1
					print("num Elements", numElements)

				elif(numElements == 2):
					messageSender.sendSMS(listTitle[ix], listStarting[ix], listEnding[ix], listDescritption[ix])
					listReminderTimes[ix] = listReminderTimes[ix+1]
					listTitle[ix] = listTitle[ix+1]
					listStarting[ix] = listStarting[ix+1]
					listEnding[ix] = listEnding[ix+1]
					listDescritption[ix] = listDescritption[ix+1]
					numElements = numElements - 1
					print("num Elements", numElements)

				elif(numElements > 2 and numElements <= 10):
					messageSender.sendSMS(listTitle[ix], listStarting[ix], listEnding[ix], listDescritption[ix])
					listReminderTimes[ix] = "0:00"
					numElements = numElements - 1
					shouldShiftLeft = True
					print("num Elements", numElements)

		if(shouldShiftLeft):
			for jx in range(0, numElements):
				listReminderTimes[jx] = listReminderTimes[jx+1]
				listTitle[jx] = listTitle[jx+1]
				listStarting[jx] = listStarting[jx+1]
				listEnding[jx] = listEnding[jx+1]
				listDescritption[jx] = listDescritption[jx+1]
			shouldShiftLeft = False
        
	print("End of function")
