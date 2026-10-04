from tkinter import *
window=Tk()
window.geometry("400x600")
window.config(background="green")
window.title("Spinbox")

heading=Label(window,text="access spinbox",font=("Comic sans",10,"bold"))
heading.place(x=100,y=100)

sb1=Spinbox(window,values=("brick","plastic","wood","steel","glass"),font=("Comic sans",10,"bold"))
sb1.place(x=100,y=200)

sb2=Spinbox(window,from_=0,to=100,font=("Comic sans",10,"bold"))
sb2.place(x=120,y=300)

window.mainloop()