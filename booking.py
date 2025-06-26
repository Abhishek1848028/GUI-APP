from tkinter import*
from PIL import Image,ImageTk,ImageGrab
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
import datetime
import room as room_window
from mysql.connector import Error
from reportlab.pdfgen import canvas  # For optional PDF conversion
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet




class booking_window:
    def __init__(self,root):
        self.root=root
        self.root.title("ROOM FINDING GUI APP")     #for giving title the app
        self.root.geometry("1295x550+230+228")

        #=======================varibles===============
        self.var_bookingid=StringVar()
        x=random.randint(10000,99999)
        self.var_bookingid.set(str(x))

        self.var_owner_phone=StringVar()
        self.var_costumer_phone=StringVar()
        self.var_regi_time=StringVar()
        self.var_finale_rent=StringVar()
        self.var_agreement_duration=StringVar()
        self.var_room_visittime=StringVar()
        self.var_cpmeny_charge=StringVar()
        self.var_agent_name=StringVar()
        self.var_discription=StringVar()

        self.owner_dataframe = None  # Store reference to owner's showdataframe
        self.customer_dataframe = None  # Store reference to customer's showdataframe
        self.booking_dataframe = None

        lbl_title=Label(self.root,text="BOOKING",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        img2=Image.open(r"C:\Users\ashis\OneDrive\Documents\Desktop\ROOM_FINDING_GUI_APP\IMAGES\logo.jpg")      
        img2=img2.resize((120,40),Image.LANCZOS)      
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)     
        lblimg.place(x=5,y=4,width=120,height=40)

        #=================== lavel frame====================
        levelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="BOOKING DETAIL",font=("times new roman",12,"bold"),padx=2)
        levelframeleft.place(x=5,y=50,width=425,height=490)


        #============ lavels and entrys========================
        #custmor_id
        lbl_booking_id=Label(levelframeleft,text="Booking ID",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_booking_id.grid(row=0,column=0,sticky=W)

        entry_id=ttk.Entry(levelframeleft,textvariable=self.var_bookingid,width=29,state="readonly",font=("times new roman",13,"bold"))
        entry_id.grid(row=0,column=1)

        #owner contact
        lbl_owner_phone=Label(levelframeleft,text="Owner ID",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_owner_phone.grid(row=1,column=0,sticky=W)

        entry_owner_phone=ttk.Entry(levelframeleft,textvariable=self.var_owner_phone,width=18,font=("times new roman",13,"bold"))
        entry_owner_phone.grid(row=1,column=1,sticky=W)

        #fetch data button
        btnfetchdata=Button(levelframeleft,command=self.fetch_owner_data,text="FETCH DATA",font=("arial",10,"bold"),bg="black",fg="gold",width=10,cursor="hand2")
        btnfetchdata.place(x=318,y=28)

        #cust contact
        lbl_cust_phone=Label(levelframeleft,text="Costumer ID",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_cust_phone.grid(row=2,column=0,sticky=W)

        entry_cust_phone=ttk.Entry(levelframeleft,textvariable=self.var_costumer_phone,width=18,font=("times new roman",13,"bold"))
        entry_cust_phone.grid(row=2,column=1,sticky=W)

        #fetch data button
        btnfetchdata=Button(levelframeleft,command=self.fetch_costumer_data,text="FETCH DATA",font=("arial",10,"bold"),bg="black",fg="gold",width=10,cursor="hand2")
        btnfetchdata.place(x=318,y=52)

        #booking time
        lbl_bookingtime=Label(levelframeleft,text="Booking time",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_bookingtime.grid(row=3,column=0,sticky=W)

        entry_bookingtime=ttk.Entry(levelframeleft,textvariable=self.var_regi_time,width=29,font=("times new roman",13,"bold"))
        entry_bookingtime.grid(row=3,column=1)

        #Agrrement duration
        lbl_agree_duration=Label(levelframeleft,text="Agreement duration",font=("times new roman",11,"bold"),padx=2,pady=2)
        lbl_agree_duration.grid(row=4,column=0,sticky=W)

        combo_duration=ttk.Combobox(levelframeleft,textvariable=self.var_agreement_duration,font=("arial",12,"bold"),width=27,state="readonly")
        combo_duration["values"]=("Select","1 Year","2 Year","3 Year","4 Year","5 Year","6 Year","7 Year","8 Year","9 Year","10 Year","11 Year","12 Year")
        combo_duration.current(0)
        combo_duration.grid(row=4,column=1)

        #Fianle rent
        lbl_finale_rent=Label(levelframeleft,text="Finale rent",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_finale_rent.grid(row=5,column=0,sticky=W)

        entry_finale_rent=ttk.Entry(levelframeleft,textvariable=self.var_finale_rent,width=29,font=("times new roman",13,"bold"))
        entry_finale_rent.grid(row=5,column=1)

        #company charge
        lbl_companeycharge=Label(levelframeleft,text="Compney Charge",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_companeycharge.grid(row=6,column=0,sticky=W)

        entry_companeycharge=ttk.Entry(levelframeleft,textvariable=self.var_cpmeny_charge,width=29,font=("times new roman",13,"bold"))
        entry_companeycharge.grid(row=6,column=1)

        #room visit time
        lbl_roomvisittime=Label(levelframeleft,text="Room visit time",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_roomvisittime.grid(row=7,column=0,sticky=W)

        entry_roomvisittime=ttk.Entry(levelframeleft,textvariable=self.var_room_visittime,width=29,font=("times new roman",13,"bold"))
        entry_roomvisittime.grid(row=7,column=1)

        #agent name
        lbl_agentname=Label(levelframeleft,text="Agent Name",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_agentname.grid(row=8,column=0,sticky=W)

        entry_agentname=ttk.Entry(levelframeleft,textvariable=self.var_agent_name,width=29,font=("times new roman",13,"bold"))
        entry_agentname.grid(row=8,column=1)

        #description
        lbl_description=Label(levelframeleft,text="Description",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_description.grid(row=9,column=0,sticky=W)

        entry_description=ttk.Entry(levelframeleft,textvariable=self.var_discription,width=29,font=("times new roman",13,"bold"))
        entry_description.grid(row=9,column=1)

        #bill bottun
        btnbill=Button(levelframeleft,command=self.fetch_booking_data,text="BILLING",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnbill.place(x=106,y=370)

        #print botton
        btnprint=Button(levelframeleft,command=self.print_dataframes,text="PRINT",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnprint.place(x=208,y=370)

        #===============buttons in booking======================

        btn_frame=Frame(levelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=410,width=412,height=40)

        btnAdd=Button(btn_frame,command=self.add_data,text="BOOK",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnAdd.grid(row=0,column=1,padx=1)

        btnUpdate=Button(btn_frame,command=self.update,text="UPDATE",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnUpdate.grid(row=0,column=2,padx=1)

        btnDelete=Button(btn_frame,command=self.mdelete,text="DELETE",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnDelete.grid(row=0,column=3,padx=1)

        btnReset=Button(btn_frame,command=self.reset,text="RESET",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnReset.grid(row=0,column=4,padx=1)

        #============ tabel frame search system================
        leveltabelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View detail & search system",font=("times new roman",12,"bold"),padx=2)
        leveltabelframe.place(x=435,y=230,width=853,height=310)

        lbl_searchby=Label(leveltabelframe,text="Search By",font=("times new roman",12,"bold"),bg="red",fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(leveltabelframe,textvariable=self.search_var,font=("arial",12,"bold"),width=20,state="readonly")
        combo_search["values"]=("booking_id","Owner_phone","Costumer_phone")
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

        self.Room_Details_table=ttk.Treeview(details_table,column=("booking_id","Owner_phone","Costumer_phone","Regi_time","Agree_duration","finale_rent","Compeny_charge","R_visit_time","Agent_name"
                                                                ,"discription"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Room_Details_table.xview)
        scroll_y.config(command=self.Room_Details_table.yview)

        self.Room_Details_table.heading("booking_id",text="Booking ID")
        self.Room_Details_table.heading("Owner_phone",text="Owner ID")
        self.Room_Details_table.heading("Costumer_phone",text="Costumer ID")
        self.Room_Details_table.heading("Regi_time",text="Registration time")
        self.Room_Details_table.heading("Agree_duration",text="Agreement Duration")
        self.Room_Details_table.heading("finale_rent",text="finale rent")
        self.Room_Details_table.heading("Compeny_charge",text="Compeny Charge")
        self.Room_Details_table.heading("R_visit_time",text="Room Visit time")
        self.Room_Details_table.heading("Agent_name",text="Agent Name")
        self.Room_Details_table.heading("discription",text="Discription")

        self.Room_Details_table["show"]="headings"

        self.Room_Details_table.column("booking_id",width=100)
        self.Room_Details_table.column("Owner_phone",width=100)
        self.Room_Details_table.column("Costumer_phone",width=100)
        self.Room_Details_table.column("Regi_time",width=100)
        self.Room_Details_table.column("Agree_duration",width=100)
        self.Room_Details_table.column("finale_rent",width=100)
        self.Room_Details_table.column("Compeny_charge",width=100)
        self.Room_Details_table.column("R_visit_time",width=100)
        self.Room_Details_table.column("Agent_name",width=100)
        self.Room_Details_table.column("discription",width=100)
        
        self.fetch_data()
        self.Room_Details_table.pack(fill=BOTH,expand=1)
        self.Room_Details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def print_dataframes(self):
        """Creates a PDF representation of the owner and customer dataframes."""
        if self.owner_dataframe and self.customer_dataframe and self.booking_dataframe:
            try:
                # Extract data from owner dataframe
                owner_data = []
                for widget in self.owner_dataframe.winfo_children():
                    if isinstance(widget, Label):
                        owner_data.append(widget.cget("text"))

                # Extract data from customer dataframe
                customer_data = []
                for widget in self.customer_dataframe.winfo_children():
                    if isinstance(widget, Label):
                        customer_data.append(widget.cget("text"))

                # Extract data from booking dataframe
                booking_data = []
                for widget in self.booking_dataframe.winfo_children():
                    if isinstance(widget, Label):
                        booking_data.append(widget.cget("text"))

                # Format data into tables
                owner_table_data = [owner_data[i:i+2] for i in range(0, len(owner_data), 2)]
                customer_table_data = [customer_data[i:i+2] for i in range(0, len(customer_data), 2)]
                booking_table_data = [booking_data[i:i+2] for i in range(0, len(booking_data), 2)]

                # Create PDF
                filename = "dataframe_print.pdf"
                filepath = os.path.join(os.getcwd(), filename)
                doc = SimpleDocTemplate(filepath, pagesize=letter)  # Use filepath here
                elements = []

                # Add owner table
                elements.append(Paragraph("Owner Data", getSampleStyleSheet()["Heading2"]))
                owner_table = Table(owner_table_data)
                owner_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                                ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
                elements.append(owner_table)

                # Add customer table
                elements.append(Paragraph("Customer Data", getSampleStyleSheet()["Heading2"]))
                customer_table = Table(customer_table_data)
                customer_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                                    ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
                elements.append(customer_table)

                # Add owner table
                elements.append(Paragraph("Booking Data", getSampleStyleSheet()["Heading2"]))
                booking_table = Table(booking_table_data)
                booking_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                                ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
                elements.append(booking_table)

                elements.append(Paragraph("Compeny name: Find my rooms .""place:................", getSampleStyleSheet()["Heading2"]))
                elements.append(Paragraph("Stamp & Sign: ................""Date and Time: ................... ", getSampleStyleSheet()["Heading2"]))


                # Build the PDF after adding all elements
                doc.build(elements)
                

                # Open the PDF using the default PDF viewer
                if os.name == 'nt':  # Windows
                    os.startfile(filepath)
                else:  # macOS and Linux
                    subprocess.Popen(['xdg-open', filepath])

                messagebox.showinfo("Print", f"Dataframes saved and opened as {filename}",parent=self.root)


            except Exception as e:
                messagebox.showerror("Error", f"Failed to print dataframes: {e}")
        else:
            messagebox.showerror("Error", "Dataframes not available.",parent=self.root)
    

    def add_data(self):
        if self.var_owner_phone.get()=="" or self.var_costumer_phone.get()=="" or self.var_bookingid.get()=="" or self.var_agreement_duration.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Abhi@2127',database="room_finding_gui")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into booking values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                self.var_bookingid.get(),
                                                self.var_owner_phone.get(),
                                                self.var_costumer_phone.get(),
                                                self.var_regi_time.get(),
                                                self.var_agreement_duration.get(),
                                                self.var_finale_rent.get(),
                                                self.var_cpmeny_charge.get(),
                                                self.var_room_visittime.get(),
                                                self.var_agent_name.get(),
                                                self.var_discription.get()
                                                
                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Booking has been Done",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Abhi@2127',database="room_finding_gui")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from booking")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Room_Details_table.delete(*self.Room_Details_table.get_children())
            for i in rows:
                self.Room_Details_table.insert("",END,values=i)

            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Room_Details_table.focus()
        content=self.Room_Details_table.item(cursor_row)
        row=content["values"]

        self.var_bookingid.set(row[0]),
        self.var_owner_phone.set(row[1]),
        self.var_costumer_phone.set(row[2]),
        self.var_regi_time.set(row[3]),
        self.var_agreement_duration.set(row[4]),
        self.var_finale_rent.set(row[5]),
        self.var_cpmeny_charge.set(row[6]),
        self.var_room_visittime.set(row[7]),
        self.var_agent_name.set(row[8]),
        self.var_discription.set(row[9]),
        

    def update(self):
        if self.var_owner_phone.get() == "" or self.var_costumer_phone.get()=="":
            messagebox.showerror("error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE booking SET Owner_phone=%s, Costumer_phone=%s, Regi_time=%s, Agree_duration=%s, finale_rent=%s, Compeny_charge=%s, R_visit_time=%s, Agent_name=%s, discription=%s WHERE booking_id=%s", (
                                                self.var_owner_phone.get(),
                                                self.var_costumer_phone.get(),
                                                self.var_regi_time.get(),
                                                self.var_agreement_duration.get(),
                                                self.var_finale_rent.get(),
                                                self.var_cpmeny_charge.get(),
                                                self.var_room_visittime.get(),
                                                self.var_agent_name.get(),
                                                self.var_discription.get(),
                                                self.var_bookingid.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Booking has been updated successfully",parent=self.root)
            
    def mdelete(self):
        mdelete=messagebox.askyesno("Room finding app","Do you want to delete this data",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
            my_cursor=conn.cursor()
            query="delete from booking where booking_id=%s"
            value=(self.var_bookingid.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                    return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        
        self.var_owner_phone.set(""),
        self.var_costumer_phone.set(""),
        d1=datetime.datetime.today(),
        self.var_regi_time.set(d1),
        self.var_agreement_duration.set("Select"),
        self.var_finale_rent.set(""),
        self.var_cpmeny_charge.set(""),
        self.var_room_visittime.set(""),
        self.var_agent_name.set(""),
        self.var_discription.set(""),
        if self.owner_dataframe:
            self.owner_dataframe.destroy()
            self.owner_dataframe = None

        if self.customer_dataframe:
            self.customer_dataframe.destroy()
            self.customer_dataframe = None

        if self.booking_dataframe:
            self.booking_dataframe.destroy()
            self.booking_dataframe = None
        
        x=random.randint(10000,99999)
        self.var_bookingid.set(str(x))
        

# ... (rest of your code) with the help of gemini
#first show detail

    def fetch_owner_data(self):
        if self.var_owner_phone.get() == "":
            messagebox.showerror("Error", "Please fill Owner id", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                my_cursor = conn.cursor()
                query = ("select c_id from room where c_id=%s")
                value = (self.var_owner_phone.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "This ID not found", parent=self.root)
                else:
                    if self.owner_dataframe: #check if the frame already exist.
                        self.owner_dataframe.destroy() #if yes then destroy it
                    self.owner_dataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2, pady=6)
                    self.owner_dataframe.place(x=435, y=55, width=290, height=175)

                    #oner id
                    lblownerid = Label(self.owner_dataframe, text="Owner ID:", font=("arial", 8, "bold"))
                    lblownerid.place(x=0, y=0)

                    lbl = Label(self.owner_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl.place(x=110, y=0)

                    #name
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select name from room where c_id=%s")
                    value = (self.var_owner_phone.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblname = Label(self.owner_dataframe, text="Owner Name:", font=("arial", 8, "bold"))
                    lblname.place(x=0, y=20)

                    lbl2 = Label(self.owner_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl2.place(x=110, y=20)

                    #mobile
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select mobile from room where c_id=%s")
                    value = (self.var_owner_phone.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblmobile = Label(self.owner_dataframe, text="Mobile No:", font=("arial", 8, "bold"))
                    lblmobile.place(x=0, y=40)

                    lbl3 = Label(self.owner_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl3.place(x=110, y=40)

                    #email
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select email from room where c_id=%s")
                    value = (self.var_owner_phone.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblemail = Label(self.owner_dataframe, text="Email:", font=("arial", 8, "bold"))
                    lblemail.place(x=0, y=60)

                    lbl4 = Label(self.owner_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl4.place(x=110, y=60)

                    #adhar
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select adhar from room where c_id=%s")
                    value = (self.var_owner_phone.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lbladhar = Label(self.owner_dataframe, text="Adhar No:", font=("arial", 8, "bold"))
                    lbladhar.place(x=0, y=80)

                    lbl5 = Label(self.owner_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl5.place(x=110, y=80)

                    #registration time
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select regi_time from room where c_id=%s")
                    value = (self.var_owner_phone.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblregitime = Label(self.owner_dataframe, text="Registration Time:", font=("arial", 8, "bold"))
                    lblregitime.place(x=0, y=100)

                    lbl6 = Label(self.owner_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl6.place(x=110, y=100)

                    #building detail
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select nation from room where c_id=%s")
                    value = (self.var_owner_phone.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblbuilding = Label(self.owner_dataframe, text="Building:", font=("arial", 8, "bold"))
                    lblbuilding.place(x=0, y=120)

                    lbl7 = Label(self.owner_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl7.place(x=110, y=120)

                    #Area
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select parea1 from room where c_id=%s")
                    value = (self.var_owner_phone.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblarea = Label(self.owner_dataframe, text="Area:", font=("arial", 8, "bold"))
                    lblarea.place(x=0, y=140)

                    lbl8 = Label(self.owner_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl8.place(x=110, y=140)


            except Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}", parent=self.root)
            finally:
                if 'conn' in locals() and conn.is_connected():
                    conn.close()


    def fetch_costumer_data(self):
        if self.var_costumer_phone.get() == "":
            messagebox.showerror("Error", "Please fill Costumer Id", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                my_cursor = conn.cursor()
                query = ("select c_id from costumer where c_id=%s")
                value = (self.var_costumer_phone.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "This ID not found", parent=self.root)
                else:
                    if self.customer_dataframe: #check if the frame already exist.
                        self.customer_dataframe.destroy() #if yes then destroy it.

                    self.customer_dataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2, pady=6)
                    self.customer_dataframe.place(x=725, y=55, width=290, height=175)

                    #costumer id
                    lblownerid = Label(self.customer_dataframe, text="Costumer ID:", font=("arial", 8, "bold"))
                    lblownerid.place(x=0, y=0)

                    lbl = Label(self.customer_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl.place(x=110, y=0)

                    #name
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select name from costumer where c_id=%s")
                    value = (self.var_costumer_phone.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblname = Label(self.customer_dataframe, text="Costumer Name:", font=("arial", 8, "bold"))
                    lblname.place(x=0, y=20)

                    lbl2 = Label(self.customer_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl2.place(x=110, y=20)

                    #mobile
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select mobile from costumer where c_id=%s")
                    value = (self.var_costumer_phone.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblmobile = Label(self.customer_dataframe, text="Mobile No:", font=("arial", 8, "bold"))
                    lblmobile.place(x=0, y=40)

                    lbl3 = Label(self.customer_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl3.place(x=110, y=40)

                    #email
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select email from costumer where c_id=%s")
                    value = (self.var_costumer_phone.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblemail = Label(self.customer_dataframe, text="Email:", font=("arial", 8, "bold"))
                    lblemail.place(x=0, y=60)

                    lbl4 = Label(self.customer_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl4.place(x=110, y=60)

                    #adhar
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select adhar from costumer where c_id=%s")
                    value = (self.var_costumer_phone.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lbladhar = Label(self.customer_dataframe, text="Adhar No:", font=("arial", 8, "bold"))
                    lbladhar.place(x=0, y=80)

                    lbl5 = Label(self.customer_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl5.place(x=110, y=80)

                    #registration time
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select regi_time from costumer where c_id=%s")
                    value = (self.var_costumer_phone.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblregitime = Label(self.customer_dataframe, text="Registration Time:", font=("arial", 8, "bold"))
                    lblregitime.place(x=0, y=100)

                    lbl6 = Label(self.customer_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl6.place(x=110, y=100)

                    #permanent address
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select addr from costumer where c_id=%s")
                    value = (self.var_costumer_phone.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblbuilding = Label(self.customer_dataframe, text="Permanent Add:", font=("arial", 8, "bold"))
                    lblbuilding.place(x=0, y=120)

                    lbl7 = Label(self.customer_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl7.place(x=110, y=120)

                    #gender
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select gender from costumer where c_id=%s")
                    value = (self.var_costumer_phone.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblarea = Label(self.customer_dataframe, text="Gender:", font=("arial", 8, "bold"))
                    lblarea.place(x=0, y=140)

                    lbl8 = Label(self.customer_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl8.place(x=110, y=140)


            except Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}", parent=self.root)
            finally:
                if 'conn' in locals() and conn.is_connected():
                    conn.close() 

#            my_cursor.execute("UPDATE booking SET Owner_phone=%s, Costumer_phone=%s, Regi_time=%s, Agree_duration=%s, finale_rent=%s, Compeny_charge=%s, R_visit_time=%s, Agent_name=%s, discription=%s WHERE booking_id=%s", (

    def fetch_booking_data(self):
        if self.var_bookingid.get() == "":
            messagebox.showerror("Error", "Please fill Owner id", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                my_cursor = conn.cursor()
                query = ("select booking_id from booking where booking_id=%s")
                value = (self.var_bookingid.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "This ID not found", parent=self.root)
                else:
                    if self.booking_dataframe: #check if the frame already exist.
                        self.booking_dataframe.destroy() #if yes then destroy it
                    self.booking_dataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2, pady=6)
                    self.booking_dataframe.place(x=1015,y=53,width=275,height=178)

                    #oner id
                    lblownerid = Label(self.booking_dataframe, text="Booking ID:", font=("arial", 8, "bold"))
                    lblownerid.place(x=0, y=0)

                    lbl = Label(self.booking_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl.place(x=110, y=0)

                    #booking time
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select Regi_time from booking where booking_id=%s")
                    value = (self.var_bookingid.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblname = Label(self.booking_dataframe, text="Booking Time:", font=("arial", 8, "bold"))
                    lblname.place(x=0, y=20)

                    lbl2 = Label(self.booking_dataframe, text=row, font=("arial", 7, "bold"))
                    lbl2.place(x=110, y=20)

                    #agreement duration
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select Agree_duration from booking where booking_id=%s")
                    value = (self.var_bookingid.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblmobile = Label(self.booking_dataframe, text="Agreement duration:", font=("arial", 8, "bold"))
                    lblmobile.place(x=0, y=40)

                    lbl3 = Label(self.booking_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl3.place(x=110, y=40)

                    #finale rent
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select finale_rent from booking where booking_id=%s")
                    value = (self.var_bookingid.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblemail = Label(self.booking_dataframe, text="Finale rent:", font=("arial", 8, "bold"))
                    lblemail.place(x=0, y=60)

                    lbl4 = Label(self.booking_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl4.place(x=110, y=60)

                    #room visit time
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select R_visit_time from booking where booking_id=%s")
                    value = (self.var_bookingid.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lbladhar = Label(self.booking_dataframe, text="visit time:", font=("arial", 8, "bold"))
                    lbladhar.place(x=0, y=80)

                    lbl5 = Label(self.booking_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl5.place(x=110, y=80)

                    #compeny charge
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select Compeny_charge from booking where booking_id=%s")
                    value = (self.var_bookingid.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblregitime = Label(self.booking_dataframe, text="Compeny charge:", font=("arial", 8, "bold"))
                    lblregitime.place(x=0, y=100)

                    lbl6 = Label(self.booking_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl6.place(x=110, y=100)

                    #agent name
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select Agent_name from booking where booking_id=%s")
                    value = (self.var_bookingid.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblbuilding = Label(self.booking_dataframe, text="Agent name:", font=("arial", 8, "bold"))
                    lblbuilding.place(x=0, y=120)

                    lbl7 = Label(self.booking_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl7.place(x=110, y=120)

                    #discription
                    conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                    my_cursor = conn.cursor()
                    query = ("select discription from booking where booking_id=%s")
                    value = (self.var_bookingid.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblarea = Label(self.booking_dataframe, text="Discription:", font=("arial", 8, "bold"))
                    lblarea.place(x=0, y=140)

                    lbl8 = Label(self.booking_dataframe, text=row, font=("arial", 8, "bold"))
                    lbl8.place(x=110, y=140)


            except Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}", parent=self.root)
            finally:
                if 'conn' in locals() and conn.is_connected():
                    conn.close()

    def search(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
        my_cursor = conn.cursor()

        search_by = self.search_var.get()
        search_text = self.txt_search.get()

        try:
            query = f"SELECT * FROM booking WHERE {search_by} LIKE %s"
            my_cursor.execute(query, ('%' + search_text + '%',)) # Corrected to use a tuple

            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.Room_Details_table.delete(*self.Room_Details_table.get_children())
                for i in rows:
                    self.Room_Details_table.insert("", END, values=i)
            else:
                messagebox.showinfo("Info", "No matching records found.", parent=self.root)
            conn.commit()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}", parent=self.root)
        finally:
            conn.close()          


if __name__== "__main__":
    root=Tk()
    obj=booking_window(root)
    root.mainloop()