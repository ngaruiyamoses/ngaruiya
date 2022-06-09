#!/usr/bin/python

############
#
# name : Moses Ngaruiya
# gui_examples using tkinter
# date : 7/6/2022
###########

from tkinter import *

window = Tk()
window.title("welcome to my app")
window.configure(bg='blue')
window.geometry("700x600")
t_name = Label(window, text="MOSES", font=("Arial Bold", 10))
f_name = Label(window, text="NGARUIYA", font=("Arial Bold", 10))
s_name = Label(window, text="WAWERU", font=("Arial Bold", 10))
t_name.grid(column = 20 , row = 30)
f_name.grid(column = 20 , row = 40)
s_name.grid(column = 20 , row = 50)
btn = Button(window,text = "click me" , bg='green', fg='red', font=("Arial Bold", 30))
btn.grid(column = 120 , row= 150)

txt_box = Entry(window ,width=40)
txt_box.grid(column = 30 , row = 30)
txt_box = Entry(window ,width=40)
txt_box.grid(column = 30 , row = 40)

txt_box = Entry(window ,width=40)
txt_box.grid(column = 30 , row = 50)

def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop Up Window")
    top.configure(bg= 'green')
    msg= Label(top, text= "welcome to the pop up", font=('mistral 18'))
#command= open_popup().pack()
window.mainloop()