from tkinter import *
# Graphical library of python we are importing
window = Tk()
# Creating the window of the output
window.geometry("600x600")
# defining the size of the window
window.title("My Football Academy")
# inputting window title
window.config(background="light green")
# Inputting window background colour

heading = Label(window,text="personal details form",font=("Comic sans",40,"bold"),fg="blue")
# display a text, font and foreground on window
heading.place(x=40,y=50)
# text placement

Name = Label(window,text="Name",font=("Arial",30))
Name.place(x=30,y=230)
NameEntry=Entry(window,font=("Ariel",20))
NameEntry.place(x=170,y=230)
# display Name
Age = Label(window,text="Age",font=("Arial",30))
Age.place(x=30,y=330)
AgeEntry=Entry(window,font=("Ariel",20))
AgeEntry.place(x=130,y=330)
# display Age
Email = Label(window,text="Email",font=("Ariel",30))
Email.place(x=30,y=430)
EmailEntry = Entry(window,font=("Arial",20))
EmailEntry.place(x=150,y=430)
# display Email

SubmitButton = Button(window,text="submit",font=("Calibre",30),command=window.destroy)
SubmitButton.place(x=230,y=500)
# windows.destroy closes the window fully, by clicking on the submit button




window.mainloop()
# update window to stay on screen