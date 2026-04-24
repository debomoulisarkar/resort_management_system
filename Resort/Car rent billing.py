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

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
#inserting an image
img1=PhotoImage(file='car rent.png')
Label(window,image=img1,border=0).place(x=0,y=5)

global booking
booking=1
global customer
customer=2
#________________________________________________________________
def swiftdzire():
    #to create opening window
    display=Toplevel()
    display.title('Billing Page')
    display.geometry('925x500+300+200')
    display.configure(bg='#fff')
    display.resizable(False,False)

    #inserting details
    frame=Frame(display,width=925,height=1000,bg='light pink')
    frame.place(x=0,y=0)

    def swiftbill():
        car=user.get()
        days=code.get()
        cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
        if cn.is_connected()==False:
            print('connection is not created')
        else:
            print('connection is successful')
            if car!='' and days!='':
                cr=cn.cursor()   
                command='use resort;'
                cr.execute(command)

                hotel_id=1
                order=1
                
                st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,days,'NULL','NULL','NULL','NULL','NULL') 
                cr.execute(st1)
                cn.commit()
                
                st2="update Car set Swift_Dzire=(Number_of_Cars*Number_of_hours)*10000 where Orders={};".format(order)
                cr.execute(st2)
                cn.commit()

                st3="select COALESCE(sum(Swift_Dzire),0)+ COALESCE(sum(Volvo_Bus),0)+ COALESCE(sum(Limousine),0) + COALESCE(sum(Force_Traveller),0)from Car as Total where Booking_ID={};".format(booking)
                cr.execute(st3)
                data=cr.fetchone()

                st4="set SQL_SAFE_UPDATES=0;"
                cr.execute(st4)
                cn.commit()
                        
                for i in data:
                    st5="update Car set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                    cr.execute(st5)
                    cn.commit()
                cn.close()

                messagebox.showinfo('Billing','Successfully booked')
            else:
                messagebox.showinfo('Invalid','Please enter valid number of people or days')
        
    #inserting text box number of cars
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Number of Cars')
    user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    user.place(x=550,y=120)
    user.insert(0,'Number of Cars')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    #inserting text box number of hours
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            code.insert(0,'Number of Hours')
    code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    code.place(x=550,y=160)
    code.insert(0,'Number of Hours')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    #############################################################

    #for confirm button
    Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=swiftbill).place(x=560,y=240)


def forcetraveller():
    #to create opening window
    display=Toplevel()
    display.title('Billing Page')
    display.geometry('925x500+300+200')
    display.configure(bg='#fff')
    display.resizable(False,False)

    #inserting details
    frame=Frame(display,width=925,height=1000,bg='light pink')
    frame.place(x=0,y=0)

    def travellerbill():
        car=user.get()
        days=code.get()
        cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
        if cn.is_connected()==False:
            print('connection is not created')
        else:
            print('connection is successful')
            if car!='' and days!='':
                cr=cn.cursor()   
                command='use resort;'
                cr.execute(command)

                hotel_id=1
                order=2
                
                st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,days,'NULL','NULL','NULL','NULL','NULL') 
                cr.execute(st1)
                cn.commit()
                
                st2="update Car set Force_Traveller=(Number_of_Cars*Number_of_hours)*15000 where Orders={};".format(order)
                cr.execute(st2)
                cn.commit()

                st3="select COALESCE(sum(Swift_Dzire),0)+ COALESCE(sum(Volvo_Bus),0)+ COALESCE(sum(Limousine),0) + COALESCE(sum(Force_Traveller),0)from Car as Total where Booking_ID={};".format(booking)
                cr.execute(st3)
                data=cr.fetchone()

                st4="set SQL_SAFE_UPDATES=0;"
                cr.execute(st4)
                cn.commit()
                        
                for i in data:
                    st5="update Car set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                    cr.execute(st5)
                    cn.commit()
                cn.close()

                messagebox.showinfo('Billing','Successfully booked')
            else:
                messagebox.showinfo('Invalid','Please enter valid number of people or days')
    
    #inserting text box number of cars
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Number of Cars')
    user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    user.place(x=550,y=120)
    user.insert(0,'Number of Cars')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    #inserting text box number of days
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            code.insert(0,'Number of Hours')
    code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    code.place(x=550,y=160)
    code.insert(0,'Number of Hours')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    #####################################################################
    
    #for confirm button
    Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=travellerbill).place(x=560,y=240)
    
def Limousine():
    #to create opening window
    display=Toplevel()
    display.title('Billing Page')
    display.geometry('925x500+300+200')
    display.configure(bg='#fff')
    display.resizable(False,False)

    #inserting details
    frame=Frame(display,width=925,height=1000,bg='light pink')
    frame.place(x=0,y=0)

    def limobill():
        car=user.get()
        days=code.get()
        cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
        if cn.is_connected()==False:
            print('connection is not created')
        else:
            print('connection is successful')
            if car!='' and days!='':
                cr=cn.cursor()   
                command='use resort;'
                cr.execute(command)

                hotel_id=1
                order=3
                
                st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,days,'NULL','NULL','NULL','NULL','NULL') 
                cr.execute(st1)
                cn.commit()
                
                st2="update Car set Limousine=(Number_of_Cars*Number_of_hours)*28000 where Orders={};".format(order)
                cr.execute(st2)
                cn.commit()

                st3="select COALESCE(sum(Swift_Dzire),0)+ COALESCE(sum(Volvo_Bus),0)+ COALESCE(sum(Limousine),0) + COALESCE(sum(Force_Traveller),0)from Car as Total where Booking_ID={};".format(booking)
                cr.execute(st3)
                data=cr.fetchone()

                st4="set SQL_SAFE_UPDATES=0;"
                cr.execute(st4)
                cn.commit()
                        
                for i in data:
                    st5="update Car set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                    cr.execute(st5)
                    cn.commit()
                cn.close()

                messagebox.showinfo('Billing','Successfully booked')
            else:
                messagebox.showinfo('Invalid','Please enter valid number of people or days')
    
    #inserting text box number of cars
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Number of Cars')
    user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    user.place(x=550,y=120)
    user.insert(0,'Number of Cars')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    #inserting text box number of hours
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            code.insert(0,'Number of Hours')
    code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    code.place(x=550,y=160)
    code.insert(0,'Number of Hours')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    ##############################################################
    #for confirm button
    Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=limobill).place(x=560,y=240)

def volvobus():
    #to create opening window
    display=Toplevel()
    display.title('Billing Page')
    display.geometry('925x500+300+200')
    display.configure(bg='#fff')
    display.resizable(False,False)

    #inserting details
    frame=Frame(display,width=925,height=1000,bg='light pink')
    frame.place(x=0,y=0)

    def volvobill():
        car=user.get()
        days=code.get()
        cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
        if cn.is_connected()==False:
            print('connection is not created')
        else:
            print('connection is successful')
            if car!='' and days!='':
                cr=cn.cursor()   
                command='use resort;'
                cr.execute(command)

                hotel_id=1
                order=4
                
                st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,days,'NULL','NULL','NULL','NULL','NULL') 
                cr.execute(st1)
                cn.commit()
                
                st2="update Car set Volvo_Bus=(Number_of_Cars*Number_of_hours)*15000 where Orders={};".format(order)
                cr.execute(st2)
                cn.commit()

                st3="select COALESCE(sum(Swift_Dzire),0)+ COALESCE(sum(Volvo_Bus),0)+ COALESCE(sum(Limousine),0) + COALESCE(sum(Force_Traveller),0)from Car as Total where Booking_ID={};".format(booking)
                cr.execute(st3)
                data=cr.fetchone()

                st4="set SQL_SAFE_UPDATES=0;"
                cr.execute(st4)
                cn.commit()
                        
                for i in data:
                    st5="update Car set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                    cr.execute(st5)
                    cn.commit()
                cn.close()

                messagebox.showinfo('Billing','Successfully booked')
            else:
                messagebox.showinfo('Invalid','Please enter valid number of people or days')
    
    #inserting text box number of cars
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Number of Cars')
    user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    user.place(x=550,y=120)
    user.insert(0,'Number of Cars')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    #inserting text box number of hours
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            code.insert(0,'Number of Hours')
    code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    code.place(x=550,y=160)
    code.insert(0,'Number of Hours')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)


    ##############################################################
    #for confirm button
    Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=volvobill).place(x=560,y=240)
    
#________________________________________________________________
##############################################
frame1=Frame(window,width=160,height=110,bg='white')
frame1.place(x=530,y=50)
swift_dzire=PhotoImage(file='swift.png')
swift=Button(frame1,image=swift_dzire,bg='white',bd=0,command=swiftdzire)
swift.place(x=-2,y=15)
label1=Label(window,text="swift d'zire",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label1.place(x=580,y=160)

frame2=Frame(window,width=160,height=110,bg='white')
frame2.place(x=720,y=50)
force_traveller=PhotoImage(file='traveller.png')
traveller=Button(frame2,image=force_traveller,bg='white',bd=0,command=forcetraveller)
traveller.place(x=0,y=10)
label1=Label(window,text="force traveller",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label1.place(x=760,y=160)

frame3=Frame(window,width=160,height=110,bg='white')
frame3.place(x=530,y=200)
volvo_bus=PhotoImage(file='volvo.png')
volvo=Button(frame3,image=volvo_bus,bg='white',bd=0,command=volvobus)
volvo.place(x=-20,y=0)
label1=Label(window,text="volvo bus",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label1.place(x=580,y=310)

frame4=Frame(window,width=160,height=110,bg='white')
frame4.place(x=720,y=200)
limousine=PhotoImage(file='limo.png')
limo=Button(frame4,image=limousine,bg='white',bd=0,command=Limousine)
limo.place(x=-2,y=0)
label1=Label(window,text="limousine",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label1.place(x=780,y=310)

##############################################

window.mainloop()

