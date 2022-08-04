from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


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
        img3 = Image.open(r"image\bg.jpg")
        img3 = img3.resize((1366,768),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image =self.photoimg3 )
        bg_img.place(x =0 ,y=0,relwidth = 1,relheight= 1)

    #=============left image========
        img4 = Image.open(r"image\self.jpg")
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
        img = Image.open(r"image\right.jpg")
        img = img.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)

        b1 = Button(frame,image =self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold") )
        b1.place(x =10 ,y=450,width = 300)


        img1 = Image.open(r"image\right.jpg")
        img1 = img1.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        b1 = Button(frame,image =self.photoimage1,borderwidth=0,cursor="hand2")
        b1.place(x =330 ,y=450,width = 300)

        #========================Function Declaration===============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
            messagebox.showerror("Error","All fields are required")
        elif  self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")     
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


                










if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()