from tkinter import *
login=Tk()
login.geometry("300x300")
login.title("system login")

heading=Label(login,text="sign up today!",font=("gothic",15,"bold"))
heading.place(x=75,y=10)

username=Label(login,text="username",font=("Arial",12))
username.place(x=30,y=75)
user=Entry(login,font=("Ariel",12))
user.place(x=110,y=75)

password=Label(login,text="pasword",font=("Arial",12))
password.place(x=30,y=125)
word=Entry(login,font=("Ariel",12))
word.place(x=100,y=125)

Button1 = Button(login,text="sign in",font=("Calibre",15),fg="green",command=login.destroy)
Button1.place(x=50,y=175)

Button2 = Button(login,text="cancel",font=("Calibre",15),fg="red",command=login.destroy)
Button2.place(x=150,y=175)

















login.mainloop()