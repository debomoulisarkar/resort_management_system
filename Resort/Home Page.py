#Home Page using Tkinter
from tkinter import *
from tkinter import messagebox
import ast

#to create opening window
screen=Tk()
screen.title('Home Page')
screen.geometry('925x500+300+200')
screen.configure(bg='#fff')
screen.resizable(False,False)

#inserting an image
img=PhotoImage(file='home page.png')
Label(screen,image=img,border=0).place(x=-20,y=-30)

#inserting button for customer and hotel staff
Button(width=20,pady=7,text='Customer', bg='dark green',fg='white',border=0).place(x=340,y=325)
Button(width=20,pady=7,text='Hotel', bg='dark green',fg='white',border=0).place(x=515,y=325)

