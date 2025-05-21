from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Criminal Face Recognition System")
    
        title_lbl=Label(self.root, text="HELP", font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"images\black1.jpg")
        img_top=img_top.resize((1530,720),Image.LANCZOS)
        self.photoimage_top=ImageTk.PhotoImage(img_top)
        f_lbl1=Label(self.root,image=self.photoimage_top, bd=0, highlightthickness=0, borderwidth=0)
        f_lbl1.place(x=0,y=55,width=1530,height=720)

        help_label1=Label(f_lbl1, text="nakshatrarane503@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="white")
        help_label1.place(x=50,y=5)
        help_label2=Label(f_lbl1, text="krishmali7171@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="white")
        help_label2.place(x=50,y=100)
        help_label3=Label(f_lbl1, text="aadisurve@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="white")
        help_label3.place(x=50,y=200)
        help_label4=Label(f_lbl1, text="nimishbhalerao@icloud.com",font=("times new roman",20,"bold"),fg="blue",bg="white")
        help_label4.place(x=50,y=300)


if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()