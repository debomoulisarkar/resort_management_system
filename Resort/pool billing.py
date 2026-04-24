import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ast
import csv
import random
import mysql.connector as mc

#to create opening window
display=Tk()
display.title('Billing Page')
display.geometry('925x500+300+200')
display.configure(bg='#fff')
display.resizable(False,False)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#mail and password check
def pool_bill():
    lst=[]
    people=user.get()
    days=code.get()
    hotel=hotelname.get()
    customer=customer_id.get()
    cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
    if cn.is_connected()==False:
        print('connection is not created')
    else:
        print('connection is successful')
        if people!='' and days!='' and hotel!='' and customer!='':
            cr=cn.cursor()   
            command='use resort;'
            cr.execute(command)

            if hotel=='Borcelle Resorts' or hotel=='Borcelle':
                hotel_id=1
                st1="insert into Pool values({},{},{},{},{});".format(customer,hotel_id,people,days,'NULL')
                cr.execute(st1)
                cn.commit()
            if hotel=="Lenora's Resorts" or hotel=="Lenoras Resorts":
                hotel_id=2
                st1="insert into Pool values({},{},{},{},{});".format(customer,hotel_id,people,days,'NULL')
                cr.execute(st1)
                cn.commit()
            if hotel=="Kallidan Normann":
                hotel_id=3
                st1="insert into Pool values({},{},{},{},{});".format(customer,hotel_id,people,days,'NULL')
                cr.execute(st1)
                cn.commit()
            if hotel=="Margot Roberts" or hotel=="Margot Roberts Resorts":
                hotel_id=4
                st1="insert into Pool values({},{},{},{},{});".format(customer,hotel_id,people,days,'NULL')
                cr.execute(st1)
                cn.commit()

            st="update Pool set Price=(Number_of_people*Number_of_days)*500;"
            cr.execute(st)
            cn.commit()
            cn.close()

            messagebox.showinfo('Billing','Successfully booked')
        else:
            messagebox.showinfo('Invalid','Please enter valid number of people or days')
        
#inserting an image
img1=PhotoImage(file='pool.png')
Label(display,image=img1,border=0).place(x=0,y=-10)
frame1=Frame(display,width=390,height=410)
frame1.place(x=35,y=50)
img2=PhotoImage(file='pool rate.png')
Label(frame1,image=img2,border=0).place(x=-10,y=0)
################################################
#inserting text box number of people
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'No. of people')
user=Entry(width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
user.place(x=550,y=180)
user.insert(0,'No. of people')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

###############################################

#inserting text box number of days
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'No. of days')
code=Entry(width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
code.place(x=550,y=210)
code.insert(0,'No. of days')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

##############################################

#inserting text box hotel name
def on_enter(e):
    hotelname.delete(0,'end')
def on_leave(e):
    name=hotelname.get()
    if name=='':
        hotelname.insert(0,'Hotel name')
hotelname=Entry(width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
hotelname.place(x=550,y=240)
hotelname.insert(0,'Hotel name')
hotelname.bind('<FocusIn>',on_enter)
hotelname.bind('<FocusOut>',on_leave)

##############################################

#inserting text box customer id
def on_enter(e):
    customer_id.delete(0,'end')
def on_leave(e):
    name=customer_id.get()
    if name=='':
        customer_id.insert(0,'Customer ID')
customer_id=Entry(width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
customer_id.place(x=550,y=270)
customer_id.insert(0,'Customer ID')
customer_id.bind('<FocusIn>',on_enter)
customer_id.bind('<FocusOut>',on_leave)

##############################################

#confirm pool button
Button(width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=pool_bill).place(x=560,y=300)

display.mainloop()

