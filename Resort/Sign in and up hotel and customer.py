#Home Page using Tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ast
import random
import csv
import mysql.connector as mc

#to create opening window
screen=Tk()
screen.title('Home Page')
screen.geometry('925x500+300+200')
screen.configure(bg='#fff')
screen.resizable(False,False)
#-----------------------------------------------------------------------------------------
def hotel():
    #creating opening screen
    root=Toplevel()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg='#fff')
    root.resizable(False,False)
    
    #username and password check
    def signin():
        username=user.get()
        password=code.get()
        file=open('account.csv','r')
        csvrd=csv.reader(file)
        for i in csvrd:
            print (i)
        file.close()
        file=open('account.csv','r',newline='')
        try:
            csvrd=csv.reader(file)
            for i in csvrd:
                for j in i:
                    if len(j)<2:
                        continue
                    if len(j)==2:
                        if j[0]=='' or j[1]=='':
                            if j[0]=='' and j[1]==password:
                               messagebox.showerror('Invalid','Please enter username to sign in')
                            if j[0]==username and j[1]=='':
                                messagebox.showerror('Invalid','Please enter password to sign in')
                        if j[0]=='Username' and j[1]=='Password':
                            continue
                        if j[0]==username and j[1]==password:
                            messagebox.showinfo('Connected','Successfully signed in')

                
                        elif j[0]!=username or j[1]!=password:
                            messagebox.showerror('Invalid','Invalid username or password')
        except EOFError:
            messagebox.showerror('Invalid','File Ended')
        file.close()
    #inserting image
    img=PhotoImage(file='login1.png')
    Label(root,image=img).place(x=-40,y=-190)

    ########################################################

    #inserting text box mail
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user= Entry(root,width=35,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    user.place(x=50,y=140)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)


    ########################################################

    #inserting text box password
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')
    code= Entry(root,width=35,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    code.place(x=50,y=180)
    code.insert(0,'Password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)


    ########################################################

    #sign in button
    Button(root,width=39,pady=7,text='Sign In', bg='#57a1f8',fg='white',border=0,command=signin).place(x=50,y=230)

    root.mainloop()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def customer():
    #creating an opening window
    root=Toplevel()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg='#fff')
    root.resizable(False,False)
    
    #username and password check and connect with database
    def signin():
        mail=user.get()
        password=code.get()
        if (mail=='' or mail=='Email ID') or (password=='' or password=='Password'):
                messagebox.showerror('Entry error','Type mail or password')
        else:
            try:
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
                cr=cn.cursor()
                print('Connection is successful')   

            except:
                messagebox.showerror('Connection','Connection is not created')
                return

            st='use resort;'
            cr.execute(st)
        
            st="select * from customer_signup where Mail=%s and Passwd=%s;"
            cr.execute(st,(mail,password))
            data=cr.fetchone()
            print(data)

            if data==None:
                messagebox.showinfo('Invalid','Invalid Mail ID or Password')

            
            else:
                messagebox.showinfo('Sign In','Successfully Signed In!')
            cn.close()
    #____________________________________________________________________________

    def signup_command():
        window=Toplevel(root)
        window.title('Register')
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        #mail and password check
        def signup():
            lst=[]
            mail=user.get()
            password=code.get()
            confirm_password=confirm_code.get()
            phone_number=phone.get()
            customer=random.randint(0,1000)
            if password==confirm_password and mail!='' and password!='':
                cn=mc.connect(host='localhost',user='root',passwd='d654321$',database='resort')
              
                if cn.is_connected()==False:
                    print('connection is not created')
                else:
                    print('connection is successful')

                    command='use resort;'
                    st="insert into customer_signup values({},'{}','{}','{}');".format(customer,password,phone_number,mail)
                    cr=cn.cursor()
                    cr.execute(command)
                    cr.execute(st)
                    cn.commit()
                    cn.close()

                    messagebox.showinfo('SignUp','Successfully signed up')
            
            else:
                messagebox.showerror('Invalid','Please confirm the same password')
                

        def sign():
            window.destroy()

        #inserting an image
        img=PhotoImage(file='login3.png')
        Label(window,image=img,border=0).place(x=0,y=0)

        ################################################

        #inserting text box email
        def on_enter(e):
            user.delete(0,'end')
        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'Email ID')
        user=Entry(window,width=25,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        user.place(x=600,y=150)
        user.insert(0,'Email ID')
        user.bind('<FocusIn>',on_enter)
        user.bind('<FocusOut>',on_leave)

        ###############################################

        #inserting text box password
        def on_enter(e):
            code.delete(0,'end')
        def on_leave(e):
            name=code.get()
            if name=='':
                code.insert(0,'Password')
        code=Entry(window,width=25,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        code.place(x=600,y=180)
        code.insert(0,'Password')
        code.bind('<FocusIn>',on_enter)
        code.bind('<FocusOut>',on_leave)

        ##############################################

        #inserting text box confirm password
        def on_enter(e):
            confirm_code.delete(0,'end')
        def on_leave(e):
            name=confirm_code.get()
            if name=='':
                confirm_code.insert(0,'Confirm Password')
        confirm_code=Entry(window,width=25,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        confirm_code.place(x=600,y=210)
        confirm_code.insert(0,'Confirm Password')
        confirm_code.bind('<FocusIn>',on_enter)
        confirm_code.bind('<FocusOut>',on_leave)

        ##############################################

        #inserting text box Phone number
        def on_enter(e):
            phone.delete(0,'end')
        def on_leave(e):
            name=phone.get()
            if name=='':
                phone.insert(0,'Phone Number')
        phone=Entry(window,width=25,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
        phone.place(x=600,y=240)
        phone.insert(0,'Phone Number')
        phone.bind('<FocusIn>',on_enter)
        phone.bind('<FocusOut>',on_leave)

        ##############################################

        #sign up button
        Button(window,width=25,pady=7,text='Sign Up', bg='#57a1f8',fg='white',border=0,command=signup).place(x=610,y=270)
        label=Label(window,text='I have an account',fg='black',font=('Microsoft YaHei UI Light',9))
        label.place(x=655,y=310)

        #sign in option
        signin=Button(window,width=6,text='Sign In',border=0,cursor='hand2',fg='#57a1f8', command=sign)
        signin.place(x=680,y=330)

        window.mainloop()
    #____________________________________________________________________________

    #inserting image
    img=PhotoImage(file='login1.png')
    Label(root,image=img).place(x=-40,y=-190)

    ########################################################

    #inserting text box mail
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user= Entry(root,width=35,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    user.place(x=50,y=140)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)


    ########################################################

    #inserting text box password
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')
    code= Entry(root,width=35,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    code.place(x=50,y=180)
    code.insert(0,'Password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    ########################################################

    #sign in button
    Button(root,width=39,pady=7,text='Sign In', bg='#57a1f8',fg='white',border=0,command=signin).place(x=50,y=230)
    label=Label(root,text="Don't have an account?",fg='black',font=('Microsoft YaHei UI Light',9))
    label.place(x=120,y=280)

    #sign up option
    sign_up=Button(root,width=6,text='Sign Up',border=0,cursor='hand2',fg='#57a1f8',command=signup_command)
    sign_up.place(x=170,y=310)

    root.mainloop()
#-----------------------------------------------------------------------------------------

#inserting an image
img=PhotoImage(file='home page.png')
Label(screen,image=img,border=0).place(x=-20,y=-30)

#inserting button for customer and hotel staff
custom=Button(width=20,pady=7,text='Customer', bg='dark green',fg='white',border=0,command=customer)
custom.place(x=340,y=325)
hot=Button(width=20,pady=7,text='Hotel', bg='dark green',fg='white',border=0,command=hotel)
hot.place(x=515,y=325)

screen.mainloop()
