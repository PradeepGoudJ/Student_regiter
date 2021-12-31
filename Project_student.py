import tkinter as tk
from tkinter.constants import X, Y
from tkinter.font import BOLD
from typing import Text
import sqlite3

con = sqlite3.connect('studentDev.db')

cur = con.cursor()
#cur.execute("create table details(FirstName text, LastName text, Age number, MailId text)")

def checkMail(mailid):
    #print("checkMail called & MID: ",mailid)
    mailids = cur.execute("select MailId from details")
    mailList = []
    for row in mailids:
        mailList.append(row[0])

    if mailid in mailList:
        return userExists()
    else:
        return "New User"

def checkMailLogin(mailid):
    #print("checkMail called & MID: ",mailid)
    mailids = cur.execute("select MailId from details")
    mailList = []
    for row in mailids:
        mailList.append(row[0])

    if mailid in mailList:
        return openAc()
    else:
        return noMailAlert()   #add dialogue screen = mailId not found   


def Enter():
    #print("Enter called")
    data = (FirstName.get(),LastName.get(),Age.get(),MailId.get())
    if checkMail(MailId.get()) == "New User":
        cur.execute("insert into details values (?,?,?,?)",data)
        con.commit()
        return success()
    else:
        return "User exists"


    

top = tk.Tk() 
top.geometry("500x450")
top.title("Student Registration Form")


qres = cur.execute("select * from details")
for r in qres:
    print(r)

def userExists():
    ueTop =  tk.Toplevel(top)
    ueTop.geometry("300x150")
    ueTop.title("Alert")
    alertL = tk.Label(ueTop,text = "User Already Exists")
    alertL.place(x= 100, y= 60)
    ueTop.mainloop()

def success():
    ueTop =  tk.Toplevel(top)
    ueTop.geometry("300x150")
    ueTop.title("Alert")
    alertL = tk.Label(ueTop,text = "User created successfully!")
    alertL.place(x= 100, y= 60)
    ueTop.mainloop()

def LoginForm():
    loginTop = tk.Toplevel(top)
    loginTop.geometry("420x210")
    loginTop.title("LoginForm")
    mailL = tk.Label(loginTop,text= "MailId",font=10)
    mailL.place(x= 130, y= 80)
    mailV = tk.StringVar()
    mailE = tk.Entry(loginTop,textvariable= mailV)
    mailE.place(x= 180,y= 80)
    Loginb = tk.Button(loginTop,text="Login",width=10,height=1,command= lambda:checkMailLogin( mailV.get()))
    Loginb.place(x=180 ,y= 130)
    loginTop.mainloop()

def openAc():
    openAcTop = tk.Toplevel(top)
    openAcTop.geometry("450x320")
    openAcTop.title("home")
    openAcL = tk.Label(openAcTop,text= "THIS IS THE HOME PAGE!!",font= 20)
    openAcL.pack()
    logoutB = tk.Button(openAcTop,text= "Logout",command= openAcTop.destroy) 
    logoutB.pack()
    openAcTop.mainloop()

def noMailAlert():
    ueTop =  tk.Toplevel(top)
    ueTop.geometry("300x150")
    ueTop.title("Alert")
    alertL = tk.Label(ueTop,text = "MailId not found")
    alertL.place(x= 100, y= 60)
    ueTop.mainloop()


FirstName= tk.StringVar()
Fn = tk.Label(top,text = "First Name",font= 15)
Fn.place(x=140,y=50)
FnEntry = tk.Entry(top,textvariable= FirstName)
FnEntry.place(x=230,y=50)

LastName= tk.StringVar()
Ln = tk.Label(top,text = "Last Name",font= 15)
Ln.place(x=140,y=90)
LnEntry = tk.Entry(top,textvariable= LastName)
LnEntry.place(x=230,y=90)

Age= tk.StringVar()
AgeL = tk.Label(top,text = "Age",font= 15)
AgeL.place(x=140,y=130)
AgeEntry = tk.Entry(top,textvariable= Age)
AgeEntry.place(x=230,y=130)

MailId= tk.StringVar()
MailIdL = tk.Label(top,text = "Mail Id",font= 15)
MailIdL.place(x=140,y=170)
MailIdEntry = tk.Entry(top,textvariable= MailId)
MailIdEntry.place(x=230,y=170)

'''
Password= tk.StringVar()
Pn = tk.Label(top,text = "Password",font= 15)
Pn.place(x=140,y=200)
PnEntry = tk.Entry(top,textvariable= Password)
PnEntry.place(x=230,y=200)

'''

register = tk.Button(top,text = "Enter",width=10,height=1,command= Enter)
register.place(x=220,y=240)

LoginL = tk.Label(top,text="If already have a account!",font=10)
LoginL.place(x=160,y=300)

Loginb = tk.Button(top,text="Login",width=10,height=1,command= LoginForm)
Loginb.place(x=220,y=330)





top.mainloop()

con.close()