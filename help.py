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


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer Profile")


        title_lbl = Label(self.root, text="HELP DESKS", font=(
            "times new roman", 30, "bold"), bd=2, bg="#8379FA", fg="White")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        img_top = Image.open(r"./college_images/KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img_top = img_top.resize((1530, 730), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=0, y=55, width=1530, height=730)

        dev_label = Label(f_lb1, text="dev.singh.nitish@gmail.com  Nitish Singh", font=("times new roman",30, "bold"),fg="blue", bg="white")
        dev_label.place(x=400,y=10)

        dev_label = Label(f_lb1, text="dev.singh.nitish@gmail.com  Parshant Kumar", font=("times new roman",30, "bold"),fg="blue", bg="white")
        dev_label.place(x=400,y=80)

        dev_label = Label(f_lb1, text="dev.singh.nitish@gmail.com  Manu Kumar Ram", font=("times new roman",30, "bold"),fg="blue", bg="white")
        dev_label.place(x=400,y=150)

        dev_label = Label(f_lb1, text="dev.singh.nitish@gmail.com  Mukesh Sharma", font=("times new roman",30, "bold"),fg="blue", bg="white")
        dev_label.place(x=400,y=220)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
