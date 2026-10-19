from tkinter import *
window=Tk()
window.geometry("1000x800")
window.config(background="light blue")
window.title("food order app")

def calculator():
    price=0
# The user takes fruit from the spinbox can be obtained using "get()" function 
    food=sb1.get()
    if food=="pasta":
        price==2
    elif food=="salad":
        price==1
    elif food=="steak":
        price==4
    elif food=="shrimp":
        price==3

    beverage=sb3.get()
    if beverage=="water":
        price==2
    elif beverage=="soda":
        price==1
    elif beverage=="tea":
        price==3
    elif beverage=="coffee":
        price==3

    dessert=sb5.get()
    if dessert==




Email = Label(window,text="Email",font=("Arial",20))
Email.place(x=35,y=50)
EmailEntry=Entry(window,font=("Ariel",20))
EmailEntry.place(x=140,y=50)

Password= Label(window,text="Password",font=("Arial",20))
Password.place(x=35,y=120)
PasswordEntry=Entry(window,font=("Ariel",20))
PasswordEntry.place(x=190,y=120)


food=Label(window,text="what type of food? pasta, salad, steak, shrimp",font=("Comic sans",20))
food.place(x=80,y=200)
sb1=Spinbox(window,values=("pasta","salad","steak","shrimp"),font=("Comic sans",20))
sb1.place(x=20,y=240)
sb2=Spinbox(window,from_=0,to=10,font=("Comic sans",20))
sb2.place(x=400,y=240)

beverage=Label(window,text="What type of beverage? water, soda, tea, coffee",font=("Comic sans",20))
beverage.place(x=80,y=360)
sb3=Spinbox(window,values=("water","soda","tea","coffee"),font=("Comic sans",20))
sb3.place(x=20,y=400)
sb4=Spinbox(window,from_=0,to=10,font=("Comic sans",20))
sb4.place(x=400,y=400)

dessert=Label(window,text="Lastly what type of dessert? icecream, yogurt, jelly, cupcake",font=("Comic sans",20))
dessert.place(x=80,y=560)
sb5=Spinbox(window,values=("icecream", "yogurt", "jelly", "cupcake"),font=("Comic sans",20))
sb5.place(x=20,y=600)
sb6=Spinbox(window,from_=0,to=10,font=("Comic sans",20))
sb6.place(x=400,y=600)

# total
# total

# totalprice
# totalprice

window.mainloop()
