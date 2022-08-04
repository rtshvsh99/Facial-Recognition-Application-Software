from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk  # pip install pillow


class ChatBot:
    def __init__(self,root):
        self.root = root
        self.root.title("chatBot")
        self.root.geometry("800x650+0+0")
        self.root.title("ChatBot")
        self.root.bind('<Return>',self.enter_func)


        # -----------Main DFrame--------
        main_frame = Frame(self.root, bd=4, bg='powder blue', width=610)
        main_frame.pack()

        img_chat = Image.open(r"image\help.jpg")
        img_chat = img_chat.resize((200,70),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        # 
        Title_label = Label(main_frame, bd=3,relief=RAISED,anchor= 'nw', width=730,compound=LEFT,image=self.photoimg, text='Help Desk', font=('arial', 30,'bold'),fg='green',bg='white' )
        Title_label.pack(side=TOP)

        # --------------------Text area---------------
        text_msg = Label(main_frame,relief=RAISED, width=200, text='Welcome to Help Desk', font=('arial', 15,'bold'),fg='Blue',bg='white' )
        text_msg.pack(side=TOP)


        self.scroll_y = ttk.Scrollbar(main_frame,orient=VERTICAL) 
        self.text= Text(main_frame,width=65,height=20,bd=5,relief = RAISED, font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

         # button
        btn_frame = Frame(self.root, bd=4, bg='white', width=610)
        btn_frame.pack()

        label_1  = Label(btn_frame,text='Type Something:-',font=('arial', 14,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)

#entry box
        # variable for entry box
        self.entry=StringVar()
        self.entry1 = ttk.Entry(btn_frame,textvariable=self.entry,width=30,font=('arial',14,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send = Button(btn_frame,text="Send",command=self.send,font=('arial', 12,'bold'),width=6,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)


        self.clear = Button(btn_frame,text="Clear Data",command=self.clear,font=('arial', 12,'bold'),width=11,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        #===========label for message ko show karane ke liye
        self.msg=''
        self.label_2  = Label(btn_frame,text=self.msg,font=('arial', 14,'bold'),fg='red',bg='white')
        self.label_2.grid(row=1,column=1,padx=5,sticky=W)



    #  ======================Function declaration=============================

    #prss enter function button

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')


    #===========clear function===========
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

        


# ,text="Welcome to Log Window"
 # self.text.insert('end', '>>> Welcome to Log Window', 'welcome')


    def send(self):       
        send='\t\t\t'+'You: ' +self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg= 'Please enter some input'
            self.label_2.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.label_2.config(text=self.msg,fg='red')


        if (self.entry.get()=='hi'):
            self.text.insert(END,'\n\n' + 'Bot: Hi! How can I help You?')

        elif (self.entry.get()=='hello'):
            self.text.insert(END,'\n\n' + 'Bot: Hi?')

            
        elif (self.entry.get()=='hi'):
            self.text.insert(END,'\n\n' + 'Bot: Hello')


        elif (self.entry.get()=='How are you?'):
            self.text.insert(END,'\n\n' + 'Bot: Fine and You')

            
        elif (self.entry.get()=='good'):
            self.text.insert(END,'\n\n' + 'Bot: Nice to hear.')

        elif (self.entry.get()=='Who created you?'):
            self.text.insert(END,'\n\n' + 'Bot: Ritesh Vishwakarma')


        elif (self.entry.get()=='Who are you?'):
            self.text.insert(END,'\n\n' + 'Bot: I am ChatBot.')

            
        elif (self.entry.get()=='ok'):
            self.text.insert(END,'\n\n' + 'Bot: okay! anything else do you want to know ?')


        elif (self.entry.get()=='no'):
            self.text.insert(END,'\n\n' + 'Bot: its Okay. Nice to talk to you')

            
        elif (self.entry.get()=='bye'):
            self.text.insert(END,'\n\n' + 'Bot: okay bye.  Thank you for your chatting')
        else:
            self.text.insert(END,'\n\n' + "Bot: Sorry I didn't get it. ")










if __name__ == '__main__':
    root= Tk()
    obj = ChatBot(root)
    root.mainloop()
