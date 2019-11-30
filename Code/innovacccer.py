import tkinter as tk
import tkinter.messagebox
from tkinter import *
import mysql.connector
import datetime
import smtplib
import twilio
HEIGHT = 656
WIDTH = 771
HEIGHT2 = 1500
WIDTH2 = 1500
from Phone import *
from Mail import *
from SQLREQ import *
from openpyxl import Workbook
from database import *

#checking if the user have already checked in and trying to checkin again without checking out first
#Also checking the validity of the email address entered

def checkifalradychecked(entry):
    mydb = mysql.connector.connect(host=Host,user=User,password=Pass,auth_plugin=auth_plugin_1,database=database_1)
    mycursor = mydb.cursor()
    fr="select * from users where v_email=%s;"
    mycursor.execute(fr,(entry,))
    myresult=mycursor.fetchall()
    mail=entry
    flag=33
    for i in range(len(mail)):
        if mail[i] is '@':
            flag=1
            if not myresult:
                checkin(entry)

            else:
                db = mysql.connector.connect(host=Host,user=User,password=Pass,auth_plugin=auth_plugin_1,database=database_1)
                cr = db.cursor()
                formula="select * from users where v_email=%s"
                cr.execute(formula,(entry,))
                result=cr.fetchall()
                if not result:
                    checkin(entry)
                else:
                    outtime=""
                    intime=""
                    for i in result:
                        intime=i[7]
                        outtime=i[8]
                    if not outtime:
                        messagebox.showerror("ALERT!!!", "User is already checked in")
                    else:

                        checkin(entry)
            break
        else:
            flag=0
    if flag == 0:
        messagebox.showerror("ALERT!!!", "Invalid Input")




#database entry
#Sending the details to the email and sms functions

def submit(a,b,c,d,e,f,g,top):

    checkin_time = datetime.datetime.now()
    mydb = mysql.connector.connect(host=Host,user=User,password=Pass,auth_plugin=auth_plugin_1,database=database_1)
    mycursor = mydb.cursor()
    sqlFormula = "insert into users values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    visitor1=(a,b,g,c,d,e,f,checkin_time,"")
    mycursor.execute(sqlFormula,visitor1)
    mydb.commit()
    email(a,b,c,d,e,f,g,checkin_time)
    sms(a,b,c,d,e,f,g,checkin_time)
    messagebox.showinfo("Message", "Checkin successfull")
    close_window(top)


#closing the window when the task is done for entry of the data

def close_window(top):
    top.destroy()


#gui design for the checkin page
#entry of data

def checkin(entry):

    top = tk.Tk()
    top.title("Entry Management Software")
    top.geometry("1500x1500")
    frame2 = tk.Frame(top,bg='pink',bd=5)
    frame2.place(relx=0,rely=0,relwidth=1 , relheight=1)
    new=tk.Label(frame2,text="Visitor information",bg="pink",font=('Arial', 16, 'bold', 'italic'),foreground="purple")
    new.place(x=500,y=20)

    name = tk.Label(frame2, text = "Visitor Name",bg="pink",font=("Candara",13,"bold"),foreground="purple")
    name.place(x = 470,y = 50)
    visitor_email=entry
    phone_no = tk.Label(frame2, text = "Visitor Phone No",bg="pink",font=("Candara",13,"bold"),foreground="purple")
    phone_no.place(x = 470, y = 90)

    background_image2 = tk.PhotoImage(file='innov3.png')
    background_label2 = tk.Label(root,image=background_image2,bg="pink")
    background_label2.place(relx=0.5,rely=1,anchor='s')

    new=tk.Label(frame2,text="Host information",bg="pink",font=('Arial', 16, 'bold', 'italic'),foreground="purple")
    new.place(x=500,y=130)
    name_host=tk.Label(frame2,text = "Host Name",bg="pink",font=("Candara",13,"bold"),foreground="purple")
    name_host.place(x = 470,y = 160)
    email_host=tk.Label(frame2,text = "Host email",bg="pink",font=("Candara",13,"bold"),foreground="purple")
    email_host.place(x = 470,y = 200)
    phnno_host=tk.Label(frame2,text = "Host phoneno",bg="pink",font=("Candara",13,"bold"),foreground="purple")
    phnno_host.place(x = 470,y = 240)
    host_address=tk.Label(frame2,text = "Host address",bg="pink",font=("Candara",13,"bold"),foreground="purple")
    host_address.place(x = 470,y = 280)
    sbmitbtn = tk.Button(frame2, text = "Submit",bg="white",activebackground = "pink", activeforeground = "white",bd=3,command=lambda:submit(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),visitor_email,top))
    sbmitbtn.place(x = 550, y = 340,relwidth=0.2)
    e1 = tk.Entry(frame2,bd=4)
    e1.place(x = 600, y = 50,relwidth=0.3)
    e2 = tk.Entry(frame2,bd=4)
    e2.place(x = 600, y = 90,relwidth=0.3)
    e3 = tk.Entry(frame2,bd=4)
    e3.place(x = 600, y = 160,relwidth=0.3)
    e4 = tk.Entry(frame2,bd=4)
    e4.place(x = 600, y = 200,relwidth=0.3)
    e5 = tk.Entry(frame2,bd=4)
    e5.place(x = 600, y = 240,relwidth=0.3)
    e6 = tk.Entry(frame2,bd=4)
    e6.place(x = 600, y = 280,relwidth=0.3)



    top.mainloop()

#checkout after the validation of the key i.e email address

def checkout(entry):
    #email to the visitor
    answer = tkinter.messagebox.askquestion('Question 1','Checkout Confirmation')
    if answer == 'yes':
        checkout_time = datetime.datetime.now()
        mydb = mysql.connector.connect(host=Host,user=User,password=Pass,auth_plugin=auth_plugin_1,database=database_1)
        mycursor = mydb.cursor()
        fr="select * from users where v_email=%s;"
        mycursor.execute(fr,(entry,))
        myresult=mycursor.fetchall()
        if not myresult:
            messagebox.showerror("ALERT!!!", "Please check in first")
        else:
            for row in myresult:
                ct=row[8]
                ci=row[7]
                ha=row[6]
                hp=row[5]
                he=row[4]
                hn=row[3]
                ve=row[2]
                vp=row[1]
                vn=row[0]
                if len(ct) is 0:
                    #print("here")
                    emailvisitor(entry,vn,vp,hn,he,hp,ha,ci,str(checkout_time))
                    #print("there")
                    sqlFormula = "update users set checkout =%s where v_email=%s;"
                    mycursor.execute(sqlFormula,(checkout_time,entry))
                    mydb.commit()
                    exit()
            messagebox.showerror("ALERT!!!", "User has already checked out")
            exit()
        #email to visitor with information




#main GUI

root=tk.Tk()
menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="File",menu=subm1)
subm1.add_command(label="Export data to excel sheet",command=data())
root.title("Entry Management Software")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH,bg="pink")
canvas.pack()
background_image = tk.PhotoImage(file='zez9iqg8lghajcaq65ai.png')
background_label = tk.Label(root,image=background_image,bg="pink",bd=5)
background_label.place(relx=0.5,rely=0.1,relwidth=1,relheight=1,anchor='center')

background_image2 = tk.PhotoImage(file='innov3.png')
background_label2 = tk.Label(root,image=background_image2,bg="pink")
background_label2.place(relx=0.5,rely=1,relwidth=1,anchor='s')
frame = tk.Frame(root,bg='pink',bd=5)
frame.place(relx=0.5,rely=0.25,relwidth=0.75 , relheight=0.1,anchor='n')

button1 = tk.Button(frame,text="CheckIN",bg="white",bd=5,font=40,command= lambda:checkifalradychecked(entry.get()))
button1.place(relx=0.7,relwidth=0.3,relheight=0.45)

root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='logo.png'))

entry = tk.Entry(frame,font=40,bd=5)
entry.place(relwidth=0.65,relheight=1)

button2 = tk.Button(frame,text="CheckOUT",bg="white",bd=5,font=40,command=lambda:checkout(entry.get()))
button2.place(relx=0.7,rely=0.5,relwidth=0.3,relheight=0.45)

lower_frame = tk.Frame(root,bg='pink',bd=10)
lower_frame.place(relx=0.5,rely=0.15,relwidth=0.75,relheight=0.1,anchor='n')

label = tk.Label(lower_frame,text="Please Enter Your Email Address",bg='pink',font=40)
label.place(relx=0.15,rely=0.15,relwidth=0.7,relheight=0.5)

root.mainloop()

