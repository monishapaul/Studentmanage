from tkinter import *
import mysql.connector  # for connector
from mysql.connector import errorcode  # for error handling


def add():
    laddres.grid(row=2, column=1)
    contact = econtact.get()
    name = ename.get()
    branch = ebranch.get()
    year = eyear.get()
    dob = edob.get()
    location = elocation.get()
    if name == '' or branch == '' or year == '':
        laddres.config(text="Fill all details")
    else:
        try:
            db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='projects')
            # host=Ip of server '198.112.23.10:3361'

            cursor = db.cursor()  # reference to database

            query = "insert into skilled_student_management (contact,name,branch,year,dob,location) values(%s,%s,%s,%s,%s,%s)"
            values = (contact,name,branch,year,dob,location)
            # SQL query written'''
            cursor.execute(query, values)  # query to run
            db.commit()
            laddres.config(text="Student details added")  # list of tuples

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Access denied/wrong  user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                laddres.config(text="Database does not exists")
            else:
                laddres.config(text=err)
        else:
            db.close()


def search():
    lsearchres.grid(row=2, column=1)
    try:
        db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='projects')
        # host=Ip of server '198.112.23.10:3361'

        cursor = db.cursor()  # reference to database
        contact = econtact.get()
        query = "select * from skilled_student_management where contact='%s'" % (contact)

        cursor.execute(query)  # query to run
        res = cursor.fetchall()
        if cursor.rowcount < 1:  # 0 means no records
            lsearchres.config(text="No record found")
        else:
            print("total records ", cursor.rowcount)
            for record in res:  # iterating over res
                lsearchres.config(
                    text="Record found\n\n   Contact no: " + str(record[0]) + "\nName: " + record[1] + "\n Branch: " + record[
                        2] + "\n Year: " + record[3] + " \n Date of birth: " + str(record[4])+ " \n Location: " + record[5])

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied/wrong  user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            lsearchres.config(text="Database does not exists")
        else:
            lsearchres.config(text=err)
    else:
        db.close()


def delete():
    ldeleteres.grid(row=2, column=1)
    try:
        db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='projects')
        # host=Ip of server '198.112.23.10:3361'

        cursor = db.cursor()  # reference to database
        rn = econtact.get()
        query = "delete from skilled_student_management where contact=%s" % (rn)
        cursor.execute(query)  # query to run
        db.commit();
        ldeleteres.config(text='Details deleted')  # list of tuples

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied/wrong  user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            ldeleteres.config(text="Database does not exists")
        else:
            ldeleteres.config(text=err)
    else:
        db.close()


def update():
    lupdateres.grid(row=2, column=1)
    contact = econtact.get()
    name = ename.get()
    branch = ebranch.get()
    year = eyear.get()
    dob = edob.get()
    location = elocation.get()
    if name == '' or branch == '' or year == '':
        laddres.config(text="Fill all details")
    else:
        try:
            db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='projects')
            # host=Ip of server '198.112.23.10:3361'

            cursor = db.cursor()  # reference to database

            query = "update skilled_student_management set name=%s,branch=%s,year=%s, dob=%s, location=%s where contact=%s"  # SQL query written'''
            values = (ename.get(), ebranch.get(), eyear.get(), edob.get(), elocation.get(), econtact.get())
            cursor.execute(query, values)  # query to run
            db.commit();
            lupdateres.config(text="Student details updated")  # list of tuples

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Access denied/wrong  user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                lupdateres.config(text="Database does not exists")
            else:
                lupdateres.config(text=err)
        else:
            db.close()


def clear():


    laddres.grid_forget()
    ldeleteres.grid_forget()
    lsearchres.grid_forget()
    lupdateres.grid_forget()


root = Tk()
root.title("Student Management")
root.config(bg = 'gold1')
title = Label(root, text=" Rkdemy Skilled Python fullstack \nThane(w)", font="bold", bg="royal blue", fg="white")
title.pack(side=TOP, fill=X)
root.geometry('1100x650+200+100')
root.resizable(False, False)

menuframe = LabelFrame(root, text="Enter Details", font=("bold", 20), bd=12)
menuframe.place(x=20,y=90, width=400, height=500)
resultframe = LabelFrame(root,bd=12)
resultframe.place(x=460, y=90, width=610, height=100)
showframe = LabelFrame(root, bd = 12)
showframe.place(x=460, y=200, width= 610, height = 400 )

lcontact = Label(menuframe, text="Contact:", bd=7,font=("bold",17))
lcontact.grid(row=0, column=0, padx=3,pady=3)
econtact = Entry(menuframe)
econtact.grid(row=0, column=1)

lname = Label(menuframe, text="Name:", bd=7,font=("bold",17))
lname.grid(row=2, column=0, padx = 3,pady = 3)
ename = Entry(menuframe)
ename.grid(row=2, column=1)

lbranch = Label(menuframe, text="Branch:", bd=7,font=("bold",17))
lbranch.grid(row=3, column=0, padx = 3,pady = 3)
ebranch = Entry(menuframe)
ebranch.grid(row=3, column=1)

lyear = Label(menuframe, text="Year:", bd=7,font=("bold",17))
lyear.grid(row=4, column=0, padx = 3,pady = 3)
eyear = Entry(menuframe)
eyear.grid(row=4, column=1)

ldob = Label(menuframe, text="Date of birth:", bd=7,font=("bold",17))
ldob.grid(row=5, column=0, padx = 3,pady = 3)
edob = Entry(menuframe)
edob.grid(row=5, column=1)

llocation = Label(menuframe, text="Location:",  bd=7,font=("bold",17))
llocation.grid(row=6, column=0, padx = 3,pady = 3)
elocation = Entry(menuframe)
elocation.grid(row=6, column=1)

btadd = Button(resultframe, text="Add Student", width="10",bd=7,font=("Bold",13), command=add)
btsearch = Button(resultframe, text="Search", width="10",bd=7,font=("Bold",13),  command=search)
btdelete = Button(resultframe, text="Delete", width="10",bd=7,font=("Bold",13), command=delete)
btupdate = Button(resultframe, text="Update", width="10",bd=7,font=("Bold",13) , command=update)
btclear = Button(resultframe, text="Clear", width="10", bd=8,font=("Bold",13), command=clear)
btadd.grid(row=0, column=0, padx = 3,pady = 3)
btsearch.grid(row=0, column=1, padx = 3,pady = 3)
btdelete.grid(row=0, column=2, padx = 3,pady = 3)
btupdate.grid(row=0, column=3, padx = 3,pady = 3)
btclear.grid(row=0, column=4, padx = 3,pady = 3)


laddres = Label(showframe, text="", bd=8,font=("Bold",13) )

ldeleteres = Label(showframe, text="",bd=8,font=("Bold",13))

lupdateres = Label(showframe, text="",bd=8,font=("Bold",13))

lsearchres = Label(showframe, text="", bd=8,font=("Bold",13))


root.mainloop()