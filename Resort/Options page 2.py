import tkinter as tk
from tkinter import *
from tkinter import messagebox

#to create opening window
display=Tk()
display.title('Home Page')
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

#for the icons

frame2=Frame(display,width=130,height=130,bg='white')
frame2.place(x=110,y=100)
pool_icon=PhotoImage(file='pool icon.png')
pool=Button(frame2,image=pool_icon,bg='white',bd=0)
pool.place(x=0,y=5)
label1=Label(frame2,text="pool",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label1.place(x=50,y=105)
#################################################################################################
frame3=Frame(display,width=130,height=130,bg='white')
frame3.place(x=300,y=100)
gym_icon=PhotoImage(file='gym icon.png')
gym=Button(frame3,image=gym_icon,bg='white',bd=0)
gym.place(x=0,y=10)
label2=Label(frame3,text="gym",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label2.place(x=50,y=105)

#################################################################################################

frame4=Frame(display,width=130,height=130,bg='white')
frame4.place(x=490,y=100)
sauna_icon=PhotoImage(file='sauna icon.png')
sauna=Button(frame4,image=sauna_icon,bg='white',bd=0)
sauna.place(x=15,y=11)
label3=Label(frame4,text="sauna",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label3.place(x=50,y=105)

#################################################################################################

frame5=Frame(display,width=130,height=130,bg='white')
frame5.place(x=680,y=100)
car_icon=PhotoImage(file='car icon.png')
car=Button(frame5,image=car_icon,bg='white',bd=0)
car.place(x=-10,y=4)
label4=Label(frame5,text="transport",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label4.place(x=40,y=105)

#################################################################################################

frame6=Frame(display,width=130,height=130,bg='white')
frame6.place(x=110,y=265)
room_icon=PhotoImage(file='room icon.png')
room=Button(frame6,image=room_icon,bg='white',bd=0)
room.place(x=-10,y=4)
label5=Label(frame6,text="rooms",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label5.place(x=40,y=105)

#################################################################################################

frame7=Frame(display,width=130,height=130,bg='white')
frame7.place(x=300,y=265)
parking_icon=PhotoImage(file='parking icon.png')
parking=Button(frame7,image=parking_icon,bg='white',bd=0)
parking.place(x=15,y=5)
label6=Label(frame7,text="parking",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label6.place(x=40,y=105)

#################################################################################################

frame8=Frame(display,width=130,height=130,bg='white')
frame8.place(x=490,y=265)
medical_icon=PhotoImage(file='medical icon.png')
medical=Button(frame8,image=medical_icon,bg='white',bd=0)
medical.place(x=25,y=8)
label7=Label(frame8,text="medical",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label7.place(x=40,y=105)

#################################################################################################

frame9=Frame(display,width=130,height=130,bg='white')
frame9.place(x=680,y=265)
experience_icon=PhotoImage(file='experience icon.png')
experience=Button(frame9,image=experience_icon,bg='white',bd=0)
experience.place(x=3,y=10)
label8=Label(frame9,text="experiences",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label8.place(x=30,y=105)








display.mainloop()
