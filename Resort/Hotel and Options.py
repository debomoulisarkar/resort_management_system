#hotel and options page

import tkinter as tk
from tkinter import *
from tkinter import messagebox

#to create opening window
display=Tk()
display.title('Hotel Page')
display.geometry('925x500+300+200')
display.configure(bg='#fff')
display.resizable(False,False)

#inserting an image
img1=PhotoImage(file='hotel page.png')
Label(display,image=img1,border=0).place(x=0,y=0)
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
label3=Label(frame_3,text="Customer Care: 9892665359",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
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
label1=Label(frame_4,text="Margot Roberts Resorts",fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
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

