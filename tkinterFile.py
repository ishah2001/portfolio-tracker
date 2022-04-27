from tkinter import *

root = Tk()

#creating a label widget
myLabel1= Label(root, text="Hello World!")
myLabel2= Label(root, text="Please Select the Ticker: ")

#showing it onto the screen

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
e= Entry(root, width=20,bg="blue")

#entry line: user can enter anything
e.grid(row=4, column=0)
e.insert(0, "Enter your Name: ")


def myClick():
    stockTicker= e.get()
    myLabel3= Label(root, text=stockTicker)
    myLabel3.grid(row=3, column=0)



# myButton = Button(root, text="Click me",state=DISABLED)
#this disables the button
myButton = Button(root, text="Click me", padx=50, command= myClick, fg="blue", bg="red")
#padx changes the size of the button
#command creates an action




myButton.grid(row=2, column=0)





root.mainloop()



