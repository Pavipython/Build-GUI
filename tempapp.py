from tkinter import *
window=Tk()
window.geometry("800x500")
window.config(background="light green")
window.title("Temperature converter")

header=Label(window,text="Temperature converter from C to F",font=("Arial",20))
header.place(x=200,y=30)

Instructions=Label(window,text="Pick a random number from Celsius",font=("Arial",20))
Instructions.place(x=200,y=250)
Instructions2=Label(window,text="and convert it into Farenheit",font=("Arial",20))
Instructions2.place(x=200,y=280)

Temp=Entry(window,font=("Ariel",20))
Temp.place(x=250,y=100)

window.mainloop()
