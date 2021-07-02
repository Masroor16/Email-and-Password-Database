from tkinter import *
from tkinter import messagebox
import sqlite3
link = "D:/Email_Details/"
conn =sqlite3.connect(link+'mail_details.db')
TABLE="EmaiL_Database"

def w1():
    windows = Tk()
    windows.title("Email_Database")
    windows.geometry('250x100')

    lbl = Label(windows,text = "Email :")
    lbl.grid(column = 0,row = 0)
    em = Entry(windows,width = 25)
    em.grid(column = 1,row = 0)

    lbl1 = Label(windows,text = "Password :")
    lbl1.grid(column = 0,row = 1)
    ps = Entry(windows,width = 25)
    ps.grid(column = 1,row = 1)

    lbl2 = Label(windows,text = "Site :")
    lbl2.grid(column = 0,row = 2)
    si = Entry(windows,width = 25)
    si.grid(column = 1,row = 2)
    

    
    #conn.execute('''CREATE TABLE '''+TABLE+''' 
    #           (EMAIL  CHAR(50),
    #            PSWD    CHAR(50),
    #            SITE    String    NOT NULL);''')

    def delt():
        windows.destroy()
        w2()
        
    def clicked():
        EMAIL=em.get()
        PSWD = ps.get()
        SITE = si.get()

        val=(EMAIL,PSWD,SITE)
        sql="INSERT INTO "+TABLE+" (EMAIL,PSWD,SITE)VALUES (?,?,?)"
        conn.execute(sql,val);

        conn.commit()
        messagebox.showinfo('Save successful' , 'Save Completed!!')

    btn = Button(windows,text = "SAVE" , command = clicked)
    btn.grid(column = 0,row = 4)

    btn1 = Button(windows,text = "Delete" , command = delt)
    btn1.grid(column = 1,row = 4)
    
    windows.mainloop()

def w2():

    windows = Tk()
    windows.title("Delete")
    windows.geometry('160x80')

    lbl=Label(windows,text="Enter Email to be deleted:.")
    lbl.grid(column=0,row=0)

    em=Entry(windows,width = 25)
    em.grid(column=0,row=1)

    mail=em.get()
    
    def clicked():
        try :
            conn.execute("DELETE FROM "+TABLE+" WHERE EMAIL = '"+mail+"';")
            conn.commit()
            messagebox.showinfo('Task completed','Deleted!!')
            windows.destroy()
            w1()
        except:
            messagebox.showerror('Error','ERROR!!!')

    btn = Button(windows,text = "Delete" , command = clicked)
    btn.grid(column = 0,row = 2)
    windows.mainloop()

w1()
