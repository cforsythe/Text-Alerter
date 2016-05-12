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
