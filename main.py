from logging import root
from tkinter import *
import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime
from employee import Student2_Data_2
from chatbot import ChatBot



class Face_Recogniition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
       
       

       #FIRST IMAGE
        img = Image.open(r"image\1.jpg")
        img = img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image =self.photoimg )
        f_lbl.place(x = 0,y=0,width = 500,height= 130)

#SECOND IMAGE
        img1 = Image.open(r"image\studentbutton.jpg")
        img1 = img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image =self.photoimg1 )
        f_lbl.place(x = 500,y=0,width = 500,height= 130)

#ThIRD IMAGE
        img2 = Image.open(r"image\3.jpg")
        img2 = img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image =self.photoimg2 )
        f_lbl.place(x =1000 ,y=0,width = 500,height= 130)



#Background Image
        img3 = Image.open(r"image\finalbackground.jpg")
        img3 = img3.resize((1366,768),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image =self.photoimg3 )
        bg_img.place(x =0 ,y=130,width = 1366,height= 768)


        title_lbl = Label(bg_img,text = "FACE RECOGNITION ATTENDANCE SOFTWARE SYSTEM ", font = ("times new roman",30,"bold"),bg = "white",fg = "red")
        title_lbl.place(x=0,y=0,width=1366,height=40)

        #===================time==============

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text= string)
            lbl.after(1000,time)

        lbl = Label(title_lbl,font = ('times new roman',14,'bold'),background = 'white',foreground='blue')
        lbl.place(x=0,y=0 ,width=110,height=50)
        time()


#Student_Button
        img4 = Image.open(r"image\st_details.jpg")
        img4 = img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image = self.photoimg4,command=self.student_details,cursor= "hand2")
        b1.place(x=120,y=65,width=220,height=220)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor= "hand2", font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=120,y=265,width=220,height=40)


#Detect_Face_Button
        img5 = Image.open(r"image\face_recog_1.jpg")
        img5 = img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image = self.photoimg5,cursor= "hand2",command= self.face_data)
        b1.place(x=420,y=65,width=220,height=220)

        b1_1 = Button(bg_img,text="Face Detector",cursor= "hand2",command= self.face_data, font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=420,y=265,width=220,height=40)


#  Attendance_Button
        img6 = Image.open(r"image\atbutton.jpg")
        img6 = img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image = self.photoimg6,cursor= "hand2",command= self.attendance_data)
        b1.place(x=720,y=65,width=220,height=220)

        b1_1 = Button(bg_img,text="Attendance",cursor= "hand2",command= self.attendance_data, font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=720,y=265,width=220,height=40)



#  Employee_Button
        img7 = Image.open(r"image\stu_record_button.png")
        img7 = img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image = self.photoimg7,cursor= "hand2",command = self.Employee_data)
        b1.place(x=1020,y=65,width=220,height=220)

        b1_1 = Button(bg_img,text="Student Record",cursor= "hand2",command = self.Employee_data, font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=1020,y=265,width=220,height=40)


#  Train_Button
        img8 = Image.open(r"image\train.jpg")
        img8 = img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image = self.photoimg8,cursor= "hand2",command= self.train_data)
        b1.place(x=120,y=315,width=220,height=220)

        b1_1 = Button(bg_img,text="Train data",cursor= "hand2",command= self.train_data, font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=120,y=500,width=220,height=40)

 #Photos_Button
        img9 = Image.open(r"image\photos1.jpg")
        img9 = img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image = self.photoimg9,cursor= "hand2",command = self.open_img)
        b1.place(x=420,y=315,width=220,height=220)

        b1_1 = Button(bg_img,text="Photos",cursor= "hand2",command = self.open_img, font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=420,y=500,width=220,height=40)

#Help Button
        # img10 = Image.open(r"image\developer.jpg")
        # img10 = img10.resize((220,220),Image.Resampling.LANCZOS)
        # self.photoimg10 = ImageTk.PhotoImage(img10)

        # b1 = Button(bg_img,image = self.photoimg10,cursor= "hand2",command= self.help_data)
        # b1.place(x=720,y=315,width=220,height=220)

        # b1_1 = Button(bg_img,text="Help Desk",cursor= "hand2",command= self.help_data ,font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        # b1_1.place(x=720,y=500,width=220,height=40)


# ChatBot Button 
        img10 = Image.open(r"image\developer.jpg")
        img10 = img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,image = self.photoimg10,cursor= "hand2",command= self.chatBot)
        b1.place(x=720,y=315,width=220,height=220)

        b1_1 = Button(bg_img,text="Help Desk",cursor= "hand2",command= self.chatBot ,font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=720,y=500,width=220,height=40)

#Exit_Button
        img11 = Image.open(r"image\exit_button_pics.jpg")
        img11 = img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,image = self.photoimg11,cursor= "hand2",command= self.iExit)
        b1.place(x=1020,y=315,width=220,height=220)

        b1_1 = Button(bg_img,text="Exit",cursor= "hand2",command= self.iExit, font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=1020,y=500,width=220,height=40)


    def open_img(self):
        os.startfile("data")


#============================exit Button=====================

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent= self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return



       # -------------------------------------Function Buttons---------------------------------
    def student_details(self):
        self.new_window =Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window =Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window =Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window =Toplevel(self.root)
        self.app=Attendance(self.new_window)


    # def developer_data(self):
    #     self.new_window =Toplevel(self.root)
    #     self.app=Developer(self.new_window)

    
    # def help_data(self):
    #     self.new_window =Toplevel(self.root)
    #     self.app=Help(self.new_window)

    def chatBot(self):
        self.new_window= Toplevel(self.root)
        self.app = ChatBot(self.new_window)


    def Employee_data(self):
        self.new_window =Toplevel(self.root)
        self.app=Student2_Data_2(self.new_window)

    




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recogniition_System(root)
    root.mainloop()


 