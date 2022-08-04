from logging import root
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")



        #TITLE
        title_lbl = Label(self.root,text = "HELP DESK ", font = ("times new roman",30,"bold"),bg = "white",fg = "blue")
        title_lbl.place(x=0,y=0,width=1366,height=40)
#IMAGE
        img_top = Image.open(r"image\help2.jpg")
        img_top = img_top.resize((1366,620),Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image =self.photoimg_top )
        f_lbl.place(x =0,y=55,width = 1366,height= 620)
#==================lebel=====================
        dev_label=Label(f_lbl,text="Name:- Ritesh Vishwakarma ",font=("times new roman",30,"bold"),fg="blue",bg="white")
        dev_label.place(x=450,y=300)
        dev1_label=Label(f_lbl,text="Email: rtshvsh99@gmail.com ",font=("times new roman",30,"bold"),fg="blue",bg="white")
        dev1_label.place(x=450,y=350)




        # -------------self ke bare me------
        main_frame = Frame(f_lbl,bd = 2,bg="white")
        main_frame.place(x=900,y=43,width= 400,height=300)


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



          # back butons
        back_button = Button(self.root,command = self.back,text="Back",font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red" )
        back_button.place(x =50 ,y=50,width = 100,height=35)



        btn =Button(self.root,text="Learn More",command = self.click,font=('arial',10,'bold'),fg='red',bg='black')
        btn.place(x=200,y=100)

       

        self.name_var= StringVar()


    def click(self):
        lbl = Label(self.root,text="",font=("times new roman",20,'bold'))
        lbl.place(x=100,y=150)
        lbl.config(text="Hurricane Leslie (2018) was a cyclone of tropical origin, the strongest to strike the Iberian Peninsula since 1842. A large, long-lived, and very erratic tropical cyclone, Leslie developed from an extratropical cyclone that was situated over the northern Atlantic on 22 September. It became a Category 1 hurricane early on 3 October before falling to tropical storm intensity late on 4 October. After re-intensifying, Leslie reached hurricane status for the second time on 10 October, reaching peak intensity two days later and passing between the Azores and Madeira. It thereafter weakened, making landfall over central Portugal before dissipating by 16 October over Spain. The storm was responsible for 17 deaths in mainland Europe, including 2 direct deaths in Portugal and 15 indirect deaths in France. Over 300,000 citizens were left without power in Portugal, with damage there estimated to be about €120 million (US$145 million). The storm and a", wraplength=800, justify="center")
        



        #def functions
    def back(self):
        #self.back = tkinter.messagebox.askyesno("Face Recognition","Are you sure back this project",parent= self.root)
        #if self.back>0:
        self.root.destroy()
        #else:
        #    return
        







if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()