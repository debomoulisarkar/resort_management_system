import tkinter as tk
from tkinter import *
from tkinter import messagebox

#to create opening window
window=Tk()
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
                    display.mainloop()

                #inserting an image
                img1=PhotoImage(file='grounds.png')
                Label(display,image=img1,border=0).place(x=180,y=18)

                #for next button
                Button(display,width=15,pady=10,text='Next', bg='brown',fg='white',border=0,command=Rooms).place(x=750,y=230)
                display.mainloop()

            #inserting an image
            img1=PhotoImage(file='dining experience.png')
            Label(display,image=img1,border=0).place(x=280,y=0)
            
            #for next button
            Button(display,width=15,pady=10,text='Next', bg='black',fg='white',border=0,command=Grounds).place(x=750,y=230)
            display.mainloop()

        #inserting an image
        img1=PhotoImage(file='gym experience.png')
        Label(display,image=img1,border=0).place(x=280,y=-10)

        #for next button
        Button(display,width=15,pady=10,text='Next', bg='grey',fg='white',border=0,command=Dining).place(x=750,y=230)
        display.mainloop()
        
    #inserting an image
    img1=PhotoImage(file='spa experience.png')
    Label(display,image=img1,border=0).place(x=120,y=-10)

    #for next button
    Button(display,width=15,pady=10,text='Next', bg='brown',fg='white',border=0,command=Gym).place(x=750,y=230)
    display.mainloop()
    
#for next button
Button(window,width=15,pady=10,text='Next', bg='brown',fg='white',border=0,command=Spa).place(x=750,y=230)

window.mainloop()


