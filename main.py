from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import tkinter
from criminal import Criminal
import os
from criminal import Criminal
from train import train
from face_recognition import Face_Recognition
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Criminal Face Recognition System")

        # top image 1
        img = Image.open(r"images\black.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimage, bd=0, highlightthickness=0, borderwidth=0)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # top image 2
        img1 = Image.open(r"images\black1.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        f_lbl1=Label(self.root,image=self.photoimage1, bd=0, highlightthickness=0, borderwidth=0)
        f_lbl1.place(x=500,y=0,width=500,height=130)

        #top image 3
        img2 = Image.open(r"images\black1.jpg")
        img2=img2.resize((1000,130),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        f_lbl2=Label(self.root,image=self.photoimage2, bd=0, highlightthickness=0, borderwidth=0)
        f_lbl2.place(x=1000,y=0,width=500,height=130)

        #bg image
        img3 = Image.open(r"images\bg.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        bg_lbl=Label(self.root,image=self.photoimage3, bd=0, highlightthickness=0, borderwidth=0)
        bg_lbl.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_lbl, text="CRIMINAL RECOGNITION AND RECORD SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #time
        def time():
           string = strftime('%H:%M:%S %p')
           lbl.config(text =string)
           lbl.after(1000,time)

        lbl = Label(title_lbl, font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #criminal button
        img4 = Image.open(r"images\b1.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        b1=Button(bg_lbl,image=self.photoimage4,command=self.criminal_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        b1_1=Button(bg_lbl,text="Criminal Details",command=self.criminal_details, cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        #scan face button
        img5 = Image.open(r"images\face.webp")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimage5=ImageTk.PhotoImage(img5)
        b2=Button(bg_lbl,image=self.photoimage5, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)
        b2_1=Button(bg_lbl,text="Criminal Details", cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b2_1.place(x=500, y=300, width=220, height=40)

        # face button
        img5 = Image.open(r"images\face.webp")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimage5=ImageTk.PhotoImage(img5)
        b2=Button(bg_lbl,image=self.photoimage5,command=self.face_data, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)
        b2_1=Button(bg_lbl,text="Face Recognition",command=self.face_data, cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b2_1.place(x=500, y=300, width=220, height=40)

         # attendance button
        #img6 = Image.open(r"images\b3.webp")
        #img6=img6.resize((220,220),Image.LANCZOS)
        #self.photoimage6=ImageTk.PhotoImage(img6)
        #b3=Button(bg_lbl,image=self.photoimage6, cursor="hand2")
        #b3.place(x=800, y=100, width=220, height=220)
        #b3_1=Button(bg_lbl,text="Attendance", cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        #b3_1.place(x=800, y=300, width=220, height=40)

        # Help desk
        img7 = Image.open(r"images\b4.webp")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimage7=ImageTk.PhotoImage(img7)
        b4=Button(bg_lbl,image=self.photoimage7,command=self.help_data, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)
        b4_1=Button(bg_lbl,text="Help Desk", cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b4_1.place(x=1100, y=300, width=220, height=40)

        # Train Data
        img8 = Image.open(r"images\b5.webp")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimage8=ImageTk.PhotoImage(img8)
        b5=Button(bg_lbl,image=self.photoimage8,command=self.train_data, cursor="hand2")
        b5.place(x=200, y=380, width=220, height=220)
        b5_1=Button(bg_lbl,text="Train Data",command=self.train_data, cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b5_1.place(x=200, y=580, width=220, height=40)

          # Photos
        img9 = Image.open(r"images\b6.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimage9=ImageTk.PhotoImage(img9)
        b6=Button(bg_lbl,image=self.photoimage9, cursor="hand2",command=self.open_img)
        b6.place(x=500, y=380, width=220, height=220)
        b6_1=Button(bg_lbl,text="Photos", cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b6_1.place(x=500, y=580, width=220, height=40)

         #Developer
        img10 = Image.open(r"images\b7.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimage10=ImageTk.PhotoImage(img10)
        b7=Button(bg_lbl,image=self.photoimage10,command=self.developer_data, cursor="hand2")
        b7.place(x=800, y=380, width=220, height=220)
        b7_1=Button(bg_lbl,text="Developer", cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b7_1.place(x=800, y=580, width=220, height=40)

           #Exit
        img11 = Image.open(r"images\b8.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimage11=ImageTk.PhotoImage(img11)
        b8=Button(bg_lbl,image=self.photoimage11,command=self.iExit, cursor="hand2")
        b8.place(x=1100, y=380, width=220, height=220)
        b8_1=Button(bg_lbl,text="Exit", cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b8_1.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
      self.iExit=tkinter.messagebox.askyesno("Criminal Recognition","Are you sure exit this program",parent=self.root)
      if self.iExit >0:
        self.root.destroy()
      else:
        return



        #function button
    def criminal_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Criminal(self.new_window)

    def train_data(self):
      self.new_window=Toplevel(self.root)
      self.app=train(self.new_window)

    def face_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Face_Recognition(self.new_window)

    def developer_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Developer(self.new_window)

    def help_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Help(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
