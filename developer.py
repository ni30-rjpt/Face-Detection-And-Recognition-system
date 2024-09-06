from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from employee import employee
from train import train
from face_recog import Face_Recognition
from Attendence import attendance
import os
import tkinter
from time import strftime
from datetime import datetime


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer Profile")


        title_lbl = Label(self.root, text="Face Recoginition", font=(
            "times new roman", 30, "bold"), bd=2, bg="#8379FA", fg="White")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # _______________First Image

        img_top = Image.open(r"./college_images/dev.jpg")
        img_top = img_top.resize((1530, 730), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=0, y=55, width=1530, height=730)


        main_frame = Frame(f_lb1, bd=2)
        main_frame.place(x=1000, y=0, width=500, height=670)


        img_top1 = Image.open(r"./college_images/profile.jpg")
        img_top1 = img_top1.resize((160, 160), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lb1 = Label(main_frame, image=self.photoimg_top1)
        f_lb1.place(x=300, y=0, width=160, height=160)


        # Department
        dev_label = Label(main_frame, text="Hello My Name, Nitish Kumar", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=0,y=5) 

        dev_label = Label(main_frame, text="My College Name: BBSBEC", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=0,y=35)                

        dev_label = Label(main_frame, text="My Roll No: 2100379", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=0,y=65)  

        dev_label = Label(main_frame, text="Course : B.Tech (CSE) ", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=0,y=95)

        dev_label = Label(main_frame, text="Contact: 62xxxxxxx", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=0,y=125)


        img_top2 = Image.open(r"./college_images/profile.jpg")
        img_top2 = img_top2.resize((160, 160), Image.ANTIALIAS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)

        f_lb1 = Label(main_frame, image=self.photoimg_top2)
        f_lb1.place(x=0, y=170, width=160, height=160)  

        dev_label = Label(main_frame, text="Hello My Name, Parshant Kumar", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=180,y=170) 

        dev_label = Label(main_frame, text="My College Name: BBSBEC", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=180,y=200)                

        dev_label = Label(main_frame, text="My Roll No: 2100385", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=180,y=230)  

        dev_label = Label(main_frame, text="Course : B.Tech (CSE) ", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=180,y=260)

        dev_label = Label(main_frame, text="Contact: 9874563210", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=180,y=290)         


        img_top3 = Image.open(r"./college_images/profile.jpg")
        img_top3 = img_top3.resize((160, 160), Image.ANTIALIAS)
        self.photoimg_top3 = ImageTk.PhotoImage(img_top3)

        f_lb1 = Label(main_frame, image=self.photoimg_top3)
        f_lb1.place(x=300, y=340, width=160, height=160) 

        dev_label = Label(main_frame, text="Hello My Name,Manu Kumar Ram", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=0,y=340) 

        dev_label = Label(main_frame, text="My College Name: BBSBEC", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=0,y=370)                

        dev_label = Label(main_frame, text="My Roll No: 2100379", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=0,y=400)  

        dev_label = Label(main_frame, text="Course : B.Tech (CSE) ", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=0,y=430)

        dev_label = Label(main_frame, text="Contact: 620xxxxxx", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=0,y=460)

        img_top4 = Image.open(r"./college_images/profile.jpg")
        img_top4 = img_top4.resize((160, 160), Image.ANTIALIAS)
        self.photoimg_top4 = ImageTk.PhotoImage(img_top4)

        f_lb1 = Label(main_frame, image=self.photoimg_top3)
        f_lb1.place(x=0, y=510, width=160, height=160)

        dev_label = Label(main_frame, text="Hello My Name, Parshant Kumar", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=180,y=510) 

        dev_label = Label(main_frame, text="My College Name: BBSBEC", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=180,y=540)                

        dev_label = Label(main_frame, text="My Roll No: 2100385", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=180,y=570)  

        dev_label = Label(main_frame, text="Course : B.Tech (CSE) ", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=180,y=600)

        dev_label = Label(main_frame, text="Contact: 987xxxxx", font=("times new roman",16, "bold"), bg="white")
        dev_label.place(x=180,y=630)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()