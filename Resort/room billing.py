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
        
#inserting an image
img1=PhotoImage(file='room.png')
Label(window,image=img1,border=0).place(x=100,y=-5)

def chooserooms():
    #to create opening window
    root=Toplevel()
    root.title('Billing Page')
    root.geometry('925x500+300+200')
    root.configure(bg='#fff')
    root.resizable(False,False)

    #inserting an image
    img1=PhotoImage(file='room.png')
    Label(window,image=img1,border=0).place(x=100,y=-10)

    
    #________________________________________________________________
    def room__1():
        #to create opening window
        display=Toplevel()
        display.title('Billing Page')
        display.geometry('925x500+300+200')
        display.configure(bg='#fff')
        display.resizable(False,False)

        #inserting details
        frame=Frame(display,width=925,height=1000,bg='light pink')
        frame.place(x=0,y=0)

        def room1bill():
            entry=enter.get()
            depart=leave.get()
            cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
            if cn.is_connected()==False:
                print('connection is not created')
            else:
                print('connection is successful')
                if customer!='' and entry!='' and depart!='':
                    cr=cn.cursor()   
                    command='use resort;'
                    cr.execute(command)

                    hotel_id=1
                    room='Suite'
                    st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                    cr.execute(st1)
                    cn.commit()
                    
                    st2="select datediff('{}','{}') from Room;".format(depart,entry)
                    cr.execute(st2)
                    data=cr.fetchone()
                    
                    for i in data:
                        print(i)
                        st3="update Room set Price=({}*25000) where Customer_ID={} and Booking_ID={};".format(i,customer,booking)
                        cr.execute(st3)
                        cn.commit()
                        cn.close()

                    messagebox.showinfo('Billing','Successfully booked')
                else:
                    messagebox.showinfo('Invalid','Please enter valid number of people or days')


        #inserting text box for entry date
        def on_enter(e):
            enter.delete(0,'end')
        def on_leave(e):
            name=enter.get()
            if name=='':
                enter.insert(0,'Entry date')
        enter=Entry(frame,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        enter.place(x=100,y=70)
        enter.insert(0,'Date of Entry (yyyy/mm/dd)')
        enter.bind('<FocusIn>',on_enter)
        enter.bind('<FocusOut>',on_leave)

        #inserting text box for exit date
        def on_enter(e):
            leave.delete(0,'end')
        def on_leave(e):
            name=leave.get()
            if name=='':
                leave.insert(0,'Departure Date')
        leave=Entry(frame,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        leave.place(x=580,y=70)
        leave.insert(0,'Date of Departure (yyyy/mm/dd)')
        leave.bind('<FocusIn>',on_enter)
        leave.bind('<FocusOut>',on_leave)

        #####################################################################
    
        #for confirm button
        Button(display,width=30,pady=7,text='Confirm to Proceed', bg='#57a1f8',fg='white',border=0,command=room1bill).place(x=560,y=240)

    def room__2():
        #to create opening window
        display=Toplevel()
        display.title('Billing Page')
        display.geometry('925x500+300+200')
        display.configure(bg='#fff')
        display.resizable(False,False)

        #inserting details
        frame=Frame(display,width=925,height=1000,bg='light pink')
        frame.place(x=0,y=0)

        def room2bill():
            entry=enter.get()
            depart=leave.get()
            cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
            if cn.is_connected()==False:
                print('connection is not created')
            else:
                print('connection is successful')
                if customer!='' and entry!='' and depart!='':
                    cr=cn.cursor()   
                    command='use resort;'
                    cr.execute(command)

                    hotel_id=2
                    room='Deluxe Double Bed'
                    st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                    cr.execute(st1)
                    cn.commit()
                    
                    st2="select datediff('{}','{}') from Room;".format(depart,entry)
                    cr.execute(st2)
                    data=cr.fetchone()
                    
                    for i in data:
                        print(i)
                        st3="update Room set Price=({}*17000) where Customer_ID={} and Booking_ID={};".format(i,customer,booking)
                        cr.execute(st3)
                        cn.commit()
                        cn.close()

                    messagebox.showinfo('Billing','Successfully booked')
                else:
                    messagebox.showinfo('Invalid','Please enter valid number of people or days')


        #inserting text box for entry date
        def on_enter(e):
            enter.delete(0,'end')
        def on_leave(e):
            name=enter.get()
            if name=='':
                enter.insert(0,'Entry date')
        enter=Entry(frame,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        enter.place(x=100,y=70)
        enter.insert(0,'Date of Entry (yyyy/mm/dd)')
        enter.bind('<FocusIn>',on_enter)
        enter.bind('<FocusOut>',on_leave)

        #inserting text box for exit date
        def on_enter(e):
            leave.delete(0,'end')
        def on_leave(e):
            name=leave.get()
            if name=='':
                leave.insert(0,'Departure Date')
        leave=Entry(frame,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        leave.place(x=580,y=70)
        leave.insert(0,'Date of Departure (yyyy/mm/dd)')
        leave.bind('<FocusIn>',on_enter)
        leave.bind('<FocusOut>',on_leave)

        #####################################################################
    
        #for confirm button
        Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=room2bill).place(x=560,y=240)

    def room__3():
        #to create opening window
        display=Toplevel()
        display.title('Billing Page')
        display.geometry('925x500+300+200')
        display.configure(bg='#fff')
        display.resizable(False,False)

        #inserting details
        frame=Frame(display,width=925,height=1000,bg='light pink')
        frame.place(x=0,y=0)

        def room3bill():
            entry=enter.get()
            depart=leave.get()
            cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
            if cn.is_connected()==False:
                print('connection is not created')
            else:
                print('connection is successful')
                if customer!='' and entry!='' and depart!='':
                    cr=cn.cursor()   
                    command='use resort;'
                    cr.execute(command)

                    hotel_id=1
                    room='Standard Double Bed'
                    st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                    cr.execute(st1)
                    cn.commit()
                    st2="select datediff('{}','{}') from Room;".format(depart,entry)
                    cr.execute(st2)
                    data=cr.fetchone()
                    for i in data:
                        print(i)
                        st3="update Room set Price=({}*10000) where Customer_ID={} and Booking_ID={};".format(i,customer,booking)
                        cr.execute(st3)
                        cn.commit()
                        cn.close()

                    messagebox.showinfo('Billing','Successfully booked')
                else:
                    messagebox.showinfo('Invalid','Please enter valid number of people or days')


        #inserting text box for entry date
        def on_enter(e):
            enter.delete(0,'end')
        def on_leave(e):
            name=enter.get()
            if name=='':
                enter.insert(0,'Entry date')
        enter=Entry(frame,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        enter.place(x=100,y=70)
        enter.insert(0,'Date of Entry (yyyy/mm/dd)')
        enter.bind('<FocusIn>',on_enter)
        enter.bind('<FocusOut>',on_leave)

        #inserting text box for exit date
        def on_enter(e):
            leave.delete(0,'end')
        def on_leave(e):
            name=leave.get()
            if name=='':
                leave.insert(0,'Departure Date')
        leave=Entry(frame,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        leave.place(x=580,y=70)
        leave.insert(0,'Date of Departure (yyyy/mm/dd)')
        leave.bind('<FocusIn>',on_enter)
        leave.bind('<FocusOut>',on_leave)

        #####################################################################
    
        #for confirm button
        Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=room3bill).place(x=560,y=240)
        
    def room__4():
        #to create opening window
        display=Toplevel()
        display.title('Billing Page')
        display.geometry('925x500+300+200')
        display.configure(bg='#fff')
        display.resizable(False,False)

        #inserting details
        frame=Frame(display,width=925,height=1000,bg='light pink')
        frame.place(x=0,y=0)

        def room4bill():
            entry=enter.get()
            depart=leave.get()
            cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
            if cn.is_connected()==False:
                print('connection is not created')
            else:
                print('connection is successful')
                if customer!='' and entry!='' and depart!='':
                    cr=cn.cursor()   
                    command='use resort;'
                    cr.execute(command)

                    hotel_id=1
                    room='Deluxe Single Bed'
                    st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                    cr.execute(st1)
                    cn.commit()
                    st2="select datediff('{}','{}') from Room;".format(depart,entry)
                    cr.execute(st2)
                    data=cr.fetchone()
                    for i in data:
                        print(i)
                        st4="update Room set Price=({}*15000) where Customer_ID={} and Booking_ID={};".format(i,customer,booking)
                        cr.execute(st4)
                        cn.commit()
                        cn.close()

                    messagebox.showinfo('Billing','Successfully booked')
                else:
                    messagebox.showinfo('Invalid','Please enter valid number of people or days')
                    

        #inserting text box for entry date
        def on_enter(e):
            enter.delete(0,'end')
        def on_leave(e):
            name=enter.get()
            if name=='':
                enter.insert(0,'Entry date')
        enter=Entry(frame,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        enter.place(x=100,y=70)
        enter.insert(0,'Date of Entry (yyyy/mm/dd)')
        enter.bind('<FocusIn>',on_enter)
        enter.bind('<FocusOut>',on_leave)

        #inserting text box for exit date
        def on_enter(e):
            leave.delete(0,'end')
        def on_leave(e):
            name=leave.get()
            if name=='':
                leave.insert(0,'Departure Date')
        leave=Entry(frame,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        leave.place(x=580,y=70)
        leave.insert(0,'Date of Departure (yyyy/mm/dd)')
        leave.bind('<FocusIn>',on_enter)
        leave.bind('<FocusOut>',on_leave)

        #####################################################################
    
        #for confirm button
        Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=room4bill).place(x=560,y=240)

#________________________________________________________________
        
    ##############################################
    frame=Frame(root,width=1500,height=150,bg='blue')
    frame.place(x=0,y=0)

    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    frame1=Frame(root,width=250,height=150,bg='brown')
    frame1.place(x=80,y=160)
    room_1=PhotoImage(file='room1.png')
    room1=Button(frame1,image=room_1,bg='white',bd=0,command=room__1)
    room1.place(x=-10,y=-20)
    label1=Label(root,text="Suite",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label1.place(x=335,y=220)

    frame2=Frame(root,width=250,height=150,bg='brown')
    frame2.place(x=550,y=160)
    room_2=PhotoImage(file='room2.png')
    room2=Button(frame2,image=room_2,bg='white',bd=0,command=room__2)
    room2.place(x=-30,y=-50)
    label1=Label(root,text="Deluxe Double Bed",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label1.place(x=800,y=225)

    frame3=Frame(root,width=250,height=150,bg='brown')
    frame3.place(x=80,y=320)
    room_4=PhotoImage(file='room3.png')
    room4=Button(frame3,image=room_4,bg='white',bd=0,command=room__4)
    room4.place(x=-50,y=0)
    label1=Label(root,text="Deluxe Single Bed",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label1.place(x=335,y=380)

    frame4=Frame(root,width=250,height=150,bg='brown')
    frame4.place(x=550,y=320)
    room_3=PhotoImage(file='room4.png')
    room3=Button(frame4,image=room_3,bg='white',bd=0,command=room__3)
    room3.place(x=-2,y=0)
    label1=Label(root,text="Standard Double Bed",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label1.place(x=800,y=380)

    root.mainloop()
    ##############################################

#for book now button
Button(window,width=15,pady=10,text='Book now', bg='brown',fg='white',border=0,command=chooserooms).place(x=750,y=230)

window.mainloop()

