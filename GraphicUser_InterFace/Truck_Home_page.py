import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage
from tkinter import messagebox
import mysql.connector
import Modules.SQL as sql

window6 = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue") 

class Truck(customtkinter.CTk):
    """
    Truck class represents the GUI for Truck Booking Services.

    Attributes:
        appearance_mode_label (customtkinter.CTkLabel): Label for selecting appearance mode.
        appearance_mode_optionemenu (customtkinter.CTkOptionMenu): Option menu for selecting appearance mode.
        scaling_label (customtkinter.CTkLabel): Label for selecting UI scaling.
        scaling_optionemenu (customtkinter.CTkOptionMenu): Option menu for selecting UI scaling.
        sidebar_frame0 (customtkinter.CTkFrame): Frame for displaying the logo and title.
        sidebar_frame1 (customtkinter.CTkFrame): Frame for selecting departure and arrival locations.
        from_optionemenu (customtkinter.CTkOptionMenu): Option menu for selecting departure location.
        to_optionemenu (customtkinter.CTkOptionMenu): Option menu for selecting arrival location.
        continue_button (customtkinter.CTkButton): Button to proceed with the selected locations.
        string_input_button (customtkinter.CTkButton): Button to return to the main window.
    """
    def __init__(self):
        """Initialize the Truck GUI."""
        super().__init__()
        self.title("Truck Home Page")
        self.geometry(f"{1100}x{340}")

        # Sidebar frame for appearance mode and UI scaling
        self.sidebar_frame = customtkinter.CTkFrame(self, width=120, corner_radius=15)
        self.sidebar_frame.grid(row=9, column=0, rowspan=4, sticky="nse")
        self.sidebar_frame.grid_rowconfigure(1, weight=1)
        
        # Appearance mode label and option menu
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode", anchor="center")
        self.appearance_mode_label.grid(row=5, column=0, padx=10, pady=(5,0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady =(10,10))

        # UI scaling label and option menu
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling", anchor="center")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10,0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["70%", "80%", "90%", "100%", "110%", "120%", "130%"],command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(5,20))

        # Set default values for appearance mode and UI scaling
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        # Logo and title frame
        self.sidebar_frame0 = customtkinter.CTkFrame(self, width=120,height=100, corner_radius=15) 
        self.sidebar_frame0.grid(row=0, column=15, rowspan=15, sticky = 'nsew')
        self.sidebar_frame0.grid_rowconfigure(8, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame0, text="Truck Booking Services", font=customtkinter.CTkFont(size=42, weight="bold"))
        self.logo_label.grid(row=0, column=15, padx=220, pady=50)

        # Departure and arrival locations frame
        self.sidebar_frame1=customtkinter.CTkFrame(self,width=200,height=100,corner_radius=15)
        self.sidebar_frame1.grid(row=15,column=15, padx=0, pady=5,sticky='nsew')

        # Departure location label and option menu
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="From",font=customtkinter.CTkFont(size=20),anchor="w")
        self.to_label.grid(row=15, column=10, padx=100, pady=(5,0),sticky='sw')
        self.from_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1,values=["Select","GWL", "BHP","MUM", "DLH"])
        self.from_optionemenu.grid(row=16, column=10, padx=60, pady=(5,5),sticky='sw')

        # Arrival location label and option menu
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="To",font=customtkinter.CTkFont(size=20), anchor="w")
        self.to_label.grid(row=15, column=20, padx=140, pady=(5,0),sticky='se')
        self.to_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1, values=["Select", "DLH","MUM","BHP","GWL"])
        self.to_optionemenu.grid(row=16, column=20, padx=80, pady=(5,5),sticky='se')

        # Continue button
        self.continue_button = customtkinter.CTkButton(self,text="Continue",command=self.end_e)
        self.continue_button.grid(row=150, column=15,rowspan=100, padx=20, pady=(10,10),sticky='se')

        # Home button
        self.string_input_button = customtkinter.CTkButton(self,text="Home", command=self.open_Main_window)
        self.string_input_button.grid(row=150, column=0, padx=20, pady=(10, 10),sticky='sw')


    def open_Main_window(self):
        """Open the main window."""
            self.destroy()            
            import StartPageGUI
            StartPageGUI.Main().mainloop()

    def end_e(self):
        """Function to handle the end of the app-GUI."""
        #function to end app-GUI
        global rawa
        global rawc
        global f1
        f1 = self.from_optionemenu.get()  #from value
        global f2
        f2 = self.to_optionemenu.get() #to value

        # Error handling for invalid location selection
        if f1=='-Select-' and f2=='-Select-':
            return messagebox.showerror('Error','Please select Departure & Arrival locations')
        elif f2=='-Select-':
            return messagebox.showerror("Error", "Select Arrival location")
        elif f1==f2:
            return messagebox.showerror("Error", "Invalid location entry!")
        elif f1=='-Select-':
            return messagebox.showerror('Error','Please select Departure location')
        
        else:
            # Query available trucks
            availableTRUCK=sql.Query_GetAvailableTruck(0, 0)
            sql.Query_WriteSearchResult(availableTRUCK)
            Number_of_vehicle = len(availableTRUCK)
            
            if Number_of_vehicle == 0:
                return messagebox.showerror("Error", "No Transport for this ")
            self.open_Info_window()
    
    def open_Info_window(self):
        """Open the information window to display available trucks."""
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
    app6 = Truck()
    app6.mainloop()
