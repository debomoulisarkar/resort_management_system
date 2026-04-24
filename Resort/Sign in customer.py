#SIGN IN customer page using tkinter
from tkinter import *
from tkinter import messagebox
import ast
import csv
import random
import mysql.connector as mc

#creating opening screen
root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

#username and password check and connect with database
import csv
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

        command='use resort;'
        cr.execute(command)
        
        st="select * from customer_signup where Mail=%s and Passwd=%s;"
        cr.execute(st,(mail,password))
        data=cr.fetchone()
        print(data)

        if data==None:
            messagebox.showinfo('Invalid','Invalid Mail ID or Password')

            
        else:
            messagebox.showinfo('Sign In','Successfully Signed In!')
        cn.close()
        
        
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
        user.insert(0,'Email ID')
user= Entry(width=35,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
user.place(x=50,y=140)
user.insert(0,'Email ID')
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
code= Entry(width=35,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
code.place(x=50,y=180)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)


########################################################

#sign in button
Button(width=39,pady=7,text='Sign In', bg='#57a1f8',fg='white',border=0,command=signin).place(x=50,y=230)
label=Label(text="Don't have an account?",fg='black',font=('Microsoft YaHei UI Light',9))
label.place(x=120,y=280)

#sign up option
sign_up=Button(width=6,text='Sign Up',border=0,cursor='hand2',fg='#57a1f8')
sign_up.place(x=170,y=310)

root.mainloop()

