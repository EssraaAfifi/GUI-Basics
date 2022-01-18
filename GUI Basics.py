from tkinter import *

def change_text ():
    my_label.config(text='Hello World')

window = Tk()
window.title ('First GUI')

my_label = Label (window, width=25, height=0, text='')
my_label.grid (row=0, column=0)

my_button = Button (window, text='Press Me', width=10, command=change_text)
my_button.grid (row=1, column=0)

window.mainloop()
