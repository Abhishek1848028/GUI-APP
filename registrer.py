from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
import datetime
from terms import terms_and_conditions

class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        #============variables===============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_squestion=StringVar()
        self.var_answer=StringVar()
        self.var_password=StringVar()
        self.var_confirmpass=StringVar()
        self.entry_user_id=StringVar()



        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ashis\OneDrive\Documents\Desktop\ROOM_FINDING_GUI_APP\IMAGES\bg2[1][1].jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        #left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\ashis\OneDrive\Documents\Desktop\ROOM_FINDING_GUI_APP\IMAGES\bg3.png")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        #================main frame================
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,height=550,width=800)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green",bg="white")
        register_lbl.place(x=20,y=20)

        #=================labels & entry===============
        #row 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.lname_entry.place(x=370,y=130,width=250)
        
        #row 2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.contact_entry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email ID",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.email_entry.place(x=370,y=200,width=250)

        #row 3
        squestion=Label(frame,text="Select Sequerity Question",font=("times new roman",15,"bold"),bg="white")
        squestion.place(x=50,y=240)

        combo_squestion=ttk.Combobox(frame,textvariable=self.var_squestion,font=("arial",12,"bold"),width=27,state="readonly")
        combo_squestion["values"]=("Select","Your nick name","your first school name","your birth place","your pet name")
        combo_squestion.current(0)
        combo_squestion.place(x=50,y=270,width=250)

        answer=Label(frame,text="Answer",font=("times new roman",15,"bold"),bg="white")
        answer.place(x=370,y=240)

        self.answer_entry=ttk.Entry(frame,textvariable=self.var_answer,font=("times new roman",15,"bold"))
        self.answer_entry.place(x=370,y=270,width=250)

        #row 4
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        password.place(x=50,y=310)

        self.password_entry=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15,"bold"))
        self.password_entry.place(x=50,y=340,width=250)

        confirmpass=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirmpass.place(x=370,y=310)

        self.confirmpass_entry=ttk.Entry(frame,textvariable=self.var_confirmpass,font=("times new roman",15,"bold"))
        self.confirmpass_entry.place(x=370,y=340,width=250)

        #================check button==============
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=65,y=400)

        termbtn=Button(frame,command=self.term_details,text="Terms & Conditions",font=("times new roman",12,"bold"),borderwidth=0,fg="blue",bg="white")
        termbtn.place(x=170,y=400,width=135)

        registerbtn=Button(frame,command=self.register_data,text="Register Now",font=("times new roman",15,"bold"),fg="white",bg="red")
        registerbtn.place(x=50,y=450,width=200)

        loginbtn=Button(frame,text="Login Now",font=("times new roman",15,"bold"),fg="white",bg="red")
        loginbtn.place(x=400,y=450,width=200)


    #===============function declaration===============4
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_squestion.get()=="Select" or self.var_password.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_password.get()!=self.var_confirmpass.get():
            messagebox.showerror("Error","Password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree terms and conditions")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Abhi@2127',database="room_finding_gui")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already Exist, please another email or contact no")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_squestion.get(),
                                                                                    self.var_answer.get(),
                                                                                    self.var_password.get(),
                                                                                    
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Succes","welcome you are registered")


    def term_details(self):
        self.new_window=Toplevel(self.root)
        self.app=terms_and_conditions(self.new_window)



if __name__== "__main__":
    root=Tk()
    app=register(root)
    root.mainloop()