import tkinter as tk
from tkinter import *
from tkinter import messagebox

#to create opening window
window=Tk()
window.title('Parking Service')
window.geometry('925x500+300+200')
window.configure(bg='black')
window.resizable(False,False)

#inserting an image
img1=PhotoImage(file='parking.png')
Label(window,image=img1,border=0).place(x=270,y=3)

window.mainloop()


