from tkinter.ttk import *
from tkinter import *
import time

window=Tk()
window.geometry("400x900")
window.config(background="light green")

loadbar=Progressbar(window,orient=VERTICAL,length=650)
def bar():
    loadbar['value']=0
    window.update_idletasks()
    time.sleep(1)
    loadbar['value']=10
    window.update_idletasks()
    time.sleep(1)
    loadbar['value']=20
    window.update_idletasks()
    time.sleep(1)
    loadbar['value']=50
    window.update_idletasks()
    time.sleep(1)
    loadbar['value']=70
    window.update_idletasks()
    time.sleep(1)
    loadbar['value']=85
    window.update_idletasks()
    time.sleep(1)
    loadbar['value']=97
    window.update_idletasks()
    time.sleep(1)
    loadbar['value']=100
    window.update_idletasks()
    time.sleep(1)
loadbar.place(x=200,y=100)

start=Button(window,text="start",font=("gothic",18),fg="blue",command=bar)
start.place(x=50,y=175)








window.mainloop()