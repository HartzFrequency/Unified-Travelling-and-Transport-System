import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage
from tkinter import messagebox
import mysql.connector
import Modules.SQL as sql

# Create a custom tkinter window
window5 = customtkinter.CTk()
# Set appearance mode to system theme
customtkinter.set_appearance_mode("System")  
# Set default color theme to blue
customtkinter.set_default_color_theme("blue") 

class Airplane(customtkinter.CTk):
    """
    Class representing the Airplane Home Page GUI.

    Attributes:
        sidebar_frame: Frame for appearance mode and UI scaling options.
        appearance_mode_label: Label for appearance mode option.
        appearance_mode_optionemenu: Option menu for appearance mode.
        scaling_label: Label for UI scaling option.
        scaling_optionemenu: Option menu for UI scaling.
        sidebar_frame0: Frame for the name of the transport.
        sidebar_frame1: Frame for input options such as From, To, Adults, and Children.
        continue_button: Button to continue with the selection.
        string_input_button: Button to return to the main window.
    """
    
    def __init__(self):
        """Initialize the Airplane Home Page GUI."""
        super().__init__()
        self.title("Airplane Home Page")
        self.geometry(f"{1098}x{360}")

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

        # Frame for the name of the transport
        self.sidebar_frame0 = customtkinter.CTkFrame(self, width=120,height=100, corner_radius=15) 
        self.sidebar_frame0.grid(row=0, column=15, rowspan=15, sticky = 'nsew')
        self.sidebar_frame0.grid_rowconfigure(8, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame0, text="Airplane Booking Services", font=customtkinter.CTkFont(size=42, weight="bold"))
        self.logo_label.grid(row=0, column=15, padx=220, pady=50)

        # Frame for input options
        self.sidebar_frame1=customtkinter.CTkFrame(self,width=200,height=100,corner_radius=15)
        self.sidebar_frame1.grid(row=15,column=15, padx=0, pady=5,sticky='nsew')

        
        # Widgets for input options: From, To, Adults, Children
        #FROM TEXT
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="From",font=customtkinter.CTkFont(size=20),anchor="w")
        self.to_label.grid(row=15, column=10, padx=100, pady=(5,0),sticky='sw')
        
        #DROP DOWN MENU FOR 
        self.from_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1,values=["Select","CDG", "DEL","BOM", "LHR","PEK","ATL","SYD","FRA"])
        self.from_optionemenu.grid(row=16, column=10, padx=60, pady=(5,5),sticky='sw')
        
        #ADULT TEXT
        self.adult_label = customtkinter.CTkLabel(self.sidebar_frame1, text="Adults ",font=customtkinter.CTkFont(size=20) ,anchor="w")
        self.adult_label.grid(row=17, column=10, padx=100, pady=(5,0),sticky='sw')
        
        #VALUE SELECTOR 
        self.adult_optionemenu= tk.Spinbox(self.sidebar_frame1,from_=0, to=5, increment =1)
        self.adult_optionemenu.grid(row=18, column=10,padx=75, pady=(5,5),sticky='sw')

        
        #TO TEXT
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="To",font=customtkinter.CTkFont(size=20), anchor="w")
        self.to_label.grid(row=15, column=20, padx=140, pady=(5,0),sticky='se')
        
        #DROP DOWN MENU FOR TO
        self.to_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1, values=["Select", "ORD","HND","LHR","DXB","JFK","SFO","LAX","CDG"])
        self.to_optionemenu.grid(row=16, column=20, padx=80, pady=(5,5),sticky='se')
        
        #CHILDREN TEXT
        self.children_label = customtkinter.CTkLabel(self.sidebar_frame1, text="Childrens ", font=customtkinter.CTkFont(size=20),anchor="w")
        self.children_label.grid(row=17, column=20, padx=100, pady=(5,0),sticky='se')
        
        #VALUE SELECTOR
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
        # Input validation and further actions
        #function to end app-GUI
        global rawa
        global rawc
        global f1
        f1 = self.from_optionemenu.get()  #From value
        global f2
        f2 = self.to_optionemenu.get() #To value
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
            return messagebox.showerror("Error", "choose no. of passengers")
        else:
            availableFLIGHT=sql.Query_GetAvailableFlight(f1, f2)
            sql.Query_WriteSearchResult(availableFLIGHT)
            # vehicle availability check
            Number_of_vehicle = len(availableFLIGHT)
            if Number_of_vehicle == 0:
                return messagebox.showerror("Error", "No Flight for this Route")
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
            new_scaling (str): The new UI scaling factor.

        Returns:
            None
        """
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

# Run the application if executed as the main script
if __name__ == "__main__":
    app5 = Airplane()
    app5.mainloop()
