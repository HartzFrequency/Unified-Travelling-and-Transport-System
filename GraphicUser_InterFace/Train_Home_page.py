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
    password='harsh',
    database='UTTS')
cur=UTTSdb.cursor()


window4 = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("green") 


class Train(customtkinter.CTk):

    
    def __init__(self):
        super().__init__()
        self.title("Train Home Page")
        self.geometry(f"{1054}x{360}")


        self.sidebar_frame = customtkinter.CTkFrame(self, width=120, corner_radius=15)
        self.sidebar_frame.grid(row=9, column=0, rowspan=4, sticky="nse")
        self.sidebar_frame.grid_rowconfigure(1, weight=1)
        
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="center")
        self.appearance_mode_label.grid(row=5, column=0, padx=10, pady=(5,0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady =(10,10))
        
        
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="center")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10,0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["70%", "80%", "90%", "100%", "110%", "120%", "130%"],command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10,20), sticky ="ew")

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        self.sidebar_frame0 = customtkinter.CTkFrame(self, width=120,height=100, corner_radius=15) 
        self.sidebar_frame0.grid(row=0, column=15, rowspan=15,sticky='nsew')
        self.sidebar_frame0.grid_rowconfigure(8, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame0, text="Train Booking Services", font=customtkinter.CTkFont(size=42, weight="bold"))
        self.logo_label.grid(row=0, column=15, padx=220, pady=50)


        self.sidebar_frame1=customtkinter.CTkFrame(self,width=200,height=100,corner_radius=15)
        self.sidebar_frame1.grid(row=15,column=15, padx=0, pady=5,sticky='nsew')

        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="From",font=customtkinter.CTkFont(size=20),anchor="w")
        self.to_label.grid(row=15, column=10, padx=100, pady=(5,0),sticky='sw')

        self.from_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1,values=["Select","GWL", "BHP","MUM", "DLH"])
        self.from_optionemenu.grid(row=16, column=10, padx=60, pady=(5,5),sticky='sw')
        
        self.adult_label = customtkinter.CTkLabel(self.sidebar_frame1, text="Adults ",font=customtkinter.CTkFont(size=20) ,anchor="w")
        self.adult_label.grid(row=17, column=10, padx=100, pady=(5,0),sticky='sw')
        
        self.adult_optionemenu= tk.Spinbox(self.sidebar_frame1,from_=0, to=5, increment =1)
        self.adult_optionemenu.grid(row=18, column=10,padx=75, pady=(5,5),sticky='sw')

        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="To",font=customtkinter.CTkFont(size=20), anchor="w")
        self.to_label.grid(row=15, column=20, padx=140, pady=(5,0),sticky='se')

        self.to_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1, values=["Select","GWL", "BHP","MUM", "DLH"])
        self.to_optionemenu.grid(row=16, column=20, padx=80, pady=(5,5),sticky='se')

        self.children_label = customtkinter.CTkLabel(self.sidebar_frame1, text="Childrens ", font=customtkinter.CTkFont(size=20),anchor="w")
        self.children_label.grid(row=17, column=20, padx=100, pady=(5,0),sticky='se')
        
        self.children_optionemenu= tk.Spinbox(self.sidebar_frame1,from_=0, to=5, increment =1)
        self.children_optionemenu.grid(row=18, column=20, padx=100, pady=(5,5),sticky='se')

#continue button
        self.continue_button = customtkinter.CTkButton(self,text="Continue",command=self.end_e)
        self.continue_button.grid(row=150, column=15,rowspan=100, padx=20, pady=(10,10),sticky='se')
# back button
        self.string_input_button = customtkinter.CTkButton(self,text="Home", command=self.open_Main_window)
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
        # elif selection=='':
        #     return messagebox.showerror("Error", "choose method of travel")
        # elif selection1=='':
        #     return messagebox.showerror("Error", "choose class of travel") 
        else:
            # Train1_PNR = 0
            # Train2_PNR = 0
            Query="SELECT PNR,Name,Duration,type,capacity,fare FROM train WHERE FromLocation='{}' AND ToLocation='{}'".format(f1,f2)
            cur.execute(Query)
            availableTRAIN=cur.fetchall()


            
            travel_vehicle = "Railway"
            os.environ['TRAVEL_VEHICLE'] = str(travel_vehicle)
            os.environ['F1'] = str(f1)
            os.environ['F2'] = str(f2)
            os.environ['RAWA'] = str(rawa)
            os.environ['RAWC'] = str(rawc)
            
            Number_of_vehicle = len(availableTRAIN)
            # print(Number_of_train)
            os.environ['NUMBER_OF_VEHICLE'] = str(Number_of_vehicle)
            if Number_of_vehicle == 2:
               Train1_PNR=availableTRAIN[0][0]
               Train1_Name=availableTRAIN[0][1]
               Train1_dur=availableTRAIN[0][2]
               Train1_type=availableTRAIN[0][3]
               Train1_cap=availableTRAIN[0][4]       
               Train1_fare=availableTRAIN[0][5]
   
               os.environ['VEHICLE1_ID'] =  str(Train1_PNR)
               os.environ['VEHICLE1_NAME']  = str(Train1_Name)
               os.environ['VEHICLE1_DUR']  = str(Train1_dur)
               os.environ['VEHICLE1_TYPE']  = str(Train1_type)
               os.environ['VEHICLE1_CAP']  = str(Train1_cap)
               os.environ['VEHICLE1_FARE']  = str(Train1_fare)
   
   
               Train2_PNR=availableTRAIN[1][0]
               Train2_Name=availableTRAIN[1][1]
               Train2_dur=availableTRAIN[1][2]
               Train2_type=availableTRAIN[1][3]
               Train2_cap=availableTRAIN[1][4]
               Train2_fare=availableTRAIN[1][5]
               
               os.environ['VEHICLE2_ID'] =  str(Train2_PNR)
               os.environ['VEHICLE2_PNR'] =  str(Train2_PNR)
               os.environ['VEHICLE2_NAME']  = str(Train2_Name)
               os.environ['VEHICLE2_DUR']  = str(Train2_dur)
               os.environ['VEHICLE2_TYPE']  = str(Train2_type)
               os.environ['VEHICLE2_CAP']  = str(Train2_cap)
               os.environ['VEHICLE2_FARE'] =  str(Train2_fare)
            elif Number_of_vehicle == 1:
               Train1_PNR=availableTRAIN[0][0]
               Train1_Name=availableTRAIN[0][1]
               Train1_dur=availableTRAIN[0][2]
               Train1_type=availableTRAIN[0][3]
               Train1_cap=availableTRAIN[0][4]       
               Train1_fare=availableTRAIN[0][5]
   
               os.environ['VEHICLE1_ID'] =  str(Train1_PNR)
               os.environ['VEHICLE1_NAME']  = str(Train1_Name)
               os.environ['VEHICLE1_DUR']  = str(Train1_dur)
               os.environ['VEHICLE1_TYPE']  = str(Train1_type)
               os.environ['VEHICLE1_CAP']  = str(Train1_cap)
               os.environ['VEHICLE1_FARE']  = str(Train1_fare)
            else:
                return messagebox.showerror("Error", "No trian for this Route ")

        
            self.open_Info_window()


    
    def open_Info_window(self):
        self.destroy()            
        import Route_Info
        Route_Info.Route().mainloop()


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)



    # def itenary():
    #     global flightname
    #     global origin
    #     global destination
    #     global departure
    #     global arrival
    #     global totalprice
    #     global f1
    #     global f2
    #     itenary=tk.Tk()
    #     itenary.title('Itenary')
    #     itenary.geometry('500x500')
    #     # flightname=flname1
    #     # totalprice=str(tprice1*2)


if __name__ == "__main__":
    app4 = Train()
    app4.mainloop()
    
    
