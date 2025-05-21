from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Criminal Face Recognition System")


        title_lbl=Label(self.root, text="FACE RECOGNITION", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        b1_1=Button(title_lbl,command=self.face_recognition, text="FACE RECOGNITION",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"images\black1.jpg")
        img_top=img_top.resize((800,800),Image.LANCZOS)
        self.photoimage_top=ImageTk.PhotoImage(img_top)
        f_lbl1=Label(self.root,image=self.photoimage_top, bd=0, highlightthickness=0, borderwidth=0)
        f_lbl1.place(x=0,y=55,width=650,height=800)

        img_bottom = Image.open(r"images\black1.jpg")
        img_bottom=img_bottom.resize((1500,800),Image.LANCZOS)
        self.photoimage_bottom=ImageTk.PhotoImage(img_top)
        f_lbl1=Label(self.root,image=self.photoimage_bottom, bd=0, highlightthickness=0, borderwidth=0)
        f_lbl1.place(x=650,y=55,width=850,height=800)

    #face revognition
    def face_recognition(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbor,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbor)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                face_id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="Root", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT name, dob, phone, adhaar FROM criminal WHERE adhaar=%s", (str(face_id),))
                data = my_cursor.fetchone()

                if data is not None and len(data) == 4:
                    name, dob, phone, adhaar = data
                else:
                    name = "Unknown"
                    dob = "Unknown"
                    phone = "Unknown"
                    adhaar = "Unknown"


                if confidence > 77:
                    cv2.putText(img, f"Name: {name}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"DOB: {dob}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Phone No: {phone}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                    cv2.putText(img, "Not registered", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)

                coord=[x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
            
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()