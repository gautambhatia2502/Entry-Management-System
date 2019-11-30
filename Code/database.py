import tkinter as tk
import tkinter.messagebox
from tkinter import *
import mysql.connector
import datetime
import smtplib
import twilio
from Phone import *
from Mail import *
from SQLREQ import *
from openpyxl import Workbook
def data():

    wb = Workbook()
    mydb = mysql.connector.connect(host=Host,user=User,password=Pass,auth_plugin=auth_plugin_1,database=database_1)
    mycursor = mydb.cursor()
    SQL = 'SELECT * from users;'
    mycursor.execute(SQL)
    results = mycursor.fetchall()
    ws = wb.create_sheet()
    ws.append(mycursor.column_names)
    for row in results:
        ws.append(row)

    workbook_name = database_1
    wb.save(workbook_name + ".xlsx")
