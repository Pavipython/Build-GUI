from tkinter import * 
window=Tk()
window.geometry("400x400")
window.config(background="red",border=10,relief="raised")
window.title("my first gui app")

def abc():
    value=a.get()
    Label(window,text=value).place(x=200,y=200)

Label(window,text="my first gui app",fg="black",bg="red",font=("comic sans",24,"bold")).pack(pady=20)
a=Entry(window)
a.pack(pady=20,side="left",anchor="s")
Button(window,text="submit",bg="blue",width=30,height=3,command=abc,relief="sunken",border=10).pack(pady=20)
a.config(bg="orange")




window.mainloop()
