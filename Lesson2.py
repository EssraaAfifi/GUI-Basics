from tkinter import *

root=Tk()#This is the Basic Frame work [IMPORTANT]

#Frame, and invisible rectangle that can be a basic layout, place things in
topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM) #Inside the brackets, it tells the compiler the parameter/where exactly to put it

button1 = Button(topframe, text="PRESS ME!", fg="red")#making a widget button, basic rectangle to press on
#First part indicates parameter
#second part indicates 'What text do you want to show up in the button'
#Third part 'fg' [stands for 'foreground'] sets the colour of the "text" not button- it is optional
button2 = Button(topframe, text="WHY HIM! PRESS ME!", fg="blue")
button3 = Button(bottomframe, text="YOU IDIOT! PRESS ME!", fg="green")
button4 = Button(bottomframe, text="WHY AM I LAST?!", fg="purple")

#Finally we tell the compiler to show these buttons on the window
#by default, whenever you use pack, theyre packed above eachother, (with empty brackets)
#if you want the button e.g. to appear onthe left, 'side=LEFT
button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)

root.mainloop()#This too is the Basic Frame work [IMPORTANT]
