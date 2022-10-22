import os
import math
import random
import smtplib
from tkinter import * 
import tkinter as tk
from tkinter import messagebox

global Otp 
root=Tk()
root.title("")



def validation1():
    Email = e1.get()
    if len(Email)==0:
        e1.configure(bg='red')
        messagebox.showinfo('Email OTP Verification','Fill the fields marked in red')
    '''elif (Email[len(Email)-3] != '.' or Email[len(Email)-4] != '.'):
        e1.configure(bg='red')
        messagebox.showinfo('Email OTP Verification','Enter Proper Email Address')'''

    

def validation2():
    OTP = e2.get()
    if len(OTP)==0:
        e2.configure(bg='red')
        messagebox.showinfo('Email OTP Verification','Fill the fields marked in red')

        
def sotp():
    Email = e1.get()
    global Otp
    digits = "0123456789"
    Otp = ""
    for i in range (8):
        Otp+= digits[math.floor(random.random()*10)]
    otp = "Don't reveal the OTP to anyone! \n" + Otp + " is your OTP"
    message = otp
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("hyeah933@gmail.com", "iqsjwulhsrkntpia")
    s.sendmail('&&&&&&',Email,message)
    messagebox.showinfo('Email OTP Verification','Please check the sent OTP')

def verify():
    OTP = e2.get()
    if (OTP == Otp):
        messagebox.showinfo('Email OTP Verification','Email Verified')
    else:
        messagebox.showinfo('Email OTP Verification','Please check the OTP or Email ID')
    
c1=Canvas(root, width = 500, height = 400, bg="white")
c1.pack()

l1=Label(root, text='Email Verification')
l1.config(font=("bold", 20),bg="black",fg='white')
c1.create_window(250, 30, window=l1)

br1=Label(root, text='------------------------------------------------------------')
br1.config(font=("bold", 18),bg="white",fg='grey')
c1.create_window(250, 80, window=br1)

l2=Label(root, text='EMAIL:')
l2.config(font=('helvetica',18),bg="white")
c1.create_window(80, 120, window=l2)
e1=Entry(root,font=(18),borderwidth=3, width = 25)
c1.create_window(280, 120, window=e1)

l9=Label(root, text='OTP:')
l9.config(font=('helvetica',18),bg="white")
c1.create_window(75, 270, window=l9)
e2=Entry(root,font=(30),borderwidth=3, width = 8)
c1.create_window(210, 270, window=e2)

br2=Label(root, text='------------------------------------------------------------')
br2.config(font=("bold", 18),bg="white",fg='grey')
c1.create_window(250, 220, window=br2)

br1=Label(root, text='------------------------------------------------------------')
br1.config(font=("bold", 18),bg="white",fg='grey')
c1.create_window(250, 370, window=br1)

#command=sotp
Submit=Button(text='Verify',command=lambda:[validation1(),validation2(),verify()], bg='pink', fg='black', font=('helvetica', 15, 'bold'))
c1.create_window(250, 330, window=Submit)
Sendotp=Button(text='Send OTP',command=lambda:[ validation1(),sotp()], bg='pink', fg='black', font=('helvetica', 15, 'bold'))
c1.create_window(250, 180, window=Sendotp)
