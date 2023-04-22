import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage
import random
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import simpledialog
import mysql.connector
import PIL
from PIL import ImageTk,Image





window8 = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue") 

class Route(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Route Information Page")
        self.geometry(f"{1100}x{580}")


      


        self.sidebar_frame0 = customtkinter.CTkFrame(self, width=100,height=30, corner_radius=0) 
        self.sidebar_frame0.grid(row=0, column=15, rowspan=10)
        self.sidebar_frame0.grid_rowconfigure(8, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame0, text="Available Buses", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=15, padx=150, pady=20)
        

        # f1 = os.environ['F1']
        self.sidebar_frame1=customtkinter.CTkFrame(self,width=200,height=100)
        self.sidebar_frame1.grid(row=15,column=15,rowspan=25, padx=20, pady=10)
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text=f1,font=customtkinter.CTkFont(size=20),anchor="w")
        self.to_label.grid(row=15, column=15, padx=100, pady=10)




       



   


if __name__ == "__main__":
    app7 = Route()
    app7.mainloop()
