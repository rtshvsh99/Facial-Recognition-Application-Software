from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import tkinter




class Student2_Data_2:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Management System")
        


        #-------------variable--------------------------
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_designation = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_married = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_idproofcomb = StringVar()
        self.var_idproof = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()

        #****************variable for search***********
        self.var_com_search = StringVar()
        self.var_search = StringVar()
        




        lbl_title = Label(self.root,text = "STUDENT RECORDS ", font = ("times new roman",30,"bold"),bg = "white",fg = "dark green")
        lbl_title.place(x=0,y=0,width=1366,height=50)

        img_logo = Image.open(r"image\stu_record0.png")
        img_logo = img_logo.resize((45,45),Image.Resampling.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root,image =self.photo_logo )
        self.logo.place(x =270 ,y=5,width =45,height= 45)


        img_frame = Frame(self.root,bd = 2,relief=RIDGE,bg="white")
        img_frame.place(x=0,y=50,width= 1366,height=150)


        #1st image
        img1 = Image.open(r"image\stu_record1.jpg")
        img1 = img1.resize((455,145),Image.Resampling.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame,image =self.photo1 )
        self.img_1.place(x =0 ,y=0,width =455,height= 145)

        #2nd image
        img2 = Image.open(r"image\stu_record2.png")
        img2 = img2.resize((455,145),Image.Resampling.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame,image =self.photo2 )
        self.img_2.place(x =456 ,y=0,width =455,height= 145)

        #3rd image
        img3 = Image.open(r"image\stu_record3.jpg")
        img3 = img3.resize((455,145),Image.Resampling.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame,image =self.photo3 )
        self.img_3.place(x =911 ,y=0,width =455,height= 145)



        #back Buttons

        back_button = Button(self.root,command = self.back,text="Back",font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red" )
        back_button.place(x =1150 ,y=136,width = 120,height=35)




        #------------------------main Frame
        Main_frame = Frame(self.root,bd = 2,relief=RIDGE,bg="white")
        Main_frame.place(x=10,y=205,width= 1340,height=480)

#--------------------upper frame

        upper_frame = LabelFrame(Main_frame,bd = 2,relief=RIDGE,text="Student Information", font = ("times new roman",11,"bold"),bg = "white",fg = "red")
        upper_frame.place(x=10,y=10,width= 1320,height=230)


        #  labels== and Entry fields=========

        lbl_dep= Label(upper_frame,text='Department',font = ("arial",11,"bold"),bg = "white")
        lbl_dep.grid(row=0,column=0,padx= 2,sticky=W)
        
        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font = ("arial",11,"bold"),width=17,state="readonly")
        combo_dep['value'] = ('Select Department',"ECE","EI","Mechanical","CS")
        combo_dep.current(0)
        combo_dep.grid(row =0,column=1,padx= 2,pady=10,sticky=W)

        #--------name-------------
        lbl_Name= Label(upper_frame,text='Name',font = ("arial",11,"bold"),bg = "white")
        lbl_Name.grid(row=0,column=2,padx= 2,pady=7,sticky=W)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font = ("arial",11,"bold"))
        txt_name.grid(row =0,column=3,padx= 2,pady=7)

        #--------designamtion
        lbl_Designation= Label(upper_frame,text='Designation',font = ("arial",11,"bold"),bg = "white")
        lbl_Designation.grid(row=1,column=0,padx= 2,pady=7,sticky=W)

        txt_Designation=ttk.Entry(upper_frame,textvariable=self.var_designation,width=22,font = ("arial",11,"bold"))
        txt_Designation.grid(row =1,column=1,padx= 2,pady=7,sticky=W)

        #email
        lbl_email= Label(upper_frame,text='Email:',font = ("arial",11,"bold"),bg = "white")
        lbl_email.grid(row=1,column=2,padx= 2,pady=7,sticky=W)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font = ("arial",11,"bold"))
        txt_email.grid(row =1,column=3,padx= 2,pady=7,sticky=W)

        #--------Address
        lbl_address= Label(upper_frame,text='Address:',font = ("arial",11,"bold"),bg = "white")
        lbl_address.grid(row=2,column=0,padx= 2,pady=7,sticky=W)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font = ("arial",11,"bold"))
        txt_address.grid(row =2,column=1,padx= 2,pady=7,sticky=W)

        #married
        lbl_married= Label(upper_frame,text='Marital Status:',font = ("arial",11,"bold"),bg = "white")
        lbl_married.grid(row=2,column=2,padx= 2,sticky=W)
        
        combo_married=ttk.Combobox(upper_frame,textvariable=self.var_married,font = ("arial",11,"bold"),state="readonly")
        combo_married['value'] = (' Unmarried'," Married")
        combo_married.current(0)
        combo_married.grid(row =2,column=3,padx= 2,pady=7,sticky=W)

        #--------dob
        lbl_dob= Label(upper_frame,text='DOB:',font = ("arial",11,"bold"),bg = "white")
        lbl_dob.grid(row=3,column=0,padx= 2,pady=7,sticky=W)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font = ("arial",11,"bold"))
        txt_dob.grid(row =3,column=1,padx= 2,pady=7,sticky=W)

        #--------Doj
        lbl_doj= Label(upper_frame,text='Batch:',font = ("arial",11,"bold"),bg = "white")
        lbl_doj.grid(row=3,column=2,padx= 2,pady=7,sticky=W)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font = ("arial",11,"bold"))
        txt_doj.grid(row =3,column=3,padx= 2,pady=7,sticky=W)


#id proof

        # com_txt_proof= Label(upper_frame,text='Select Id proof:',font = ("arial",11,"bold"),bg = "white")
        # com_txt_proof.grid(row=2,column=2,padx= 2,sticky=W)
        
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,font = ("arial",11,"bold"),width=17,state="readonly")
        com_txt_proof['value'] = ('Select ID Proof',"Pan Card","Adhar Card","Driving Liscence")
        com_txt_proof.current(0)
        com_txt_proof.grid(row =4,column=0,padx= 2,pady=10,sticky=W)

        txt_proof = ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=('arial',11,"bold"))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)

        #---------gender-----------
        #married
        lbl_gender= Label(upper_frame,text='Gender:',font = ("arial",11,"bold"),bg = "white")
        lbl_gender.grid(row=4,column=2,padx= 2,sticky=W)
        
        combo_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font = ("arial",11,"bold"),width=17,state="readonly")
        combo_gender['value'] = ('Male ',"Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row =4,column=3,padx= 2,pady=7,sticky=W)

         #--------Phone-------------
        lbl_phone= Label(upper_frame,text='Phone No.:',font = ("arial",11,"bold"),bg = "white")
        lbl_phone.grid(row=0,column=4,padx= 2,pady=7,sticky=W)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font = ("arial",11,"bold"))
        txt_phone.grid(row =0,column=5,padx= 2,pady=7)

        #--------Country-------------
        lbl_country= Label(upper_frame,text='Country:',font = ("arial",11,"bold"),bg = "white")
        lbl_country.grid(row=1,column=4,padx= 2,pady=7,sticky=W)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font = ("arial",11,"bold"))
        txt_country.grid(row =1,column=5,padx= 2,pady=7)

        # Mask image

        img_mask = Image.open(r"image\stu_record4.png")
        img_mask = img_mask.resize((200,200),Image.Resampling.LANCZOS)
        self.photomask = ImageTk.PhotoImage(img_mask)

        self.img_mask = Label(upper_frame,image =self.photomask )
        self.img_mask.place(x =950 ,y=0,width =200,height= 200)


        #------------frame for button
        
        button_frame = Frame(upper_frame,bd = 2,relief=RIDGE,bg="white")
        button_frame.place(x=1160,y=10,width= 150,height=180)

        btn_add = Button(button_frame,command=self.add_data,text="Save",font = ("arial",10,"bold"),width=17,bg='blue',fg="white")
        btn_add.grid(row = 0,column=0,padx=1,pady=3)

        btn_update = Button(button_frame,command=self.update_data,text="Update",font = ("arial",10,"bold"),width=17,bg='blue',fg="white")
        btn_update.grid(row = 1,column=0,padx=1,pady=3)

        btn_delete = Button(button_frame,command=self.delete_data,text="Delete",font = ("arial",10,"bold"),width=17,bg='blue',fg="white")
        btn_delete.grid(row = 3,column=0,padx=1,pady=3)

        btn_clear = Button(button_frame,command= self.reset_data,text="Clear",font = ("arial",10,"bold"),width=17,bg='blue',fg="white")
        btn_clear.grid(row = 4,column=0,padx=1,pady=3)







        #-------------------down frame-------------
        down_frame = LabelFrame(Main_frame,bd = 2,relief=RIDGE,text="Student Information Table", font = ("times new roman",11,"bold"),bg = "white",fg = "red")
        down_frame.place(x=10,y=240,width= 1320,height=230)

        #search franme
        search_frame = LabelFrame(down_frame,bd = 2,relief=RIDGE,text="Search Student Information", font = ("times new roman",11,"bold"),bg = "white",fg = "red")
        search_frame.place(x=0,y=0,width= 1310,height=60)

        search_by= Label(search_frame,font=("arial",11,"bold"),text="Search By:",fg="white",bg="red")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #search
        
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=("arial",11,"bold"),width=18)
        com_txt_search['value']=("select Option","Phone","Id_Proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)


        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search = Button(search_frame,command=self.search_data,text="Search",font = ("arial",10,"bold"),width=17,bg='blue',fg="white")
        btn_search.grid(row = 0,column=3,padx=5)

        btn_ShowAll = Button(search_frame,command=self.fetch_data,text="Show All",font = ("arial",10,"bold"),width=17,bg='blue',fg="white")
        btn_ShowAll.grid(row = 0,column=4,padx=5)

        # stayhome= Label(search_frame,font=("times new roman",25,"bold"),text="Wear a Mask",fg="red",bg="white")
        # stayhome.place(x=780,y=0,width=600,height=30)

#----------------------Employee Table---------------

        #------table Frame
        table_frame= Frame(down_frame,bd= 3,relief= RIDGE)
        table_frame.place(x=0,y=60,width=1310,height=150)
        #---------scroll bar--
         #Scroll Bar
        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame,orient=VERTICAL)

        #all entry fields name
        #----isme hm kuchh bhi likh sakte hai header ko hm niche likhenge
        self.student_table = ttk.Treeview(table_frame,column=("dep","name","degi","email","address","married","dob","doj","idproofcomb","idproof","gender","phone","country"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #----------To show header
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("degi",text="Designation")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("married",text="Marrital Status")
        self.student_table.heading("dob",text="Date Of Birth")
        self.student_table.heading("doj",text="Date Of Joining")
        self.student_table.heading("idproofcomb",text="ID Type")
        
        self.student_table.heading("idproof",text="ID Proof")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("country",text="Country")

        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)


        #table ke sath bind krne ke liye
        self.student_table.bind("<ButtonRelease>",self.get_cursor)


        self.fetch_data()

        # -- widthh set krne ke liye
        self.student_table.column("dep",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("degi",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("married",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("doj",width=100)
        self.student_table.column("idproofcomb",width=100)
        
        self.student_table.column("idproof",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("country",width=100)
      

#**************function for data save***********************************
    def add_data(self):
                if self.var_dep.get()=="" or self.var_email.get()=="":
                        messagebox.showerror("Error","All Fields are Required")
                else:
                        try:
                                conn = mysql.connector.connect(host = "localhost",username = "root",password= "Ritesh170908@@",database="project")
                                my_cursor = conn.cursor()
                                my_cursor.execute("insert into employee1 values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                    self.var_dep.get(),
                                                                    self.var_name.get(),
                                                                    self.var_designation.get(),
                                                                    self.var_email.get(),
                                                                    self.var_address.get(),
                                                                    self.var_married.get(),
                                                                    self.var_dob.get(),
                                                                    self.var_doj.get(),
                                                                    self.var_idproofcomb.get(),
                                                                    self.var_idproof.get(),
                                                                    
                                                                   
                                                                    self.var_gender.get(),
                                                                    self.var_phone.get(),
                                                                    self.var_country.get()
                                                                 

                                                                ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Success","Student details has been added:",parent= self.root)
                        except Exception as es:
                                messagebox.showerror("Error",f"Due To :{str(es)}",parent= self.root) 

    #=================fetch data from database into table============================
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost",username = "root",password= "Ritesh170908@@",database="project")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM employee1")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #********************get Curuor to show data in enyyry field
    def get_cursor(self,event=""):
        cursor_row = self.student_table.focus()
        content  = self.student_table.item(cursor_row)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_name.set(data[1]),
        self.var_designation.set(data[2]),
        self.var_email.set(data[3]),
        self.var_address.set(data[4]),
        self.var_married.set(data[5]),
        self.var_dob.set(data[6]),
        self.var_doj.set(data[7]),
        self.var_idproofcomb.set(data[8]),
        self.var_idproof.set(data[9]),
        self.var_gender.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_country.set(data[12])


        #******************Update Function********************
    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            #to show message box
            messagebox.showerror("Error","All Fields are Required",parent = self.root)

        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update this student details ?",parent = self.root)
                if Update>0:
                    conn = mysql.connector.connect(host = "localhost",username = "root",password= "Ritesh170908@@",database="project")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update employee1 set Department= %s,Name= %s,Designation= %s,Email= %s,Address = %s, Married_status= %s,DOB= %s,DOJ= %s,id_proof_type= %s,Gender= %s,Phone= %s,Country= %s where id_proof = %s",(
                                                self.var_dep.get(),
                                                 self.var_name.get(),
                                                self.var_designation.get(),
                                                self.var_email.get(),
                                                self.var_address.get(),
                                                self.var_married.get(),
                                                self.var_dob.get(),
                                                self.var_doj.get(),
                                                self.var_idproofcomb.get(),
                                                
                                                
                                                
                                                self.var_gender.get(),
                                                self.var_phone.get(),
                                                self.var_country.get(),
                                                self.var_idproof.get()
                                                                                                        
                                                                                                                
        
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

#********************delete Function***************************
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror("Error","All Fields are required",parent = self.root)
        
        else:
            try:
                delete = messagebox.askyesno("Student Delete page","Do you want to delete this Student Details",parent = self.root)
                if delete>0:
                    conn = mysql.connector.connect(host = "localhost",username = "root",password= "Ritesh170908@@",database="project")
                    my_cursor = conn.cursor()
                    sql ="delete from employee1 where id_proof = %s"
                    val = (self.var_idproof.get(),)
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

#***********************resert data*************
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_name.set(""),
        self.var_designation.set(""),
        self.var_email.set(""),
        self.var_address.set(""),
        self.var_married.set("Married"),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_idproofcomb.set("Select ID Proof"),
        self.var_idproof.set(""),
        self.var_gender.set(""),
        self.var_phone.set(""),
        self.var_country.set("")

        #********************function for serach**********************
        #pahle hmko variable bnaye hai upr and then define kiye hai 
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please Select Option")
        else:
            try:
                conn = mysql.connector.connect(host = "localhost",username = "root",password= "Ritesh170908@@",database="project")
                my_cursor = conn.cursor()
                my_cursor.execute('select * from employee1 where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows = my_cursor.fetchall()
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)



     

     # def functions
    def back(self):
        self.back = tkinter.messagebox.askyesno("Face Recognition","Are you sure back this project",parent= self.root)
        if self.back>0:
            self.root.destroy()
        else:
            return




   

    


        




if __name__ == "__main__":
    root = Tk()
    obj = Student2_Data_2(root)
    root.mainloop()