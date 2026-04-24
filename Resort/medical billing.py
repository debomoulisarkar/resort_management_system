import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ast
import csv
import random
import mysql.connector as mc
from tkinter.messagebox import showinfo

#to create opening window
window=Tk()
window.title('Billing Page')
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)

global customer
customer=1
global booking
booking=2
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def wheelchair():
    #to create opening window
    display=Toplevel()
    display.title('Billing Page')
    display.geometry('925x500+300+200')
    display.configure(bg='#fff')
    display.resizable(False,False)

    #inserting an image
    img1=PhotoImage(file='wheelchair.png')
    Label(display,image=img1,border=0).place(x=25,y=7)

    def wheelchairbill():
        people=code.get()
        days=user.get()
        cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
        if cn.is_connected()==False:
            print('connection is not created')
        else:
            print('connection is successful')
            if people!='' and days!='' and customer!='':
                cr=cn.cursor()   
                command='use resort;'
                cr.execute(command)
                hotel_id=1
                order=1
                
                st1="insert into Medical values({},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,people,days,'NULL','NULL','NULL','NULL')
                cr.execute(st1)
                cn.commit()
                
                st2="update Medical set Wheelchair=(Number_of_people*Number_of_days)*700 where Orders={};".format(order)
                cr.execute(st2)
                cn.commit()

                st3="select COALESCE(sum(Bed),0)+ COALESCE(sum(Wheelchair),0)+ COALESCE(sum(Doctor),0) from Medical as Total where Booking_ID={};".format(booking)
                cr.execute(st3)
                data=cr.fetchone()

                st4="set SQL_SAFE_UPDATES=0;"
                cr.execute(st4)
                cn.commit()
                        
                for i in data:
                    st5="update Medical set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                    cr.execute(st5)
                    cn.commit()
                    cn.close()

                messagebox.showinfo('Billing','Successfully booked')
            else:
                messagebox.showinfo('Invalid','Please enter valid number of people or days')

    #inserting text box number of people
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Number of People')
    code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    code.place(x=150,y=240)
    code.insert(0,'Number of People')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    #inserting text box number of days
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Number of Days')
    user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    user.place(x=150,y=200)
    user.insert(0,'Number of Days')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    #####################################################################
    
    #for billing button
    Button(display,width=20,pady=7,text='Confirm Booking', bg='turquoise',fg='white',border=0,command=wheelchairbill).place(x=190,y=330)

    label1=Label(display,text="click here",fg='black',font=('Microsoft YaHei UI Light',9))
    label1.place(x=235,y=365)

    display.mainloop()

def bed():
    #to create opening window
    display=Toplevel()
    display.title('Billing Page')
    display.geometry('925x500+300+200')
    display.configure(bg='#fff')
    display.resizable(False,False)

    #inserting an image
    img1=PhotoImage(file='bed.png')
    Label(display,image=img1,border=0).place(x=25,y=7)

    def bedbill():
        people=code.get()
        days=user.get()
        cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
        if cn.is_connected()==False:
            print('connection is not created')
        else:
            print('connection is successful')
            if people!='' and days!='' and customer!='':
                cr=cn.cursor()   
                command='use resort;'
                cr.execute(command)
                hotel_id=1
                order=2
                
                st1="insert into Medical values({},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,people,days,'NULL','NULL','NULL','NULL')
                cr.execute(st1)
                cn.commit()
                
                st2="update Medical set Bed=(Number_of_people*Number_of_days)*900 where Orders={};".format(order)
                cr.execute(st2)
                cn.commit()

                st3="select COALESCE(sum(Bed),0)+ COALESCE(sum(Wheelchair),0)+ COALESCE(sum(Doctor),0) from Medical as Total where Booking_ID={};".format(booking)
                cr.execute(st3)
                data=cr.fetchone()

                st4="set SQL_SAFE_UPDATES=0;"
                cr.execute(st4)
                cn.commit()
                        
                for i in data:
                    st5="update Medical set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                    cr.execute(st5)
                    cn.commit()
                    cn.close()


                messagebox.showinfo('Billing','Successfully booked')
            else:
                messagebox.showinfo('Invalid','Please enter valid number of people or days')


    #inserting text box number of people
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Number of People')
    code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    code.place(x=550,y=240)
    code.insert(0,'Number of People')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    #inserting text box number of days
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Number of Days')
    user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    user.place(x=550,y=200)
    user.insert(0,'Number of Days')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    #####################################################################
    
    #for billing button
    Button(display,width=20,pady=7,text='Confirm Booking', bg='turquoise',fg='white',border=0,command=bedbill).place(x=590,y=330)

    label1=Label(display,text="click here",fg='black',font=('Microsoft YaHei UI Light',9))
    label1.place(x=630,y=365)

    display.mainloop()
    
def doctor():
    #to create opening window
    display=Toplevel()
    display.title('Billing Page')
    display.geometry('925x500+300+200')
    display.configure(bg='#fff')
    display.resizable(False,False)

    #inserting an image
    img1=PhotoImage(file='doctor.png')
    Label(display,image=img1,border=0).place(x=25,y=7)

    def doctorbill():
        people=code.get()
        days=user.get()
        cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
        if cn.is_connected()==False:
            print('connection is not created')
        else:
            print('connection is successful')
            if people!='' and days!='' and customer!='':
                cr=cn.cursor()   
                command='use resort;'
                cr.execute(command)
                hotel_id=1
                order=3
                
                st1="insert into Medical values({},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,people,days,'NULL','NULL','NULL','NULL')
                cr.execute(st1)
                cn.commit()
                
                st2="update Medical set Doctor=(Number_of_people*Number_of_days)*800 where Orders={};".format(order)
                cr.execute(st2)
                cn.commit()

                st3="select COALESCE(sum(Bed),0)+ COALESCE(sum(Wheelchair),0)+ COALESCE(sum(Doctor),0) from Medical as Total where Booking_ID={};".format(booking)
                cr.execute(st3)
                data=cr.fetchone()

                st4="set SQL_SAFE_UPDATES=0;"
                cr.execute(st4)
                cn.commit()
                        
                for i in data:
                    st5="update Medical set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                    cr.execute(st5)
                    cn.commit()
                    cn.close()


                messagebox.showinfo('Billing','Successfully booked')
            else:
                messagebox.showinfo('Invalid','Please enter valid number of people or days')


    #inserting text box number of people
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Number of People')
    code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    code.place(x=550,y=240)
    code.insert(0,'Number of People')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    #inserting text box number of days
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Number of Days')
    user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    user.place(x=550,y=200)
    user.insert(0,'Number of Days')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    #####################################################################
    
    #for billing button
    Button(display,width=20,pady=7,text='Confirm Booking', bg='turquoise',fg='white',border=0,command=doctorbill).place(x=590,y=330)

    label1=Label(display,text="click here",fg='black',font=('Microsoft YaHei UI Light',9))
    label1.place(x=630,y=365)

    display.mainloop()
    
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        
#inserting an image
img1=PhotoImage(file='medical.png')
Label(window,image=img1,border=0).place(x=25,y=8)

#for wheelchair booking button
Button(window,width=20,pady=7,text='Book Now', bg='turquoise',fg='white',border=0,command=wheelchair).place(x=425,y=120)
    
#for bed booking button
Button(window,width=20,pady=7,text='Book Now', bg='turquoise',fg='white',border=0,command=bed).place(x=650,y=330)
    
#for doctor booking button
Button(window,width=20,pady=7,text='Book Now', bg='turquoise',fg='white',border=0,command=doctor).place(x=225,y=425)
    
window.mainloop()
