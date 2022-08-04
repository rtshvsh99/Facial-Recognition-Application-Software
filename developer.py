from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        


        #TITLE
        title_lbl = Label(self.root,text = "DEVELOPER ", font = ("times new roman",30,"bold"),bg = "white",fg = "blue")
        title_lbl.place(x=0,y=0,width=1366,height=40)
#IMAGE
        img_top = Image.open(r"image\help.jpg")
        img_top = img_top.resize((1366,620),Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image =self.photoimg_top )
        f_lbl.place(x =0,y=55,width = 1366,height= 620)

    #======================frame for details=============
        main_frame = Frame(f_lbl,bd = 2,bg="white")
        main_frame.place(x=900,y=43,width= 400,height=520)

    #=====================pics
        img_top_self = Image.open(r"image\123.jpg")
        img_top_self = img_top_self.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg_top_self = ImageTk.PhotoImage(img_top_self)

        f_lbl = Label(main_frame,image =self.photoimg_top_self )
        f_lbl.place(x =200,y=0,width = 150,height= 150)

        #============Developer ifo label   

        dev_label=Label(main_frame,text="Hello Developer ",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=5)
        
        dev_label=Label(main_frame,text="We are full_stack_Developer ",font=("times new roman",12,"bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=40)

        #=====================seconds pics===========
        img_top_self2 = Image.open(r"image\at2.png") 
        img_top_self2 = img_top_self2.resize((400,600),Image.Resampling.LANCZOS)
        self.photoimg_top_self2 = ImageTk.PhotoImage(img_top_self2)

        f_lbl = Label(main_frame,image =self.photoimg_top_self2 )
        f_lbl.place(x =0,y=160,width = 400,height= 600)







if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()