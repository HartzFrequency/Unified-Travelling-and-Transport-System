import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage




window8 = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue") 

class Route(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Route Information Page")
        self.geometry(f"{1100}x{580}")


        self.string_input_button = customtkinter.CTkButton(self,text="Back Button")
        self.string_input_button.grid(row=10, column=6, padx=20, pady=(10, 10))


       



   


if __name__ == "__main__":
    app7 = Route()
    app7.mainloop()
