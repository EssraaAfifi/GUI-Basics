from tkinter import*

root = Tk() #this creates a blank window

theLabel = Label(root, text="This is hard to grab") #whenever you want to add text in Tkinter, use Label
#First part asks 'Where do you want to put it?' You place the blank window's name
#Second part asks what you want to write, and we use [text= ""]

theLabel.pack() #The third line is about the specifics of the layout
#you take whatever obeject you wanna place 'thelabel in our case', adding .pack is a short and lazy way

root.mainloop() #This is the last line, you place main window/blank window name
#this allows the window to stay continously on the screen until you decide closing it
