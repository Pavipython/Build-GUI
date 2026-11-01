from tkinter import *
window=Tk()
window.geometry("800x500")
window.config(background="light green")
window.title("Temperature converter")

def CtoF():
    Celsius=int(Temp.get())
    Farenheit=Celsius*(9/5)+32
    Answer.config(text="conversion of Celsius to Farenheit is: "+str(Farenheit))

header=Label(window,text="Temperature converter from C to F",font=("Arial",20))
header.place(x=200,y=30)

Instructions=Label(window,text="Pick a random number from Celsius",font=("Arial",20))
Instructions.place(x=200,y=250)
Instructions2=Label(window,text="and convert it into Farenheit",font=("Arial",20))
Instructions2.place(x=200,y=280)

Temp=Entry(window,font=("Ariel",20))
Temp.place(x=250,y=100)

Answer=Label(window,font=("Ariel",20),text="°F to °C = ")
Answer.place(x=200,y=165)

Submit=Button(window,text="submit",font=("Calibre",20),command=CtoF)
Submit.place(x=350,y=350)

window.mainloop()
