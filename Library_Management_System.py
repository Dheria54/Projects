from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        #======================Variable=========================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.duedate_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()

        lbtitle= Label(self.root,text="Library Management System", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman",50,"bold"), padx=2, pady=6)
        lbtitle.pack(side=TOP, fill=X)

        frame= Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1360,height=370)

        # ==========================DataFrameLeft===================================

        DataFrameLeft=LabelFrame(frame,text="Library Membership Information", bg="powder blue", fg="green", bd=12, relief=RIDGE, font=("times new roman",12,"bold"), padx=2, pady=6)
        DataFrameLeft.place(x=0,y=5,width=750,height=330)

        lblMember=Label(DataFrameLeft,text="Member Type",bg="powder blue",font=("arial",12,"bold"), padx=2, pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.member_var,width=25,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No = Label(DataFrameLeft, text="PRN No", bg="powder blue", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(DataFrameLeft,font=("arial", 13, "bold"),textvariable=self.prn_var,width=25)
        txtPRN_No.grid(row=1,column=1)

        lblTitle = Label(DataFrameLeft, text="ID No", bg="powder blue", font=("arial", 12, "bold"), padx=2, pady=6)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.id_var, width=25)
        txtTitle.grid(row=2, column=1)

        lblFName = Label(DataFrameLeft, text="First Name", bg="powder blue", font=("arial", 12, "bold"), padx=2, pady=6)
        lblFName.grid(row=3, column=0, sticky=W)
        txtFName = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.firstname_var, width=25)
        txtFName.grid(row=3, column=1)

        lblLName = Label(DataFrameLeft, text="Last Name", bg="powder blue", font=("arial", 12, "bold"), padx=2, pady=6)
        lblLName.grid(row=4, column=0, sticky=W)
        txtLName = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.lastname_var, width=25)
        txtLName.grid(row=4, column=1)

        lblAdd1 = Label(DataFrameLeft, text="Address1", bg="powder blue", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAdd1.grid(row=5, column=0, sticky=W)
        txtAdd1 = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.address1_var, width=25)
        txtAdd1.grid(row=5, column=1)

        lblAdd2 = Label(DataFrameLeft, text="Address2", bg="powder blue", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAdd2.grid(row=6, column=0, sticky=W)
        txtAdd2 = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.address2_var, width=25)
        txtAdd2.grid(row=6, column=1)

        lblPC = Label(DataFrameLeft, text="Post Code", bg="powder blue", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPC.grid(row=7, column=0, sticky=W)
        txtPC = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.postcode_var, width=25)
        txtPC.grid(row=7, column=1)

        lblMob = Label(DataFrameLeft, text="Mobile", bg="powder blue", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMob.grid(row=0, column=2, sticky=W)
        txtMob = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.mobile_var, width=25)
        txtMob.grid(row=0, column=3)

        lblBookID = Label(DataFrameLeft, text="Book ID", bg="powder blue", font=("arial", 12, "bold"), padx=2, pady=6)
        lblBookID.grid(row=1, column=2, sticky=W)
        txtBookID = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.bookid_var, width=25)
        txtBookID.grid(row=1, column=3)

        lblBookTit = Label(DataFrameLeft, text="Book Title", bg="powder blue", font=("arial", 12, "bold"), padx=2, pady=6)
        lblBookTit.grid(row=2, column=2, sticky=W)
        txtBookTit = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.booktitle_var, width=25)
        txtBookTit.grid(row=2, column=3)

        lblAuthor = Label(DataFrameLeft, text="Author", bg="powder blue", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAuthor.grid(row=3, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.author_var, width=25)
        txtAuthor.grid(row=3, column=3)

        lblBorrow = Label(DataFrameLeft, text="Date Borrowed", bg="powder blue", font=("arial", 12, "bold"), padx=2, pady=6)
        lblBorrow.grid(row=4, column=2, sticky=W)
        txtBorrow = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.dateborrowed_var, width=25)
        txtBorrow.grid(row=4, column=3)

        lblDue = Label(DataFrameLeft, text="Due Date", bg="powder blue", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDue.grid(row=5, column=2, sticky=W)
        txtDue = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.duedate_var, width=25)
        txtDue.grid(row=5, column=3)

        lblFine = Label(DataFrameLeft, text="Late Return Fine", bg="powder blue", font=("arial", 12, "bold"), padx=2, pady=6)
        lblFine.grid(row=6, column=2, sticky=W)
        txtFine = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.latereturnfine_var, width=25)
        txtFine.grid(row=6, column=3)

        lblDoD = Label(DataFrameLeft, text="Date over Due", bg="powder blue", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDoD.grid(row=7, column=2, sticky=W)
        txtDoD = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.dateoverdue_var, width=25)
        txtDoD.grid(row=7, column=3)

        # ========================Data Frame Right==============================================
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="green", bd=12,relief=RIDGE, font=("times new roman", 12, "bold"), padx=2, pady=6)
        DataFrameRight.place(x=760, y=5, width=550, height=330)

        self.txtBox=Text(DataFrameRight, font=("arial", 12, "bold"),width=27,height=14,padx=2,pady=6)
        self.txtBox.grid(row=0 , column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head First Book','Learn Python The Hard Way', 'Python Programming', ' Python CookBook''Machine Learning',
                                             'Machine Tecno','My Python','Joss Ellif Guru','Elite Jungle Python','Machine Python',
                                            'Introduction To Java','Core Python','Core Java','Database Management System','Cloud Computing',
                   'Computer Peripherals and Interface'
]

        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Head First Book"):
                self.bookid_var.set("BKID1676")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Berry")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")

            elif (x=="Learn Python The Hard Way"):
                self.bookid_var.set("BKID7679")
                self.booktitle_var.set("Basic of Python")
                self.author_var.set("ZED A.SHAW")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")

            elif (x == "Python Programming"):
                self.bookid_var.set("BKID7689")
                self.booktitle_var.set("Core Python")
                self.author_var.set("Rajesh Kumar")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")

            elif (x == "Python CookBook"):
                self.bookid_var.set("BKID7680")
                self.booktitle_var.set("Python Basics")
                self.author_var.set("Mohit Kumar")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")

            elif (x == "Machine Learning"):
                self.bookid_var.set("BKID7676")
                self.booktitle_var.set("Python Basics")
                self.author_var.set("Mohit Kumar")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")

            elif (x == "Machine Tecno"):
                self.bookid_var.set("BKID5786")
                self.booktitle_var.set("Machine Basics")
                self.author_var.set("Mohit Kumar")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")

            elif (x == "My Python"):
                self.bookid_var.set("BKID7098")
                self.booktitle_var.set("Python Basics")
                self.author_var.set("Mohit Kumar")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")

            elif (x == "Joss Ellif Guru"):
                self.bookid_var.set("BKID7069")
                self.booktitle_var.set("Python Basics")
                self.author_var.set("Aman Deep")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")

            elif (x == "Elite Jungle Python"):
                self.bookid_var.set("BKID8968")
                self.booktitle_var.set("Python Basics")
                self.author_var.set("Elite")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")

            elif (x == "Introduction To Java"):
                self.bookid_var.set("BKID8989")
                self.booktitle_var.set("Introduction To Java")
                self.author_var.set("Rajesh Kumar")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")

            elif (x == "Computer Peripherals and Interface"):
                self.bookid_var.set("BKID8990")
                self.booktitle_var.set("Computer Peripherals and Interface")
                self.author_var.set("Hitesh Kumar")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")





        listBox= Listbox(DataFrameRight,font=("arial",12,"bold"),width=18,height=14)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        # ================================== Buttons Frame======================================
        framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        framebutton.place(x=0, y=500, width=1360, height=70)

        btnAddData = Button(framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=30,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData = Button(framebutton,command=self.showData, text="Show Data", font=("arial", 12, "bold"), width=30, bg="blue", fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(framebutton,command=self.reset, text="Reset", font=("arial", 12, "bold"), width=30, bg="blue", fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(framebutton,command=self.iExit, text="Exit", font=("arial", 12, "bold"), width=30, bg="blue", fg="white")
        btnAddData.grid(row=0, column=5)

        # ================================== Information Frame==================================
        frameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frameDetails.place(x=0, y=570, width=1360, height=130)

        tableframe = Frame(self.root,bd=6,relief=RIDGE,bg="powder blue")
        tableframe.place(x=8,y=580,width=1340,height=130)

        xscroll=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(tableframe,orient=VERTICAL)

        self.library_table=ttk.Treeview(tableframe,column=("membertype","prnno","id","firstname","lastname","address1",
                                                      "address2","postid","mobile","bookid","booktitle","author",
                                                      "dateborrowed","duedate","latereturnfine","dateoverdue"),xscrollcommand=xscroll.set,
                                                        yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("id",text="ID")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("duedate",text="Due Date")
        self.library_table.heading("latereturnfine",text="LAteReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("id",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("duedate",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Dheria@2003",database="dheriadb")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                               self.member_var.get(),self.prn_var.get(),
            self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.address1_var.get(),
            self.address2_var.get(),self.postcode_var.get(),self.mobile_var.get(),self.bookid_var.get(),
            self.booktitle_var.get(),self.author_var.get(),self.dateborrowed_var.get(),self.duedate_var.get(),
            self.latereturnfine_var.get(),self.dateoverdue_var.get() ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Member Has been inserted successfully")
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Dheria@2003", database="dheriadb")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library1")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.duedate_var.set(row[13]),
        self.latereturnfine_var.set(row[14]),
        self.dateoverdue_var.set(row[15])

    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN No\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"FirstName\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LastName\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address1\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address2\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No.\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book ID\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Author\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END,"DateBorrowed\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"DueDate\t\t"+ self.duedate_var.get() + "\n")
        self.txtBox.insert(END,"LateReturnFine\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"DateoverDue\t\t"+ self.dateoverdue_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.duedate_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do You Want To Exit")
        if iExit>0:
            self.root.destroy()
            return

if __name__ == "__main__":
    root= Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()