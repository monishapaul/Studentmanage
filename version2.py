from tkinter import *
import mysql.connector  # for connector
from mysql.connector import errorcode  # for error handling


def add():
    laddres.grid(row=2, column=1)
    rollno = erollno.get()
    name = ename.get()
    branch = ebranch.get()
    year = eyear.get()
    gender = egender.get()
    if name == '' or branch == '' or year == '':
        laddres.config(text="Fill all details")
    else:
        try:
            db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='projects')
            # host=Ip of server '198.112.23.10:3361'

            cursor = db.cursor()  # reference to database

            query = "insert into student_management (rollno,name,branch,year,gender) values(%s,%s,%s,%s,%s)"
            values = (rollno, name, branch, year, gender)
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
        rollno = erollno.get()
        query = "select * from student_management where rollno='%s'" % (rollno)

        cursor.execute(query)  # query to run
        res = cursor.fetchall()
        if cursor.rowcount < 1:  # 0 means no records
            lsearchres.config(text="No record found")
        else:
            print("total records ", cursor.rowcount)
            for record in res:  # iterating over res
                lsearchres.config(
                    text="Record found\n   Roll no:" + str(record[0]) + "  Name:" + record[1] + "   Branch:" + record[
                        2] + "  Year:" + record[3] + "  Gender:" + record[4])

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
        rn = erollno.get()
        query = "delete from student_management where rollno=%s" % (rn)
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
    rollno = erollno.get()
    name = ename.get()
    branch = ebranch.get()
    year = eyear.get()
    gender = egender.get()
    if name == '' or branch == '' or year == '':
        laddres.config(text="Fill all details")
    else:
        try:
            db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='projects')
            # host=Ip of server '198.112.23.10:3361'

            cursor = db.cursor()  # reference to database

            query = "update student_management set name=%s,branch=%s,year=%s, gender=%s where rollno=%s"  # SQL query written'''
            values = (ename.get(), ebranch.get(), eyear.get(), egender.get(), erollno.get())
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
title = Label(root, text="ABC COLLEGE OF ENGINEERING\nThane(w)", font="bold", bg="royal blue", fg="white")
title.pack(side=TOP, fill=X)
root.geometry('620x500+200+100')
menuframe = Frame(root, bg="light blue")
menuframe.place(x=10, y=60, width=600, height=200)
resultframe = Frame(root, bg="light blue")
resultframe.place(x=10, y=280, width=600, height=200)

lrollno = Label(menuframe, text="Roll no:", bg="light blue")
lrollno.grid(row=0, column=0)
erollno = Entry(menuframe)
erollno.grid(row=0, column=1)

lname = Label(menuframe, text="Name:", bg="light blue")
lname.grid(row=2, column=0)
ename = Entry(menuframe)
ename.grid(row=2, column=1)

lbranch = Label(menuframe, text="Branch:", bg="light blue")
lbranch.grid(row=3, column=0)
ebranch = Entry(menuframe)
ebranch.grid(row=3, column=1)

lyear = Label(menuframe, text="Year:", bg="light blue")
lyear.grid(row=4, column=0)
eyear = Entry(menuframe)
eyear.grid(row=4, column=1)

lgender = Label(menuframe, text="Gender:", bg="light blue")
lgender.grid(row=5, column=0)
egender = Entry(menuframe)
egender.grid(row=5, column=1)

btadd = Button(menuframe, text="Add Student", width="20", height="2", bg="sky blue", command=add)
btsearch = Button(menuframe, text="Search", width="20", height="2", bg="sky blue", command=search)
btdelete = Button(menuframe, text="Delete", width="20", height="2", bg="sky blue", command=delete)
btupdate = Button(menuframe, text="Update", width="20", height="2", bg="sky blue", command=update)
btclear = Button(menuframe, text="Clear", width="20", height="2", bg="sky blue", command=clear)
btadd.grid(row=8, column=0)
btsearch.grid(row=8, column=6)
btdelete.grid(row=8, column=3)
btupdate.grid(row=8, column=1)
btclear.grid(row=10, column=3)

lresult=Label(resultframe, text="Result", bg = "royal blue", font="bold")
lresult.grid(row=0, column=5)
laddres = Label(resultframe, text="", bg="light blue")

ldeleteres = Label(resultframe, text="", bg="light blue")

lupdateres = Label(resultframe, text="", bg="light blue")

lsearchres = Label(resultframe, text="", bg="light blue")


root.mainloop()