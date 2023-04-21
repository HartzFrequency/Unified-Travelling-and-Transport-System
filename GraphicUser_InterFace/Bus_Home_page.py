import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage
from tkinter import messagebox



window2 = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue") 


class Bus(customtkinter.CTk):

    
    def __init__(self):
        super().__init__()
        self.title("Bus Home Page")
        self.geometry(f"{1700}x{580}")
        self.part1()
         
        
    def part1(self):    
        self.sidebar_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=12, rowspan=4, sticky="ew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0 , column=18, padx=(20, 20), pady=(20, 10), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)

# back button
        self.string_input_button = customtkinter.CTkButton(self,text="Back Button", command=self.open_Main_window)
        self.string_input_button.grid(row=10, column=0, padx=20, pady=(10, 10))

# name of transport
        self.sidebar_frame0 = customtkinter.CTkFrame(self, width=80, corner_radius=0) 
        self.sidebar_frame0.grid(row=0, column=2, rowspan=1, sticky="nsew")
        self.sidebar_frame0.grid_rowconfigure(1, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame0, text="Bus Booking Services", font=customtkinter.CTkFont(size=50, weight="bold"))
        self.logo_label.grid(row=0, column=2, padx=10, pady=(20, 10))

# textbox
        self.textbox = customtkinter.CTkTextbox(self, width=450)
        self.textbox.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew")
        self.textbox.insert("1.0", "About our services\n\n" + "This is s gui for flight booking system made under python sbmp..\n\n" * 20)
        # self.open_new_window()

# from button
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame, text="FROM", anchor="w")
        self.to_label.grid(row=5, column=2, padx=20, pady=(10,0))
        self.from_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,values=["-Select-","Muscat", "Mumbai", "Delhi",'Bangalore'])
        self.from_optionemenu.grid(row=5, column=2, padx=20, pady=(10,20), sticky ="ew")

# to button
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame, text="TO", anchor="w")
        self.to_label.grid(row=5, column=2, padx=20, pady=(10,0))
        self.to_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["-Select-","Muscat", "Mumbai", "Delhi",'Bangalore'])
        self.to_optionemenu.grid(row=5, column=2, padx=20, pady=(10,20), sticky ="ew")

# to select no. of adults travelling
        self.adult_label = customtkinter.CTkLabel(self.sidebar_frame, text="Adults ", anchor="w")
        self.adult_label.grid(row=5, column=2, padx=20, pady=(10,0))
        self.adult_optionemenu= tk.Spinbox(self.sidebar_frame,from_=0, to=5, increment =1)
        self.adult_optionemenu.grid(row=5, column=2, padx=25, pady=(10,20), sticky ="ew")

# to select no. of children travelling
        self.children_label = customtkinter.CTkLabel(self.sidebar_frame, text="Childrens ", anchor="w")
        self.children_label.grid(row=5, column=2, padx=20, pady=(10,0))
        self.children_optionemenu= tk.Spinbox(self.sidebar_frame,from_=0, to=5, increment =1)
        self.children_optionemenu.grid(row=5, column=2, padx=20, pady=(10,20), sticky ="ew")

# method of travel
        var=int
        var1=int
        selection=''
        selection1=''
        def sel1():
            global selection
            selection=str(var.get())
            print(selection) 

        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Method of Travel")
        self.label_radio_group.grid(row=19, column=11, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text="One1-way",variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=20, column=11, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="Round-trip", variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=21, column=11, pady=10, padx=20, sticky="n")

# select class
        def cls():
            global selection1
            selection1=str(var1.get())

        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="CLASS")
        self.label_radio_group.grid(row=22, column=11, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text="Economy",variable=self.radio_var, value=0)
        self.radio_button_3.grid(row=23, column=11, pady=10, padx=20, sticky="n")
        self.radio_button_4 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="Business", variable=self.radio_var, value=1)
        self.radio_button_4.grid(row=24, column=11, pady=10, padx=20, sticky="n")


# continue button
        self.continue_button = customtkinter.CTkButton(self,text="Continue",command=self.end_e, anchor="c")
        self.continue_button.grid(row=12, column=0, padx=20, pady=(10,10))

    def open_new_window(self):
        self.destroy()            
        import StartPageGUI
        StartPageGUI.Main().mainloop()



        # window3 = customtkinter.CTk()
        # customtkinter.set_appearance_mode("System")  
        # customtkinter.set_default_color_theme("blue")
        # window3.title("new win")
        # window3.geometry(f"{500}x{580}")
        # window3.mainloop()
        # self.part1()
        # # window3.destroy()
        
    def end_e(self):#function to end app-GUI
        global rawa
        global rawc
        f1= self.from_optionemenu.get()  #from value
        f2= self.to_optionemenu.get() #to value
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
        elif selection=='':
            return messagebox.showerror("Error", "choose method of travel")
        elif selection1=='':
            return messagebox.showerror("Error", "choose class of travel") 
        else:
            self.open_new_window()

    def open_Main_window(self):
            self.destroy()            
            import StartPageGUI
            StartPageGUI.Main().mainloop()

    def itenary():
        global flightname
        global origin
        global destination
        global departure
        global arrival
        global totalprice
        global f1
        global f2
        itenary=tk.Tk()
        itenary.title('Itenary')
        itenary.geometry('500x500')
        # flightname=flname1
        # totalprice=str(tprice1*2)


if __name__ == "__main__":
    app2 = Bus()
    app2.mainloop()
    
    
