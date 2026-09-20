from tkinter import *
window=Tk()
window.geometry("400x600")
window.config(background="blue")
window.title("Menu Bar")

menubar=Menu(window)
# it creates the menu on the window
window.config(menu=menubar)
# places the menu bar on the screen
filemenu=Menu(menubar,tearoff=0)
# it will create a file menu, tearoff will give a dropdown list
menubar.add_cascade(label="file",menu=filemenu)
# it will add a file menu inside the main menu bar
filemenu.add_command(label="new file",command=None)
filemenu.add_command(label="new folder",command=None)
filemenu.add_separator()
filemenu.add_command(label="open file",command=None)
filemenu.add_command(label="open folder",command=None)
filemenu.add_separator()
filemenu.add_command(label="save",command=None)
filemenu.add_command(label="delete",command=None)
filemenu.add_separator()
filemenu.add_command(label="exit",command=window.destroy)
# add and change new commands in file menu


editmenu=Menu(menubar,tearoff=0)
# it will create a file menu, tearoff will give a dropdown list
menubar.add_cascade(label="edit",menu=editmenu)
# it will add a file menu inside the main menu bar
editmenu.add_command(label="cut",command=None)
editmenu.add_command(label="copy",command=None)
editmenu.add_command(label="paste",command=None)
editmenu.add_command(label="undo",command=None)
editmenu.add_separator()
editmenu.add_command(label="replace file",command=None)
editmenu.add_command(label="find file",command=None)
editmenu.add_separator()
editmenu.add_command(label="check folder",command=None)

window.mainloop()