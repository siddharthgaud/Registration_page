from tkinter import *
import mysql.connector as db
from tkinter import messagebox
import pandas as pd



Top=Tk()
Top.geometry("1000x600")
Top.title("Register page")
Top.config(bg="lightblue")

# functionality


def exit_1():
    Top.destroy()

def insert_data():
    name_value = str(var1.get())
    age_value = str(var2.get())
    location_value = str(var3.get())

    # print(name_value)
    # print(type(name_value))
    # print(age_value)
    # print(type(age_value)) 
    # print(location_value)  
    # print(type(location_value))  


    # create database

    mydb = db.connect(host = "localhost",user = "root" , passwd = "siddharth1996")
    print("server connected")
    cur = mydb.cursor()
    cur.execute("create database if not exists personal_info;")
    print("database created")


    # create table

    mydb = db.connect(host = "localhost",user = "root" , passwd = "siddharth1996" , database = "personal_info")
    cur = mydb.cursor()
    cur.execute("create table if not exists private(name varchar(50), age int, location varchar(50));")

    # condition
    if (name_value == "" ) or (age_value == "0") or (location_value == "") :
        messagebox.showerror("Empty Entries", "Fill All Three Entry Values")

    else:
        cur.execute("insert into private(name,age,location) values(%s , %s , %s)",(name_value ,age_value,location_value))
        cur.execute("commit")

        # Delete Entry values

        e1.delete(0 , "end")
        e2.delete(0 , "end")
        e3.delete(0 , "end")
        
        messagebox.showinfo("Successful", "Values Inserted ")

def show_last_data():
    mydb = db.connect(host = "localhost",user = "root" , passwd = "siddharth1996" , database = "personal_info")
    cur = mydb.cursor()
    cur.execute("select * from private;")
    data = cur.fetchall()
    #print(data)

    a , b, c = zip(*data)
    a = list(a)
    b = list(b)
    c = list(c)
    #print(a)
    #print(b)
    #print(c)

    texty = f"Name is : {a[-1]}\nAge is : {b[-1]}\nLocation is : {c[-1]} "

    o_l.config(text = texty)   

def clear():
    o_l.config(text = "")  


def show_all_data():
    mydb = db.connect(host = "localhost",user = "root" , passwd = "siddharth1996" , database = "personal_info")
    cur = mydb.cursor()
    cur.execute("select * from private;")
    data = cur.fetchall()
    #print(data)

    a , b, c = zip(*data)
    a = list(a)
    b = list(b)
    c = list(c)

    # create new window

    top2 = Toplevel()
    top2.geometry("600x600")
    top2.title("Show all Data ")
    top2.config(bg = "cyan")

    # Label
    nl = Label(top2 , text = "Show All Data ",font = ("arial",15 ,"bold"),bg = "blue",fg = "white")
    nl.place(x = 120 , y = 5)

    # label for table

    name_l = Label(top2 , text = "Name",font = ("arial 10"),bg = "blue",fg = "white")
    name_l.place(x = 10 , y = 50)

    account_l = Label(top2 , text = "Age",font = ("arial 10"),bg = "blue",fg = "white")
    account_l.place(x = 110 , y = 50)

    amount_1 = Label(top2 , text = "Location",font = ("arial 10"),bg = "blue",fg = "white")
    amount_1.place(x = 280 , y = 50)

    # create scroll bar

    sb = Scrollbar(top2)
    sb.pack(side = RIGHT , fill = Y)

    # create list box

    name_box = Listbox(top2 ,height = 18 , width = 12 ,font = ("arial 10"), yscrollcommand = sb.set)
    name_box.place(x = 5 , y = 80)
    sb.config(command = name_box.yview)

    # insert info

    for i in range(len(a)):
        name_box.insert(END , f"{a[i]}")
    
    acount_box = Listbox(top2 ,height = 18 , width = 18 ,font = ("arial 10"), yscrollcommand = sb.set)
    acount_box.place(x = 110 , y = 80)
    sb.config(command = acount_box.yview)

    for i in range(len(b)):
        acount_box.insert(END , f"{b[i]}")

    amount_box = Listbox(top2 ,height = 18 , width = 15 ,font = ("arial 10"), yscrollcommand = sb.set)
    amount_box.place(x = 250 , y = 80)
    sb.config(command = amount_box.yview)

    for i in range(len(c)):
        amount_box.insert(END , f"{c[i]}")

    top2.mainloop()

def import_data():
    #
    mydb = db.connect(host = "localhost",user = "root" , passwd = "siddharth1996" , database = "personal_info")
    cur = mydb.cursor()
    cur.execute("select * from private;")
    data = cur.fetchall()
    #print(data)

    a , b, c = zip(*data)
    a = list(a)
    b = list(b)
    c = list(c)

    # create table (dataframe )

    table = pd.DataFrame({
        "Name ": a ,
        "Age ": b,
        "Location":c
        })

    #print(table)

    # convert data into excel format

    table.to_csv("private_data.csv" , index = False)


# label  heading

l1=Label(Top,text="Register",font=("arial",20,"bold","underline"),bg="lightblue",fg="blue")
l1.pack()


# label information

l2=Label(Top,text="Name",font=("arial",15),bg="lightblue",fg="blue")
l2.place(x=50,y=40)

l2=Label(Top,text="Age",font=("arial",15),bg="lightblue",fg="blue")
l2.place(x=50,y=90)

l2=Label(Top,text="Location",font=("arial",15),bg="lightblue",fg="blue")
l2.place(x=50,y=140)


# entry 


var1=StringVar()
e1=Entry(Top,font=("arial",12),textvariable=var1)
e1.place(x=150,y=40)

var2=IntVar()
e2=Entry(Top,font=("arial",12),textvariable=var2)
e2.place(x=150,y=90)

var3=StringVar()
e3=Entry(Top,font=("arial",12),textvariable=var3)
e3.place(x=150,y=140)


# buttons

b1 = Button(Top,text = "Insert Data",font = ("arial"),bg = "blue",fg = "white",command=insert_data)
b1.place(x = 10 , y = 200)

b2 = Button(Top,text = "Show Last Data",font = ("arial"),bg = "blue",fg = "white",command=show_last_data)
b2.place(x = 130 , y = 200)

b3 = Button(Top,text = "Show All Data",font = ("arial"),bg = "blue",fg = "white",command=show_all_data)
b3.place(x = 290 , y = 200)

b4 = Button(Top,text = "Import Data",font = ("arial"),bg = "blue",fg = "white",command=import_data)
b4.place(x = 450 , y = 200)

b5 = Button(Top,text = "Clear",font = ("arial"),bg = "blue",fg = "white",command=clear)
b5.place(x = 600 , y = 200)

b5 = Button(Top,text = "Exit",font = ("arial"),bg = "blue",fg = "white",command=exit_1)
b5.place(x = 700 , y = 200)



# output label

o_l = Label(Top,font = ("arial 15") , bg = "cyan")
o_l.place(x = 110 , y = 260)

Top.mainloop()

