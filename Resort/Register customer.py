#REGISTER using Tkinter
from tkinter import *
from tkinter import messagebox
import ast
import csv
import random
import mysql.connector as mc

#to create opening window
window=Tk()
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
            print('connection is successful',cn)
            
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
user=Entry(width=25,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
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
code=Entry(width=25,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
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
confirm_code=Entry(width=25,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
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
phone=Entry(width=25,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
phone.place(x=600,y=240)
phone.insert(0,'Phone Number')
phone.bind('<FocusIn>',on_enter)
phone.bind('<FocusOut>',on_leave)

##############################################

#sign up button
Button(width=25,pady=7,text='Sign Up', bg='#57a1f8',fg='white',border=0,command=signup).place(x=610,y=270)
label=Label(text='I have an account',fg='black',font=('Microsoft YaHei UI Light',9))
label.place(x=655,y=310)

#sign in option
signin=Button(width=6,text='Sign In',border=0,cursor='hand2',fg='#57a1f8', command=sign)
signin.place(x=680,y=330)

window.mainloop()
