from tkinter import *

root = Tk()

#creating a label widget
myLabel1= Label(root, text="Welcome!")
myLabel2= Label(root, text="This app assist you with your portfolio needs")

nameValue= Entry(root, width=20)
stockTicker= Entry(root, width=20)
emailValue= Entry(root, width=20)

nameValue.insert(0, "Enter your Name: ")
emailValue.insert(0, "Enter your email: ")
stockTicker.insert(0,"Enter Stock Ticker: ")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
nameValue.grid(row=2, column=0)
emailValue.grid(row=3, column=0)
stockTicker.grid(row=4, column=0)


def myClick():
    stockName= stockTicker.get()
    myLabel3= Label(root, text= stockName)
    myLabel3.grid(row=6, column=0)

def myClick1():
    stockName= stockTicker.get()
    myLabel4= Label(root, text= stockName)
    myLabel4.grid(row=6, column=1)



# myButton = Button(root, text="Click me",state=DISABLED)
#this disables the button
myButton = Button(root, text="Click here to recieve stock updates!", padx=50, command= myClick, fg="blue", bg="red")
myButton1 = Button(root, text="Click here to STOP recieving stock updates!", padx=50, command= myClick1, fg="blue", bg="red")
#padx changes the size of the button
#command creates an action




myButton.grid(row=5, column=0)
myButton1.grid(row=5, column=1)






root.mainloop()



