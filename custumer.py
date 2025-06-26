from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
import datetime


class cust_window:
    def __init__(self,root):
        self.root=root
        self.root.title("ROOM FINDING GUI APP")     #for giving title the app
        self.root.geometry("1295x550+230+228")

        #==========================variables===============
        self.var_c_id=StringVar()
        x=random.randint(10000,99999)
        self.var_c_id.set(str(x))

        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_adhar=StringVar()
        self.var_add=StringVar()
        self.var_regi_time=StringVar()
        self.var_nation=StringVar()
        self.var_local_person=StringVar()
        self.var_person_con=StringVar()
        self.var_parea1=StringVar()
        self.var_parea2=StringVar()
        self.var_parea3=StringVar()
        self.var_room_type=StringVar()
        self.var_no_of_rooms=StringVar()
        self.var_kitchen=StringVar()
        self.var_att_wash=StringVar()
        self.var_rent=StringVar()
        self.var_no_of_person=StringVar()
        self.var_deposite=StringVar()
        self.var_other_remark=StringVar()


        #======================LEVEL===================
        lbl_title=Label(self.root,text="CUSTOMER",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        img2=Image.open(r"C:\Users\ashis\OneDrive\Documents\Desktop\ROOM_FINDING_GUI_APP\IMAGES\logo.jpg")      
        img2=img2.resize((120,40),Image.LANCZOS)      
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)     
        lblimg.place(x=5,y=4,width=120,height=40)

        #=================== lavel frame====================
        levelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",font=("times new roman",12,"bold"),padx=2)
        levelframeleft.place(x=5,y=50,width=425,height=490)

        #============ lavels and entrys========================
        #custmor_id
        lbl_cust_id=Label(levelframeleft,text="Customer ID",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_cust_id.grid(row=0,column=0,sticky=W)

        entry_id=ttk.Entry(levelframeleft,textvariable=self.var_c_id,width=29,state="readonly",font=("times new roman",13,"bold"))
        entry_id.grid(row=0,column=1)

        #name
        lbl_name=Label(levelframeleft,text="Name",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_name.grid(row=1,column=0,sticky=W)

        entry_name=ttk.Entry(levelframeleft,textvariable=self.var_name,width=29,font=("times new roman",13,"bold"))
        entry_name.grid(row=1,column=1)

        #gender combobox
        lbl_gender=Label(levelframeleft,text="Gender",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_gender.grid(row=2,column=0,sticky=W)

        combo_gender=ttk.Combobox(levelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["values"]=("Select","Male","female","other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)

        #mobile
        lbl_mob=Label(levelframeleft,text="MOBILE NO",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_mob.grid(row=3,column=0,sticky=W)

        entry_mob=ttk.Entry(levelframeleft,textvariable=self.var_mobile,width=29,font=("times new roman",13,"bold"))
        entry_mob.grid(row=3,column=1)

        #email
        lbl_email=Label(levelframeleft,text="Email ID",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_email.grid(row=4,column=0,sticky=W)

        entry_email=ttk.Entry(levelframeleft,textvariable=self.var_email,width=29,font=("times new roman",13,"bold"))
        entry_email.grid(row=4,column=1)

        #adhar
        lbl_adhar=Label(levelframeleft,text="Adhar No",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_adhar.grid(row=5,column=0,sticky=W)

        entry_adhar=ttk.Entry(levelframeleft,textvariable=self.var_adhar,width=29,font=("times new roman",13,"bold"))
        entry_adhar.grid(row=5,column=1) 

        #permanent address
        lbl_address=Label(levelframeleft,text="Permanent Address",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_address.grid(row=6,column=0,sticky=W)

        entry_address=ttk.Entry(levelframeleft,textvariable=self.var_add,width=29,font=("times new roman",13,"bold"))
        entry_address.grid(row=6,column=1)

        #Registration time
        lbl_address=Label(levelframeleft,text="Registration time",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_address.grid(row=7,column=0,sticky=W)

        entry_address=ttk.Entry(levelframeleft,textvariable=self.var_regi_time,width=29,font=("times new roman",13,"bold"))
        entry_address.grid(row=7,column=1)

        #nationality
        lbl_address=Label(levelframeleft,text="Nationality",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_address.grid(row=8,column=0,sticky=W)

        entry_address=ttk.Entry(levelframeleft,textvariable=self.var_nation,width=29,font=("times new roman",13,"bold"))
        entry_address.grid(row=8,column=1)

        #person in city
        lbl_local=Label(levelframeleft,text="Local person",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_local.grid(row=9,column=0,sticky=W)

        entry_local=ttk.Entry(levelframeleft,textvariable=self.var_local_person,width=29,font=("times new roman",13,"bold"))
        entry_local.grid(row=9,column=1)

        #person contact
        lbl_localphone=Label(levelframeleft,text="Person's contact",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_localphone.grid(row=10,column=0,sticky=W)

        entry_localphone=ttk.Entry(levelframeleft,textvariable=self.var_person_con,width=29,font=("times new roman",13,"bold"))
        entry_localphone.grid(row=10,column=1)

        #prefferd area 1
        lbl_area1=Label(levelframeleft,text="Preffered area 1",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_area1.grid(row=11,column=0,sticky=W)

        entry_area1=ttk.Entry(levelframeleft,textvariable=self.var_parea1,width=29,font=("times new roman",13,"bold"))
        entry_area1.grid(row=11,column=1)

        #preffered area 2
        lbl_area2=Label(levelframeleft,text="Preffered area 2",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_area2.grid(row=12,column=0,sticky=W)

        entry_area2=ttk.Entry(levelframeleft,textvariable=self.var_parea2,width=29,font=("times new roman",13,"bold"))
        entry_area2.grid(row=12,column=1)

        #preffered area 3
        lbl_area3=Label(levelframeleft,text="Preffered area 3",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_area3.grid(row=13,column=0,sticky=W)

        entry_area3=ttk.Entry(levelframeleft,textvariable=self.var_parea3,width=29,font=("times new roman",13,"bold"))
        entry_area3.grid(row=13,column=1)

        #===============buttons in costumer======================

        btn_frame=Frame(levelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnAdd.grid(row=0,column=1,padx=1)

        btnUpdate=Button(btn_frame,command=self.update,text="UPDATE",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnUpdate.grid(row=0,column=2,padx=1)

        btnDelete=Button(btn_frame,text="DELETE",command=self.mdelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnDelete.grid(row=0,column=3,padx=1)

        btnReset=Button(btn_frame,command=self.reset,text="RESET",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnReset.grid(row=0,column=4,padx=1)

        #============ room detail fraim================
        levelroomdetail=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Detail",font=("times new roman",12,"bold"),padx=2)
        levelroomdetail.place(x=435,y=50,width=853,height=180)
        
        #room type
        lbl_roomtype=Label(levelroomdetail,text="Room type",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_roomtype.grid(row=0,column=0,sticky=W)

        combo_roomtype=ttk.Combobox(levelroomdetail,textvariable=self.var_room_type,font=("arial",12,"bold"),width=27,state="readonly")
        combo_roomtype["values"]=("Select","Boys student","Girls student","Family","Any one")
        combo_roomtype.current(0)
        combo_roomtype.grid(row=0,column=1)
        
        #no of rooms
        lbl_noroom=Label(levelroomdetail,text="No.of Rooms",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_noroom.grid(row=0,column=2,sticky=W)

        combo_noroom=ttk.Combobox(levelroomdetail,textvariable=self.var_no_of_rooms,font=("arial",12,"bold"),width=27,state="readonly")
        combo_noroom["values"]=("Select",1,2,3,4,5,6,7,8,8,10)
        combo_noroom.current(0)
        combo_noroom.grid(row=0,column=3)

        #kitchen
        lbl_Kitchen=Label(levelroomdetail,text="Kitchen",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_Kitchen.grid(row=1,column=0,sticky=W)

        combo_kitchen=ttk.Combobox(levelroomdetail,textvariable=self.var_kitchen,font=("arial",12,"bold"),width=27,state="readonly")
        combo_kitchen["values"]=("Select","Yes","NO")
        combo_kitchen.current(0)
        combo_kitchen.grid(row=1,column=1)

        #Attached washroom
        lbl_washroom=Label(levelroomdetail,text="Att. Washroom",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_washroom.grid(row=1,column=2,sticky=W)

        combo_washroom=ttk.Combobox(levelroomdetail,textvariable=self.var_att_wash,font=("arial",12,"bold"),width=27,state="readonly")
        combo_washroom["values"]=("Select","Yes","No")
        combo_washroom.current(0)
        combo_washroom.grid(row=1,column=3)

        #expected rent
        lbl_rent=Label(levelroomdetail,text="Expected Rent",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_rent.grid(row=2,column=0,sticky=W)

        combo_rent=ttk.Combobox(levelroomdetail,textvariable=self.var_rent,font=("arial",12,"bold"),width=27,state="readonly")
        combo_rent["values"]=("Select","1000","1500","2000","2500","3000","3500","4000","4500","5000","5500","6000","6500","7000","7500","8000","8500","9000","9500","10000","11000","12000","13000","14000","15000","16000","17000","18000","19000","20000")
        combo_rent.current(0)
        combo_rent.grid(row=2,column=1)

         #no of person
        lbl_person=Label(levelroomdetail,text="No of Persons",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_person.grid(row=2,column=2,sticky=W)

        combo_person=ttk.Combobox(levelroomdetail,textvariable=self.var_no_of_person,font=("arial",12,"bold"),width=27,state="readonly")
        combo_person["values"]=("Select",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
        combo_person.current(0)
        combo_person.grid(row=2,column=3)

        #Deposite
        lbl_Deposite=Label(levelroomdetail,text="Deposite",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_Deposite.grid(row=3,column=0,sticky=W)

        combo_Deposite=ttk.Combobox(levelroomdetail,textvariable=self.var_deposite,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Deposite["values"]=("Select","Yes","No")
        combo_Deposite.current(0)
        combo_Deposite.grid(row=3,column=1)

        #Remark
        lbl_remark=Label(levelroomdetail,text="Other Remark",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_remark.grid(row=3,column=2,sticky=W)

        entry_remark=ttk.Entry(levelroomdetail,textvariable=self.var_other_remark,width=33,font=("times new roman",12,"bold"))
        entry_remark.grid(row=3,column=3)

        


        #============ tabel frame search system================
        leveltabelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View detail & search system",font=("times new roman",12,"bold"),padx=2)
        leveltabelframe.place(x=435,y=230,width=853,height=310)

        lbl_searchby=Label(leveltabelframe,text="Search By",font=("times new roman",12,"bold"),bg="red",fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(leveltabelframe,textvariable=self.search_var,font=("arial",12,"bold"),width=20,state="readonly")
        combo_search["values"]=("Select","mobile","c_id","adhar","parea1","parea2","parea3")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        entry_search=ttk.Entry(leveltabelframe,textvariable=self.txt_search,width=30,font=("times new roman",12,"bold"))
        entry_search.grid(row=0,column=2,padx=4,pady=4,sticky=W)

        btnsearch=Button(leveltabelframe,command=self.search,text="SEARCH",font=("arial",11,"bold"),bg="green",fg="gold",width=9,cursor="hand2")
        btnsearch.grid(row=0,column=3,padx=2)

        btnshow=Button(leveltabelframe,command=self.fetch_data,text="SHOW ALL",font=("arial",11,"bold"),bg="green",fg="gold",width=9,cursor="hand2")
        btnshow.grid(row=0,column=4,padx=2)

        #===================show data table==================
        details_table=LabelFrame(leveltabelframe,bd=2,relief=RIDGE)
        details_table.place(x=0,y=36,width=845,height=250)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_table=ttk.Treeview(details_table,column=("c_id","name","gender","mobile","email","adhar","addr","regi_time","nation"
                                                                ,"local_person","person_con","parea1","parea2","parea3","room _type","no_of_rooms"
                                                                ,"kitchen","att_wash","rent","no_of_person","deposite","other_remark"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_table.xview)
        scroll_y.config(command=self.Cust_Details_table.yview)

        self.Cust_Details_table.heading("c_id",text="Costumer ID")
        self.Cust_Details_table.heading("name",text="Name")
        self.Cust_Details_table.heading("gender",text="Gender")
        self.Cust_Details_table.heading("mobile",text="Mobile No")
        self.Cust_Details_table.heading("email",text="Email ID")
        self.Cust_Details_table.heading("adhar",text="Adhar No")
        self.Cust_Details_table.heading("addr",text="Permanent Address")
        self.Cust_Details_table.heading("regi_time",text="Registration time")
        self.Cust_Details_table.heading("nation",text="Nationality")
        self.Cust_Details_table.heading("local_person",text="Local Person")
        self.Cust_Details_table.heading("person_con",text="Person's Contact")
        self.Cust_Details_table.heading("parea1",text="Prefferd area 1")
        self.Cust_Details_table.heading("parea2",text="Preffered area 2")
        self.Cust_Details_table.heading("parea3",text="Preffered area 3")
        self.Cust_Details_table.heading("room _type",text="Room type")
        self.Cust_Details_table.heading("no_of_rooms",text="No of Rooms")
        self.Cust_Details_table.heading("kitchen",text="Kitchen")
        self.Cust_Details_table.heading("att_wash",text="Att. Washroom")
        self.Cust_Details_table.heading("rent",text="Expected Rent")
        self.Cust_Details_table.heading("no_of_person",text="No of Persons")
        self.Cust_Details_table.heading("deposite",text="Deposite")
        self.Cust_Details_table.heading("other_remark",text="Other Remark")

        self.Cust_Details_table["show"]="headings"

        self.Cust_Details_table.column("c_id",width=100)
        self.Cust_Details_table.column("name",width=100)
        self.Cust_Details_table.column("gender",width=100)
        self.Cust_Details_table.column("mobile",width=100)
        self.Cust_Details_table.column("email",width=100)
        self.Cust_Details_table.column("adhar",width=100)
        self.Cust_Details_table.column("addr",width=100)
        self.Cust_Details_table.column("regi_time",width=100)
        self.Cust_Details_table.column("nation",width=100)
        self.Cust_Details_table.column("local_person",width=100)
        self.Cust_Details_table.column("person_con",width=100)
        self.Cust_Details_table.column("parea1",width=100)
        self.Cust_Details_table.column("parea2",width=100)
        self.Cust_Details_table.column("parea3",width=100)
        self.Cust_Details_table.column("room _type",width=100)
        self.Cust_Details_table.column("no_of_rooms",width=100)
        self.Cust_Details_table.column("kitchen",width=100)
        self.Cust_Details_table.column("att_wash",width=100)
        self.Cust_Details_table.column("rent",width=100)
        self.Cust_Details_table.column("no_of_person",width=100)
        self.Cust_Details_table.column("deposite",width=100)
        self.Cust_Details_table.column("other_remark",width=100)

        self.Cust_Details_table.pack(fill=BOTH,expand=1)
        self.Cust_Details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_gender.get()=="Select" or self.var_c_id.get()=="" or self.var_name.get()=="" or self.var_room_type.get()=="Select" or self.var_no_of_rooms.get()=="Select" or self.var_kitchen.get()=="Select" or self.var_att_wash.get()=="Select" or self.var_rent.get()=="Select" or self.var_no_of_person.get()=="Select" or self.var_deposite.get()=="Select" or self.var_other_remark.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Abhi@2127',database="room_finding_gui")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into costumer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                self.var_c_id.get(),
                                                self.var_name.get(),
                                                self.var_gender.get(),
                                                self.var_mobile.get(),
                                                self.var_email.get(),
                                                self.var_adhar.get(),
                                                self.var_add.get(),
                                                self.var_regi_time.get(),
                                                self.var_nation.get(),
                                                self.var_local_person.get(),
                                                self.var_person_con.get(),
                                                self.var_parea1.get(),
                                                self.var_parea2.get(),
                                                self.var_parea3.get(),
                                                self.var_room_type.get(),
                                                self.var_no_of_rooms.get(),
                                                self.var_kitchen.get(),
                                                self.var_att_wash.get(),
                                                self.var_rent.get(),
                                                self.var_no_of_person.get(),
                                                self.var_deposite.get(),
                                                self.var_other_remark.get()
                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)
        
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Abhi@2127',database="room_finding_gui")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from costumer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_table.delete(*self.Cust_Details_table.get_children())
            for i in rows:
                self.Cust_Details_table.insert("",END,values=i)

            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_table.focus()
        content=self.Cust_Details_table.item(cursor_row)
        row=content["values"]

        self.var_c_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_mobile.set(row[3]),
        self.var_email.set(row[4]),
        self.var_adhar.set(row[5]),
        self.var_add.set(row[6]),
        self.var_regi_time.set(row[7]),
        self.var_nation.set(row[8]),
        self.var_local_person.set(row[9]),
        self.var_person_con.set(row[10]),
        self.var_parea1.set(row[11]),
        self.var_parea2.set(row[12]),
        self.var_parea3.set(row[13]),
        self.var_room_type.set(row[14]),
        self.var_no_of_rooms.set(row[15]),
        self.var_kitchen.set(row[16]),
        self.var_att_wash.set(row[17]),
        self.var_rent.set(row[18]),
        self.var_no_of_person.set(row[19]),
        self.var_deposite.set(row[20]),
        self.var_other_remark.set(row[21])
    
    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE costumer SET name=%s, gender=%s, mobile=%s, email=%s, adhar=%s, `addr`=%s, regi_time=%s, nation=%s, local_person=%s, person_con=%s, parea1=%s, parea2=%s, parea3=%s, room_type=%s, no_of_rooms=%s, kitchen=%s, att_wash=%s, rent=%s, no_of_person=%s, deposite=%s, other_remark=%s WHERE c_id=%s", (
                self.var_name.get(),
                self.var_gender.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_adhar.get(),
                self.var_add.get(),
                self.var_regi_time.get(),
                self.var_nation.get(),
                self.var_local_person.get(),
                self.var_person_con.get(),
                self.var_parea1.get(),
                self.var_parea2.get(),
                self.var_parea3.get(),
                self.var_room_type.get(),
                self.var_no_of_rooms.get(),
                self.var_kitchen.get(),
                self.var_att_wash.get(),
                self.var_rent.get(),
                self.var_no_of_person.get(),
                self.var_deposite.get(),
                self.var_other_remark.get(),
                self.var_c_id.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Costumer has been updated successfully",parent=self.root)
            
    def mdelete(self):
        if self.var_name.get()=="" or self.var_email.get()=="" or self.var_mobile.get()=="":
                        messagebox.showerror("Error","First select the member")
        else:
            mdelete=messagebox.askyesno("Room finding app","Do you want to delete this data",parent=self.root)
            if mdelete>0:
                conn=mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                my_cursor=conn.cursor()
                query="delete from costumer where c_id=%s"
                value=(self.var_c_id.get(),)
                my_cursor.execute(query,value)
            else:
                if not mdelete:
                        return
            conn.commit()
            self.fetch_data()
            conn.close()

    def reset(self):
        #self.var_c_id.set(""),
        self.var_name.set(""),
        self.var_gender.set("Select"),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_adhar.set(""),
        self.var_add.set(""),
        d1=datetime.datetime.today(),
        self.var_regi_time.set(d1),
        self.var_nation.set(""),
        self.var_local_person.set(""),
        self.var_person_con.set(""),
        self.var_parea1.set(""),
        self.var_parea2.set(""),
        self.var_parea3.set(""),
        self.var_room_type.set("Select"),
        self.var_no_of_rooms.set("Select"),
        self.var_kitchen.set("Select"),
        self.var_att_wash.set("Select"),
        self.var_rent.set("Select"),
        self.var_no_of_person.set("Select"),
        self.var_deposite.set("Select"),
        self.var_other_remark.set(""),
        self.search_var.set("Select")

        x=random.randint(10000,99999)
        self.var_c_id.set(str(x))


# ... (your other code) with help of gemini

    def search(self):
        if self.search_var.get()=="Select":
                         messagebox.showerror("Error","Please select which criteria have to search",parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
            my_cursor = conn.cursor()

            search_by = self.search_var.get()
            search_text = self.txt_search.get()

            try:
                query = f"SELECT * FROM costumer WHERE {search_by} LIKE %s"
                my_cursor.execute(query, ('%' + search_text + '%',)) # Corrected to use a tuple

                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.Cust_Details_table.delete(*self.Cust_Details_table.get_children())
                    for i in rows:
                        self.Cust_Details_table.insert("", END, values=i)
                else:
                    messagebox.showinfo("Info", "No matching records found.", parent=self.root)
                conn.commit()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}", parent=self.root)
            finally:
                conn.close()

        










if __name__== "__main__":
    root=Tk()
    obj=cust_window(root)
    root.mainloop()