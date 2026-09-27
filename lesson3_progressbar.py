from tkinter.ttk import *
from tkinter import *
import time

window=Tk()
window.geometry("800x400")
window.config(background="gray")

progressbar=Progressbar(window,orient=HORIZONTAL,length=500)
# inputs bar in window, can customize bar. 
def bar():
    progressbar['value']=20
    window.update_idletasks()
    # starting value of 20
    time.sleep(2)
    progressbar['value']=40
    window.update_idletasks()
    time.sleep(2)
    progressbar['value']=60
    window.update_idletasks()
    time.sleep(2)
    progressbar['value']=70
    window.update_idletasks()
    time.sleep(2)
    progressbar['value']=90
    window.update_idletasks()
    time.sleep(2)
    progressbar['value']=100
    window.update_idletasks()
    # To end value 100
    time.sleep(2)
progressbar.place(x=200,y=100)

start=Button(window,text="start",font=("Calibre",15),fg="green",command=bar)
start.place(x=50,y=175)








window.mainloop()


