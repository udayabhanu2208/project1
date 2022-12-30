import tkinter as tk
from tkinter import *
from tkinter import messagebox

import mysql.connector


class log:
    def _init_(self):
        pass
    def mainn(self):
        global window
        window = Tk()
        window.geometry("400x400")
        window.title("HCL EMP system")
        menubar = Menu(window)
        menubar.add_command(label="Login", command=self.main1)
        menubar.add_command(label="New user", command=self.main2)
        menubar.add_command(label="Search", command=self.main3)
        window.config(menu=menubar)
        window.mainloop()

    def connection(self,user, passw):
        conn = mysql.connector.connect(host='localhost', user='root', password='password', port=3306, db='hcl')
        query = "select id from login where username =%s and password =%s"
        vals = (user, passw)
        cur = conn.cursor(prepared=True)
        cur.execute(query, vals)
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result

    def check(self):
        self.u_name = un.get()
        self.pass_word = pw.get()
        data = self.connection(self.u_name, self.pass_word)
        # print(data)
        # print(data[0])
        if data is not None:
            messagebox.showinfo(title="Hello user", message="welcome")
        else:
            messagebox.showinfo(title="Hello user", message="please enter correct credentials")

    def main1(self):
        root = Toplevel(window)
        root.geometry("400x400")
        t = Label(root, text="Login Form", font=('arial', 14), bd=15)
        t.pack()
        form = Frame(root)
        form.pack(side=TOP, fill=X)
        global un
        global pw
        un = StringVar()
        pw = StringVar()

        nameL = Label(form, text="Username: ", font=('arial', 14), bd=15)
        passL = Label(form, text="Password: ", font=('arial', 14), bd=15)
        nameL.grid(row=1, stick=W)
        passL.grid(row=2, stick=W)
        nameE = Entry(form, textvariable=un)
        passE = Entry(form, textvariable=pw, show="*")
        nameE.grid(row=1, column=2)
        passE.grid(row=2, column=2)
        login = Button(root, text="Login", command=self.check)
        login.pack()
        root.mainloop()

    def connection1(self,user, passw):
        conn = mysql.connector.connect(host='localhost', user='root', password='password', port=3306, db='hcl')
        query = "select username from login where username like'%{0}'".format(user, )
        cur = conn.cursor(prepared=True)
        cur.execute(query)
        result = cur.fetchone()
        if result:
            messagebox.showinfo(title="Hello user",
                                message="""Already user registered with same username try with another""")
        else:
            # q = """insert into login(username, password) values ('{0}','{1}')""".format(user, passw)
            q1 = "insert into login(username,password) values(?,?)"
            val = (user, passw)

            cur.execute(q1, val)
            conn.commit()
            messagebox.showinfo(title="Hello user",
                                message="""new user registered""")

        cur.close()
        conn.close()
        return result

    def checkfornewentry(self):
        self.u_name = un.get()
        self.pass_word1 = pw1.get()
        self.pass_word2 = pw2.get()
        print(self.u_name)
        print(self.pass_word2)
        if (self.pass_word1 == self.pass_word2):
            self.pass_word = self.pass_word1
        else:
            messagebox.showinfo(title="Hello user", message="incorrect entry")
        self.connection1(self.u_name,self.pass_word)

    def main2(self):
        root1 = Toplevel(window)
        root1.geometry("400x400")
        t = Label(root1, text="Login registration Form", font=('arial', 14), bd=15)
        t.pack()
        form = Frame(root1)
        form.pack(side=TOP, fill=X)
        global un
        global pw1
        global pw2
        un = StringVar()
        pw1 = StringVar()
        pw2 = StringVar()

        nameL = Label(form, text="Username: ", font=('arial', 14), bd=15)
        passL1 = Label(form, text="Type Password  : ", font=('arial', 14), bd=15)
        passL2 = Label(form, text="Retype Password: ", font=('arial', 14), bd=15)
        nameL.grid(row=1, stick=W)
        passL1.grid(row=2, stick=W)
        passL2.grid(row=3, stick=W)
        nameE = Entry(form, textvariable=un)
        passE1 = Entry(form, textvariable=pw1)
        passE2 = Entry(form, textvariable=pw2, show="*")

        nameE.grid(row=1, column=2)
        passE1.grid(row=2, column=2)
        passE2.grid(row=3, column=2)
        login = Button(root1, text="Register", command=self.checkfornewentry)
        login.pack()
        root1.mainloop()



    def main3(self):
        root =Toplevel(window)
        root.geometry("400x200")
        l1 = tk.Label(root, text='Enter ID to search: ', width=25)
        l1.grid(row=1, column=1)
        t1 = tk.Text(root, height=1, width=4, bg='yellow')
        t1.grid(row=1, column=2)
        b1 = tk.Button(root, text='Show Details', width=15, bg='red', command=lambda: my_details(t1.get('1.0', END)))
        b1.grid(row=1, column=4)
        search = tk.StringVar()
        l2 = tk.Label(root, textvariable=search, width=30, fg='red')
        l2.grid(row=3, column=1, columnspan=2)
        search.set("")

        def my_details(id):
            conn = mysql.connector.connect(host='localhost', user='root', password='password', port=3306, db='hcl')
            cur1= conn.cursor()
            try:
                val = int(id)  # check input is integer or not
                try:
                    cur1.execute("SELECT * FROM login WHERE id=" + id)
                    result = cur1.fetchone()
                    search.set(result)
                except:
                    search.set("Database error")
            except:
                search.set("Check input")

        root.mainloop()


obj1=log()
obj1.mainn()