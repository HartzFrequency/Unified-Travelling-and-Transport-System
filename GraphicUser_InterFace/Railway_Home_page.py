import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage
from tkinter import messagebox
import mysql.connector
import Modules.SQL as sql

# Initialize the main application window
window6 = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue") 

class Railway(customtkinter.CTk):
    """Main class for the Railway Booking Services application."""
    def __init__(self):
        super().__init__()
        self.title("Truck Home Page")
        self.geometry(f"{1100}x{340}")

        # Sidebar frame for appearance mode and scaling options
        self.sidebar_frame = customtkinter.CTkFrame(self, width=120, corner_radius=15)
        self.sidebar_frame.grid(row=9, column=0, rowspan=4, sticky="nse")
        self.sidebar_frame.grid_rowconfigure(1, weight=1)
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode", anchor="center")
        self.appearance_mode_label.grid(row=5, column=0, padx=10, pady=(5,0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady =(10,10))
        
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling", anchor="center")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10,0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["70%", "80%", "90%", "100%", "110%", "120%", "130%"],command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(5,20))

        # Set default values for appearance mode and scaling
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        # Main title label
        self.sidebar_frame0 = customtkinter.CTkFrame(self, width=120,height=100, corner_radius=15) 
        self.sidebar_frame0.grid(row=0, column=15, rowspan=15, sticky = 'nsew')
        self.sidebar_frame0.grid_rowconfigure(8, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame0, text="Railway Booking Services", font=customtkinter.CTkFont(size=42, weight="bold"))
        self.logo_label.grid(row=0, column=15, padx=220, pady=50)

        # Frame for 'From' and 'To' selection
        self.sidebar_frame1=customtkinter.CTkFrame(self,width=200,height=100,corner_radius=15)
        self.sidebar_frame1.grid(row=15,column=15, padx=0, pady=5,sticky='nsew')

        # 'From' label and dropdown menu
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="From",font=customtkinter.CTkFont(size=20),anchor="w")
        self.to_label.grid(row=15, column=10, padx=100, pady=(5,0),sticky='sw')
        self.from_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1,values=["Select","GWL", "BHP","MUM", "DLH"])
        self.from_optionemenu.grid(row=16, column=10, padx=60, pady=(5,5),sticky='sw')


        # 'To' label and dropdown menu
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="To",font=customtkinter.CTkFont(size=20), anchor="w")
        self.to_label.grid(row=15, column=20, padx=140, pady=(5,0),sticky='se')
        self.to_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1, values=["Select", "DLH","MUM","BHP","GWL"])
        self.to_optionemenu.grid(row=16, column=20, padx=80, pady=(5,5),sticky='se')

        # Continue button
        self.continue_button = customtkinter.CTkButton(self,text="Continue",command=self.end_e)
        self.continue_button.grid(row=150, column=15,rowspan=100, padx=20, pady=(10,10),sticky='se')

        # Back button
        self.string_input_button = customtkinter.CTkButton(self,text="Home", command=self.open_Main_window)
        self.string_input_button.grid(row=150, column=0, padx=20, pady=(10, 10),sticky='sw')


    def open_Main_window(self):
        """Open the main window and destroy the current one."""
            self.destroy()            
            import StartPageGUI
            StartPageGUI.Main().mainloop()

    def end_e(self):
        """Function to validate user input and proceed to the next window."""
        #function to end app-GUI
        global rawa
        global rawc
        global f1
        f1 = self.from_optionemenu.get()  # 'From' value
        global f2
        f2 = self.to_optionemenu.get()    # 'To' value
        
        # Validation of input fields
        if f1=='-Select-' and f2=='-Select-':
            return messagebox.showerror('Error','Please select Departure & Arrival locations')
        elif f2=='-Select-':
            return messagebox.showerror("Error", "Select Arrival location")
        elif f1==f2:
            return messagebox.showerror("Error", "Invalid location entry!")
        elif f1=='-Select-':
            return messagebox.showerror('Error','Please select Departure location')

        else:
            # Query the database for available railway options
            availableRAILWAY = sql.Query_GetAvailableRailway(0, 0)
            sql.Query_WriteSearchResult(availableRAILWAY)
            
            Number_of_vehicle = len(availableRAILWAY)
            if Number_of_vehicle == 0:
                return messagebox.showerror("Error", "No Transport for this ")
            self.open_Info_window()
    
    def open_Info_window(self):
        """Open the information window and destroy the current one."""
        self.destroy()            
        import Display_availability    
        Display_availability.Available().mainloop()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Change the appearance mode of the application."""
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        """Change the UI scaling of the application."""
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


if __name__ == "__main__":
    app6 = Railway()
    app6.mainloop()
