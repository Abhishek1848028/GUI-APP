from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
import datetime

class about_window:
    def __init__(self,root):
        self.root=root
        self.root.title("ROOM FINDING GUI APP")     #for giving title the app
        self.root.geometry("1295x550+230+228")

        




if __name__== "__main__":
    root=Tk()
    obj=about_window(root)
    root.mainloop()