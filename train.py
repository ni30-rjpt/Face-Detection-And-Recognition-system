from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import cv2 
import mysql.connector
import os
import numpy as np
import face_recognition

class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        #_____________title

        title_lbl=Label(self.root,text="TRAIN DATA SET", font=("times new roman",35,"bold"),bd=2,bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #-----first Image

        img_top=Image.open(r"./college_images/BestFacialRecognition.jpg")
        img_top=img_top.resize((1530,400),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1530,height=400)


        #-----second Image

        img2=Image.open(r"./college_images/facialrecognition.png")
        img2=img2.resize((1530,450),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb2=Label(self.root,image=self.photoimg2)
        f_lb2.place(x=0,y=430,width=1530,height=390)


        #-------------------Train Button

        b1_1=Button(self.root,text="Train Data",command=self.train_classifier, cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=420,width=1530,height=45)

    def train_classifier(self):
        data_dir=("data")
        path= [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            # "C:\Users\Dell\OneDrive\Desktop\Face_Rec\data\user.2.1.jpg"

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training ",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #-------------------Train the Classifier And Save-----------
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result ","Training datasets Completed !!")





if __name__ == "__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()
