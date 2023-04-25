import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage
from tkinter import messagebox
import mysql.connector

UTTSdb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Rajput@MySQL',
    database='UTTS')
cur=UTTSdb.cursor()



window6 = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue") 

class Railway(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Truck Home Page")
        self.geometry(f"{1100}x{340}")

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

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

# name of transport
        self.sidebar_frame0 = customtkinter.CTkFrame(self, width=120,height=100, corner_radius=15) 
        self.sidebar_frame0.grid(row=0, column=15, rowspan=15, sticky = 'nsew')
        self.sidebar_frame0.grid_rowconfigure(8, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame0, text="Railway Booking Services", font=customtkinter.CTkFont(size=42, weight="bold"))
        self.logo_label.grid(row=0, column=15, padx=220, pady=50)



 
        self.sidebar_frame1=customtkinter.CTkFrame(self,width=200,height=100,corner_radius=15)
        self.sidebar_frame1.grid(row=15,column=15, padx=0, pady=5,sticky='nsew')

#FROM TEXT
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="From",font=customtkinter.CTkFont(size=20),anchor="w")
        self.to_label.grid(row=15, column=10, padx=100, pady=(5,0),sticky='sw')
#DROP DOWN MENU FOR 
        self.from_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1,values=["Select","GWL", "BHP","MUM", "DLH"])
        self.from_optionemenu.grid(row=16, column=10, padx=60, pady=(5,5),sticky='sw')




#TO TEXT
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="To",font=customtkinter.CTkFont(size=20), anchor="w")
        self.to_label.grid(row=15, column=20, padx=140, pady=(5,0),sticky='se')
#DROP DOWN MENU FOR TO
        self.to_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1, values=["Select", "DLH","MUM","BHP","GWL"])
        self.to_optionemenu.grid(row=16, column=20, padx=80, pady=(5,5),sticky='se')

#COMTINUE
        self.continue_button = customtkinter.CTkButton(self,text="Continue",command=self.end_e)
        self.continue_button.grid(row=150, column=15,rowspan=100, padx=20, pady=(10,10),sticky='se')

#BACK BUTTON 
        self.string_input_button = customtkinter.CTkButton(self,text="Back Button", command=self.open_Main_window)
        self.string_input_button.grid(row=150, column=0, padx=20, pady=(10, 10),sticky='sw')


    def open_Main_window(self):
            self.destroy()            
            import StartPageGUI
            StartPageGUI.Main().mainloop()

    def end_e(self):#function to end app-GUI
        global rawa
        global rawc
        global f1
        f1 = self.from_optionemenu.get()  #from value
        global f2
        f2 = self.to_optionemenu.get() #to value
        # a = self.adult_optionemenu.get()
        # rawa=a
        # b= self.children_optionemenu.get()
        # rawc=b
        if f1=='-Select-' and f2=='-Select-':
            return messagebox.showerror('Error','Please select Departure & Arrival locations')
        elif f2=='-Select-':
            return messagebox.showerror("Error", "Select Arrival location")
        elif f1==f2:
            return messagebox.showerror("Error", "Invalid location entry!")
        elif f1=='-Select-':
            return messagebox.showerror('Error','Please select Departure location')
        # elif rawa=='0' and rawc=='0':
        #     return messagebox.showerror("Error", "choose no. of passengers")
        # elif selection=='':
        #     return messagebox.showerror("Error", "choose method of travel")
        # elif selection1=='':
        #     return messagebox.showerror("Error", "choose class of travel") 
        else:
            Query="SELECT truckNo,Name,fare,time FROM trucks WHERE fare = '500'"
            cur.execute(Query)
            availableTRUCK=cur.fetchall()

          
            travel_vehicle = "Truck"
            os.environ['TRAVEL_VEHICLE'] = str(travel_vehicle)
            os.environ['F1'] = str(f1)
            os.environ['F2'] = str(f2)
            # os.environ['RAWA'] = str(rawa)
            # os.environ['RAWC'] = str(rawc)

            
            Number_of_vehicle = len(availableTRUCK)
            
            os.environ['NUMBER_OF_VEHICLE'] = str(Number_of_vehicle)
            if Number_of_vehicle == 2:
               truck1_ID=availableTRUCK[0][0]
               truck1_Name=availableTRUCK[0][1]
               truck1_fare=availableTRUCK[0][2]
               truck1_dur=availableTRUCK[0][3]
            #    truck1_type=availableTRUCK[0][3]
            #    truck1_cap=availableTRUCK[0][4]       
               
               os.environ['VEHICLE1_ID'] = str(truck1_ID)
               os.environ['VEHICLE1_NAME'] = str(truck1_Name)
               os.environ['VEHICLE1_DUR'] = str(truck1_dur)
            #    os.environ['VEHICLE1_TYPE'] = str(truck1_type)
            #    os.environ['VEHICLE1_CAP'] = str(truck1_cap)
               os.environ['VEHICLE1_FARE'] = str(truck1_fare)


               truck2_ID=availableTRUCK[1][0]
               truck2_Name=availableTRUCK[1][1]
               truck2_fare=availableTRUCK[1][2]
               truck2_dur=availableTRUCK[1][3]
            #    truck2_type=availableTRUCK[1][3]
            #    truck2_cap=availableTRUCK[1][4]
               os.environ['VEHICLE2_ID'] = str(truck2_ID)
               os.environ['VEHICLE2_NAME'] = str(truck2_Name)
               os.environ['VEHICLE2_DUR'] = str(truck2_dur)
            #    os.environ['VEHICLE2_TYPE'] = str(truck2_type)
            #    os.environ['VEHICLE2_CAP'] = str(truck2_cap)
               os.environ['VEHICLE2_FARE'] = str(truck2_fare)
            elif Number_of_vehicle == 1:
               truck1_ID=availableTRUCK[0][0]
               truck1_Name=availableTRUCK[0][1]
               truck1_fare=availableTRUCK[0][2]
               truck1_dur=availableTRUCK[0][3]
            #    truck1_type=availableTRUCK[0][3]
            #    truck1_cap=availableTRUCK[0][4]       
            
               os.environ['VEHICLE1_ID'] = str(truck1_ID)
               os.environ['VEHICLE1_NAME'] = str(truck1_Name)
               os.environ['VEHICLE1_DUR'] = str(truck1_dur)
            #    os.environ['VEHICLE1_TYPE'] = str(truck1_type)
            #    os.environ['VEHICLE1_CAP'] = str(truck1_cap)
               os.environ['VEHICLE1_FARE'] = str(truck1_fare)

            else:
                return messagebox.showerror("Error", "No Truck for this Route ")
            self.open_Info_window()

    
    def open_Info_window(self):
        self.destroy()            
        import Transport_Route_Info
        Transport_Route_Info.Route().mainloop()


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)




if __name__ == "__main__":
    app6 = Truck()
    app6.mainloop()
