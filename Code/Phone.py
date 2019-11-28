import tkinter as tk
import tkinter.messagebox
from tkinter import *
import mysql.connector
import datetime
import smtplib
import twilio
def sms(a,b,c,d,e,f,g,h):
    from twilio.rest import Client

    # Your Account SID from twilio.com/console
    account_sid = " "
    # Your Auth Token from twilio.com/console
    auth_token  = " "

    client = Client(account_sid, auth_token)
    strinq='Subject: Visitor information \n\n '+'There is a visitor to meet you . Visitor Information is:'+'\nName: '+a+'\nPhone no: '+b+'\nCheckin time: '+str(h)+' .'
    message = client.messages.create(
        to=str(e),
        from_="enter the number you get from twilio ",
        body=strinq)
