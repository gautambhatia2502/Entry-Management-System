import tkinter as tk
import tkinter.messagebox
from tkinter import *
import mysql.connector
import datetime
import smtplib
import twilio
email_address='Enter the email address from which you want to send the email'
password='enter the password for email_address'
def email(a,b,c,d,e,f,g,h):
    connection = smtplib.SMTP('smtp.gmail.com',587)
    connection.ehlo()
    connection.starttls()
    connection.login(email_address,password)
    strinq='Subject: Visitor information \n\n '+'Visitor Information is:'+'\nName: '+a+'\nPhone no: '+b+'\nCheckin time: '+str(h)+' .'
    connection.sendmail(email_address,d,strinq)
    connection.quit()


def emailvisitor(entry,vn,vp,hn,he,hp,ha,ci,ct):
    #print(entry)
    connection = smtplib.SMTP('smtp.gmail.com',587)
    connection.ehlo()
    connection.starttls()
    connection.login(email_address,password)
    strin= 'Subject: Your visit report \n\n Visitor Name:'+vn+'\nHost Name:'+hn+'\nPhone no :'+hp+'\n Host address:'+ha+'\nCheckin Time: '+ci+'\nCheckout Time:'+ct
    connection.sendmail(email_address,entry,strin)
    connection.quit()
