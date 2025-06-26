from tkinter import*                
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import tkinter
from Roomgui import roomguiapp
from terms import terms_and_conditions
from tkdocviewer import*
import tkinter as tk




def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.entry_user_id=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ashis\OneDrive\Documents\Desktop\ROOM_FINDING_GUI_APP\IMAGES\123.jpg")    #background image of mai login window

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")                                #frame for login window
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\ashis\OneDrive\Documents\Desktop\ROOM_FINDING_GUI_APP\IMAGES\login_symbol.webp")          #image login symbol
        img1=img1.resize((100,100),Image.LANCZOS)                                        #resize
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)                               #place

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #=============================entry fill and labels for user id and password in main window========================
        lbl_user_id=Label(frame,text="User ID",font=("times new roman",12,"bold"),fg="white",bg="black",padx=2,pady=2)
        lbl_user_id.place(x=75,y=150)

        self.entry_user_id=ttk.Entry(frame,font=("times new roman",13,"bold"))
        self.entry_user_id.place(x=40,y=180,width=270)

        lbl_pass=Label(frame,text="Password",font=("times new roman",12,"bold"),fg="white",bg="black",padx=2,pady=2)
        lbl_pass.place(x=70,y=225)

        self.entry_pass=ttk.Entry(frame,font=("times new roman",13,"bold"),show="*")
        self.entry_pass.place(x=40,y=250,width=270)


        #==========icon image===============
        img2=Image.open(r"C:\Users\ashis\OneDrive\Documents\Desktop\ROOM_FINDING_GUI_APP\IMAGES\login_symbol.webp")      #login symbol imfront of user id
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\ashis\OneDrive\Documents\Desktop\ROOM_FINDING_GUI_APP\IMAGES\password icon.jpg")     #password symbol infront of password
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)

        #login btn
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activebackground="red",activeforeground="white")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register btn
        registerbtn=Button(frame,command=self.register_window,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="white")
        registerbtn.place(x=15,y=350,width=160)

        #forget pass btn
        forgetbtn=Button(frame,command=self.forgot_password_window,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="white")
        forgetbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)                      #function declaration for importing register window in login window
        self.app=register(self.new_window)
    
    def login(self):
        if self.entry_user_id.get() == "" or self.entry_pass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Abhi@2127',database="room_finding_gui")
                my_cursor=conn.cursor()
                
                my_cursor.execute("SELECT email, fmane, password FROM register WHERE email=%s", (self.entry_user_id.get(),))
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid username or Password", parent=self.root)
                elif row[2] != self.entry_pass.get():
                    messagebox.showerror("Error", "Invalid Password", parent=self.root)
                    
                else:
                    open_main=messagebox.askyesno("YesNO","Acces Only Admin",parent=self.root)
                    if open_main>0:
                        logged_in_email, logged_in_fname, _ = row  # Get email and fname
                        logged_in_info = {"fname": logged_in_fname, "email": logged_in_email}
                        self.new_window = tk.Toplevel(self.root)
                        self.app = roomguiapp(self.new_window, logged_in_info)  # Pass user info
                        self.root.withdraw()
                    else:
                        if not open_main:
                            return
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


    #======================reset password==============
    
    def reset_pass(self):
        if self.combo_squestion.get() == "Select":
            messagebox.showerror("Error", "Select security question",parent=self.root2)
        elif self.answer_entry.get() == "":
            messagebox.showerror("Error", "Please enter the answer",parent=self.root2)
        elif self.password_entry.get() == "":
            messagebox.showerror("Error", "Please enter password",parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Abhi@2127', database="room_finding_gui")
                my_cursor = conn.cursor()
                query = "select * from register where email=%s and squestion=%s and answer=%s"
                value = (self.entry_user_id.get(), self.combo_squestion.get(), self.answer_entry.get()) #Corrected answer entry
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please enter the correct answer",parent=self.root2)
                else:
                    query = ("update register set password=%s where email=%s") #Corrected regester to register
                    value = (self.password_entry.get(), self.entry_user_id.get())
                    my_cursor.execute(query, value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Your password has been reset, please login with new password",parent=self.root2)
                    self.root2.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}",parent=self.root2)




    #===========================forget pass window=======================
    def forgot_password_window(self):
        if self.entry_user_id.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Abhi@2127',database="room_finding_gui")
            my_cursor=conn.cursor()
            query1=("select *from register where email=%s")
            value=(self.entry_user_id.get(),)
            my_cursor.execute(query1,value)
            row=my_cursor.fetchone()

            #print(row)

            if row==None:
                messagebox.showerror("Error","Please enter the valid username",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget password",font=("times new roman",12,"bold"),fg="red")
                l.place(x=0,y=10,relwidth=1)

                squestion=Label(self.root2,text="Select Sequerity Question",font=("times new roman",15,"bold"))
                squestion.place(x=50,y=80)

                self.combo_squestion=ttk.Combobox(self.root2,font=("arial",12,"bold"),width=27,state="readonly")
                self.combo_squestion["values"]=("Select","Your nick name","your first school name","your birth place","your pet name")
                self.combo_squestion.current(0)
                self.combo_squestion.place(x=50,y=110,width=250)

                answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"))
                answer.place(x=50,y=150)

                self.answer_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.answer_entry.place(x=50,y=180,width=250)

                password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"))
                password.place(x=50,y=220)

                self.password_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.password_entry.place(x=50,y=250,width=250)

                resetbtn=Button(self.root2,command=self.reset_pass,text="Reset",font=("times new roman",15,"bold"),fg="black",bg="light green")
                resetbtn.place(x=80,y=300,width=200)

    

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

        loginbtn=Button(frame,command=self.loginnow,text="Login Now",font=("times new roman",15,"bold"),fg="white",bg="red")
        loginbtn.place(x=400,y=450,width=200)


    #===============function declaration===============4
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_squestion.get()=="Select" or self.var_password.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_password.get()!=self.var_confirmpass.get():
            messagebox.showerror("Error","Password and confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree terms and conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Abhi@2127',database="room_finding_gui")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already Exist, please another email or contact no",parent=self.root)
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
            messagebox.showinfo("Succes","welcome you are registered",parent=self.root)

    
    def loginnow(self):
        self.new_window=Toplevel(self.root)
        self.app=login_window(self.new_window)

    def term_details(self):
        self.new_window=Toplevel(self.root)
        self.app=terms_and_conditions(self.new_window)
 



if __name__== "__main__":
    main()

