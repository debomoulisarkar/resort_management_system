#SIGN IN page using tkinter
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
                        screen=Toplevel(root)
                        screen.title('App')
                        screen.geometry('925x500+300+200')
                        screen.config(bg='white')
                        Label(screen,text='Hello everyone!',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)
                        screen.mainloop()
                
                    elif j[0]!=username or j[1]!=password:
                        messagebox.showerror('Invalid','Invalid username or password')
    except EOFError:
        messagebox.showerror('Invalid','File Ended')
    file.close()
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


########################################################

#sign in button
Button(width=39,pady=7,text='Sign In', bg='#57a1f8',fg='white',border=0,command=signin).place(x=50,y=230)
label=Label(text="Don't have an account?",fg='black',font=('Microsoft YaHei UI Light',9))
label.place(x=120,y=280)

#sign up option
sign_up=Button(width=6,text='Sign Up',border=0,cursor='hand2',fg='#57a1f8')
sign_up.place(x=170,y=310)

root.mainloop()

