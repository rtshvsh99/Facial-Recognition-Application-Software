from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


#from main
import tkinter

import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime


def main():
    win =Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root3):
        self.root3 = root3
        self.root3.geometry("1366x768+0+0")
        self.root3.title("Face Recognition System")
        
       


    


        #------------for photo--------------------
       # self.bg =ImageTk.PhotoImage(file=r"")
        img4 = Image.open(r"image\home_background.jpg")
        img4 = img4.resize((1366,768),Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(img4)

        lbl_bg = Label(self.root3,image =self.bg )
        lbl_bg.place(x =0 ,y=0,relwidth = 1,relheight= 1)

        #=============frame===============
        
        frame = Frame(self.root3,bd = 2,bg="royalblue")
        frame.place(x=510,y=110,width= 350,height=450)



        #=------------image 
        img1 = Image.open(r"image\head12.png")
        img1 = img1.resize((150,120),Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(image = self.photoimage1,bg="royal blue",borderwidth=0 )
        lblimg1.place(x =600 ,y=120,width =180 ,height= 130)

        #----------label------------------
        get_str=Label(lbl_bg,text="Welcome", font = ("arial",20,"bold"),bg = "royal blue",fg = "white")
        get_str.place(x=630,y=50)


        #label for username-----------
        username=Label(frame,text="Email:",font=("times new roman",12,"bold"),bg = "royal blue",fg = "white")
        username.place(x=100,y=155)
        #Entry Field
        self.textuser=ttk.Entry(frame,width=15,font=("times new roman",12,"bold"))
        self.textuser.place(x=80,y=180,width=200)


        #label for Password-----------
        password=Label(frame,text="Password:",font=("times new roman",12,"bold"),bg = "royal blue",fg = "white")
        password.place(x=100,y=232)
        #Entry Field
        self.textpass=ttk.Entry(frame,width=15,font=("times new roman",12,"bold"))
        self.textpass.place(x=80,y=260,width=200)


        #-----------------icon images----------
        img2 = Image.open(r"image\user.png")
        img2 = img2.resize((20,20),Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(image = self.photoimage2,bg="royalblue",borderwidth=0 )
        lblimg2.place(x =590 ,y=267,width =25 ,height= 25)

 #-----------------icon images----------

        img3 = Image.open(r"image\pass.png")
        img3 = img3.resize((20,20),Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(image = self.photoimage3,bg="royal blue",borderwidth=0 )
        lblimg3.place(x =590 ,y=344,width =25 ,height= 25)

        #---------- Login_button-------------
       
        loginbtn = Button(frame,text="Login",command=self.login,font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="red" )
        loginbtn.place(x =120 ,y=300,width = 120,height=35)

#---------- register_button-------------
        registerbtn = Button(frame,text="New User",command= self.register_window,font=("times new roman",13,"bold"),borderwidth=0,fg="black",bg="royal blue",activeforeground="white",activebackground="black" )
        registerbtn.place(x =5 ,y=350,width = 160)

       # --- forget_button-------------
        forgetbtn = Button(frame,text="Forgot Password",command= self.forgot_password_window,font=("times new roman",13,"bold"),borderwidth=0,fg="black",bg="royal blue",activeforeground="white",activebackground="black" )
        forgetbtn.place(x =180 ,y=350,width = 140)



        


    #---------------=============function for calling new_Register
    def register_window(self):
        self.new_window = Toplevel(self.root3)
        self.app = Register(self.new_window)



        #-----------------login Button Working Start-----------
    def login(self):
        if self.textuser.get()==""  or self.textpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.textuser.get()=="kapu" and self.textpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to Face_Recognition_System")
        else:
           # messagebox.showerror("Error","Invalid username and password")
            conn = mysql.connector.connect(host = "localhost",username = "root",password= "Ritesh170908@@",database="project")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email =%s and password = %s ",(

                                                                                self.textuser.get(),
                                                                                self.textpass.get()

                                                                                     ))

            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main =messagebox.askyesno("Authentication","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root3)
                    self.app=Face_Recogniition_System(self.new_window)
                else:
                    if not open_main:
                        return


            conn.commit()
            conn.close()




#========================for reset passwod=====================
    def reset_password(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the Security question",parent=self.root2)
        elif self.txt_security_A.get()=="":
            messagebox.showerror("Error","Please Enter the Answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please Enter the new Password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host = "localhost",username = "root",password= "Ritesh170908@@",database="project")
            my_cursor = conn.cursor()
            qury = ("select * from register where email = %s and securityQ = %s and securityA = %s")
            value = (self.textuser.get(),self.combo_security_Q.get(),self.txt_security_A.get(),)
            my_cursor.execute(qury,value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Plese Enter the correct Answer",parent=self.root2)
            else:
                query = ("update register set password = %s where email = %s")
                vlue= (self.txt_new_password.get(),self.textuser.get())
                my_cursor.execute(query,vlue)


                conn.commit()
                conn.close()
                messagebox.showinfo("Infor","Your password has been reset ,please login new password",parent=self.root2)
                self.root2.destroy()


    #=====================forgot  password window==============
    def forgot_password_window(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","Please Enter The Email address to reset Password")
        else:
            conn = mysql.connector.connect(host = "localhost",username = "root",password= "Ritesh170908@@",database="project")
            my_cursor = conn.cursor()
            query = ("select * from register where email = %s")
            value = (self.textuser.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("My Error","Please Enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot password")
                self.root2.geometry("340x450+610+170")


                l= Label(self.root2,text = "Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions:",font=("times new roman",16,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",13,"bold"),state="readonly")
                self.combo_security_Q['values']=("Select","Your Birth Place","Your Nickname","Your pet name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A =Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg = "white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security_A=ttk.Entry(self.root2,width=20,font=("times new roman",16))
                self.txt_security_A.place(x=50,y=180,width=250)
#=======for New Password
                new_password =Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg = "white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_new_password=ttk.Entry(self.root2,width=20,font=("times new roman",16))
                self.txt_new_password.place(x=50,y=250,width=250)

                btn = Button(self.root2,text ="Reset",command= self.reset_password,font=("times new roman",15,"bold"),bg = "white",fg="green")
                btn.place(x=100,y=290)


    






            




class Register:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")




        #--------------variables for textfileld--------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check =IntVar()

#==============Backgrond image================
        img3 = Image.open(r"image\finalbackground.jpg")
        img3 = img3.resize((1366,768),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image =self.photoimg3 )
        bg_img.place(x =0 ,y=0,relwidth = 1,relheight= 1)

    #=============left image========
        img4 = Image.open(r"image\register2.jpg")
        img4 = img4.resize((500,550),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(bg_img,image =self.photoimg4 )
        bg_img.place(x =50 ,y=60,width = 500,height= 550)


        #=============frame===============
        #frame for details
        frame = Frame(self.root,bd = 2,bg="white")
        frame.place(x=550,y=60,width= 700,height=550)


        #================label ===============
        register_lbl = Label(frame,text = "REGISTER HERE ", font = ("times new roman",15,"bold"),bg = "white",fg = "dark green")
        register_lbl.place(x=20,y=20)

        #============labels and entry field===============

        #----------------------row 1--------------------
        fname_label=Label(frame,text="First Name:",font=("times new roman",16,"bold"),bg="white")
        fname_label.place(x=50,y=100)
        #Entry Field
        fname_entry=ttk.Entry(frame,width=20,textvariable=self.var_fname,font=("times new roman",16,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname_label=Label(frame,text="Last Name:",font=("times new roman",16,"bold"),bg="white")
        lname_label.place(x=370,y=100)
        #Entry Field
        self.txt_lname=ttk.Entry(frame,width=20,textvariable=self.var_lname,font=("times new roman",16,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)



#==-------------------------------------row 2---------------------------------
        contact=Label(frame,text="Contact  No.:",font=("times new roman",16,"bold"),bg="white")
        contact.place(x=50,y=170)
        #Entry Field
        self.txt_contact=ttk.Entry(frame,width=20,textvariable=self.var_contact,font=("times new roman",16,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email:",font=("times new roman",16,"bold"),bg="white")
        email.place(x=370,y=170)
        #Entry Field
        self.txt_email=ttk.Entry(frame,width=20,textvariable=self.var_email,font=("times new roman",16,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        #-----------------------row 3--------------------------------------

        security_Q=Label(frame,text="Select Security Questions:",font=("times new roman",16,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",13,"bold"),state="readonly")
        self.combo_security_Q['values']=("Select","Your Birth Place","Your Nickname","Your pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A =Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg = "white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security_A=ttk.Entry(frame,width=20,textvariable=self.var_securityA,font=("times new roman",16))
        self.txt_security_A.place(x=370,y=270,width=250)

      



#---------------------------row4--------------------------------

        pswd =Label(frame,text="Password",font=("times new roman",15,"bold"),bg = "white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,width=20,textvariable=self.var_pass,font=("times new roman",16,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd =Label(frame,text= "Confirm Password",font=("times new roman",15,"bold"),bg = "white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,width=20,textvariable=self.var_confpass,font=("times new roman",16,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)


        checkbtn = Checkbutton(frame,text="I Agree The Terms and Conditions",variable=self.var_check,font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #================Buttons======================
        img = Image.open(r"image\register.jpg")
        img = img.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)

        b1 = Button(frame,image =self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold") )
        b1.place(x =10 ,y=450,width = 300)


        img1 = Image.open(r"image\login.png")
        img1 = img1.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        b1 = Button(frame,image =self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x =330 ,y=450,width = 300)

        #========================Function Declaration===============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif  self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition",parent=self.root)     
        else:
            conn = mysql.connector.connect(host = "localhost",username = "root",password= "Ritesh170908@@",database="project")
            my_cursor = conn.cursor()
            query=("select * from register where email =%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            #-----to fetch data from database---------
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,Please try another email")
                #----------data enter krna hai database me-----------
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(

                                                                                   self.var_fname.get(),
                                                                                   self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                   self.var_email.get(),
                                                                                   self.var_securityQ.get(),
                                                                                   self.var_securityA.get(),
                                                                                   self.var_pass.get()

                                                                                       ))  
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
        self.root.destroy()


       
     

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
        img = Image.open(r"image\finalbackground.jpg")
        img = img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image =self.photoimg )
        f_lbl.place(x = 0,y=0,width = 500,height= 130)

#SECOND IMAGE
        img1 = Image.open(r"image\finalbackground.jpg")
        img1 = img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image =self.photoimg1 )
        f_lbl.place(x = 500,y=0,width = 500,height= 130)

#ThIRD IMAGE
        img2 = Image.open(r"image\finalbackground.jpg")
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


        title_lbl = Label(bg_img,text = "FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM ", font = ("times new roman",28,"bold"),bg = "#3385ff",fg = "white")
        title_lbl.place(x=0,y=0,width=1366,height=40)

        #===================time==============

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text= string)
            lbl.after(1000,time)

        lbl = Label(title_lbl,font = ('times new roman',14,'bold'),background = 'white',foreground='black')
        lbl.place(x=0,y=0 ,width=110,height=50)
        time()


#Student_Button
        img4 = Image.open(r"image\finalstudent details3.jpg")
        img4 = img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image = self.photoimg4,command=self.student_details,cursor= "hand2")
        b1.place(x=120,y=65,width=220,height=220)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor= "hand2", font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=120,y=265,width=220,height=40)


#train_Button


        img8 = Image.open(r"image\finaltrain.jpg")
        img8 = img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)


        b1 = Button(bg_img,image = self.photoimg8,cursor= "hand2",command= self.train_data)
        b1.place(x=420,y=65,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Train data",cursor= "hand2",command= self.train_data, font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=420,y=265,width=220,height=40)
        

    #  Face_ detect Button

        img5 = Image.open(r"image\facedetector.jpg")
        img5 = img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image = self.photoimg5,cursor= "hand2",command= self.face_data)
        b1.place(x=720,y=65,width=220,height=220)
        


        b1_1 = Button(bg_img,text="Face Detector",cursor= "hand2",command= self.face_data, font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=720,y=265,width=220,height=40)
        
       

       

       

#  Attendance_Button
        img6 = Image.open(r"image\finalattendence.jpg")
        img6 = img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image = self.photoimg6,cursor= "hand2",command= self.attendance_data)
        b1.place(x=1020,y=65,width=220,height=220)
        
        

        b1_1 = Button(bg_img,text="Attendance",cursor= "hand2",command= self.attendance_data, font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=1020,y=265,width=220,height=40)
        
        



#  Student Record button_Button
        img7 = Image.open(r"image\stu_record_button.png")
        img7 = img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image = self.photoimg7,cursor= "hand2",command = self.Employee_data)
        b1.place(x=420,y=315,width=220,height=220)
        
        

        b1_1 = Button(bg_img,text="Student Record",cursor= "hand2",command = self.Employee_data, font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=420,y=500,width=220,height=40)
        
        




        
        

 #Photos_Button
        img9 = Image.open(r"image\finalphotos.png")
        img9 = img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image = self.photoimg9,cursor= "hand2",command = self.open_img)
        b1.place(x=120,y=315,width=220,height=220)
        

        b1_1 = Button(bg_img,text="Photos",cursor= "hand2",command = self.open_img, font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=120,y=500,width=220,height=40)
        

# #Help Button
#         img10 = Image.open(r"image\finalhelpdesk2.jpg")
#         img10 = img10.resize((220,220),Image.Resampling.LANCZOS)
#         self.photoimg10 = ImageTk.PhotoImage(img10)

#         b1 = Button(bg_img,image = self.photoimg10,cursor= "hand2",command= self.help_data)
#         b1.place(x=720,y=315,width=220,height=220)

#         b1_1 = Button(bg_img,text="Help Desk",cursor= "hand2",command= self.help_data ,font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
#         b1_1.place(x=720,y=500,width=220,height=40)


#Chat Bot Button
        img10 = Image.open(r"image\finalhelpdesk2.jpg")
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
        self.iExit = tkinter.messagebox.askyesno("Face Recognition system","Are you sure?",parent= self.root)
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
    main()