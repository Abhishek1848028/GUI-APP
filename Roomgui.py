from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from custumer import cust_window
from room import room_window
from booking import booking_window
from about import about_window
from tkinter import messagebox
import tkinter
import time
import datetime
from registrer import register
import mysql.connector


class roomguiapp:
    def __init__(self,root,logged_in_user_data=None):
        self.root=root
        self.root.title("ROOM FINDING GUI APP")     #for giving title the app
        self.root.geometry("1550x800+0+0")
        
        self.logged_in_user = logged_in_user_data if logged_in_user_data else {}  # Store user data


        #================= 1st image ====================
        img1=Image.open(r"C:\Users\ashis\OneDrive\Documents\Desktop\ROOM_FINDING_GUI_APP\IMAGES\img1.jpg")      #image pathin storage
        img1=img1.resize((1550,140),Image.LANCZOS)      #image resizing and lesser quality
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)     #place image as label
        lblimg.place(x=0,y=0,width=1550,height=140)


        #===========logo==================
        img2=Image.open(r"C:\Users\ashis\OneDrive\Documents\Desktop\ROOM_FINDING_GUI_APP\IMAGES\logo.jpg")      
        img2=img2.resize((230,140),Image.LANCZOS)      
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)     
        lblimg.place(x=0,y=0,width=230,height=140)

        

        #=================title=============

        self.levelframetitle=Frame(self.root,bg="black",bd=4,relief=RIDGE)
        self.levelframetitle.place(x=0,y=140,width=1550,height=50)

        self.lbl_userid=Label(self.levelframetitle,font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        self.lbl_userid.place(x=1225,y=0,height=45,width=310)

        # Labels for User Info (right side of self.levelframetitle)
        self.lbl_user_fname = Label(self.lbl_userid, text="", font=("arial", 9, "bold"), bg="black", fg="gold", anchor="e")
        self.lbl_user_fname.place(x=0,y=0)

        self.lbl_user_email = Label(self.lbl_userid, text="", font=("arial", 9,"bold"), bg="black", fg="gold", anchor="e")
        self.lbl_user_email.place(relx=0,rely=0.4)

    


        
        lbl_title=Label(self.levelframetitle,text="FIND MY ROOM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=223,y=0,width=1000,height=45)

        # Date and Time Label (initially empty)
        self.lbl_datetime = Label(self.levelframetitle, text="", font=("times new roman", 15,"bold"), bg="black", fg="gold",bd=4,relief=RIDGE, anchor="w")
        self.lbl_datetime.place(x=0, y=0, height=45) # Adjust y and height as needed

        self.update_datetime()
        self.display_user_info()  # Call to display user info

    
        #========== main frame===============
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #========menu======================
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230,height=50)

        #===========button frame=============
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=50,width=230,height=185)

        cust_btn=Button(btn_frame,text="COSTUMER",command=self.cust_details,width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,command=self.room_details,text="ROOM DETAIL",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        booking_btn=Button(btn_frame,command=self.booking_details,text="BOOKING",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        booking_btn.grid(row=2,column=0,pady=1)

        about_btn=Button(btn_frame,command=self.about_details,text="ABOUT US",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        about_btn.grid(row=3,column=0,pady=1)

        log_btn=Button(btn_frame,command=self.logout,text="LOG OUT",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        log_btn.grid(row=4,column=0,pady=1)

        #=====================right side image =====================
        img3=Image.open(r"C:\Users\ashis\OneDrive\Documents\Desktop\ROOM_FINDING_GUI_APP\IMAGES\img4.jpg")      
        img3=img3.resize((1310,590),Image.LANCZOS)      
        self.photoimg3=ImageTk.PhotoImage(img3)

        
        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)     
        lblimg.place(x=225,y=0,width=1310,height=590)


        #================down left side images==============
        img4=Image.open(r"C:\Users\ashis\OneDrive\Documents\Desktop\ROOM_FINDING_GUI_APP\IMAGES\1.jpg")      
        img4=img4.resize((225,190),Image.LANCZOS)      
        self.photoimg4=ImageTk.PhotoImage(img4)

        
        lblimg2=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)     
        lblimg2.place(x=0,y=230,width=225,height=190)


        img5=Image.open(r"C:\Users\ashis\OneDrive\Documents\Desktop\ROOM_FINDING_GUI_APP\IMAGES\img3.jpg")      
        img5=img5.resize((225,190),Image.LANCZOS)      
        self.photoimg5=ImageTk.PhotoImage(img5)

        
        lblimg3=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)     
        lblimg3.place(x=0,y=420,width=225,height=190)

        

    def update_datetime(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M:%S %p")  # 12-hour format
        current_date = now.strftime("%d-%m-%Y")
        self.lbl_datetime.config(text=f"{current_date}  {current_time}")
        self.root.after(1000, self.update_datetime) # Update every 1000 milliseconds (1 second)

       



    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_window(self.new_window)

    def room_details(self):
        self.new_window=Toplevel(self.root)
        self.app=room_window(self.new_window)
        
    def booking_details(self):
        self.new_window=Toplevel(self.root)
        self.app=booking_window(self.new_window)

    def about_details(self):
        self.new_window=Toplevel(self.root)
        self.app=about_window(self.new_window)

    def logout(self):
        logout=tkinter.messagebox.askyesno("ROOM GUI APP","Do you want to Exit",parent=self.root)
        if logout>0:
            self.root.destroy()
            return
        
        
    def display_user_info(self):
        fname = self.logged_in_user.get("fname", "Guest")  # Get first name
        email = self.logged_in_user.get("email", "N/A")    # Get email
        self.lbl_user_fname.config(text=f"Welcome: {fname}")
        self.lbl_user_email.config(text=f"Email: {email}")




if __name__== "__main__":
    root=Tk()
    fake_user = {"fname": "Test", "email": "test@example.com"}
    obj = roomguiapp(root, logged_in_user_data=fake_user)
    root.mainloop()