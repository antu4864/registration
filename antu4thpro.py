
from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title('ACET FORM')
root.configure(background='pink')
def a1():
    root.quit()
def a2():
    t2 = Toplevel()
    t2.title('REGISTRATION FORM')
    t2.geometry("300x300+500+100")
    s1 = StringVar()
    s2 = StringVar()

    def login():

        ss1 = s1.get()
        ss2 = s2.get()
        if (ss1 == '1')and (ss2 == '1'):
            t3 = Toplevel()
            t3.geometry("900x900+300+50")
            l = Label(t3, text='Login succesfully').pack()
            conn = sqlite3.connect('s.sqlite')
            c = conn.cursor()
            l1 = Label(t3, text='Name\t\tFather name\t  Email\t\t\tGender\tDOB\t\tCourse\tMark\tYOP      Address').pack()
            for row in c.execute("select * from antudata"):
               l=Label(t3,text=str(row[0])+"                       "+str(row[1])+'\t'+str(row[2])+'\t    '+str(row[3])+'\t'+str(row[4])+'\t '+str(row[5])+'\t '+str(row[9])+'\t  '+str(row[10])+'\t  '+str(row[11])).pack()

            conn.commit()
            conn.close()
        else:
            t3=Toplevel()

            ll = Label(t3, text='error').pack()
    def back():
        t2.destroy()

    Button(t2, text='LOGIN', width=15, bg='green', command=login).place(x=100, y=200)
    Button(t2, text='BACK', width=15, bg='brown', command=back).place(x=100, y=230)

    M = Label(t2, text='Enter your username and password', width=35, fg="blue" ,font=('bold', 12))
    M.place(x=0, y=60)
    we_1 = Label(t2, text='User name', width=20, font=('bold', 10))
    we_1.place(x=50, y=100)
    me_1 = Entry(t2,textvariable=s1)
    me_1.place(x=100, y=120)

    we_2 = Label(t2, text='Password', width=20, font=('bold', 10))
    we_2.place(x=49, y=140)
    me_2 = Entry(t2,textvariable=s2, show='*')
    me_2.place(x=100, y=160)



root.geometry("300x300+500+100")

def call():
    t1=Toplevel()
    t1.title('antu')


    def db_create():
        conn = sqlite3.connect('s.sqlite')
        c = conn.cursor()
        c.execute('''CREATE TABLE if not exists antudata 
                (name text not null,
        f_name text  not null,
        email text not null,
        gender text not null,
        dob date not null,
        course text not null ,
        category text not null,  
        phone number not null,
        national text not null ,
        inter_marks number not null,
        yop date not null,
        p_address text not null);
        ''')
        print('created')
        conn.commit()
        conn.close()

    def db_add():
        z1 = x1.get()
        z2 = x3.get()
        z3 = x4.get()
        z4 = x5.get()
        z5 = x6.get()
        z6 = x7.get()
        z7 = x8.get()
        z8 = x9.get()
        z9 = var.get()
        z10 = c4.get()
        z11 = c1.get()
        z12 = c2.get()
        z13=y1.get()
        if z9 == 1:
            z9 = 'Male'
        else:
            z9 = 'female'
        conn = sqlite3.connect('s.sqlite')
        c = conn.cursor()

        c.execute("insert into antudata (name,f_name,email,gender,dob,course,category,phone,national,inter_marks,"
                  "yop,p_address) values (?,?,?,?,?,?,?,?,?,?,?,?)",(z1, z2, z3, z9, z4, z10, z11, z13,z12,z5,z6,z7,));
        conn.commit()
        conn.close()

    def db_dis():
        conn = sqlite3.connect('s.sqlite')
        c = conn.cursor()
        for r in c.execute("select * from antudata"):
            print('Name: ', r[0])
            print('F_name: ', r[1])
            print('Email: ', r[2])
            print('Gender:', r[3])
            print('Dob', r[4])
            print('course', r[5])
            print('category', r[6])
            print('phone', r[7])
            print('nation', r[8])
            print('mark12th', r[9])
            print('YOP', r[10])
            print('p_address', r[11])

        conn.commit()
        conn.close()

    def call_me():
        db_create()
        answer = messagebox.askyesno('submit', 'Do you want to submit now')
        if answer == True:
            db_add()
            db_dis()
            t1.destroy()


        else:
            x3.set('')
            x4.set('')
            x5.set('')
            x6.set('')
            x7.set('')
            x8.set('')
            x9.set('')
            c4.set('select your course')
            c1.set('select your Category')
            c2.set('Select Nationality')
            y11 = y1.get()
            if y11 == '':
                x2 = "Not enter phone no"
                l26 = Label(t1, text=x2, fg='red').place(x=440, y=310)
            else:
                try:
                    x2 = "                              "
                    l26 = Label(t1, text=x2, fg='red').place(x=440, y=310)
                    sp = (25 + y11)
                    if len(y11) == 10:
                        print('hello')

                    else:
                        print('invalid')
                        z = 'enter 10 digit no'
                        l27 = Label(t1, text=z, fg='red').place(x=440, y=310)

                        y1.set('')
                except Exception:
                    x2 = "                              "
                    l26 = Label(t1, text=x2, fg='red').place(x=440, y=310)
                    x = 'invalid'
                    l25 = Label(t1, text=x, fg='red').place(x=440, y=310)

    x1 = StringVar()
    x3 = StringVar()
    x4 = StringVar()
    x5 = StringVar()
    x6 = StringVar()
    x7 = StringVar()
    x8 = StringVar()
    x9 = StringVar()

    y1 = StringVar()

    t1.geometry("550x550+300+5")

    t1.title('ACET')
    label_11 = Label(t1, text='Amritsar Group of College',fg='blue', width=20, font=('bold', 30))
    label_11.place(x=60, y=10)

    root.title('REGISTRATION FORM')
    label_0 = Label(t1, text='REGISTRATION FORM', width=20,fg='brown', font=('bold', 15))
    label_0.place(x=170, y=60)

    label_1 = Label(t1, text='Fullname:', width=20, font=('bold', 10))
    label_1.place(x=70, y=100)
    entry_1 = Entry(t1, textvariable=x1)
    entry_1.place(x=260, y=100, width=200)

    label_2 = Label(t1, text='Father_Name', width=20, font=('bold', 10))
    label_2.place(x=80, y=130)
    entry_2 = Entry(t1, textvariable=x3)
    entry_2.place(x=260, y=130, width=200)

    label_3 = Label(t1, text='Email', width=20, font=('bold', 10))
    label_3.place(x=60, y=160)
    entry_3 = Entry(t1, textvariable=x4)
    entry_3.place(x=260, y=160, width=200)

    label_4 = Label(t1, text='Gender', width=20, font=('bold', 10))
    label_4.place(x=62, y=190)
    var = IntVar()
    Radiobutton(t1, text='Male', padx=5, variable=var, value=1).place(x=248, y=190)
    Radiobutton(t1, text='Female', padx=5, variable=var, value=2).place(x=300, y=190)

    label_8 = Label(t1, text='Date of Birth', width=20, font=('bold', 10))
    label_8.place(x=79, y=220)
    entry_8 = Entry(t1, textvariable=x5)
    entry_8.place(x=260, y=220, width=200)

    label_9 = Label(t1, text='Course', width=20, font=('bold', 10))
    label_9.place(x=64, y=250)

    list1 = ['B.Tech', 'B.Sc', 'B.B.A', 'B.C.A', 'B.Com', 'M.Sc', 'M.B.A', 'M.C.A', 'M.Tech']
    c4 = StringVar()
    droplist = OptionMenu(t1, c4, *list1)
    droplist.config(width=15)
    c4.set('select your course')
    droplist.place(x=258, y=250, width=200)

    label_10 = Label(t1, text='Category', width=20, font=('bold', 10))
    label_10.place(x=69, y=280)

    list1 = ['General', 'OBC', 'SC', 'ST', ]
    c1 = StringVar()
    droplist = OptionMenu(t1, c1, *list1)
    droplist.config(width=15)
    c1.set('select your Category')
    droplist.place(x=258, y=280, width=200)

    label_5 = Label(t1, text='Phone No', width=20, font=('bold', 10))
    label_5.place(x=72, y=310)
    entry_5 = Entry(t1, textvariable=y1)
    entry_5.place(x=260, y=310, width=200)

    label_6 = Label(t1, text='Nationality', width=20, font=('bold', 10))
    label_6.place(x=75, y=340)

    list1 = ['Afghanistan', 'Australia', 'Bangladesh', 'Canada', 'China', 'India', 'japan', 'Nepal', 'Pakistan',
             'Russia'
        , 'Sudan, South', 'Sri Lanka', 'United States', 'United Kingdom']
    c2 = StringVar()
    droplist = OptionMenu(t1, c2, *list1)
    droplist.config(width=15)
    c2.set('Select Nationality')
    droplist.place(x=258, y=340, width=200)

    label_14 = Label(t1, text='Mark of 12th', width=20, font=('bold', 10))
    label_14.place(x=77, y=370)
    entry_14 = Entry(t1, textvariable=x6)
    entry_14.place(x=260, y=370, width=200)

    label_16 = Label(t1, text='Year of Passing(12th)', width=20, font=('bold', 10))
    label_16.place(x=108, y=400)
    entry_16 = Entry(t1, textvariable=x7)
    entry_16.place(x=260, y=400, width=200)

    label_17 = Label(t1, text='Perment Address', width=20, font=('bold', 10))
    label_17.place(x=99, y=430)
    entry_17 = Entry(t1, textvariable=x8)
    entry_17.place(x=260, y=430, height=40, width=200)


    Button(t1, text='submit', width=20, bg='red', fg='blue', command=call_me).place(x=300, y=490)
    #Button(t1, text='BACK', width=15, bg='brown', command=back).place(x=100, y=230)

label_1 = Label(root, text='WELCOME TO REGISTRATION FORM',fg='blue', width=33, font=('bold', 12))
label_1.place(x=1, y=20)

Button(root, text='Apply form', width=20, bg='red', command=call).place(x=80, y=120)
Button(root, text='Adminstration', width=20, bg='blue', command=a2).place(x=80, y=80)
Button(root, text='Exit', width=20, bg='brown', command=a1).place(x=80, y=160)

mainloop()


