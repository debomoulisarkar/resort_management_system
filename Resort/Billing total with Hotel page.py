#hotel and options page

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ast
import csv
import random
import mysql.connector as mc
from tkinter.messagebox import showinfo
import random

#to create opening window
display=Tk()
display.title('Hotel Page')
display.geometry('925x500+300+200')
display.configure(bg='#fff')
display.resizable(False,False)

#inserting an image
img1=PhotoImage(file='hotel page.png')
Label(display,image=img1,border=0).place(x=0,y=0)

global booking
booking=random.randint(0,1000)
global customer
customer=1
#__________________________________________________________________________________________
def option1():
    #to create opening window
    display=Toplevel()
    display.title('Options Page')
    display.geometry('925x500+300+200')
    display.configure(bg='#fff')
    display.resizable(False,False)

    #inserting an image
    img1=PhotoImage(file='options 1.png')
    Label(display,image=img1,border=0).place(x=-20,y=-150)

    #inserting a frame
    frame1=Frame(display,width=850,height=390)
    frame1.place(x=35,y=50)
    img2=PhotoImage(file='option.png')
    Label(frame1,image=img2,border=0).place(x=0,y=0)

    #-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
    
    def poolbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        ####################################################

        def pool_bill():
            lst=[]
            people=user.get()
            days=code.get()
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
                    st1="insert into Pool values({},{},{},{},{},{});".format(booking,customer,hotel_id,people,days,'NULL')
                    cr.execute(st1)
                    cn.commit()

                    st2="update Pool set Price=(Number_of_people*Number_of_days)*500 where Customer_ID={} and Booking_ID={};".format(customer,booking)
                    cr.execute(st2)
                    cn.commit()
                    cn.close()

                    messagebox.showinfo('Billing','Successfully booked')
                else:
                    messagebox.showinfo('Invalid','Please enter valid number of people or days')
        
        #inserting an image
        img1=PhotoImage(file='pool.png')
        Label(window,image=img1,border=0).place(x=0,y=-10)
        frame1=Frame(window,width=390,height=410)
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
        user=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
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
        code=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        code.place(x=550,y=210)
        code.insert(0,'No. of days')
        code.bind('<FocusIn>',on_enter)
        code.bind('<FocusOut>',on_leave)

        ##############################################

        #confirm pool button
        Button(window,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=pool_bill).place(x=560,y=270)

        window.mainloop()

    def gymbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #mail and password check
        def gym_bill():
            lst=[]
            people=user.get()
            days=code.get()
            cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
            if cn.is_connected()==False:
                print('connection is not created')
            else:
                print('connection is successful')
                if people!='' and days!='':
                    cr=cn.cursor()   
                    command='use resort;'
                    cr.execute(command)
                    
                    hotel_id=1
                    st1="insert into Gym values({},{},{},{},{},{});".format(booking,customer,hotel_id,people,days,'NULL')
                    cr.execute(st1)
                    cn.commit()

                    st2="update Gym set Price=(Number_of_people*Number_of_days)*800 where Customer_ID={} and Booking_ID={};".format(customer,booking)
                    cr.execute(st2)
                    cn.commit()
                    cn.close()

                    messagebox.showinfo('Billing','Successfully booked')
                else:
                    messagebox.showinfo('Invalid','Please enter valid number of people or days')
        
        #inserting an image
        img1=PhotoImage(file='gym.png')
        Label(window,image=img1,border=0).place(x=0,y=-10)
        frame1=Frame(window,width=390,height=410)
        frame1.place(x=35,y=50)
        img2=PhotoImage(file='gym rate.png')
        Label(frame1,image=img2,border=0).place(x=0,y=-10)
        
        ################################################
        #inserting text box number of people
        def on_enter(e):
            user.delete(0,'end')
        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'No. of people')
        user=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
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
        code=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        code.place(x=550,y=210)
        code.insert(0,'No. of days')
        code.bind('<FocusIn>',on_enter)
        code.bind('<FocusOut>',on_leave)


        ##############################################

        #confirm pool button
        Button(window,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=gym_bill).place(x=560,y=270)

        window.mainloop()

    def spabill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        #inserting an image
        img1=PhotoImage(file='spa.png')
        Label(window,image=img1,border=0).place(x=0,y=0)
        frame=Frame(window,width=390,height=410)
        frame.place(x=15,y=50)
        img2=PhotoImage(file='spa rate.png')
        Label(frame,image=img2,border=0).place(x=-20,y=0)

        ##############################################################
        
        #________________________________________________________________
        def bmassage():
            #to create opening window
            display=Toplevel()
            display.title('Billing Page')
            display.geometry('925x500+300+200')
            display.configure(bg='#fff')
            display.resizable(False,False)

            #inserting details
            frame=Frame(display,width=925,height=1000,bg='light pink')
            frame.place(x=0,y=0)

            def massagebill():
                people=user.get()
                days=code.get()
                hotel_id=1
                order=1
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if people!='' and days!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        st1="insert into Spa values({},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,'NULL','NULL','NULL','NULL')
                        cr=cn.cursor()
                        cr.execute(st1)
                        cn.commit()
                
                        st2="update Spa set Body_Massage=({}*{})*1200 where Orders={};".format(people,days,order)
                        cr.execute(st2)
                        cn.commit()

                        st3="select COALESCE(sum(Body_Massage),0)+ COALESCE(sum(Body_Care),0)+ COALESCE(sum(Face_Treatment),0) from Spa as Total where Booking_ID={};".format(booking)
                        cr.execute(st3)
                        data=cr.fetchone()

                        st4="set SQL_SAFE_UPDATES=0;"
                        cr.execute(st4)
                        cn.commit()
                        
                        for i in data:
                            st5="update Spa set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                            cr.execute(st5)
                            cn.commit()
                        cn.close()

                        messagebox.showinfo('Billing','Successfully booked')
                    else:
                        messagebox.showinfo('Invalid','Please enter valid number of people or days')
        
            #inserting text box number of people
            def on_enter(e):
                user.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    user.insert(0,'Number of People')
            user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            user.place(x=550,y=120)
            user.insert(0,'Number of People')
            user.bind('<FocusIn>',on_enter)
            user.bind('<FocusOut>',on_leave)

            #inserting text box number of days
            def on_enter(e):
                code.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    code.insert(0,'Number of Days')
            code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            code.place(x=550,y=160)
            code.insert(0,'Number of Days')
            code.bind('<FocusIn>',on_enter)
            code.bind('<FocusOut>',on_leave)

            #############################################################

            #for confirm button
            Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=massagebill).place(x=560,y=240)


        def bcare():
            #to create opening window
            display=Toplevel()
            display.title('Billing Page')
            display.geometry('925x500+300+200')
            display.configure(bg='#fff')
            display.resizable(False,False)

            #inserting details
            frame=Frame(display,width=925,height=1000,bg='light pink')
            frame.place(x=0,y=0)

            def carebill():
                people=user.get()
                days=code.get()
                order=2
                hotel_id=1

                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if people!='' and days!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        st1="insert into Spa values({},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,'NULL','NULL','NULL','NULL')
                        cr=cn.cursor()
                        cr.execute(st1)
                        cn.commit()
                        
                        st2="update Spa set Body_Care=({}*{})*1500 where Orders={};".format(people,days,order)
                        cr.execute(st2)
                        cn.commit()

                        st3="select COALESCE(sum(Body_Massage),0)+ COALESCE(sum(Body_Care),0)+ COALESCE(sum(Face_Treatment),0) from Spa as Total where Booking_ID={};".format(booking)
                        cr.execute(st3)
                        data=cr.fetchone()

                        st4="set SQL_SAFE_UPDATES=0;"
                        cr.execute(st4)
                        cn.commit()
                        
                        for i in data:
                            st5="update Spa set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                            cr.execute(st5)
                            cn.commit()
                        cn.close()

                        messagebox.showinfo('Billing','Successfully booked')
                    else:
                        messagebox.showinfo('Invalid','Please enter valid number of people or days')
    
            #inserting text box number of people
            def on_enter(e):
                user.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    user.insert(0,'Number of People')
            user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            user.place(x=550,y=120)
            user.insert(0,'Number of People')
            user.bind('<FocusIn>',on_enter)
            user.bind('<FocusOut>',on_leave)

            #inserting text box number of days
            def on_enter(e):
                code.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    code.insert(0,'Number of Days')
            code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            code.place(x=550,y=160)
            code.insert(0,'Number of Days')
            code.bind('<FocusIn>',on_enter)
            code.bind('<FocusOut>',on_leave)


            #####################################################################
    
            #for confirm button
            Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=carebill).place(x=560,y=240)
    
        def htreat():
            #to create opening window
            display=Toplevel()
            display.title('Billing Page')
            display.geometry('925x500+300+200')
            display.configure(bg='#fff')
            display.resizable(False,False)

            #inserting details
            frame=Frame(display,width=925,height=1000,bg='light pink')
            frame.place(x=0,y=0)

            def treatbill():
                people=user.get()
                days=code.get()
                order=3
                hotel_id=1

                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if people!='' and days!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        st1="insert into Spa values({},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,'NULL','NULL','NULL','NULL')
                        cr=cn.cursor()
                        cr.execute(st1)
                        cn.commit()
                        
                        st2="update Spa set Face_Treatment=({}*{})*800 where Orders={};".format(people,days,order)
                        cr.execute(st2)
                        cn.commit()

                        st3="select COALESCE(sum(Body_Massage),0)+ COALESCE(sum(Body_Care),0)+ COALESCE(sum(Face_Treatment),0) from Spa as Total where Booking_ID={};".format(booking)
                        cr.execute(st3)
                        data=cr.fetchone()

                        st4="set SQL_SAFE_UPDATES=0;"
                        cr.execute(st4)
                        cn.commit()
                        
                        for i in data:
                            st5="update Spa set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                            cr.execute(st5)
                            cn.commit()
                        cn.close()

                        messagebox.showinfo('Billing','Successfully booked')
                    else:
                        messagebox.showinfo('Invalid','Please enter valid number of people or days')
    
            #inserting text box number of people
            def on_enter(e):
                user.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    user.insert(0,'Number of People')
            user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            user.place(x=550,y=120)
            user.insert(0,'Number of People')
            user.bind('<FocusIn>',on_enter)
            user.bind('<FocusOut>',on_leave)

            #inserting text box number of days
            def on_enter(e):
                code.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    code.insert(0,'Number of Days')
            code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            code.place(x=550,y=160)
            code.insert(0,'Number of Days')
            code.bind('<FocusIn>',on_enter)
            code.bind('<FocusOut>',on_leave)

            ##############################################################
            #for confirm button
            Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=treatbill).place(x=560,y=240)

        #________________________________________________________________
            

        frame1=Frame(window,width=160,height=110,bg='white')
        frame1.place(x=410,y=220)
        body_massage=PhotoImage(file='body massage.png')
        bodymassage=Button(frame1,image=body_massage,bg='white',bd=0,command=bmassage)
        bodymassage.place(x=-10,y=-10)
        label1=Label(window,text="body massage",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label1.place(x=445,y=330)

        frame2=Frame(window,width=160,height=110,bg='white')
        frame2.place(x=585,y=220)
        body_care=PhotoImage(file='body care.png')
        bodycare=Button(frame2,image=body_care,bg='white',bd=0,command=bcare)
        bodycare.place(x=0,y=0)
        label2=Label(window,text="body care",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label2.place(x=635,y=330)

        frame3=Frame(window,width=160,height=110,bg='white')
        frame3.place(x=760,y=220)
        face_treatment=PhotoImage(file='face treatment.png')
        facetreatment=Button(frame3,image=face_treatment,bg='white',bd=0,command=htreat)
        facetreatment.place(x=-20,y=-10)
        label3=Label(window,text="face treatment",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label3.place(x=800,y=330)

        ##############################################

        window.mainloop()

    def experiences():
        #to create opening window
        window=Toplevel()
        window.title('Pool Experience')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #inserting an image
        img1=PhotoImage(file='pool experience.png')
        Label(window,image=img1,border=0).place(x=220,y=7)

        def Spa():
            #to create opening window
            display=Toplevel()
            display.title('Spa Experience')
            display.geometry('925x500+300+200')
            display.configure(bg='light pink')
            display.resizable(False,False)

            def Gym():
                #to create opening window
                display=Toplevel()
                display.title('Gym Experience')
                display.geometry('925x500+300+200')
                display.configure(bg='black')
                display.resizable(False,False)

                def Dining():
                    #to create opening window
                    display=Toplevel()
                    display.title('Dining Experience')
                    display.geometry('925x500+300+200')
                    display.configure(bg='grey')
                    display.resizable(False,False)

                    def Grounds():
                        #to create opening window
                        display=Toplevel()
                        display.title('Grounds Experience')
                        display.geometry('925x500+300+200')
                        display.configure(bg='dark green')
                        display.resizable(False,False)

                        def Rooms():
                            #to create opening window
                            display=Toplevel()
                            display.title('Rooms Experience')
                            display.geometry('925x500+300+200')
                            display.configure(bg='brown')
                            display.resizable(False,False)


                            #inserting an image
                            img1=PhotoImage(file='room experience.png')
                            Label(display,image=img1,border=0).place(x=220,y=0)

                            #for back button
                            Button(display,width=15,pady=10,text='back', bg='black',fg='white',border=0,command=Grounds).place(x=50,y=230)


                            display.mainloop()

                        #inserting an image
                        img1=PhotoImage(file='grounds.png')
                        Label(display,image=img1,border=0).place(x=180,y=18)

                        #for next button
                        Button(display,width=15,pady=10,text='Next', bg='green',fg='white',border=0,command=Rooms).place(x=750,y=230)

                        #for back button
                        Button(display,width=15,pady=10,text='back', bg='green',fg='white',border=0,command=Dining).place(x=50,y=230)

                        display.mainloop()

                    #inserting an image
                    img1=PhotoImage(file='dining experience.png')
                    Label(display,image=img1,border=0).place(x=320,y=0)
            
                    #for next button
                    Button(display,width=15,pady=10,text='Next', bg='black',fg='white',border=0,command=Grounds).place(x=750,y=230)

                    #for back button
                    Button(display,width=15,pady=10,text='back', bg='black',fg='white',border=0,command=Gym).place(x=50,y=230)

                    display.mainloop()

                #inserting an image
                img1=PhotoImage(file='gym experience.png')
                Label(display,image=img1,border=0).place(x=320,y=-10)

                #for next button
                Button(display,width=15,pady=10,text='Next', bg='grey',fg='white',border=0,command=Dining).place(x=750,y=230)

                #for back button
                Button(display,width=15,pady=10,text='back', bg='grey',fg='white',border=0,command=Spa).place(x=50,y=230)
            
                display.mainloop()
        
            #inserting an image
            img1=PhotoImage(file='spa experience.png')
            Label(display,image=img1,border=0).place(x=205,y=-10)

            #for next button
            Button(display,width=15,pady=10,text='Next', bg='brown',fg='white',border=0,command=Gym).place(x=750,y=230)

            #for back button
            Button(display,width=15,pady=10,text='back', bg='brown',fg='white',border=0,command=experiences).place(x=50,y=230)

            display.mainloop()
    
        #for next button
        Button(window,width=15,pady=10,text='Next', bg='brown',fg='white',border=0,command=Spa).place(x=750,y=230)

        window.mainloop()

    def roombill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

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
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*25000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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

                            hotel_id=1
                            room='Deluxe Double Bed'
                            st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                            cr.execute(st1)
                            cn.commit()
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*17000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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
                Button(display,width=30,pady=7,text='Confirm to Proceed', bg='#57a1f8',fg='white',border=0,command=room2bill).place(x=560,y=240)

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
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*10000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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
                Button(display,width=30,pady=7,text='Confirm to Proceed', bg='#57a1f8',fg='white',border=0,command=room3bill).place(x=560,y=240)
        
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
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*15000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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
                Button(display,width=30,pady=7,text='Confirm to Proceed', bg='#57a1f8',fg='white',border=0,command=room4bill).place(x=560,y=240)

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

    def carbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        #inserting an image
        img1=PhotoImage(file='car rent.png')
        Label(window,image=img1,border=0).place(x=0,y=5)

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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=1
                        order=1
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=1
                        order=2
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=1
                        order=3
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=1
                        order=4
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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

    def medicalbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #inserting an image
        img1=PhotoImage(file='medical.png')
        Label(window,image=img1,border=0).place(x=25,y=8)
        
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

        #for wheelchair booking button
        Button(window,width=20,pady=7,text='Book Now', bg='turquoise',fg='white',border=0,command=wheelchair).place(x=425,y=120)
    
        #for bed booking button
        Button(window,width=20,pady=7,text='Book Now', bg='turquoise',fg='white',border=0,command=bed).place(x=650,y=330)
    
        #for doctor booking button
        Button(window,width=20,pady=7,text='Book Now', bg='turquoise',fg='white',border=0,command=doctor).place(x=225,y=425)
    
        window.mainloop()

    def parking():
        #to create opening window
        window=Toplevel()
        window.title('Parking Service')
        window.geometry('925x500+300+200')
        window.configure(bg='black')
        window.resizable(False,False)

        #inserting an image
        img1=PhotoImage(file='parking.png')
        Label(window,image=img1,border=0).place(x=270,y=3)

        window.mainloop()
    
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
    #for the icons
    frame2=Frame(display,width=130,height=130,bg='white')
    frame2.place(x=110,y=100)
    pool_icon=PhotoImage(file='pool icon.png')
    pool=Button(frame2,image=pool_icon,bg='white',bd=0,command=poolbill)
    pool.place(x=0,y=5)
    label1=Label(frame2,text="pool",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label1.place(x=50,y=105)
    #################################################################################################
    frame3=Frame(display,width=130,height=130,bg='white')
    frame3.place(x=300,y=100)
    gym_icon=PhotoImage(file='gym icon.png')
    gym=Button(frame3,image=gym_icon,bg='white',bd=0,command=gymbill)
    gym.place(x=0,y=10)
    label2=Label(frame3,text="gym",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label2.place(x=50,y=105)
    
    #################################################################################################

    frame4=Frame(display,width=130,height=130,bg='white')
    frame4.place(x=490,y=100)
    spa_icon=PhotoImage(file='spa icon.png')
    spa=Button(frame4,image=spa_icon,bg='white',bd=0,command=spabill)
    spa.place(x=15,y=11)
    label3=Label(frame4,text="spa",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label3.place(x=50,y=105)

    #################################################################################################

    frame5=Frame(display,width=130,height=130,bg='white')
    frame5.place(x=680,y=100)
    car_icon=PhotoImage(file='car icon.png')
    car=Button(frame5,image=car_icon,bg='white',bd=0,command=carbill)
    car.place(x=-10,y=4)
    label4=Label(frame5,text="transport",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label4.place(x=40,y=105)

    #################################################################################################

    frame6=Frame(display,width=130,height=130,bg='white')
    frame6.place(x=110,y=265)
    room_icon=PhotoImage(file='room icon.png')
    room=Button(frame6,image=room_icon,bg='white',bd=0,command=roombill)
    room.place(x=-10,y=4)
    label5=Label(frame6,text="rooms",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label5.place(x=40,y=105)

    #################################################################################################

    frame7=Frame(display,width=130,height=130,bg='white')
    frame7.place(x=300,y=265)
    parking_icon=PhotoImage(file='parking icon.png')
    parking=Button(frame7,image=parking_icon,bg='white',bd=0,command=parking)
    parking.place(x=15,y=5)
    label6=Label(frame7,text="parking",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label6.place(x=40,y=105)

    #################################################################################################

    frame8=Frame(display,width=130,height=130,bg='white')
    frame8.place(x=490,y=265)
    medical_icon=PhotoImage(file='medical icon.png')
    medical=Button(frame8,image=medical_icon,bg='white',bd=0,command=medicalbill)
    medical.place(x=25,y=8)
    label7=Label(frame8,text="medical",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label7.place(x=40,y=105)

    #################################################################################################

    frame9=Frame(display,width=130,height=130,bg='white')
    frame9.place(x=680,y=265)
    experience_icon=PhotoImage(file='experience icon.png')
    experience=Button(frame9,image=experience_icon,bg='white',bd=0,command=experiences)
    experience.place(x=3,y=10)
    label8=Label(frame9,text="experiences",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label8.place(x=30,y=105)


    display.mainloop()

def option2():
    #to create opening window
    display=Toplevel()
    display.title('Hotel Page')
    display.geometry('925x500+300+200')
    display.configure(bg='#fff')
    display.resizable(False,False)

    #inserting an image
    img1=PhotoImage(file='options 2.png')
    Label(display,image=img1,border=0).place(x=0,y=0)

    #inserting a frame
    frame1=Frame(display,width=850,height=390)
    frame1.place(x=35,y=50)
    img2=PhotoImage(file='option.png')
    Label(frame1,image=img2,border=0).place(x=0,y=0)

    #-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

    def poolbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        ####################################################

        def pool_bill():
            lst=[]
            people=user.get()
            days=code.get()
            cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
            if cn.is_connected()==False:
                print('connection is not created')
            else:
                print('connection is successful')
                if people!='' and days!='' and customer!='':
                    cr=cn.cursor()   
                    command='use resort;'
                    cr.execute(command)

                    hotel_id=3
                    st1="insert into Pool values({},{},{},{},{},{});".format(booking,customer,hotel_id,people,days,'NULL')
                    cr.execute(st1)
                    cn.commit()

                    st2="update Pool set Price=(Number_of_people*Number_of_days)*500 where Customer_ID={} and Booking_ID={};".format(customer,booking)
                    cr.execute(st2)
                    cn.commit()
                    cn.close()

                    messagebox.showinfo('Billing','Successfully booked')
                else:
                    messagebox.showinfo('Invalid','Please enter valid number of people or days')
        
        #inserting an image
        img1=PhotoImage(file='pool.png')
        Label(window,image=img1,border=0).place(x=0,y=-10)
        frame1=Frame(window,width=390,height=410)
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
        user=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
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
        code=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        code.place(x=550,y=210)
        code.insert(0,'No. of days')
        code.bind('<FocusIn>',on_enter)
        code.bind('<FocusOut>',on_leave)

        ##############################################

        #confirm pool button
        Button(window,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=pool_bill).place(x=560,y=270)

        window.mainloop()

    def gymbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        #mail and password check
        def gym_bill():
            lst=[]
            people=user.get()
            days=code.get()
            cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
            if cn.is_connected()==False:
                print('connection is not created')
            else:
                print('connection is successful')
                if people!='' and days!='':
                    cr=cn.cursor()   
                    command='use resort;'
                    cr.execute(command)

                    hotel_id=3
                    st1="insert into Gym values({},{},{},{},{},{});".format(booking,customer,hotel_id,people,days,'NULL')
                    cr.execute(st1)
                    cn.commit()

                    st2="update Gym set Price=(Number_of_people*Number_of_days)*800 where Customer_ID={} and Booking_ID={};".format(customer,booking)
                    cr.execute(st2)
                    cn.commit()
                    cn.close()

                    messagebox.showinfo('Billing','Successfully booked')
                else:
                    messagebox.showinfo('Invalid','Please enter valid number of people or days')
        
        #inserting an image
        img1=PhotoImage(file='gym.png')
        Label(window,image=img1,border=0).place(x=0,y=-10)
        frame1=Frame(window,width=390,height=410)
        frame1.place(x=35,y=50)
        img2=PhotoImage(file='gym rate.png')
        Label(frame1,image=img2,border=0).place(x=0,y=-10)

        ################################################

        #inserting text box number of people
        def on_enter(e):
            user.delete(0,'end')
        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'No. of people')
        user=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
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
        code=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        code.place(x=550,y=210)
        code.insert(0,'No. of days')
        code.bind('<FocusIn>',on_enter)
        code.bind('<FocusOut>',on_leave)

        ##############################################


        #confirm gym button
        Button(window,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=gym_bill).place(x=560,y=270)

        window.mainloop()

    def spabill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        #inserting an image
        img1=PhotoImage(file='spa.png')
        Label(window,image=img1,border=0).place(x=0,y=0)
        frame=Frame(window,width=390,height=410)
        frame.place(x=15,y=50)
        img2=PhotoImage(file='spa rate.png')
        Label(frame,image=img2,border=0).place(x=-20,y=0)

        ##############################################################
        
        #________________________________________________________________
        def bmassage():
            #to create opening window
            display=Toplevel()
            display.title('Billing Page')
            display.geometry('925x500+300+200')
            display.configure(bg='#fff')
            display.resizable(False,False)

            #inserting details
            frame=Frame(display,width=925,height=1000,bg='light pink')
            frame.place(x=0,y=0)

            def massagebill():
                people=user.get()
                days=code.get()
                hotel_id=3
                order=1
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if people!='' and days!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        st1="insert into Spa values({},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,'NULL','NULL','NULL','NULL')
                        cr=cn.cursor()
                        cr.execute(st1)
                        cn.commit()
                
                        st2="update Spa set Body_Massage=({}*{})*1200 where Orders={};".format(people,days,order)
                        cr.execute(st2)
                        cn.commit()

                        st3="select COALESCE(sum(Body_Massage),0)+ COALESCE(sum(Body_Care),0)+ COALESCE(sum(Face_Treatment),0) from Spa as Total where Booking_ID={};".format(booking)
                        cr.execute(st3)
                        data=cr.fetchone()

                        st4="set SQL_SAFE_UPDATES=0;"
                        cr.execute(st4)
                        cn.commit()
                        
                        for i in data:
                            st5="update Spa set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer,customer)
                            cr.execute(st5)
                            cn.commit()
                        cn.close()

                        messagebox.showinfo('Billing','Successfully booked')
                    else:
                        messagebox.showinfo('Invalid','Please enter valid number of people or days')
        
            #inserting text box number of people
            def on_enter(e):
                user.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    user.insert(0,'Number of People')
            user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            user.place(x=550,y=120)
            user.insert(0,'Number of People')
            user.bind('<FocusIn>',on_enter)
            user.bind('<FocusOut>',on_leave)

            #inserting text box number of days
            def on_enter(e):
                code.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    code.insert(0,'Number of Days')
            code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            code.place(x=550,y=160)
            code.insert(0,'Number of Days')
            code.bind('<FocusIn>',on_enter)
            code.bind('<FocusOut>',on_leave)

            #############################################################

            #for confirm button
            Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=massagebill).place(x=560,y=240)


        def bcare():
            #to create opening window
            display=Toplevel()
            display.title('Billing Page')
            display.geometry('925x500+300+200')
            display.configure(bg='#fff')
            display.resizable(False,False)

            #inserting details
            frame=Frame(display,width=925,height=1000,bg='light pink')
            frame.place(x=0,y=0)

            def carebill():
                people=user.get()
                days=code.get()
                order=2
                hotel_id=3

                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if people!='' and days!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        st1="insert into Spa values({},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,'NULL','NULL','NULL','NULL')
                        cr=cn.cursor()
                        cr.execute(st1)
                        cn.commit()
                        
                        st2="update Spa set Body_Care=({}*{})*1500 where Orders={};".format(people,days,order)
                        cr.execute(st2)
                        cn.commit()

                        st3="select COALESCE(sum(Body_Massage),0)+ COALESCE(sum(Body_Care),0)+ COALESCE(sum(Face_Treatment),0) from Spa as Total where Booking_ID={};".format(booking)
                        cr.execute(st3)
                        data=cr.fetchone()

                        st4="set SQL_SAFE_UPDATES=0;"
                        cr.execute(st4)
                        cn.commit()
                        
                        for i in data:
                            st5="update Spa set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                            cr.execute(st5)
                            cn.commit()
                        cn.close()

                        messagebox.showinfo('Billing','Successfully booked')
                    else:
                        messagebox.showinfo('Invalid','Please enter valid number of people or days')
    
            #inserting text box number of people
            def on_enter(e):
                user.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    user.insert(0,'Number of People')
            user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            user.place(x=550,y=120)
            user.insert(0,'Number of People')
            user.bind('<FocusIn>',on_enter)
            user.bind('<FocusOut>',on_leave)

            #inserting text box number of days
            def on_enter(e):
                code.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    code.insert(0,'Number of Days')
            code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            code.place(x=550,y=160)
            code.insert(0,'Number of Days')
            code.bind('<FocusIn>',on_enter)
            code.bind('<FocusOut>',on_leave)


            #####################################################################
    
            #for confirm button
            Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=carebill).place(x=560,y=240)
    
        def htreat():
            #to create opening window
            display=Toplevel()
            display.title('Billing Page')
            display.geometry('925x500+300+200')
            display.configure(bg='#fff')
            display.resizable(False,False)

            #inserting details
            frame=Frame(display,width=925,height=1000,bg='light pink')
            frame.place(x=0,y=0)

            def treatbill():
                people=user.get()
                days=code.get()
                order=3
                hotel_id=3

                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if people!='' and days!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        st1="insert into Spa values({},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,'NULL','NULL','NULL','NULL')
                        cr=cn.cursor()
                        cr.execute(st1)
                        cn.commit()
                        
                        st2="update Spa set Face_Treatment=({}*{})*800 where Orders={};".format(people,days,order)
                        cr.execute(st2)
                        cn.commit()

                        st3="select COALESCE(sum(Body_Massage),0)+ COALESCE(sum(Body_Care),0)+ COALESCE(sum(Face_Treatment),0) from Spa as Total where Booking_ID={};".format(booking)
                        cr.execute(st3)
                        data=cr.fetchone()

                        st4="set SQL_SAFE_UPDATES=0;"
                        cr.execute(st4)
                        cn.commit()
                        
                        for i in data:
                            st5="update Spa set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                            cr.execute(st5)
                            cn.commit()
                        cn.close()

                        messagebox.showinfo('Billing','Successfully booked')
                    else:
                        messagebox.showinfo('Invalid','Please enter valid number of people or days')
    
            #inserting text box number of people
            def on_enter(e):
                user.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    user.insert(0,'Number of People')
            user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            user.place(x=550,y=120)
            user.insert(0,'Number of People')
            user.bind('<FocusIn>',on_enter)
            user.bind('<FocusOut>',on_leave)

            #inserting text box number of days
            def on_enter(e):
                code.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    code.insert(0,'Number of Days')
            code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            code.place(x=550,y=160)
            code.insert(0,'Number of Days')
            code.bind('<FocusIn>',on_enter)
            code.bind('<FocusOut>',on_leave)

            ##############################################################
            #for confirm button
            Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=treatbill).place(x=560,y=240)

        #________________________________________________________________
            

        frame1=Frame(window,width=160,height=110,bg='white')
        frame1.place(x=410,y=220)
        body_massage=PhotoImage(file='body massage.png')
        bodymassage=Button(frame1,image=body_massage,bg='white',bd=0,command=bmassage)
        bodymassage.place(x=-10,y=-10)
        label1=Label(window,text="body massage",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label1.place(x=445,y=330)

        frame2=Frame(window,width=160,height=110,bg='white')
        frame2.place(x=585,y=220)
        body_care=PhotoImage(file='body care.png')
        bodycare=Button(frame2,image=body_care,bg='white',bd=0,command=bcare)
        bodycare.place(x=0,y=0)
        label2=Label(window,text="body care",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label2.place(x=635,y=330)

        frame3=Frame(window,width=160,height=110,bg='white')
        frame3.place(x=760,y=220)
        face_treatment=PhotoImage(file='face treatment.png')
        facetreatment=Button(frame3,image=face_treatment,bg='white',bd=0,command=htreat)
        facetreatment.place(x=-20,y=-10)
        label3=Label(window,text="face treatment",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label3.place(x=800,y=330)

        ##############################################

        window.mainloop()


    def experiences():
        #to create opening window
        window=Toplevel()
        window.title('Pool Experience')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #inserting an image
        img1=PhotoImage(file='pool experience.png')
        Label(window,image=img1,border=0).place(x=220,y=7)

        def Spa():
            #to create opening window
            display=Toplevel()
            display.title('Spa Experience')
            display.geometry('925x500+300+200')
            display.configure(bg='light pink')
            display.resizable(False,False)

            def Gym():
                #to create opening window
                display=Toplevel()
                display.title('Gym Experience')
                display.geometry('925x500+300+200')
                display.configure(bg='black')
                display.resizable(False,False)

                def Dining():
                    #to create opening window
                    display=Toplevel()
                    display.title('Dining Experience')
                    display.geometry('925x500+300+200')
                    display.configure(bg='grey')
                    display.resizable(False,False)

                    def Grounds():
                        #to create opening window
                        display=Toplevel()
                        display.title('Grounds Experience')
                        display.geometry('925x500+300+200')
                        display.configure(bg='dark green')
                        display.resizable(False,False)

                        def Rooms():
                            #to create opening window
                            display=Toplevel()
                            display.title('Rooms Experience')
                            display.geometry('925x500+300+200')
                            display.configure(bg='brown')
                            display.resizable(False,False)


                            #inserting an image
                            img1=PhotoImage(file='room experience.png')
                            Label(display,image=img1,border=0).place(x=220,y=0)

                            #for back button
                            Button(display,width=15,pady=10,text='back', bg='black',fg='white',border=0,command=Grounds).place(x=50,y=230)


                            display.mainloop()

                        #inserting an image
                        img1=PhotoImage(file='grounds.png')
                        Label(display,image=img1,border=0).place(x=180,y=18)

                        #for next button
                        Button(display,width=15,pady=10,text='Next', bg='green',fg='white',border=0,command=Rooms).place(x=750,y=230)

                        #for back button
                        Button(display,width=15,pady=10,text='back', bg='green',fg='white',border=0,command=Dining).place(x=50,y=230)

                        display.mainloop()

                    #inserting an image
                    img1=PhotoImage(file='dining experience.png')
                    Label(display,image=img1,border=0).place(x=320,y=0)
            
                    #for next button
                    Button(display,width=15,pady=10,text='Next', bg='black',fg='white',border=0,command=Grounds).place(x=750,y=230)

                    #for back button
                    Button(display,width=15,pady=10,text='back', bg='black',fg='white',border=0,command=Gym).place(x=50,y=230)

                    display.mainloop()

                #inserting an image
                img1=PhotoImage(file='gym experience.png')
                Label(display,image=img1,border=0).place(x=320,y=-10)

                #for next button
                Button(display,width=15,pady=10,text='Next', bg='grey',fg='white',border=0,command=Dining).place(x=750,y=230)

                #for back button
                Button(display,width=15,pady=10,text='back', bg='grey',fg='white',border=0,command=Spa).place(x=50,y=230)
            
                display.mainloop()
        
            #inserting an image
            img1=PhotoImage(file='spa experience.png')
            Label(display,image=img1,border=0).place(x=205,y=-10)

            #for next button
            Button(display,width=15,pady=10,text='Next', bg='brown',fg='white',border=0,command=Gym).place(x=750,y=230)

            #for back button
            Button(display,width=15,pady=10,text='back', bg='brown',fg='white',border=0,command=experiences).place(x=50,y=230)

            display.mainloop()
    
        #for next button
        Button(window,width=15,pady=10,text='Next', bg='brown',fg='white',border=0,command=Spa).place(x=750,y=230)

        window.mainloop()


    def roombill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

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

                            hotel_id=3
                            room='Suite'
                            st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                            cr.execute(st1)
                            cn.commit()
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*25000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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

                            hotel_id=3
                            room='Deluxe Double Bed'
                            st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                            cr.execute(st1)
                            cn.commit()
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*17000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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
                Button(display,width=30,pady=7,text='Confirm to Proceed', bg='#57a1f8',fg='white',border=0,command=room2bill).place(x=560,y=240)

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

                            hotel_id=3
                            room='Standard Double Bed'
                            st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                            cr.execute(st1)
                            cn.commit()
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*10000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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
                Button(display,width=30,pady=7,text='Confirm to Proceed', bg='#57a1f8',fg='white',border=0,command=room3bill).place(x=560,y=240)
        
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

                            hotel_id=3
                            room='Deluxe Single Bed'
                            st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                            cr.execute(st1)
                            cn.commit()
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*15000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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
                Button(display,width=30,pady=7,text='Confirm to Proceed', bg='#57a1f8',fg='white',border=0,command=room4bill).place(x=560,y=240)

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

    def carbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        #inserting an image
        img1=PhotoImage(file='car rent.png')
        Label(window,image=img1,border=0).place(x=0,y=5)

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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=3
                        order=1
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=3
                        order=2
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=3
                        order=3
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=3
                        order=4
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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

    def medicalbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #inserting an image
        img1=PhotoImage(file='medical.png')
        Label(window,image=img1,border=0).place(x=25,y=8)
        
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

        #for wheelchair booking button
        Button(window,width=20,pady=7,text='Book Now', bg='turquoise',fg='white',border=0,command=wheelchair).place(x=425,y=120)
    
        #for bed booking button
        Button(window,width=20,pady=7,text='Book Now', bg='turquoise',fg='white',border=0,command=bed).place(x=650,y=330)
    
        #for doctor booking button
        Button(window,width=20,pady=7,text='Book Now', bg='turquoise',fg='white',border=0,command=doctor).place(x=225,y=425)
    
        window.mainloop()

    def parking():
        #to create opening window
        window=Toplevel()
        window.title('Parking Service')
        window.geometry('925x500+300+200')
        window.configure(bg='black')
        window.resizable(False,False)

        #inserting an image
        img1=PhotoImage(file='parking.png')
        Label(window,image=img1,border=0).place(x=270,y=3)

        window.mainloop()

    #################################################################################################
    
    #for the icons

    frame2=Frame(display,width=130,height=130,bg='white')
    frame2.place(x=110,y=100)
    pool_icon=PhotoImage(file='pool icon.png')
    pool=Button(frame2,image=pool_icon,bg='white',bd=0,command=poolbill)
    pool.place(x=0,y=5)
    label1=Label(frame2,text="pool",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label1.place(x=50,y=105)
    #################################################################################################
    frame3=Frame(display,width=130,height=130,bg='white')
    frame3.place(x=300,y=100)
    gym_icon=PhotoImage(file='gym icon.png')
    gym=Button(frame3,image=gym_icon,bg='white',bd=0,command=gymbill)
    gym.place(x=0,y=10)
    label2=Label(frame3,text="gym",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label2.place(x=50,y=105)

    #################################################################################################

    frame4=Frame(display,width=130,height=130,bg='white')
    frame4.place(x=490,y=100)
    spa_icon=PhotoImage(file='spa icon.png')
    spa=Button(frame4,image=spa_icon,bg='white',bd=0,command=spabill)
    spa.place(x=15,y=11)
    label3=Label(frame4,text="spa",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label3.place(x=50,y=105)

    #################################################################################################

    frame5=Frame(display,width=130,height=130,bg='white')
    frame5.place(x=680,y=100)
    car_icon=PhotoImage(file='car icon.png')
    car=Button(frame5,image=car_icon,bg='white',bd=0,command=carbill)
    car.place(x=-10,y=4)
    label4=Label(frame5,text="transport",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label4.place(x=40,y=105)

    #################################################################################################

    frame6=Frame(display,width=130,height=130,bg='white')
    frame6.place(x=110,y=265)
    room_icon=PhotoImage(file='room icon.png')
    room=Button(frame6,image=room_icon,bg='white',bd=0,command=roombill)
    room.place(x=-10,y=4)
    label5=Label(frame6,text="rooms",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label5.place(x=40,y=105)

    #################################################################################################

    frame7=Frame(display,width=130,height=130,bg='white')
    frame7.place(x=300,y=265)
    parking_icon=PhotoImage(file='parking icon.png')
    parking=Button(frame7,image=parking_icon,bg='white',bd=0,command=parking)
    parking.place(x=15,y=5)
    label6=Label(frame7,text="parking",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label6.place(x=40,y=105)

    #################################################################################################

    frame8=Frame(display,width=130,height=130,bg='white')
    frame8.place(x=490,y=265)
    medical_icon=PhotoImage(file='medical icon.png')
    medical=Button(frame8,image=medical_icon,bg='white',bd=0,command=medicalbill)
    medical.place(x=25,y=8)
    label7=Label(frame8,text="medical",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label7.place(x=40,y=105)

    #################################################################################################

    frame9=Frame(display,width=130,height=130,bg='white')
    frame9.place(x=680,y=265)
    experience_icon=PhotoImage(file='experience icon.png')
    experience=Button(frame9,image=experience_icon,bg='white',bd=0,command=experiences)
    experience.place(x=3,y=10)
    label8=Label(frame9,text="experiences",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label8.place(x=30,y=105)

    display.mainloop()


def option3():
    #to create opening window
    display=Toplevel()
    display.title('Home Page')
    display.geometry('925x500+300+200')
    display.configure(bg='#fff')
    display.resizable(False,False)

    #inserting an image
    img1=PhotoImage(file='options 3.png')
    Label(display,image=img1,border=0).place(x=0,y=0)

    #inserting a frame
    frame1=Frame(display,width=850,height=390)
    frame1.place(x=35,y=50)
    img2=PhotoImage(file='option.png')
    Label(frame1,image=img2,border=0).place(x=0,y=0)

    #-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

    def poolbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        ####################################################
        
        def pool_bill():
            lst=[]
            people=user.get()
            days=code.get()
            cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
            if cn.is_connected()==False:
                print('connection is not created')
            else:
                print('connection is successful')
                if people!='' and days!='' and customer!='':
                    cr=cn.cursor()   
                    command='use resort;'
                    cr.execute(command)

                    hotel_id=2
                    st1="insert into Pool values({},{},{},{},{},{});".format(booking,customer,hotel_id,people,days,'NULL')
                    cr.execute(st1)
                    cn.commit()

                    st2="update Pool set Price=(Number_of_people*Number_of_days)*500 where Customer_ID={} and Booking_ID={};".format(customer,booking)
                    cr.execute(st2)
                    cn.commit()
                    cn.close()

                    messagebox.showinfo('Billing','Successfully booked')
                else:
                    messagebox.showinfo('Invalid','Please enter valid number of people or days')
        
        #inserting an image
        img1=PhotoImage(file='pool.png')
        Label(window,image=img1,border=0).place(x=0,y=-10)
        frame1=Frame(window,width=390,height=410)
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
        user=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
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
        code=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        code.place(x=550,y=210)
        code.insert(0,'No. of days')
        code.bind('<FocusIn>',on_enter)
        code.bind('<FocusOut>',on_leave)

        ##############################################

        #confirm pool button
        Button(window,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=pool_bill).place(x=560,y=270)

        window.mainloop()

    def gymbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #mail and password check
        def gym_bill():
            lst=[]
            people=user.get()
            days=code.get()
            cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
            if cn.is_connected()==False:
                print('connection is not created')
            else:
                print('connection is successful')
                if people!='' and days!='':
                    cr=cn.cursor()   
                    command='use resort;'
                    cr.execute(command)

                    hotel_id=2
                    st1="insert into Gym values({},{},{},{},{},{});".format(booking,customer,hotel_id,people,days,'NULL')
                    cr.execute(st1)
                    cn.commit()

                    st2="update Gym set Price=(Number_of_people*Number_of_days)*800 where Customer_ID={} and Booking_ID={};".format(customer,booking)
                    cr.execute(st2)
                    cn.commit()
                    cn.close()

                    messagebox.showinfo('Billing','Successfully booked')
                else:
                    messagebox.showinfo('Invalid','Please enter valid number of people or days')
        
        #inserting an image
        img1=PhotoImage(file='gym.png')
        Label(window,image=img1,border=0).place(x=0,y=-10)
        frame1=Frame(window,width=390,height=410)
        frame1.place(x=35,y=50)
        img2=PhotoImage(file='gym rate.png')
        Label(frame1,image=img2,border=0).place(x=0,y=-10)
        
        ################################################
        #inserting text box number of people
        def on_enter(e):
            user.delete(0,'end')
        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'No. of people')
        user=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
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
        code=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        code.place(x=550,y=210)
        code.insert(0,'No. of days')
        code.bind('<FocusIn>',on_enter)
        code.bind('<FocusOut>',on_leave)


        ##############################################

        #confirm pool button
        Button(window,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=gym_bill).place(x=560,y=300)

        window.mainloop()

    def spabill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        #inserting an image
        img1=PhotoImage(file='spa.png')
        Label(window,image=img1,border=0).place(x=0,y=0)
        frame=Frame(window,width=390,height=410)
        frame.place(x=15,y=50)
        img2=PhotoImage(file='spa rate.png')
        Label(frame,image=img2,border=0).place(x=-20,y=0)

        ##############################################################
        
        #________________________________________________________________
        def bmassage():
            #to create opening window
            display=Toplevel()
            display.title('Billing Page')
            display.geometry('925x500+300+200')
            display.configure(bg='#fff')
            display.resizable(False,False)

            #inserting details
            frame=Frame(display,width=925,height=1000,bg='light pink')
            frame.place(x=0,y=0)

            def massagebill():
                people=user.get()
                days=code.get()
                hotel_id=2
                order=1
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if people!='' and days!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        st1="insert into Spa values({},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,'NULL','NULL','NULL','NULL')
                        cr=cn.cursor()
                        cr.execute(st1)
                        cn.commit()
                
                        st2="update Spa set Body_Massage=({}*{})*1200 where Orders={};".format(people,days,order)
                        cr.execute(st2)
                        cn.commit()

                        st3="select COALESCE(sum(Body_Massage),0)+ COALESCE(sum(Body_Care),0)+ COALESCE(sum(Face_Treatment),0) from Spa as Total where Booking_ID={};".format(booking)
                        cr.execute(st3)
                        data=cr.fetchone()

                        st4="set SQL_SAFE_UPDATES=0;"
                        cr.execute(st4)
                        cn.commit()
                        
                        for i in data:
                            st5="update Spa set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer,customer)
                            cr.execute(st5)
                            cn.commit()
                        cn.close()

                        messagebox.showinfo('Billing','Successfully booked')
                    else:
                        messagebox.showinfo('Invalid','Please enter valid number of people or days')
        
            #inserting text box number of people
            def on_enter(e):
                user.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    user.insert(0,'Number of People')
            user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            user.place(x=550,y=120)
            user.insert(0,'Number of People')
            user.bind('<FocusIn>',on_enter)
            user.bind('<FocusOut>',on_leave)

            #inserting text box number of days
            def on_enter(e):
                code.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    code.insert(0,'Number of Days')
            code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            code.place(x=550,y=160)
            code.insert(0,'Number of Days')
            code.bind('<FocusIn>',on_enter)
            code.bind('<FocusOut>',on_leave)

            #############################################################

            #for confirm button
            Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=massagebill).place(x=560,y=240)


        def bcare():
            #to create opening window
            display=Toplevel()
            display.title('Billing Page')
            display.geometry('925x500+300+200')
            display.configure(bg='#fff')
            display.resizable(False,False)

            #inserting details
            frame=Frame(display,width=925,height=1000,bg='light pink')
            frame.place(x=0,y=0)

            def carebill():
                people=user.get()
                days=code.get()
                order=2
                hotel_id=2

                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if people!='' and days!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        st1="insert into Spa values({},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,'NULL','NULL','NULL','NULL')
                        cr=cn.cursor()
                        cr.execute(st1)
                        cn.commit()
                        
                        st2="update Spa set Body_Care=({}*{})*1500 where Orders={};".format(people,days,order)
                        cr.execute(st2)
                        cn.commit()

                        st3="select COALESCE(sum(Body_Massage),0)+ COALESCE(sum(Body_Care),0)+ COALESCE(sum(Face_Treatment),0) from Spa as Total where Booking_ID={};".format(booking)
                        cr.execute(st3)
                        data=cr.fetchone()

                        st4="set SQL_SAFE_UPDATES=0;"
                        cr.execute(st4)
                        cn.commit()
                        
                        for i in data:
                            st5="update Spa set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                            cr.execute(st5)
                            cn.commit()
                        cn.close()

                        messagebox.showinfo('Billing','Successfully booked')
                    else:
                        messagebox.showinfo('Invalid','Please enter valid number of people or days')
    
            #inserting text box number of people
            def on_enter(e):
                user.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    user.insert(0,'Number of People')
            user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            user.place(x=550,y=120)
            user.insert(0,'Number of People')
            user.bind('<FocusIn>',on_enter)
            user.bind('<FocusOut>',on_leave)

            #inserting text box number of days
            def on_enter(e):
                code.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    code.insert(0,'Number of Days')
            code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            code.place(x=550,y=160)
            code.insert(0,'Number of Days')
            code.bind('<FocusIn>',on_enter)
            code.bind('<FocusOut>',on_leave)


            #####################################################################
    
            #for confirm button
            Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=carebill).place(x=560,y=240)
    
        def htreat():
            #to create opening window
            display=Toplevel()
            display.title('Billing Page')
            display.geometry('925x500+300+200')
            display.configure(bg='#fff')
            display.resizable(False,False)

            #inserting details
            frame=Frame(display,width=925,height=1000,bg='light pink')
            frame.place(x=0,y=0)

            def treatbill():
                people=user.get()
                days=code.get()
                order=3
                hotel_id=2

                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if people!='' and days!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        st1="insert into Spa values({},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,'NULL','NULL','NULL','NULL')
                        cr=cn.cursor()
                        cr.execute(st1)
                        cn.commit()
                        
                        st2="update Spa set Face_Treatment=({}*{})*800 where Orders={};".format(people,days,order)
                        cr.execute(st2)
                        cn.commit()

                        st3="select COALESCE(sum(Body_Massage),0)+ COALESCE(sum(Body_Care),0)+ COALESCE(sum(Face_Treatment),0) from Spa as Total where Booking_ID={};".format(booking)
                        cr.execute(st3)
                        data=cr.fetchone()

                        st4="set SQL_SAFE_UPDATES=0;"
                        cr.execute(st4)
                        cn.commit()
                        
                        for i in data:
                            st5="update Spa set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                            cr.execute(st5)
                            cn.commit()
                        cn.close()

                        messagebox.showinfo('Billing','Successfully booked')
                    else:
                        messagebox.showinfo('Invalid','Please enter valid number of people or days')
    
            #inserting text box number of people
            def on_enter(e):
                user.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    user.insert(0,'Number of People')
            user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            user.place(x=550,y=120)
            user.insert(0,'Number of People')
            user.bind('<FocusIn>',on_enter)
            user.bind('<FocusOut>',on_leave)

            #inserting text box number of days
            def on_enter(e):
                code.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    code.insert(0,'Number of Days')
            code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            code.place(x=550,y=160)
            code.insert(0,'Number of Days')
            code.bind('<FocusIn>',on_enter)
            code.bind('<FocusOut>',on_leave)

            ##############################################################
            #for confirm button
            Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=treatbill).place(x=560,y=240)

        #________________________________________________________________
            

        frame1=Frame(window,width=160,height=110,bg='white')
        frame1.place(x=410,y=220)
        body_massage=PhotoImage(file='body massage.png')
        bodymassage=Button(frame1,image=body_massage,bg='white',bd=0,command=bmassage)
        bodymassage.place(x=-10,y=-10)
        label1=Label(window,text="body massage",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label1.place(x=445,y=330)

        frame2=Frame(window,width=160,height=110,bg='white')
        frame2.place(x=585,y=220)
        body_care=PhotoImage(file='body care.png')
        bodycare=Button(frame2,image=body_care,bg='white',bd=0,command=bcare)
        bodycare.place(x=0,y=0)
        label2=Label(window,text="body care",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label2.place(x=635,y=330)

        frame3=Frame(window,width=160,height=110,bg='white')
        frame3.place(x=760,y=220)
        face_treatment=PhotoImage(file='face treatment.png')
        facetreatment=Button(frame3,image=face_treatment,bg='white',bd=0,command=htreat)
        facetreatment.place(x=-20,y=-10)
        label3=Label(window,text="face treatment",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label3.place(x=800,y=330)

        ##############################################

        window.mainloop()


    def experiences():
        #to create opening window
        window=Toplevel()
        window.title('Pool Experience')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #inserting an image
        img1=PhotoImage(file='pool experience.png')
        Label(window,image=img1,border=0).place(x=220,y=7)

        def Spa():
            #to create opening window
            display=Toplevel()
            display.title('Spa Experience')
            display.geometry('925x500+300+200')
            display.configure(bg='light pink')
            display.resizable(False,False)

            def Gym():
                #to create opening window
                display=Toplevel()
                display.title('Gym Experience')
                display.geometry('925x500+300+200')
                display.configure(bg='black')
                display.resizable(False,False)

                def Dining():
                    #to create opening window
                    display=Toplevel()
                    display.title('Dining Experience')
                    display.geometry('925x500+300+200')
                    display.configure(bg='grey')
                    display.resizable(False,False)

                    def Grounds():
                        #to create opening window
                        display=Toplevel()
                        display.title('Grounds Experience')
                        display.geometry('925x500+300+200')
                        display.configure(bg='dark green')
                        display.resizable(False,False)

                        def Rooms():
                            #to create opening window
                            display=Toplevel()
                            display.title('Rooms Experience')
                            display.geometry('925x500+300+200')
                            display.configure(bg='brown')
                            display.resizable(False,False)


                            #inserting an image
                            img1=PhotoImage(file='room experience.png')
                            Label(display,image=img1,border=0).place(x=220,y=0)

                            #for back button
                            Button(display,width=15,pady=10,text='back', bg='black',fg='white',border=0,command=Grounds).place(x=50,y=230)


                            display.mainloop()

                        #inserting an image
                        img1=PhotoImage(file='grounds.png')
                        Label(display,image=img1,border=0).place(x=180,y=18)

                        #for next button
                        Button(display,width=15,pady=10,text='Next', bg='green',fg='white',border=0,command=Rooms).place(x=750,y=230)

                        #for back button
                        Button(display,width=15,pady=10,text='back', bg='green',fg='white',border=0,command=Dining).place(x=50,y=230)

                        display.mainloop()

                    #inserting an image
                    img1=PhotoImage(file='dining experience.png')
                    Label(display,image=img1,border=0).place(x=320,y=0)
            
                    #for next button
                    Button(display,width=15,pady=10,text='Next', bg='black',fg='white',border=0,command=Grounds).place(x=750,y=230)

                    #for back button
                    Button(display,width=15,pady=10,text='back', bg='black',fg='white',border=0,command=Gym).place(x=50,y=230)

                    display.mainloop()

                #inserting an image
                img1=PhotoImage(file='gym experience.png')
                Label(display,image=img1,border=0).place(x=320,y=-10)

                #for next button
                Button(display,width=15,pady=10,text='Next', bg='grey',fg='white',border=0,command=Dining).place(x=750,y=230)

                #for back button
                Button(display,width=15,pady=10,text='back', bg='grey',fg='white',border=0,command=Spa).place(x=50,y=230)
            
                display.mainloop()
        
            #inserting an image
            img1=PhotoImage(file='spa experience.png')
            Label(display,image=img1,border=0).place(x=205,y=-10)

            #for next button
            Button(display,width=15,pady=10,text='Next', bg='brown',fg='white',border=0,command=Gym).place(x=750,y=230)

            #for back button
            Button(display,width=15,pady=10,text='back', bg='brown',fg='white',border=0,command=experiences).place(x=50,y=230)

            display.mainloop()
    
        #for next button
        Button(window,width=15,pady=10,text='Next', bg='brown',fg='white',border=0,command=Spa).place(x=750,y=230)

        window.mainloop()

    def roombill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

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

                            hotel_id=2
                            room='Suite'
                            st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                            cr.execute(st1)
                            cn.commit()
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*25000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*17000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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
                Button(display,width=30,pady=7,text='Confirm to Proceed', bg='#57a1f8',fg='white',border=0,command=room2bill).place(x=560,y=240)

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

                            hotel_id=2
                            room='Standard Double Bed'
                            st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                            cr.execute(st1)
                            cn.commit()
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*10000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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
                Button(display,width=30,pady=7,text='Confirm to Proceed', bg='#57a1f8',fg='white',border=0,command=room3bill).place(x=560,y=240)
        
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

                            hotel_id=2
                            room='Deluxe Single Bed'
                            st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                            cr.execute(st1)
                            cn.commit()
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*15000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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
                Button(display,width=30,pady=7,text='Confirm to Proceed', bg='#57a1f8',fg='white',border=0,command=room4bill).place(x=560,y=240)

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

    def carbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        #inserting an image
        img1=PhotoImage(file='car rent.png')
        Label(window,image=img1,border=0).place(x=0,y=5)

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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=2
                        order=1
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=2
                        order=2
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=2
                        order=3
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=2
                        order=4
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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

    def medicalbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #inserting an image
        img1=PhotoImage(file='medical.png')
        Label(window,image=img1,border=0).place(x=25,y=8)
        
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

        #for wheelchair booking button
        Button(window,width=20,pady=7,text='Book Now', bg='turquoise',fg='white',border=0,command=wheelchair).place(x=425,y=120)
    
        #for bed booking button
        Button(window,width=20,pady=7,text='Book Now', bg='turquoise',fg='white',border=0,command=bed).place(x=650,y=330)
    
        #for doctor booking button
        Button(window,width=20,pady=7,text='Book Now', bg='turquoise',fg='white',border=0,command=doctor).place(x=225,y=425)
    
        window.mainloop()

    def parking():
        #to create opening window
        window=Toplevel()
        window.title('Parking Service')
        window.geometry('925x500+300+200')
        window.configure(bg='black')
        window.resizable(False,False)

        #inserting an image
        img1=PhotoImage(file='parking.png')
        Label(window,image=img1,border=0).place(x=270,y=3)

        window.mainloop()

    #############################################################################################3

    #for the icons

    frame2=Frame(display,width=130,height=130,bg='white')
    frame2.place(x=110,y=100)
    pool_icon=PhotoImage(file='pool icon.png')
    pool=Button(frame2,image=pool_icon,bg='white',bd=0,command=poolbill)
    pool.place(x=0,y=5)
    label1=Label(frame2,text="pool",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label1.place(x=50,y=105)
    #################################################################################################
    frame3=Frame(display,width=130,height=130,bg='white')
    frame3.place(x=300,y=100)
    gym_icon=PhotoImage(file='gym icon.png')
    gym=Button(frame3,image=gym_icon,bg='white',bd=0,command=gymbill)
    gym.place(x=0,y=10)
    label2=Label(frame3,text="gym",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label2.place(x=50,y=105)

    #################################################################################################

    frame4=Frame(display,width=130,height=130,bg='white')
    frame4.place(x=490,y=100)
    spa_icon=PhotoImage(file='spa icon.png')
    spa=Button(frame4,image=spa_icon,bg='white',bd=0,command=spabill)
    spa.place(x=15,y=11)
    label3=Label(frame4,text="spa",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label3.place(x=50,y=105)

    #################################################################################################

    frame5=Frame(display,width=130,height=130,bg='white')
    frame5.place(x=680,y=100)
    car_icon=PhotoImage(file='car icon.png')
    car=Button(frame5,image=car_icon,bg='white',bd=0,command=carbill)
    car.place(x=-10,y=4)
    label4=Label(frame5,text="transport",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label4.place(x=40,y=105)

    #################################################################################################

    frame6=Frame(display,width=130,height=130,bg='white')
    frame6.place(x=110,y=265)
    room_icon=PhotoImage(file='room icon.png')
    room=Button(frame6,image=room_icon,bg='white',bd=0,command=roombill)
    room.place(x=-10,y=4)
    label5=Label(frame6,text="rooms",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label5.place(x=40,y=105)

    #################################################################################################

    frame7=Frame(display,width=130,height=130,bg='white')
    frame7.place(x=300,y=265)
    parking_icon=PhotoImage(file='parking icon.png')
    parking=Button(frame7,image=parking_icon,bg='white',bd=0,command=parking)
    parking.place(x=15,y=5)
    label6=Label(frame7,text="parking",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label6.place(x=40,y=105)

    #################################################################################################

    frame8=Frame(display,width=130,height=130,bg='white')
    frame8.place(x=490,y=265)
    medical_icon=PhotoImage(file='medical icon.png')
    medical=Button(frame8,image=medical_icon,bg='white',bd=0,command=medicalbill)
    medical.place(x=25,y=8)
    label7=Label(frame8,text="medical",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label7.place(x=40,y=105)

    #################################################################################################

    frame9=Frame(display,width=130,height=130,bg='white')
    frame9.place(x=680,y=265)
    experience_icon=PhotoImage(file='experience icon.png')
    experience=Button(frame9,image=experience_icon,bg='white',bd=0,command=experiences)
    experience.place(x=3,y=10)
    label8=Label(frame9,text="experiences",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label8.place(x=30,y=105)

    display.mainloop()

def option4():
    #to create opening window
    display=Toplevel()
    display.title('Home Page')
    display.geometry('925x500+300+200')
    display.configure(bg='#fff')
    display.resizable(False,False)

    #inserting an image
    img1=PhotoImage(file='options 4.png')
    Label(display,image=img1,border=0).place(x=0,y=0)

    #inserting a frame
    frame1=Frame(display,width=850,height=390)
    frame1.place(x=35,y=50)
    img2=PhotoImage(file='option.png')
    Label(frame1,image=img2,border=0).place(x=0,y=0)

    #####################################################################


    #-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

    def poolbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        ####################################################

        def pool_bill():
            lst=[]
            people=user.get()
            days=code.get()
            cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
            if cn.is_connected()==False:
                print('connection is not created')
            else:
                print('connection is successful')
                if people!='' and days!='' and customer!='':
                    cr=cn.cursor()   
                    command='use resort;'
                    cr.execute(command)

                    hotel_id=4
                    st1="insert into Pool values({},{},{},{},{},{});".format(booking,customer,hotel_id,people,days,'NULL')
                    cr.execute(st1)
                    cn.commit()

                    st2="update Pool set Price=(Number_of_people*Number_of_days)*500 where Customer_ID={} and Booking_ID={};".format(customer,booking)
                    cr.execute(st2)
                    cn.commit()
                    cn.close()

                    messagebox.showinfo('Billing','Successfully booked')
                else:
                    messagebox.showinfo('Invalid','Please enter valid number of people or days')
        
        #inserting an image
        img1=PhotoImage(file='pool.png')
        Label(window,image=img1,border=0).place(x=0,y=-10)
        frame1=Frame(window,width=390,height=410)
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
        user=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
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
        code=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        code.place(x=550,y=210)
        code.insert(0,'No. of days')
        code.bind('<FocusIn>',on_enter)
        code.bind('<FocusOut>',on_leave)

        ##############################################

        #confirm pool button
        Button(window,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=pool_bill).place(x=560,y=270)

        window.mainloop()

    def gymbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        #mail and password check
        def gym_bill():
            lst=[]
            people=user.get()
            days=code.get()
            cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
            if cn.is_connected()==False:
                print('connection is not created')
            else:
                print('connection is successful')
                if people!='' and days!='':
                    cr=cn.cursor()   
                    command='use resort;'
                    cr.execute(command)

                    hotel_id=4
                    st1="insert into Gym values({},{},{},{},{},{});".format(booking,customer,hotel_id,people,days,'NULL')
                    cr.execute(st1)
                    cn.commit()

                    st2="update Gym set Price=(Number_of_people*Number_of_days)*800 where Customer_ID={} and Booking_ID={};".format(customer,booking)
                    cr.execute(st2)
                    cn.commit()
                    cn.close()

                    messagebox.showinfo('Billing','Successfully booked')
                else:
                    messagebox.showinfo('Invalid','Please enter valid number of people or days')
        
        #inserting an image
        img1=PhotoImage(file='gym.png')
        Label(window,image=img1,border=0).place(x=0,y=-10)
        frame1=Frame(window,width=390,height=410)
        frame1.place(x=35,y=50)
        img2=PhotoImage(file='gym rate.png')
        Label(frame1,image=img2,border=0).place(x=0,y=-10)

        ################################################

        #inserting text box number of people
        def on_enter(e):
            user.delete(0,'end')
        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'No. of people')
        user=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
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
        code=Entry(window,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        code.place(x=550,y=210)
        code.insert(0,'No. of days')
        code.bind('<FocusIn>',on_enter)
        code.bind('<FocusOut>',on_leave)


        ##############################################

        #confirm pool button
        Button(window,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=gym_bill).place(x=560,y=270)

        window.mainloop()

    def spabill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        #inserting an image
        img1=PhotoImage(file='spa.png')
        Label(window,image=img1,border=0).place(x=0,y=0)
        frame=Frame(window,width=390,height=410)
        frame.place(x=15,y=50)
        img2=PhotoImage(file='spa rate.png')
        Label(frame,image=img2,border=0).place(x=-20,y=0)

        ##############################################################
        
        #________________________________________________________________
        def bmassage():
            #to create opening window
            display=Toplevel()
            display.title('Billing Page')
            display.geometry('925x500+300+200')
            display.configure(bg='#fff')
            display.resizable(False,False)

            #inserting details
            frame=Frame(display,width=925,height=1000,bg='light pink')
            frame.place(x=0,y=0)

            def massagebill():
                people=user.get()
                days=code.get()
                hotel_id=4
                order=1
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if people!='' and days!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        st1="insert into Spa values({},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,'NULL','NULL','NULL','NULL')
                        cr=cn.cursor()
                        cr.execute(st1)
                        cn.commit()
                
                        st2="update Spa set Body_Massage=({}*{})*1200 where Orders={};".format(people,days,order)
                        cr.execute(st2)
                        cn.commit()

                        st3="select COALESCE(sum(Body_Massage),0)+ COALESCE(sum(Body_Care),0)+ COALESCE(sum(Face_Treatment),0) from Spa as Total where Booking_ID={};".format(booking)
                        cr.execute(st3)
                        data=cr.fetchone()

                        st4="set SQL_SAFE_UPDATES=0;"
                        cr.execute(st4)
                        cn.commit()
                        
                        for i in data:
                            st5="update Spa set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer,customer)
                            cr.execute(st5)
                            cn.commit()
                        cn.close()

                        messagebox.showinfo('Billing','Successfully booked')
                    else:
                        messagebox.showinfo('Invalid','Please enter valid number of people or days')
        
            #inserting text box number of people
            def on_enter(e):
                user.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    user.insert(0,'Number of People')
            user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            user.place(x=550,y=120)
            user.insert(0,'Number of People')
            user.bind('<FocusIn>',on_enter)
            user.bind('<FocusOut>',on_leave)

            #inserting text box number of days
            def on_enter(e):
                code.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    code.insert(0,'Number of Days')
            code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            code.place(x=550,y=160)
            code.insert(0,'Number of Days')
            code.bind('<FocusIn>',on_enter)
            code.bind('<FocusOut>',on_leave)

            #############################################################

            #for confirm button
            Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=massagebill).place(x=560,y=240)


        def bcare():
            #to create opening window
            display=Toplevel()
            display.title('Billing Page')
            display.geometry('925x500+300+200')
            display.configure(bg='#fff')
            display.resizable(False,False)

            #inserting details
            frame=Frame(display,width=925,height=1000,bg='light pink')
            frame.place(x=0,y=0)

            def carebill():
                people=user.get()
                days=code.get()
                order=2
                hotel_id=4

                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if people!='' and days!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        st1="insert into Spa values({},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,'NULL','NULL','NULL','NULL')
                        cr=cn.cursor()
                        cr.execute(st1)
                        cn.commit()
                        
                        st2="update Spa set Body_Care=({}*{})*1500 where Orders={};".format(people,days,order)
                        cr.execute(st2)
                        cn.commit()

                        st3="select COALESCE(sum(Body_Massage),0)+ COALESCE(sum(Body_Care),0)+ COALESCE(sum(Face_Treatment),0) from Spa as Total where Booking_ID={};".format(booking)
                        cr.execute(st3)
                        data=cr.fetchone()

                        st4="set SQL_SAFE_UPDATES=0;"
                        cr.execute(st4)
                        cn.commit()
                        
                        for i in data:
                            st5="update Spa set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                            cr.execute(st5)
                            cn.commit()
                        cn.close()

                        messagebox.showinfo('Billing','Successfully booked')
                    else:
                        messagebox.showinfo('Invalid','Please enter valid number of people or days')
    
            #inserting text box number of people
            def on_enter(e):
                user.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    user.insert(0,'Number of People')
            user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            user.place(x=550,y=120)
            user.insert(0,'Number of People')
            user.bind('<FocusIn>',on_enter)
            user.bind('<FocusOut>',on_leave)

            #inserting text box number of days
            def on_enter(e):
                code.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    code.insert(0,'Number of Days')
            code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            code.place(x=550,y=160)
            code.insert(0,'Number of Days')
            code.bind('<FocusIn>',on_enter)
            code.bind('<FocusOut>',on_leave)


            #####################################################################
    
            #for confirm button
            Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=carebill).place(x=560,y=240)
    
        def htreat():
            #to create opening window
            display=Toplevel()
            display.title('Billing Page')
            display.geometry('925x500+300+200')
            display.configure(bg='#fff')
            display.resizable(False,False)

            #inserting details
            frame=Frame(display,width=925,height=1000,bg='light pink')
            frame.place(x=0,y=0)

            def treatbill():
                people=user.get()
                days=code.get()
                order=3
                hotel_id=4

                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if people!='' and days!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        st1="insert into Spa values({},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,'NULL','NULL','NULL','NULL')
                        cr=cn.cursor()
                        cr.execute(st1)
                        cn.commit()
                        
                        st2="update Spa set Face_Treatment=({}*{})*800 where Orders={};".format(people,days,order)
                        cr.execute(st2)
                        cn.commit()

                        st3="select COALESCE(sum(Body_Massage),0)+ COALESCE(sum(Body_Care),0)+ COALESCE(sum(Face_Treatment),0) from Spa as Total where Booking_ID={};".format(booking)
                        cr.execute(st3)
                        data=cr.fetchone()

                        st4="set SQL_SAFE_UPDATES=0;"
                        cr.execute(st4)
                        cn.commit()
                        
                        for i in data:
                            st5="update Spa set Price={} where Booking_ID={} and Customer_ID={};".format(i,booking,customer)
                            cr.execute(st5)
                            cn.commit()
                        cn.close()

                        messagebox.showinfo('Billing','Successfully booked')
                    else:
                        messagebox.showinfo('Invalid','Please enter valid number of people or days')
    
            #inserting text box number of people
            def on_enter(e):
                user.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    user.insert(0,'Number of People')
            user=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            user.place(x=550,y=120)
            user.insert(0,'Number of People')
            user.bind('<FocusIn>',on_enter)
            user.bind('<FocusOut>',on_leave)

            #inserting text box number of days
            def on_enter(e):
                code.delete(0,'end')
            def on_leave(e):
                name=user.get()
                if name=='':
                    code.insert(0,'Number of Days')
            code=Entry(display,width=30,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
            code.place(x=550,y=160)
            code.insert(0,'Number of Days')
            code.bind('<FocusIn>',on_enter)
            code.bind('<FocusOut>',on_leave)

            ##############################################################
            #for confirm button
            Button(display,width=30,pady=7,text='Confirm Booking', bg='#57a1f8',fg='white',border=0,command=treatbill).place(x=560,y=240)

        #________________________________________________________________
            

        frame1=Frame(window,width=160,height=110,bg='white')
        frame1.place(x=410,y=220)
        body_massage=PhotoImage(file='body massage.png')
        bodymassage=Button(frame1,image=body_massage,bg='white',bd=0,command=bmassage)
        bodymassage.place(x=-10,y=-10)
        label1=Label(window,text="body massage",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label1.place(x=445,y=330)

        frame2=Frame(window,width=160,height=110,bg='white')
        frame2.place(x=585,y=220)
        body_care=PhotoImage(file='body care.png')
        bodycare=Button(frame2,image=body_care,bg='white',bd=0,command=bcare)
        bodycare.place(x=0,y=0)
        label2=Label(window,text="body care",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label2.place(x=635,y=330)

        frame3=Frame(window,width=160,height=110,bg='white')
        frame3.place(x=760,y=220)
        face_treatment=PhotoImage(file='face treatment.png')
        facetreatment=Button(frame3,image=face_treatment,bg='white',bd=0,command=htreat)
        facetreatment.place(x=-20,y=-10)
        label3=Label(window,text="face treatment",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label3.place(x=800,y=330)

        ##############################################

        window.mainloop()


    def experiences():
        #to create opening window
        window=Toplevel()
        window.title('Pool Experience')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #inserting an image
        img1=PhotoImage(file='pool experience.png')
        Label(window,image=img1,border=0).place(x=220,y=7)

        def Spa():
            #to create opening window
            display=Toplevel()
            display.title('Spa Experience')
            display.geometry('925x500+300+200')
            display.configure(bg='light pink')
            display.resizable(False,False)

            def Gym():
                #to create opening window
                display=Toplevel()
                display.title('Gym Experience')
                display.geometry('925x500+300+200')
                display.configure(bg='black')
                display.resizable(False,False)

                def Dining():
                    #to create opening window
                    display=Toplevel()
                    display.title('Dining Experience')
                    display.geometry('925x500+300+200')
                    display.configure(bg='grey')
                    display.resizable(False,False)

                    def Grounds():
                        #to create opening window
                        display=Toplevel()
                        display.title('Grounds Experience')
                        display.geometry('925x500+300+200')
                        display.configure(bg='dark green')
                        display.resizable(False,False)

                        def Rooms():
                            #to create opening window
                            display=Toplevel()
                            display.title('Rooms Experience')
                            display.geometry('925x500+300+200')
                            display.configure(bg='brown')
                            display.resizable(False,False)


                            #inserting an image
                            img1=PhotoImage(file='room experience.png')
                            Label(display,image=img1,border=0).place(x=220,y=0)

                            #for back button
                            Button(display,width=15,pady=10,text='back', bg='black',fg='white',border=0,command=Grounds).place(x=50,y=230)


                            display.mainloop()

                        #inserting an image
                        img1=PhotoImage(file='grounds.png')
                        Label(display,image=img1,border=0).place(x=180,y=18)

                        #for next button
                        Button(display,width=15,pady=10,text='Next', bg='green',fg='white',border=0,command=Rooms).place(x=750,y=230)

                        #for back button
                        Button(display,width=15,pady=10,text='back', bg='green',fg='white',border=0,command=Dining).place(x=50,y=230)

                        display.mainloop()

                    #inserting an image
                    img1=PhotoImage(file='dining experience.png')
                    Label(display,image=img1,border=0).place(x=320,y=0)
            
                    #for next button
                    Button(display,width=15,pady=10,text='Next', bg='black',fg='white',border=0,command=Grounds).place(x=750,y=230)

                    #for back button
                    Button(display,width=15,pady=10,text='back', bg='black',fg='white',border=0,command=Gym).place(x=50,y=230)

                    display.mainloop()

                #inserting an image
                img1=PhotoImage(file='gym experience.png')
                Label(display,image=img1,border=0).place(x=320,y=-10)

                #for next button
                Button(display,width=15,pady=10,text='Next', bg='grey',fg='white',border=0,command=Dining).place(x=750,y=230)

                #for back button
                Button(display,width=15,pady=10,text='back', bg='grey',fg='white',border=0,command=Spa).place(x=50,y=230)
            
                display.mainloop()
        
            #inserting an image
            img1=PhotoImage(file='spa experience.png')
            Label(display,image=img1,border=0).place(x=205,y=-10)

            #for next button
            Button(display,width=15,pady=10,text='Next', bg='brown',fg='white',border=0,command=Gym).place(x=750,y=230)

            #for back button
            Button(display,width=15,pady=10,text='back', bg='brown',fg='white',border=0,command=experiences).place(x=50,y=230)

            display.mainloop()
    
        #for next button
        Button(window,width=15,pady=10,text='Next', bg='brown',fg='white',border=0,command=Spa).place(x=750,y=230)

        window.mainloop()

    def roombill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

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

                            hotel_id=4
                            room='Suite'
                            st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                            cr.execute(st1)
                            cn.commit()
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*25000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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

                            hotel_id=4
                            room='Deluxe Double Bed'
                            st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                            cr.execute(st1)
                            cn.commit()
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*17000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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
                Button(display,width=30,pady=7,text='Confirm to Proceed', bg='#57a1f8',fg='white',border=0,command=room2bill).place(x=560,y=240)

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

                            hotel_id=4
                            room='Standard Double Bed'
                            st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                            cr.execute(st1)
                            cn.commit()
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*10000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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
                Button(display,width=30,pady=7,text='Confirm to Proceed', bg='#57a1f8',fg='white',border=0,command=room3bill).place(x=560,y=240)
        
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

                            hotel_id=4
                            room='Deluxe Single Bed'
                            st1="insert into Room values({},{},{},'{}','{}','{}',{});".format(booking,customer,hotel_id,room,entry,depart,'NULL')
                            cr.execute(st1)
                            cn.commit()
                    
                            st2="select datediff('{}','{}') from Room where Customer_ID={} and Booking_ID={};".format(depart,entry,customer,booking)
                            cr.execute(st2)
                            data=cr.fetchone()

                            st3="set SQL_SAFE_UPDATES=0;"
                            cr.execute(st3)
                            cn.commit()
                    
                            for i in data:
                                price=i*15000
                                st4="update Room set Price={} where Customer_ID={} and Booking_ID={};".format(price,customer,booking)
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
                Button(display,width=30,pady=7,text='Confirm to Proceed', bg='#57a1f8',fg='white',border=0,command=room4bill).place(x=560,y=240)

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

    def carbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        #inserting an image
        img1=PhotoImage(file='car rent.png')
        Label(window,image=img1,border=0).place(x=0,y=5)

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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=4
                        order=1
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=4
                        order=2
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=4
                        order=3
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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
                hours=code.get()
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
    
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')
                    if car!='' and hours!='':
                        cr=cn.cursor()   
                        command='use resort;'
                        cr.execute(command)

                        hotel_id=4
                        order=4
                
                        st1="insert into Car values({},{},{},{},{},{},{},{},{},{},{});".format(booking,customer,hotel_id,order,car,hours,'NULL','NULL','NULL','NULL','NULL') 
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

    def medicalbill():
        #to create opening window
        window=Toplevel()
        window.title('Billing Page')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #inserting an image
        img1=PhotoImage(file='medical.png')
        Label(window,image=img1,border=0).place(x=25,y=8)
        
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

        #for wheelchair booking button
        Button(window,width=20,pady=7,text='Book Now', bg='turquoise',fg='white',border=0,command=wheelchair).place(x=425,y=120)
    
        #for bed booking button
        Button(window,width=20,pady=7,text='Book Now', bg='turquoise',fg='white',border=0,command=bed).place(x=650,y=330)
    
        #for doctor booking button
        Button(window,width=20,pady=7,text='Book Now', bg='turquoise',fg='white',border=0,command=doctor).place(x=225,y=425)
    
        window.mainloop()
        
    def parking():
        #to create opening window
        window=Toplevel()
        window.title('Parking Service')
        window.geometry('925x500+300+200')
        window.configure(bg='black')
        window.resizable(False,False)

        #inserting an image
        img1=PhotoImage(file='parking.png')
        Label(window,image=img1,border=0).place(x=270,y=3)

        window.mainloop()

        
    #####################################################################
    #for the icons

    frame2=Frame(display,width=130,height=130,bg='white')
    frame2.place(x=110,y=100)
    pool_icon=PhotoImage(file='pool icon.png')
    pool=Button(frame2,image=pool_icon,bg='white',bd=0,command=poolbill)
    pool.place(x=0,y=5)
    label1=Label(frame2,text="pool",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label1.place(x=50,y=105)
    #################################################################################################
    frame3=Frame(display,width=130,height=130,bg='white')
    frame3.place(x=300,y=100)
    gym_icon=PhotoImage(file='gym icon.png')
    gym=Button(frame3,image=gym_icon,bg='white',bd=0,command=gymbill)
    gym.place(x=0,y=10)
    label2=Label(frame3,text="gym",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label2.place(x=50,y=105)

    #################################################################################################

    frame4=Frame(display,width=130,height=130,bg='white')
    frame4.place(x=490,y=100)
    spa_icon=PhotoImage(file='spa icon.png')
    spa=Button(frame4,image=spa_icon,bg='white',bd=0,command=spabill)
    spa.place(x=15,y=11)
    label3=Label(frame4,text="spa",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label3.place(x=50,y=105)

    #################################################################################################

    frame5=Frame(display,width=130,height=130,bg='white')
    frame5.place(x=680,y=100)
    car_icon=PhotoImage(file='car icon.png')
    car=Button(frame5,image=car_icon,bg='white',bd=0,command=carbill)
    car.place(x=-10,y=4)
    label4=Label(frame5,text="transport",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label4.place(x=40,y=105)

    #################################################################################################

    frame6=Frame(display,width=130,height=130,bg='white')
    frame6.place(x=110,y=265)
    room_icon=PhotoImage(file='room icon.png')
    room=Button(frame6,image=room_icon,bg='white',bd=0,command=roombill)
    room.place(x=-10,y=4)
    label5=Label(frame6,text="rooms",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label5.place(x=40,y=105)

    #################################################################################################
    
    frame7=Frame(display,width=130,height=130,bg='white')
    frame7.place(x=300,y=265)
    parking_icon=PhotoImage(file='parking icon.png')
    parking=Button(frame7,image=parking_icon,bg='white',bd=0,command=parking)
    parking.place(x=15,y=5)
    label6=Label(frame7,text="parking",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label6.place(x=40,y=105)

    #################################################################################################

    frame8=Frame(display,width=130,height=130,bg='white')
    frame8.place(x=490,y=265)
    medical_icon=PhotoImage(file='medical icon.png')
    medical=Button(frame8,image=medical_icon,bg='white',bd=0,command=medicalbill)
    medical.place(x=25,y=8)
    label7=Label(frame8,text="medical",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label7.place(x=40,y=105)

    #################################################################################################

    frame9=Frame(display,width=130,height=130,bg='white')
    frame9.place(x=680,y=265)
    experience_icon=PhotoImage(file='experience icon.png')
    experience=Button(frame9,image=experience_icon,bg='white',bd=0,command=experiences)
    experience.place(x=3,y=10)
    label8=Label(frame9,text="experiences",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label8.place(x=30,y=105)

    display.mainloop()

#___________________________________________________________________________________________________
#inserting a frame for the icons
frame1=Frame(display,width=250,height=150,bg='white')
frame1.place(x=30,y=60)
hotel_1=PhotoImage(file='hotel 1.png')
hotel1=Button(frame1,image=hotel_1,bg='white',bd=0,command=option1)
hotel1.place(x=-30,y=-20)
frame_1=Frame(display,width=180,height=100,bg='white')
frame_1.place(x=280,y=80)
label1=Label(frame_1,text="Borcelle Resorts",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label1.place(x=0,y=0)
label2=Label(frame_1,text="Bangalore",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label2.place(x=0,y=20)
label3=Label(frame_1,text="Customer Care: 9652365592",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label3.place(x=0,y=40)
label4=Label(frame_1,text="21/6 Marriem Lane,Bangalore-560012",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label4.place(x=0,y=60)
label5=Label(frame_1,text="Reviews:*****",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label5.place(x=0,y=80)
#################################################################################################

frame2=Frame(display,width=250,height=150,bg='white')
frame2.place(x=30,y=250)
hotel_2=PhotoImage(file='hotel 2.png')
hotel2=Button(frame2,image=hotel_2,bg='white',bd=0,command=option2)
hotel2.place(x=-35,y=-20)
frame_2=Frame(display,width=180,height=100,bg='white')
frame_2.place(x=730,y=80)
label1=Label(frame_2,text="Lenora's Resorts",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label1.place(x=0,y=0)
label2=Label(frame_2,text="Chennai",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label2.place(x=0,y=20)
label3=Label(frame_2,text="Customer Care: 9467613592",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label3.place(x=0,y=40)
label4=Label(frame_2,text="13/4 Kuriyem Street,Chennai-600009",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label4.place(x=0,y=60)
label5=Label(frame_2,text="Reviews:****",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label5.place(x=0,y=80)
#################################################################################################

frame3=Frame(display,width=250,height=150,bg='white')
frame3.place(x=480,y=60)
hotel_3=PhotoImage(file='hotel 3.png')
hotel3=Button(frame3,image=hotel_3,bg='white',bd=0,command=option3)
hotel3.place(x=-35,y=-17)
frame_3=Frame(display,width=180,height=100,bg='white')
frame_3.place(x=280,y=275)
label1=Label(frame_3,text="Kallidan Normann Resorts",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label1.place(x=0,y=0)
label2=Label(frame_3,text="Kolkata",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label2.place(x=0,y=20)
label3=Label(frame_3,text="Customer Care: 9467613592",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label3.place(x=0,y=40)
label4=Label(frame_3,text="7/1 Chatterjee Lane,Kolkata-700012",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label4.place(x=0,y=60)
label5=Label(frame_3,text="Reviews:*****",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label5.place(x=0,y=80)
#################################################################################################

frame4=Frame(display,width=250,height=150,bg='white')
frame4.place(x=480,y=250)
hotel_4=PhotoImage(file='hotel 4.png')
hotel4=Button(frame4,image=hotel_4,bg='white',bd=0,command=option4)
hotel4.place(x=-35,y=-17)
frame_4=Frame(display,width=180,height=100,bg='white')
frame_4.place(x=730,y=275)
label1=Label(frame_4,text="Lenora's Resorts",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label1.place(x=0,y=0)
label2=Label(frame_4,text="Dehradun",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label2.place(x=0,y=20)
label3=Label(frame_4,text="Customer Care: 9875663556",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label3.place(x=0,y=40)
label4=Label(frame_4,text="13/4 Minchem Lane,Dehradun-248012",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label4.place(x=0,y=60)
label5=Label(frame_4,text="Reviews:*****",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
label5.place(x=0,y=80)
#################################################################################################

