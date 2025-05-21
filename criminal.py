from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Criminal Face Recognition System")

        #variables
        self.var_station=StringVar()
        self.var_pin=StringVar()
        self.var_stationID=StringVar()
        self.var_officerBatch=StringVar()
        self.var_adhaar=StringVar()
        self.var_name=StringVar()
        self.var_city=StringVar()
        self.var_state=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_crime=StringVar()

        # top image 1
        img = Image.open(r"C:\\Users\\naksh\\OneDrive\\Desktop\\criminal recognition system\\images\\black.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimage, bd=0, highlightthickness=0, borderwidth=0)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # top image 2
        img1 = Image.open(r"C:\\Users\\naksh\\OneDrive\\Desktop\\criminal recognition system\\images\\black1.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        f_lbl1=Label(self.root,image=self.photoimage1, bd=0, highlightthickness=0, borderwidth=0)
        f_lbl1.place(x=500,y=0,width=500,height=130)

        #top image 3
        img2 = Image.open(r"C:\\Users\\naksh\\OneDrive\\Desktop\\criminal recognition system\\images\\black1.jpg")
        img2=img2.resize((1000,130),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        f_lbl2=Label(self.root,image=self.photoimage2, bd=0, highlightthickness=0, borderwidth=0)
        f_lbl2.place(x=1000,y=0,width=500,height=130)

        #bg image
        img3 = Image.open(r"C:\\Users\\naksh\\OneDrive\\Desktop\\criminal recognition system\\images\\bg.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        bg_lbl=Label(self.root,image=self.photoimage3, bd=0, highlightthickness=0, borderwidth=0)
        bg_lbl.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_lbl, text="CRIMINAL MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame=Frame(bg_lbl,bd=2,bg="light gray")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="light gray",relief=RIDGE,text="Information",font=("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10,width=760,height=580)

         # top image 1 left label frame
        img_left = Image.open(r"C:\\Users\\naksh\\OneDrive\\Desktop\\criminal recognition system\\images\\black1.jpg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimage_left=ImageTk.PhotoImage(img_left)
        f_lbl1=Label(Left_frame,image=self.photoimage_left, bd=0, highlightthickness=0, borderwidth=0)
        f_lbl1.place(x=5,y=0,width=720,height=130)

        #police Information
        criminal_info_frame=LabelFrame(Left_frame,bd=2,bg="light gray",relief=RIDGE,text="Police Station Information",font=("times new roman",12,"bold"))
        criminal_info_frame.place(x=5, y=125,width=720,height=145)

        station_name_label=Label(criminal_info_frame,text="Station Name",font=("times new roman",12,"bold"),bg="light gray")
        station_name_label.grid(row=0,column=0,padx=10, sticky=W)
        station_name_combo=ttk.Combobox(criminal_info_frame,textvariable=self.var_station,font=("times new roman",12,"bold"),width=17, state="readonly")
        station_name_combo["values"]=("Select Station","Chandan Nagar","Kharadi","Viman Nagar","Loni","Hadapsar")
        station_name_combo.current(0)
        station_name_combo.grid(row=0, column=1,padx=2,pady=10, sticky=W)

        pin_label=Label(criminal_info_frame,text="Pin Code",font=("times new roman",12,"bold"),bg="light gray")
        pin_label.grid(row=0,column=2,padx=10, sticky=W)
        pin_box=ttk.Entry(criminal_info_frame,textvariable=self.var_pin,font=("times new roman",12,"bold"),width=17)
        pin_box.grid(row=0, column=3,padx=2,pady=10, sticky=W)

        ID_label=Label(criminal_info_frame,text="Police Station ID",font=("times new roman",12,"bold"),bg="light gray")
        ID_label.grid(row=1,column=0,padx=10, sticky=W)
        ID_box=ttk.Entry(criminal_info_frame,textvariable=self.var_stationID,font=("times new roman",12,"bold"),width=17)
        ID_box.grid(row=1, column=1,padx=2,pady=10, sticky=W)

        Officer_label=Label(criminal_info_frame,text="Officer Batch No.",font=("times new roman",12,"bold"),bg="light gray")
        Officer_label.grid(row=1,column=2,padx=10, sticky=W)
        Officer_box=ttk.Entry(criminal_info_frame,textvariable=self.var_officerBatch,font=("times new roman",12,"bold"),width=17)
        Officer_box.grid(row=1, column=3,padx=2,pady=10, sticky=W)

         #Criminal Information
        criminal_info_frame1=LabelFrame(Left_frame,bd=2,bg="light gray",relief=RIDGE,text="Criminal Information",font=("times new roman",12,"bold"))
        criminal_info_frame1.place(x=5, y=250,width=720,height=300)

        adhaar_label=Label(criminal_info_frame1,text="Aadhar Card",font=("times new roman",12,"bold"),bg="light gray")
        adhaar_label.grid(row=0,column=0,padx=10,pady=5 )
        adhaar_box=ttk.Entry(criminal_info_frame1,textvariable=self.var_adhaar,font=("times new roman",12,"bold"),width=17)
        adhaar_box.grid(row=0, column=1,padx=10,pady=5)

        name_label=Label(criminal_info_frame1,text="Name",font=("times new roman",12,"bold"),bg="light gray")
        name_label.grid(row=0,column=2,padx=10,pady=5)
        name_box=ttk.Entry(criminal_info_frame1,textvariable=self.var_name,font=("times new roman",12,"bold"),width=17)
        name_box.grid(row=0, column=3, padx=10,pady=5)

        city_label=Label(criminal_info_frame1,text="City",font=("times new roman",12,"bold"),bg="light gray")
        city_label.grid(row=1,column=0,padx=10,pady=5 )
        city_box=ttk.Entry(criminal_info_frame1,textvariable=self.var_city,font=("times new roman",12,"bold"),width=17)
        city_box.grid(row=1, column=1,padx=10,pady=5  )

        state_label=Label(criminal_info_frame1,text="State",font=("times new roman",12,"bold"),bg="light gray")
        state_label.grid(row=1,column=2,padx=10,pady=5 )
        state_box=ttk.Entry(criminal_info_frame1,textvariable=self.var_state,font=("times new roman",12,"bold"),width=17)
        state_box.grid(row=1, column=3,padx=10,pady=5 )

        gender_label=Label(criminal_info_frame1,text="Gender",font=("times new roman",12,"bold"),bg="light gray")
        gender_label.grid(row=2,column=0,padx=10,pady=5 )
        gender_combo=ttk.Combobox(criminal_info_frame1,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17, state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1,padx=10,pady=5 )

        DOB_label=Label(criminal_info_frame1,text="DOB",font=("times new roman",12,"bold"),bg="light gray")
        DOB_label.grid(row=2,column=2,padx=10,pady=5 )
        DOB_box=ttk.Entry(criminal_info_frame1,textvariable=self.var_dob,font=("times new roman",12,"bold"),width=17)
        DOB_box.grid(row=2, column=3,padx=10,pady=5  )

        email_label=Label(criminal_info_frame1,text="Email",font=("times new roman",12,"bold"),bg="light gray")
        email_label.grid(row=3,column=0,padx=10,pady=5 )
        email_box=ttk.Entry(criminal_info_frame1,textvariable=self.var_email,font=("times new roman",12,"bold"),width=17)
        email_box.grid(row=3, column=1,padx=10,pady=5  )

        phone_label=Label(criminal_info_frame1,text="Phone No.",font=("times new roman",12,"bold"),bg="light gray")
        phone_label.grid(row=3,column=2,padx=10,pady=5 )
        phone_box=ttk.Entry(criminal_info_frame1,textvariable=self.var_phone,font=("times new roman",12,"bold"),width=17)
        phone_box.grid(row=3, column=3,padx=10,pady=5  )

        address_label=Label(criminal_info_frame1,text="Address",font=("times new roman",12,"bold"),bg="light gray")
        address_label.grid(row=4,column=0,padx=10, pady=5)
        address_box=ttk.Entry(criminal_info_frame1,textvariable=self.var_address,font=("times new roman",12,"bold"),width=17)
        address_box.grid(row=4, column=1,padx=10,pady=5 )

        crime_label=Label(criminal_info_frame1,text="Crime Conducted",font=("times new roman",12,"bold"),bg="light gray")
        crime_label.grid(row=4,column=2,padx=10, pady=5)
        crime_box=ttk.Entry(criminal_info_frame1,textvariable=self.var_crime,font=("times new roman",12,"bold"),width=17)
        crime_box.grid(row=4, column=3,padx=10,pady=5 )

        #radio buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(criminal_info_frame1,variable=self.var_radio1,text="take a photo sample",value="Yes")
        radionbtn1.grid(row=6,column=0)

        radionbtn2=ttk.Radiobutton(criminal_info_frame1,variable=self.var_radio1,text="No photo sample",value="No")
        radionbtn2.grid(row=6,column=1)

         #button frame
        btn_frame = Frame(criminal_info_frame1,bd=2,relief=RIDGE,bg="light gray")
        btn_frame.place(x=0,y=200,width=720,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=  17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0, column=0)
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0, column=1)
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0, column=2)
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0, column=3)

        
        btn_frame1 = Frame(criminal_info_frame1,bd=2,relief=RIDGE,bg="light gray")
        btn_frame1.place(x=0,y=235,width=720,height=35)
        photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        photo_btn.grid(row=0, column=0)
        update_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0, column=1)

          #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="light gray",relief=RIDGE,text="Displayed Information",font=("times new roman",12,"bold"))
        Right_frame.place(x=780, y=10,width=660,height=580)

        # top image 1 right label frame
        img_right = Image.open(r"C:\\Users\\naksh\\OneDrive\\Desktop\\criminal recognition system\\images\\black1.jpg")
        img_right=img_right.resize((720,130),Image.LANCZOS)
        self.photoimage_right=ImageTk.PhotoImage(img_right)
        f_lbl1=Label(Right_frame,image=self.photoimage_right, bd=0, highlightthickness=0, borderwidth=0)
        f_lbl1.place(x=5,y=0,width=720,height=130)

        #Search System
        search_frame=LabelFrame(Right_frame,bd=2,bg="light gray",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5, y=135,width=700,height=70)
        search_label=Label(search_frame,text="Search By",font=("times new roman",13,"bold"),bg="light gray")
        search_label.grid(row=0,column=0,padx=10, pady=5)
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15, state="readonly")
        search_combo["values"]=("Select","Addharr", "Name", "Phone no.", "Email")
        search_combo.current(0)
        search_combo.grid(row=0, column=1,padx=2,pady=10, sticky=W)

        search_entry=ttk.Entry(search_frame,width=15, font=("time new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0, column=3,padx=4)
        showAll_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0, column=4,padx=4)

         #Table frame
        table_frame=LabelFrame(Right_frame,bd=2,bg="light gray",relief=RIDGE)
        table_frame.place(x=5, y=210,width=700,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.criminal_table=ttk.Treeview(table_frame,column=("Adharr Card", "Name","City","State","Gender","DOB","Email","Phone No.","Address","Crime","Station Name","Pin Code","Police Station ID","Officer Batch No."),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("Adharr Card",text="Adhaar Card No.")
        self.criminal_table.heading("Name",text="Name")
        self.criminal_table.heading("City",text="City")
        self.criminal_table.heading("State",text="State")
        self.criminal_table.heading("Gender",text="Gender")
        self.criminal_table.heading("DOB",text="DOB")
        self.criminal_table.heading("Email",text="Email")
        self.criminal_table.heading("Phone No.",text="Phone No.")
        self.criminal_table.heading("Address",text="Address")
        self.criminal_table.heading("Crime",text="Crime")
        self.criminal_table.heading("Station Name",text="Station Name")
        self.criminal_table.heading("Pin Code",text="Pin Code")
        self.criminal_table.heading("Police Station ID",text="Police Station ID")
        self.criminal_table.heading("Officer Batch No.",text="Officer Batch No.")
        self.criminal_table["show"]="headings"

        self.criminal_table.column("Adharr Card",width=100)
        self.criminal_table.column("Name",width=100)
        self.criminal_table.column("City",width=100)
        self.criminal_table.column("State",width=100)
        self.criminal_table.column("Gender",width=100)
        self.criminal_table.column("DOB",width=100)
        self.criminal_table.column("Email",width=100)
        self.criminal_table.column("Phone No.",width=100)
        self.criminal_table.column("Address",width=100)
        self.criminal_table.column("Crime",width=100)
        self.criminal_table.column("Station Name",width=100)
        self.criminal_table.column("Pin Code",width=100)
        self.criminal_table.column("Police Station ID",width=100)
        self.criminal_table.column("Officer Batch No.",width=200)

        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_station.get() == "Select Station" or self.var_adhaar.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Root", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO criminal (station, pin, stationID, officerBatch, adhaar, name, city, state, gender, dob, email, phone, address, crime, photoSample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_station.get(),
                    self.var_pin.get(),
                    self.var_stationID.get(),
                    self.var_officerBatch.get(),
                    self.var_adhaar.get(),
                    self.var_name.get(),
                    self.var_city.get(),
                    self.var_state.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_crime.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Criminal record has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Root", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from criminal")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.criminal_table.focus()
        content= self.criminal_table.item(cursor_focus)
        data=content["values"]

        self.var_adhaar.set(data[0])
        self.var_name.set(data[1])
        self.var_city.set(data[2])
        self.var_state.set(data[3])
        self.var_gender.set(data[4])
        self.var_dob.set(data[5])
        self.var_email.set(data[6])
        self.var_phone.set(data[7])
        self.var_address.set(data[8])
        self.var_crime.set(data[9])
        self.var_station.set(data[10])
        self.var_pin.set(data[11])
        self.var_stationID.set(data[12])
        self.var_officerBatch.set(data[13])
        
    #update function
    def update_data(self):
        if self.var_station.get() == "Select Station" or self.var_adhaar.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update detials?",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Root", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update criminal SET name=%s,city=%s,state=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,crime=%s,station=%s,pin=%s,stationID=%s,officerBatch=%s,photoSample=%s WHERE adhaar=%s",(
                        self.var_name.get(),         
                        self.var_city.get(),
                        self.var_state.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_crime.get(),
                        self.var_station.get(),
                        self.var_pin.get(),
                        self.var_stationID.get(),
                        self.var_officerBatch.get(),
                        self.var_radio1.get(),
                        self.var_adhaar.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Sucess","Details sucessfully updated",parent=self.root)
                conn.commit()
                conn.close()
                self.fetch_data
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_adhaar.get()=="":
            messagebox.showerror("Error","Adhaar number must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Root", database="face_recognizer")
                    my_cursor = conn.cursor() 
                    sql="delete from criminal where adhaar=%s"
                    val=(self.var_adhaar.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Sucessfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #reset button
    def reset_data(self):
        self.var_station.set("Select Station")
        self.var_pin.set("")
        self.var_stationID.set("")
        self.var_officerBatch.set("")
        self.var_adhaar.set("")
        self.var_name.set("")
        self.var_city.set("")
        self.var_state.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_crime.set("")
        self.var_radio1.set("")

    #generate data set take photo samples
    def generate_dataset(self):
        if self.var_station.get() == "Select Station" or self.var_adhaar.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Root", database="face_recognizer")
                my_cursor = conn.cursor()
                aadhar_id = self.var_adhaar.get()
                my_cursor.execute("SELECT * FROM criminal WHERE adhaar = %s", (aadhar_id,))
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "No criminal found with this Aadhaar number.")
                    conn.close()
                    return

                my_cursor.execute("UPDATE criminal SET name=%s, city=%s, state=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, crime=%s, station=%s, pin=%s, stationID=%s, officerBatch=%s, photoSample=%s WHERE adhaar=%s", (
                    self.var_name.get(),         
                    self.var_city.get(),
                    self.var_state.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_crime.get(),
                    self.var_station.get(),
                    self.var_pin.get(),
                    self.var_stationID.get(),
                    self.var_officerBatch.get(),
                    self.var_radio1.get(),
                    aadhar_id
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #load predifined data on face frontals from open cv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scalling factor = 1.3
                    #minimum neighbour = 5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                
                if not cap.isOpened():
                    messagebox.showerror("Error", "Could not open webcam. Please check your camera.")
                    return
                
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(aadhar_id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



if __name__ == "__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()
