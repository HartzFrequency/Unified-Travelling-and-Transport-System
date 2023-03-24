import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage




window2 = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # 

class Window2(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Window 2")
        self.geometry(f"{1100}x{580}")

