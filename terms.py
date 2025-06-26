from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

from tkinter import messagebox
import tkinter



class terms_and_conditions:
    def __init__(self,root):
        self.root=root
        self.root.title("Terms and Conditions")
        self.root.geometry("1000x600+400+100")


        
        details_table=Frame(self.root,bd=2,relief=RIDGE)
        details_table.place(x=0,y=0,width=850,height=595)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.txtbox=Text(details_table,width=91,height=29,padx=2,pady=6)
        self.txtbox.place(x=0,y=0,width=91,height=29)

        listbooks=["1. Digital marketing encompasses all marketing efforts that use an electronic device or the internet.",
                   "   Businesses leverage digital channels such as search engines, social media, email, and their websites ",
                   "   to connect with current and prospective customers.",
                   "2.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with ",
                   "    information. For this reason, buyers increasingly rely on their own ability to research solutions to their ",
                   "     problems.",
                    "3.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems. ",
                    "4.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "5.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "6.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "7.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "8.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "9.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "10.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "11.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "12.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "13.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "14.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "15.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "16.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "17.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "18.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "19.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "20.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "21.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "22.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "23.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "24.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                    "25.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "26.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "27.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "28.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "29.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "30.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "31.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "32.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "33.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "34.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "35.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "36.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "37.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "38.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "39.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "40.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "40.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "42.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
                   "43.  Digital tools put information at a buyers fingertips and give sellers the ability to flood potential clients with information. For this reason, buyers increasingly rely on their own ability to research solutions to their problems.",
]

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        

        listbox=Listbox(details_table,font=("arial",12,"bold"),width=91,height=28)
        listbox.place(x=0,y=0)
        

        
        scroll_x.config(command=listbox.xview)
        scroll_y.config(command=listbox.yview)

        for item in listbooks:
            listbox.insert(END,item)

        


if __name__== "__main__":
    root=Tk()
    obj=terms_and_conditions(root)
    root.mainloop()