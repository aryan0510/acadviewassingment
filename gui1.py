'''
#1
from tkinter import *
root =Tk()
hwl=Label(root,text='hello world')
hwl.pack()
button=Button(root,text='exit',command=root.destroy)
button.pack()
root.mainloop()

#2
from tkinter import *
root =Tk()
hwl=Label(root,text='hello world')
hwl.pack()
button=Button(root,text='exit',command=root.destroy)
button.pack()
li=Label(root)
def press():
    li.config(text='hello')

button1=Button(root,text='show_text',command=press).pack()
li.pack()
root.mainloop()
'''
#3
from tkinter import *
window = Tk() 
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
lbl = Label(window,text='hello')
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
def clicked():
    res =  txt.get()
    lbl.configure(text= res)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()

#4
from tkinter import *
window = Tk() 
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
lbl = Label(window,text='hello')
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
def clicked():
    res =  txt.get()
    lbl.configure(text= res)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
