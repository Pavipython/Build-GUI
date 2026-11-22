from tkinter import *

from time import strftime
# string format time

window=Tk()
window.geometry("300x150")
window.config(background="green")
window.title("Digital clock")

def time():
    timeformat=strftime("%I:%M:%S:%p")
    timelabel.config(text=timeformat)
    timelabel.after(1000,time)
    # update every 1000ms = 1 second

clock=Label(window,font=("Ariel",20),text="Digital clock")
clock.place(x=75,y=0)

timelabel=(Label(window,font=("Ariel",30),fg="blue"))
timelabel.place(x=50,y=100)

time()

window.mainloop()