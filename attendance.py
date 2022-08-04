from logging import root
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog 

mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
      


#=================text variables to entry field data===============
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()














        #FIRST IMAGE
        img = Image.open(r"image\finalattendance details2.png")
        img = img.resize((700,200),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image =self.photoimg )
        f_lbl.place(x = 0,y=0,width = 700,height= 200)

#SECOND IMAGE
        img1 = Image.open(r"image\finalattendance details3.png")
        img1 = img1.resize((700,200),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image =self.photoimg1 )
        f_lbl.place(x = 700,y=0,width = 700,height= 200)


#Background Image
        img3 = Image.open(r"image\finalbackground.jpg")
        img3 = img3.resize((1366,768),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image =self.photoimg3 )
        bg_img.place(x =0 ,y=200,width = 1366,height= 768)

        title_lbl = Label(bg_img,text = "ATTENDANCE MANAGEMENT SYSTEM ", font = ("times new roman",30,"bold"),bg = "white",fg = "dark green")
        title_lbl.place(x=0,y=0,width=1366,height=40)


    #frame for details
        main_frame = Frame(bg_img,bd = 2,bg="white")
        main_frame.place(x=10,y=43,width= 1340,height=520)

    #left side lebel frame
        Left_frame= LabelFrame(main_frame,bd= 2,bg="white",relief= RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold" ))
        Left_frame.place(x=10,y=10,width=670,height=500)

    #image for left side
        img_left = Image.open(r"image\finalattendance details.jpeg")
        img_left = img_left.resize((660,110),Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image =self.photoimg_left )
        f_lbl.place(x =5 ,y=0,width = 660,height= 110)


#back Buttons

        back_button = Button(self.root,command = self.back,text="Back",font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red" )
        back_button.place(x =1150 ,y=205,width = 120,height=35)





    # for entry fleft_inside

        left_inside_frame = Frame(Left_frame,bd = 2,relief= RIDGE,bg="white")
        left_inside_frame.place(x=10,y=125,width= 650,height=600)



   # ================================Lebels and Entries================
   # Attenadnvcce  label
        attendanceId_label=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",13,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        #Entry Field
        attendanceId_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

    #Rolll
        
        rollLabel = Label(left_inside_frame,text="Roll",bg= "white",font= "comicsansna 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll = ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font="comicsansna 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)

#name
        nameLabel = Label(left_inside_frame,text="Name",bg= "white",font= "comicsansna 11 bold")
        nameLabel.grid(row=1,column=0)

        atten_name = ttk.Entry(left_inside_frame,width=22,textvariable= self.var_atten_name,font="comicsansna 11 bold")
        atten_name.grid(row=1,column=1,pady=8)

    #department

        depLabel = Label(left_inside_frame,text="Daprtment",bg= "white",font= "comicsansna 11 bold")
        depLabel.grid(row=1,column=2)

        atten_dep = ttk.Entry(left_inside_frame,width=22,textvariable= self.var_atten_dep,font="comicsansna 11 bold")
        atten_dep.grid(row=1,column=3,pady=8)

    #time

        timeLabel = Label(left_inside_frame,text="Daprtment",bg= "white",font= "comicsansna 11 bold")
        timeLabel.grid(row=2,column=0)

        atten_time = ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=22,font="comicsansna 11 bold")
        atten_time.grid(row=2,column=1,pady=8)

    #Date
        dateLabel = Label(left_inside_frame,text="Date",bg= "white",font= "comicsansna 11 bold")
        dateLabel.grid(row=2,column=2)

        atten_date = ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsansna 11 bold")
        atten_date.grid(row=2,column=3,pady=8)

    #attendance

        attendanceLabel = Label(left_inside_frame,text="Attendance Status",bg= "white",font= "comicsansna 11 bold")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status = ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansna 11 bold",state="readonly")
        self.atten_status["value"] = ["Status","Present","Absent"]
        self.atten_status.grid(row=3,column = 1,pady=8)
        self.atten_status.current(0)


    #Buttons Frame
        btn_frame= Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=195,width=680,height=300)


#save Button
        save_btn=Button(btn_frame,text="Import Csv",command=self.importCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
    
        update_btn=Button(btn_frame,text="Export Csv",command=self.exportCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
    
        delete_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
    
        reset_btn=Button(btn_frame,text="Reset",width=15,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)





        


    #Right side lebel frame
        Right_frame= LabelFrame(main_frame,bd= 2,bg="white",relief= RIDGE,text="Attendance Details",font=("times new roman",12,"bold" ))
        Right_frame.place(x=690,y=10,width=630,height=500)



        #frame
        table_frame= Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=615,height=400)



        #=========================Scrolll bar Table=============
        #Scroll Bar
        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame,orient=VERTICAL)

        #==========atenadce previe=============
        self.AttedanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttedanceReportTable.xview)
        scroll_y.config(command=self.AttedanceReportTable.yview)


#=============column ke liye=============

        self.AttedanceReportTable.heading("id",text= "Attendace ID")
        self.AttedanceReportTable.heading("roll",text= "Roll")
        self.AttedanceReportTable.heading("name",text= "Name")
        self.AttedanceReportTable.heading("department",text= "Department")
        self.AttedanceReportTable.heading("time",text= "Time")
        self.AttedanceReportTable.heading("date",text= "Date")
        self.AttedanceReportTable.heading("attendance",text= "Attendance")


#  ====================To sstart from first column
        self.AttedanceReportTable["show"] = "headings"

        #============for widht set=================


        self.AttedanceReportTable.column("id",width=100)
        self.AttedanceReportTable.column("roll",width=100)
        self.AttedanceReportTable.column("name",width=100)
        self.AttedanceReportTable.column("department",width=100)
        self.AttedanceReportTable.column("time",width=100)
        self.AttedanceReportTable.column("date",width=100)
        self.AttedanceReportTable.column("attendance",width=100)



        self.AttedanceReportTable.pack(fill = BOTH,expand=1)
        

        self.AttedanceReportTable.bind("<ButtonRelease>",self.get_cursor)

#===============================Fetch_Data============================================
    def fetchData(self,rows):
        self.AttedanceReportTable.delete(*self.AttedanceReportTable.get_children())
        for i in rows:
            self.AttedanceReportTable.insert("",END,values=i)
#===================import csv======================
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title= "Open CSV",filetypes =(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter = ",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

#====================export csv==========================
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No Data Found to export",parent= self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title= "Open CSV",filetypes =(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline = "") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"successfully",parent= self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent= self.root) 


#=========================getcursor means data entry filed me show karayenge==============
    def get_cursor(self,event=""):
        cursor_row=self.AttedanceReportTable.focus()
        content= self.AttedanceReportTable.item(cursor_row)
        rows= content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

#=====================reset data==================
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")




    # def functions
    def back(self):
        #self.back = tkinter.messagebox.askyesno("Face Recognition","Are you sure back this project",parent= self.root)
        #if self.back>0:
        self.root.destroy()
        # else:
        #     return











if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()