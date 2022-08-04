from logging import root
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
   

#TITLE
        title_lbl = Label(self.root,text = "TRAIN DATA SET ", font = ("times new roman",30,"bold"),bg = "white",fg = "green")
        title_lbl.place(x=0,y=0,width=1366,height=40)
#IMAGE
        img_top = Image.open(r"image\finalbackground.jpg")
        img_top = img_top.resize((1366,300),Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image =self.photoimg_top )
        f_lbl.place(x =0,y=55,width = 1366,height= 300)


         # back butons
        back_button = Button(self.root,command = self.back,text="Back",font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red" )
        back_button.place(x =1150 ,y=136,width = 120,height=35)

    

#button

        b1_1 = Button(self.root,text="Process Your Data",command = self.train_classifier,cursor= "hand2", font = ("times new roman",30,"bold"),bg = "blue",fg = "white")
        b1_1.place(x=470,y=305,width=400,height=45)
        


#last image
        img_bottom = Image.open(r"image\train2.jpg")
        img_bottom = img_bottom.resize((1366,350),Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image =self.photoimg_bottom )
        f_lbl.place(x =0,y=350,width = 1366,height= 350)





#==============functio  for train data button ===================

    def train_classifier(self):
        data_dir =("data")
        path =  [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            #converting image in grayscale
            img = Image.open(image).convert('L')  #Gray Scale Image
            #to convert in image in gridsystem by numpy
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13     #for pressing Enter to close 

        ids = np.array(ids)


        #=============train the classifier  to use LBPH===================
        clf = cv2.face_LBPHFaceRecognizer.create()
        clf.train(faces ,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed!!",parent=self.root)



    
        # back button
    def back(self):
        #self.back = tkinter.messagebox.askyesno("Face Recognition","Are you sure back this project",parent= self.root)
        #if self.back>0:
        self.root.destroy()
        #else:
         #   return








if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()