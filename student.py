from logging import root
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
      

        #==================variables to add data====================
        self.var_dep= StringVar()
        self.var_course= StringVar()
        self.var_year= StringVar()
        self.var_semester= StringVar()
        self.var_std_id= StringVar()
        self.var_std_name= StringVar()
        # self.var_div= StringVar()
        self.var_roll= StringVar()
        self.var_gender= StringVar()
        self.var_dob= StringVar()
        self.var_email= StringVar()
        self.var_phone= StringVar()
        self.var_address= StringVar()
        self.var_teacher= StringVar()

 #FIRST IMAGE
        img = Image.open(r"image\finalbackground.jpg")
        img = img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image =self.photoimg )
        f_lbl.place(x =0,y=0,width = 500,height= 130)

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


        title_lbl = Label(bg_img,text = "STUDENT MANAGEMENT SYSTEM ", font = ("times new roman",30,"bold"),bg = "white",fg = "dark green")
        title_lbl.place(x=0,y=0,width=1366,height=40)


        


#frame for details
        main_frame = Frame(bg_img,bd = 2,bg="white")
        main_frame.place(x=10,y=43,width= 1340,height=520)

       
#left side lebel frame
        Left_frame= LabelFrame(main_frame,bd= 2,bg="white",relief= RIDGE,text="Student Details",font=("times new roman",12,"bold" ))
        Left_frame.place(x=10,y=10,width=670,height=500)

         # back butons
        back_button = Button(self.root,command= self.back,text="Back",font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red" )
        back_button.place(x =1150 ,y=136,width = 120,height=35)


        #image for left side
        img_left = Image.open(r"image\stu_details_main.png")
        img_left = img_left.resize((660,110),Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image =self.photoimg_left )
        f_lbl.place(x =5 ,y=0,width = 660,height= 110)

    #Current course Inforamtion
        current_course_frame= LabelFrame(Left_frame,bd= 2,bg="white",relief= RIDGE,text="Current Course Information",font=("times new roman",12,"bold" ))
        current_course_frame.place(x=5,y=115,width=660,height=115)

    #Department label

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        #combo box
        dep_combo=ttk.Combobox(current_course_frame,textvariable = self.var_dep,font=("times new roman",13,"bold"),state= "readonly",width=20)
        dep_combo['values']=("Select Department","Btech Department","Bsc Agriculture","Hindi Department","Forensic Department","Pharmacy Department")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


    #Course label

        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        #combo box
        course_combo=ttk.Combobox(current_course_frame,textvariable =self.var_course,font=("times new roman",13,"bold"),state= "readonly",width=20)
        course_combo['values']=("Select Course","Electronics and Communication","Mechanical","Computer Science","Electronics and Instrumentation","Biotechnology","Bio Medical","Food Technology")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

    #Year label

        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        #combo box
        year_combo=ttk.Combobox(current_course_frame,textvariable =self.var_year,font=("times new roman",13,"bold"),state= "readonly",width=20)
        year_combo['values']=("Select Year","First Year","Second Year","Third Year","Final Year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


    #Semester label

        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        #combo box
        semester_combo=ttk.Combobox(current_course_frame,textvariable =self.var_semester,font=("times new roman",13,"bold"),state= "readonly",width=20)
        semester_combo['values']=("Select Semester","semester-1","semeseter-2","semeseter-3","semeseter-4","semeseter-5","semeseter-6","semeseter-7","semeseter-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)



    #Class Student Inforamtion
        class_student_frame= LabelFrame(Left_frame,bd= 2,bg="white",relief= RIDGE,text="Class Student Information",font=("times new roman",12,"bold" ))
        class_student_frame.place(x=5,y=230,width=660,height=245)

     # StudenetID label
        studentId_label=Label(class_student_frame,text="Enrollment Id:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        #Entry Field
        studentId_entry=ttk.Entry(class_student_frame,textvariable =self.var_std_id,width=15,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


     # StudenetName label
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        #Entry Field
        studentName_entry=ttk.Entry(class_student_frame,textvariable =self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

    # Class Division label
        #class_div_label=Label(class_student_frame,text="Batch:",font=("times new roman",13,"bold"),bg="white")
        #class_div_label.grid(row=1,column=0,padx=10,pady=3,sticky=W)
        #Entry Field
        # class_div_entry=ttk.Entry(class_student_frame,textvariable =self.var_div, width=15,font=("times new roman",13,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # div_combo=ttk.Combobox(class_student_frame,textvariable =self.var_div,font=("times new roman",13,"bold"),state= "readonly",width=13)
        # div_combo['values']=("A","B","C")
        # div_combo.current(0)
        # div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

   #Roll no. label
        roll_no_div_label=Label(class_student_frame,text="Roll No.:",font=("times new roman",13,"bold"),bg="white")
        roll_no_div_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        #Entry Field
        roll_no_div_entry=ttk.Entry(class_student_frame,textvariable =self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_div_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

    # gender label
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=1,column=0,padx=10,pady=3,sticky=W)
        #Entry Field

        #gender_entry=ttk.Entry(class_student_frame,textvariable =self.var_gender,width=15,font=("times new roman",13,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable =self.var_gender,font=("times new roman",13,"bold"),state= "readonly",width=13)
        gender_combo['values']=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

    #DOB. label
        dob_label=Label(class_student_frame,text="Date Of Birth:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)
        #Entry Field
        dob_entry=ttk.Entry(class_student_frame,textvariable =self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

    # email label
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        #Entry Field
        email_entry=ttk.Entry(class_student_frame,textvariable =self.var_email,width=15,font=("times new roman",13,"bold"))
        email_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

    #phone label
        phone_label=Label(class_student_frame,text="Phone No.:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        #Entry Field
        phone_entry=ttk.Entry(class_student_frame,textvariable =self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

    # address label
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        #Entry Field
        address_entry=ttk.Entry(class_student_frame,textvariable =self.var_address,width=15,font=("times new roman",13,"bold"))
        address_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

    #teacher label
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        #Entry Field
        teacher_entry=ttk.Entry(class_student_frame,textvariable =self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

    

    #Radio Buttons
        self.var_radio1=StringVar()
       
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take a photo Sample",value="Yes")
        radiobtn1.grid(row=4,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo Sample",value="No")
        radiobtn2.grid(row=4,column=1)

#Buttons Frame
        btn_frame= Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=195,width=680,height=30)


#save Button
        save_btn=Button(btn_frame,text="Save",command= self.add_data,width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
    
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=11,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
    
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=11,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
    
        reset_btn=Button(btn_frame,text="Reset",command= self.reset_data,width=11,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=4)
    
        # update_photo_btn=Button(btn_frame,text="Update Photo Sample",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        # update_photo_btn.grid(row=0,column=5)
    
        




#Right side lebel frame
        Right_frame= LabelFrame(main_frame,bd= 2,bg="white",relief= RIDGE,text="Student Details",font=("times new roman",12,"bold" ))
        Right_frame.place(x=690,y=10,width=630,height=500)

#image for right frame
        img_right = Image.open(r"image\finalbackground.jpg")
        img_right = img_right.resize((619,110),Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame,image =self.photoimg_right )
        f_lbl.place(x =5 ,y=0,width = 620,height= 110)


#================Search System===============================

        search_frame= LabelFrame(Right_frame,bd= 2,bg="white",relief= RIDGE,text="Search System",font=("times new roman",12,"bold" ))
        search_frame.place(x=5,y=115,width=618,height=70)

        #label for search 
        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        #search Combo Box
        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state= "readonly",width=12)
        search_combo['values']=("Select","Roll_No.","Phone_No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #search EntryField
        search_entry=ttk.Entry(search_frame,width=17,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #buttons For Search
        search_btn=Button(search_frame,text="Search",width=8,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=8,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)


        #=========================Table frame========================================
        table_frame= Frame(Right_frame,bd= 2,bg="white",relief= RIDGE)
        table_frame.place(x=5,y=185,width=618,height=250)

        #Scroll Bar
        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame,orient=VERTICAL)
        #all entry fields name
        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

#   To show header
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        # self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

#set Column Width
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        # self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        #update ke liye dfata show krane ke liye
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        

#==========================function declaration ========================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==" " or self.var_std_id.get()=="":
            #to show message box
            messagebox.showerror("Error","All Fields are Required",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost",username = "root",password= "Ritesh170908@@",database="project")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                    self.var_dep.get(),
                                                                    self.var_course.get(),
                                                                    self.var_year.get(),
                                                                    self.var_semester.get(),
                                                                    self.var_std_id.get(),
                                                                    self.var_std_name.get(),
                                                                    # self.var_div.get(),
                                                                    self.var_roll.get(),
                                                                    self.var_gender.get(),
                                                                    self.var_dob.get(),
                                                                    self.var_email.get(),
                                                                    self.var_phone.get(),
                                                                    self.var_address.get(),
                                                                    self.var_teacher.get(),
                                                                    self.var_radio1.get()

                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent= self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent= self.root)    


    #=================fetch data from database into table============================
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost",username = "root",password= "Ritesh170908@@",database="project")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


      #  ========================getCursor for Update===========
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content  = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        # self.var_div.set(data[6]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_teacher.set(data[12]),
        self.var_radio1.set(data[13])

#===================Update Function=======================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            #to show message box
            messagebox.showerror("Error","All Fields are Required",parent = self.root)

        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update this student details",parent = self.root)
                if Update>0:
                    conn = mysql.connector.connect(host = "localhost",username = "root",password= "Ritesh170908@@",database="project")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student set Dep= %s,course= %s,Year= %s,Semester= %s,Name = %s,Roll= %s,Gender= %s,Dob= %s,Email= %s,Phone= %s,Address= %s,Teacher= %s,PhotoSample= %s where Student_id = %s",(


                                                                    self.var_dep.get(),
                                                                    self.var_course.get(),
                                                                    self.var_year.get(),
                                                                    self.var_semester.get(),
                                                                    
                                                                    self.var_std_name.get(),
                                                                    # self.var_div.get(),
                                                                    self.var_roll.get(),
                                                                    self.var_gender.get(),
                                                                    self.var_dob.get(),
                                                                    self.var_email.get(),
                                                                    self.var_phone.get(),
                                                                    self.var_address.get(),
                                                                    self.var_teacher.get(),
                                                                    self.var_radio1.get(),
                                                                    self.var_std_id.get()

                             
                                                                     ))
                else:
                    if  not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update Completed",parent= self.root)
                conn.commit()
                self.fetch_data()
                conn.close() 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)       


    # ===================================Delete Function====================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student must be required",parent = self.root)
        
        else:
            try:
                delete = messagebox.askyesno("Student Delete page","Do you want to delete this studenmt",parent = self.root)
                if delete>0:
                    conn = mysql.connector.connect(host = "localhost",username = "root",password= "Ritesh170908@@",database="project")
                    my_cursor = conn.cursor()
                    sql ="delete from student where Student_id = %s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Delete","Successfully Deleted student details",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)


#=========================Reset Function===============================
    def reset_data(self):
        self.var_dep.set("select Department")
        self.var_course.set("Select Course ")
        self.var_year.set("Select Year ")
        self.var_semester.set(" Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        # self.var_div.set("Select Division ")
        self.var_roll.set("")
        self.var_gender.set("Male ")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")



#=========================Generate dataset or take photo sample================================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            #to show message box
            messagebox.showerror("Error","All Fields are Required",parent = self.root)

        else:
            try:
                conn = mysql.connector.connect(host = "localhost",username = "root",password= "Ritesh170908@@",database="project")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id = id+1
                my_cursor.execute("Update student set Dep= %s,course= %s,Year= %s,Semester= %s,Name = %s,Roll= %s,Gender= %s,Dob= %s,Email= %s,Phone= %s,Address= %s,Teacher= %s,PhotoSample= %s where Student_id = %s",(


                                                                    self.var_dep.get(),
                                                                    self.var_course.get(),
                                                                    self.var_year.get(),
                                                                    self.var_semester.get(),
                                                                    
                                                                    self.var_std_name.get(),
                                                                    # self.var_div.get(),
                                                                    self.var_roll.get(),
                                                                    self.var_gender.get(),
                                                                    self.var_dob.get(),
                                                                    self.var_email.get(),
                                                                    self.var_phone.get(),
                                                                    self.var_address.get(),
                                                                    self.var_teacher.get(),
                                                                    self.var_radio1.get(),
                                                                    self.var_std_id.get()==id+1

                             
                                                                     ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


#=======================Load Predefined data on face frontal opencv=================
                face_classifier = cv2.CascadeClassifier('C:\\python 9\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')


                def face_croped(img):
                    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces= face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling  factor = 1.3
                    # minimum neighbour = 5

                    for (x,y,w,h) in faces:
                        face_croped= img[y:y+h,x:x+w]
                        return face_croped


                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame= cap.read()
                    if face_croped(my_frame) is not None:
                        img_id +=1

                        face = cv2.resize(face_croped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset Complted successfully",parent = self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)


# back button
    def back(self):
       # self.back = tkinter.messagebox.askyesno("Face Recognition","Are you sure back this project",parent= self.root)
        #if self.back>0:
        self.root.destroy()
        #else:
        #    return
    












if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()