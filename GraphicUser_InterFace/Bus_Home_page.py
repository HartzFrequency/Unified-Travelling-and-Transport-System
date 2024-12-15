import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import mysql.connector
import Modules.SQL as sql


# Create a custom tkinter window
window2 = customtkinter.CTk()
# Set appearance mode to system theme
customtkinter.set_appearance_mode("System") 
# Set default color theme to blue
customtkinter.set_default_color_theme("blue") 


class Bus(customtkinter.CTk):
     """
Class representing the Bus Home Page GUI.

This class creates a graphical user interface for booking bus services. It includes
options to select departure and arrival locations, specify the number of adults and children,
and navigate to other parts of the application.

Attributes:
    sidebar_frame: CTkFrame for appearance mode and UI scaling options.
    appearance_mode_label: CTkLabel for appearance mode option.
    appearance_mode_optionemenu: CTkOptionMenu for appearance mode.
    scaling_label: CTkLabel for UI scaling option.
    scaling_optionemenu: CTkOptionMenu for UI scaling.
    sidebar_frame0: CTkFrame for the name of the transport.
    logo_label: CTkLabel for displaying the logo and name of the service.
    sidebar_frame1: CTkFrame for input options such as From, To, Adults, and Children.
    from_label: CTkLabel for the "From" text.
    from_optionemenu: CTkOptionMenu for selecting departure location.
    adult_label: CTkLabel for the "Adults" text.
    adult_optionemenu: Spinbox for selecting the number of adults.
    to_label: CTkLabel for the "To" text.
    to_optionemenu: CTkOptionMenu for selecting arrival location.
    children_label: CTkLabel for the "Children" text.
    children_optionemenu: Spinbox for selecting the number of children.
    continue_button: CTkButton to continue with the selection and search for available buses.
    string_input_button: CTkButton to return to the main window.

Methods:
    open_Main_window(): Opens the main window of the application.
    end_e(): Validates user input and checks for available buses based on the selected options.
    open_Info_window(): Opens the window displaying available buses.
    change_appearance_mode_event(new_appearance_mode: str): Changes the appearance mode of the application.
    change_scaling_event(new_scaling: str): Changes the UI scaling of the application.
"""
    
    def __init__(self):
        """Initialize the Bus Home Page GUI."""
        super().__init__()
        self.title("Bus Home Page")
        self.geometry(f"{1024}x{360}")
        
        # Sidebar frame for appearance mode and UI scaling options
        self.sidebar_frame = customtkinter.CTkFrame(self, width=120, corner_radius=15)
        self.sidebar_frame.grid(row=9, column=0, rowspan=4, sticky="nse")
        self.sidebar_frame.grid_rowconfigure(1, weight=1)
        
        # Label and option menu for appearance mode
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode", anchor="center")
        self.appearance_mode_label.grid(row=5, column=0, padx=10, pady=(5,0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady =(10,10))
        
        # Label and option menu for UI scaling
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling", anchor="center")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10,0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["70%", "80%", "90%", "100%", "110%", "120%", "130%"],command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(5,20))

        # Set default values for appearance mode and scaling
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        #SIDE BAR FIRST
        # Frame for the name of the transport
        self.sidebar_frame0 = customtkinter.CTkFrame(self, width=120,height=100, corner_radius=15) 
        self.sidebar_frame0.grid(row=0, column=15, rowspan=15,sticky='nsew')
        self.sidebar_frame0.grid_rowconfigure(8, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame0, text="Bus Booking Services", font=customtkinter.CTkFont(size=42, weight="bold"))
        self.logo_label.grid(row=0, column=15, padx=220, pady=50)

        # Frame for input options
        self.sidebar_frame1=customtkinter.CTkFrame(self,width=200,height=100,corner_radius=15)
        self.sidebar_frame1.grid(row=15,column=15, padx=0, pady=5,sticky='nsew')

        # Widgets for input options: From, To, Adults, Children
        # From label
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="From",font=customtkinter.CTkFont(size=20),anchor="w")
        self.to_label.grid(row=15, column=10, padx=100, pady=(5,0),sticky='sw')
        # From drop down option menu
        self.from_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1,values=["Select","GWL", "BHP","MUM", "DLH"])
        self.from_optionemenu.grid(row=16, column=10, padx=75, pady=(5,5),sticky='sw')
        # Adults label
        self.adult_label = customtkinter.CTkLabel(self.sidebar_frame1, text="Adults ",font=customtkinter.CTkFont(size=20) ,anchor="w")
        self.adult_label.grid(row=17, column=10, padx=100, pady=(5,0),sticky='sw')
        # Value selector 
        self.adult_optionemenu= tk.Spinbox(self.sidebar_frame1,from_=0, to=5, increment =1)
        self.adult_optionemenu.grid(row=18, column=10,padx=95, pady=(5,5),sticky='sw')


        # To label
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="To",font=customtkinter.CTkFont(size=20), anchor="w")
        self.to_label.grid(row=15, column=20, padx=140, pady=(5,0),sticky='se')
        # To drop down option menu
        self.to_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1, values=["Select", "DLH","MUM","BHP","GWL"])
        self.to_optionemenu.grid(row=16, column=20, padx=80, pady=(5,5),sticky='se')
        # Children label
        self.children_label = customtkinter.CTkLabel(self.sidebar_frame1, text="Childrens ", font=customtkinter.CTkFont(size=20),anchor="w")
        self.children_label.grid(row=17, column=20, padx=100, pady=(5,0),sticky='se')
        # Value selector
        self.children_optionemenu= tk.Spinbox(self.sidebar_frame1,from_=0, to=5, increment =1)
        self.children_optionemenu.grid(row=18, column=20, padx=100, pady=(5,5),sticky='se')

        # Continue button
        self.continue_button = customtkinter.CTkButton(self,text="Continue",command=self.end_e)
        self.continue_button.grid(row=150, column=15,rowspan=100, padx=20, pady=(10,10),sticky='se')   
        # Back button
        self.string_input_button = customtkinter.CTkButton(self,text="Home", command=self.open_Main_window)
        self.string_input_button.grid(row=150, column=0, padx=20, pady=(10, 10),sticky='sw')


    
    def open_Main_window(self):
        """Open the main window."""
        self.destroy()            
        import StartPageGUI
        StartPageGUI.Main().mainloop()

    def end_e(self):
        """
        End the application GUI and perform input validation.

        Returns:
            None
        """
        
        global rawa
        global rawc
        global f1
        f1= self.from_optionemenu.get() # From value
        
        global f2
        f2= self.to_optionemenu.get() # To value

        a = self.adult_optionemenu.get()
        rawa=a
        b= self.children_optionemenu.get()
        rawc=b
        if f1=='-Select-' and f2=='-Select-':
            return messagebox.showerror('Error','Please select Departure & Arrival locations')
        elif f2=='-Select-':
            return messagebox.showerror("Error", "Select Arrival location")
        elif f1==f2:
            return messagebox.showerror("Error", "Invalid location entry!")
        elif f1=='-Select-':
            return messagebox.showerror('Error','Please select Departure location')
        elif rawa=='0' and rawc=='0':
            return messagebox.showerror("Error", "choose no of passengers")
        else:
            availableBUS=sql.Query_GetAvailableBus(f1, f2) 
            sql.Query_WriteSearchResult(availableBUS)
            
            Number_of_vehicle = len(availableBUS)
            if Number_of_vehicle == 0:
                return messagebox.showerror("Error", "No Bus for this Route ")
            self.open_Info_window()

    def open_Info_window(self):
        """Open the info window."""
        self.destroy()        
        import Display_availability    
        Display_availability.Available().mainloop()
       
    def change_appearance_mode_event(self, new_appearance_mode: str):
        """
        Change the appearance mode.

        Args:
            new_appearance_mode (str): The new appearance mode.

        Returns:
            None
        """
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        """
    Change the UI scaling.

    Args:
        new_scaling (str): The new UI scaling percentage as a string (e.g., "100%").

    Returns:
        None
    """
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app2 = Bus()
    app2.mainloop()
    
    
