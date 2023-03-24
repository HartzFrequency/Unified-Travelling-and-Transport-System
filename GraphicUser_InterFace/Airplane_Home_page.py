import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage




window5 = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue") 

class Airplane(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Airplane Home Page")
        self.geometry(f"{1100}x{580}")


        self.string_input_button = customtkinter.CTkButton(self,text="Back Button", command=self.open_Main_window)
        self.string_input_button.grid(row=10, column=6, padx=20, pady=(10, 10))


       



    def open_Main_window(self):
            self.destroy()            
            import StartPageGUI
            StartPageGUI.Main().mainloop()




if __name__ == "__main__":
    app5 = Airplane()
    app5.mainloop()
