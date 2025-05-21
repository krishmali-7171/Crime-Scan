from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Criminal Face Recognition System")

        title_lbl=Label(self.root, text="DEVELOPER", font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"images\black1.jpg")
        img_top=img_top.resize((1530,720),Image.LANCZOS)
        self.photoimage_top=ImageTk.PhotoImage(img_top)
        f_lbl1=Label(self.root,image=self.photoimage_top, bd=0, highlightthickness=0, borderwidth=0)
        f_lbl1.place(x=0,y=55,width=1530,height=720)

        #frame
        main_frame=Frame( f_lbl1,bd=2,bg="light gray")
        main_frame.place(x=0,y=0,width=500,height=600)

        img_top1 = Image.open(r"images\naksh.png")
        img_top1=img_top1.resize((200,200),Image.LANCZOS)
        self.photoimage_top1=ImageTk.PhotoImage(img_top1)
        f_lbl1=Label(main_frame,image=self.photoimage_top1)
        f_lbl1.place(x=0,y=55,width=200,height=200)

        img_top2 = Image.open(r"images\krish.png")
        img_top2=img_top2.resize((200,200),Image.LANCZOS)
        self.photoimage_top2=ImageTk.PhotoImage(img_top2)
        f_lbl1=Label(main_frame,image=self.photoimage_top2)
        f_lbl1.place(x=0,y=300,width=200,height=200)

        img_top3 = Image.open(r"images\aadi.png")
        img_top3=img_top3.resize((200,200),Image.LANCZOS)
        self.photoimage_top3=ImageTk.PhotoImage(img_top3)
        f_lbl1=Label(main_frame,image=self.photoimage_top3)
        f_lbl1.place(x=250,y=55,width=200,height=200)

        img_top4 = Image.open(r"images\nimish.png")
        img_top4=img_top4.resize((200,200),Image.LANCZOS)
        self.photoimage_top4=ImageTk.PhotoImage(img_top4)
        f_lbl1=Label(main_frame,image=self.photoimage_top4)
        f_lbl1.place(x=250,y=300,width=200,height=200)

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()