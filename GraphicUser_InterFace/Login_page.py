import tkinter as tk
import tkinter.messagebox
import mysql.connector
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter.font import Font

customtkinter.set_appearance_mode("dark")

class Login(customtkinter.CTk):
    width = 1240  #helps in image width
    height = 1080 #helps in image height
    def __init__(self):
        super().__init__()

        # OPENEING WINDOW SIZE
        self.title("Login")
        self.geometry(f"{1240}x{720}")
        self.bg_image = customtkinter.CTkImage(Image.open("Image/Background_gradient.jpg"),size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # LOGIN FRAME INSIDE WINDOW
        # TEXT : "Welcome!\nUnified Travelling & Transport System"
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=15)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="Welcome!\nUnified Travelling & Transport System",font=customtkinter.CTkFont(size=24, weight="bold", slant="roman", family="Helvetica"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))

        #TEXT : LOGIN PAGE
        self.login_label_2 = customtkinter.CTkLabel(self.login_frame, text="Login Page",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.login_label_2.grid(row=1, column=0, padx=30, pady=(50, 15))
        
        #TEXT : USERNAME
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=300, placeholder_text="Username")
        self.username_entry.grid(row=2, column=0, padx=30, pady=(15, 15))
        
        #TEXT : PASSWORD
        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=300, show="*", placeholder_text="Password")
        self.password_entry.grid(row=3, column=0, padx=30, pady=(0, 15))
        
        #TEXT : LOGIN BUTTON TEXT
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=4, column=0, padx=30, pady=(15, 15))

    def login_event(self):
        
        UTTSdb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Rajput@MySQL',
        database='UTTS')

        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        cur=UTTSdb.cursor()
        s="SELECT * FROM users WHERE first_name = '{}' AND Password = '{}'".format(entered_username,entered_password)
        cur.execute(s)
        QueryCheckForPassword=cur.fetchone()

        if QueryCheckForPassword:
            self.destroy()            
            import StartPageGUI
            StartPageGUI.Main().mainloop()

        else:
            print("error")
            return messagebox.showerror('Error','Incorrect Username or Password')
        
        print("Login pressed - username:", entered_username, "password:",entered_password)

if __name__ == "__main__":
    app9 = Login()
    app9.mainloop()