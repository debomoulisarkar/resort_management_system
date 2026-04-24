#SIGN IN page using tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ast

#creating opening screen
root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

#username and password check
import csv
def signin():
    username=user.get()
    password=code.get()
    file=open('account.csv','r')
    try:
        csvrd=csv.reader(file)
        for i in csvrd:
            if i[0]=='' or i[1]=='':
                if i[0]=='' and i[1]==password:
                    messagebox.showerror('Invalid','Please enter username to sign in')
                if i[0]==username and i[1]=='':
                    messagebox.showerror('Invalid','Please enter password to sign in')
            if i[0]==username and i[1]==password:
                screen=Toplevel(root)
                screen.title('App')
                screen.geometry('925x500+300+200')
                screen.config(bg='white')
        
                Label(screen,text='Hello everyone!',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)
                screen.mainloop()
                break
                
        else:
            messagebox.showerror('Invalid','Invalid username or password')
    except EOFError:
        messagebox.showerror('Invalid','File Ended')
    file.close()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import csv
def signup_command():
    window=Toplevel(root)
    window.title('SignUp')
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)

    #username and password check
    def signup():
        lst=[]
        username=user.get()
        password=code.get()
        confirm_password=confirm_code.get()
        if password==confirm_password and username!='' and password!='':
                file=open('account.csv','a+',newline='')
                swrt=csv.writer(file)
                lst=[username,password]
                swrt.writerow(lst)
                file.close()

                messagebox.showinfo('SignUp','Successfully signed up')
            
        else:
            messagebox.showerror('Invalid','Please confirm the same password')

    def sign():
        window.destroy()

    #inserting an image
    img=PhotoImage(file='login2.png')
    Label(window,image=img,border=0).place(x=-30,y=-190)

    ################################################

    #inserting text box email
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Email ID')
    user=Entry(window,width=25,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
    user.place(x=100,y=140)
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
    code.place(x=100,y=180)
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
    confirm_code.place(x=100,y=220)
    confirm_code.insert(0,'Confirm Password')
    confirm_code.bind('<FocusIn>',on_enter)
    confirm_code.bind('<FocusOut>',on_leave)

    ##############################################

    #sign up button
    Button(window,width=25,pady=7,text='Sign Up', bg='#57a1f8',fg='white',border=0,command=signup).place(x=110,y=255)
    label=Label(window,text='I have an account',fg='black',font=('Microsoft YaHei UI Light',9))
    label.place(x=140,y=300)

    #sign in option
    signin=Button(window,width=6,text='Sign In',border=0,cursor='hand2',fg='#57a1f8',command=sign)
    signin.place(x=170,y=330)

    window.mainloop()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#inserting image
img=PhotoImage(file='login1.png')
Label(root,image=img).place(x=-40,y=-190)


########################################################

#inserting text box username
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user= Entry(width=35,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
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
code= Entry(width=35,fg='black',border=0,font=('Microsoft YaHei UI Light',11))
code.place(x=50,y=180)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

#hide and show button
button_mode=True
def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=closeeye,activebackground='white')
        code.config(show='*')
        button_mode=False
    else:
        eyeButton.config(image=openeye,activebackground='white')
        code.config(show='')
        button_mode=True
 
openeye=PhotoImage(file='open eye.png')
closeeye=PhotoImage(file='close eye.png')
eyeButton=Button(image=openeye,bg='white',bd=0,command=hide)
eyeButton.place(x=330,y=178)

########################################################

#sign in button
Button(width=39,pady=7,text='Sign In', bg='#57a1f8',fg='white',border=0,command=signin).place(x=50,y=230)
label=Label(text="Don't have an account?",fg='black',font=('Microsoft YaHei UI Light',9))
label.place(x=120,y=280)

#sign up option
sign_up=Button(width=6,text='Sign Up',border=0,cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=170,y=310)

root.mainloop()

