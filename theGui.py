'''GitHub link
https://github.com/Louis-Romero/projectThree.git

Team 94
Christopher Forsythe
Marilyn Florek
Louis Romero

Summary:  This program will grab a user's 10 upcoming events through the use of Google Calendar API and alert them through SMS using TWilio API.  
Text based navigation has also been set up through the use of Google Maps Directions API and our messaging response system.  
A GUI has also been set up for the developer to see how many text messages have been sent in 24 hours.'''

from Tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

class Gui:
	def __init__(self, master):
		self.label = Label(master, text = "DATA")
		self.label.grid(row = 0, column = 0, columnspan = 2)
		Button(master, text = "Graph1",
		command = self.graph1).grid(row = 1, column = 0)
	def graph1(self):
		fig = plt.figure()
		ax1 = fig.add_subplot(1,1,1)
		def animate(i):
		    pullData = open("flatFileDatabase.txt","r").read()
		    dataArray = pullData.split('\n')
		    xar = []
		    yar = []
		    for eachLine in dataArray:
		        if len(eachLine)>1:
		            x,y = eachLine.split(',')
		            xar.append(int(x))
		            yar.append(int(y))
		    ax1.clear()
		    ax1.plot(xar,yar)
		ani = animation.FuncAnimation(fig, animate, interval=1000)
		plt.show()
		
def main():
	root = Tk()
	app = Gui(root)
	root.mainloop()

if __name__ == '__main__': 
	main()
