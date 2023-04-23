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


window3 = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue") 


class Car(customtkinter.CTk):

    
    def __init__(self):
        super().__init__()
        self.title("Car Home Page")
        self.geometry(f"{1700}x{580}")


        #Appearance and Scaling 
        self.sidebar_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0)
        self.sidebar_frame.grid(row=35, column=0, rowspan=4, sticky="ew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10,0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                  command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady =(10,10), sticky ="ew")
        
        
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10,0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["70%", "80%", "90%", "100%", "110%", "120%", "130%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10,20), sticky ="ew")

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("110%")





         
        


# name of transport
        self.sidebar_frame0 = customtkinter.CTkFrame(self, width=100,height=30, corner_radius=0) 
        self.sidebar_frame0.grid(row=0, column=15, rowspan=10)
        self.sidebar_frame0.grid_rowconfigure(8, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame0, text="Car Booking Services", font=customtkinter.CTkFont(size=50, weight="bold"))
        self.logo_label.grid(row=0, column=15, padx=600, pady=50)



# # from button
        self.sidebar_frame1=customtkinter.CTkFrame(self,width=200,height=100)
        self.sidebar_frame1.grid(row=15,column=15,rowspan=25, padx=20, pady=10)
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="FROM",font=customtkinter.CTkFont(size=20),anchor="w")
        self.to_label.grid(row=15, column=15, padx=100, pady=10)
        self.from_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1,values=["-Select-","Muscat", "Mumbai", "Delhi",'Bangalore'])
        self.from_optionemenu.grid(row=16, column=15, padx=100, pady=10)

# # to button
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="TO",font=customtkinter.CTkFont(size=20), anchor="w")
        self.to_label.grid(row=15, column=19, padx=20, pady=(10,0))
        self.to_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1, values=["-Select-","Muscat", "Mumbai", "Delhi",'Bangalore'])
        self.to_optionemenu.grid(row=16, column=19, padx=100, pady=10)

# to select no. of adults travelling
        self.adult_label = customtkinter.CTkLabel(self.sidebar_frame1, text="Adults ",font=customtkinter.CTkFont(size=20) ,anchor="w")
        self.adult_label.grid(row=17, column=15, padx=100, pady=10)
        self.adult_optionemenu= tk.Spinbox(self.sidebar_frame1,from_=0, to=5, increment =1)
        self.adult_optionemenu.grid(row=18, column=15,padx=100, pady=10)

# to select no. of children travelling
        self.children_label = customtkinter.CTkLabel(self.sidebar_frame1, text="Childrens ", font=customtkinter.CTkFont(size=20),anchor="w")
        self.children_label.grid(row=17, column=19, padx=20, pady=(10,0))
        self.children_optionemenu= tk.Spinbox(self.sidebar_frame1,from_=0, to=5, increment =1)
        self.children_optionemenu.grid(row=18, column=19, padx=100, pady=10)





        # self.radiobutton_frame = customtkinter.CTkFrame(self,width=70,height=70)
        # self.radiobutton_frame.grid(row=15 , column=15,rowspan=50, padx=300, pady=50)
        # self.radio_var = tkinter.IntVar(value=0)


        # self.label_radio_group = customtkinter.CTkLabel(master=self.sidebar_frame1, text="Type of Seat",font=customtkinter.CTkFont(size=20))
        # self.label_radio_group.grid(row=20, column=16,)

        # self.radio_button_1 = customtkinter.CTkRadioButton(master=self.sidebar_frame1, text="Seater",variable=self.radio_var, value=0)
        # self.radio_button_1.grid(row=20, column=16, pady=10, padx=20)
        # self.radio_button_2 = customtkinter.CTkRadioButton(master=self.sidebar_frame1,text="Sleeper", variable=self.radio_var, value=1)
        # self.radio_button_2.grid(row=20, column=16, pady=10, padx=20)
        
        # self.radio_var = tkinter.IntVar(value=0)

    

    #     self.radiobutton_frame = customtkinter.CTkFrame(self)
    #     self.radiobutton_frame.grid(row=0 , column=18, padx=(20, 20), pady=(20, 10), sticky="nsew")

# method of travel
        # var=int
        # var1=int
        # selection=''
        # selection1=''
        # def sel1():
        #     global selection
        #     selection=str(var.get())
        #     print(selection) 
        
        # self.radio_var = tkinter.IntVar(value=1)

       
       
       
        # self.radiobutton_frame = customtkinter.CTkFrame(self,width=70,height=70)
        # self.radiobutton_frame.grid(row=25 , column=15,rowspan=50, padx=300, pady=50)
        # self.radio_var = tkinter.IntVar(value=0)

        # self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Type of Seat",font=customtkinter.CTkFont(size=20))
        # self.label_radio_group.grid(row=25, column=16,)

        # self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text="Seater",variable=self.radio_var, value=0)
        # self.radio_button_1.grid(row=26, column=16, pady=10, padx=20)
        # self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="Sleeper", variable=self.radio_var, value=1)
        # self.radio_button_2.grid(row=27, column=16, pady=10, padx=20)






# select class
        # def cls():
        #     global selection1
        #     selection1=str(var1.get())

        # self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="CLASS")
        # self.label_radio_group.grid(row=22, column=11, columnspan=1, padx=10, pady=10, sticky="")
        # self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text="Economy",variable=self.radio_var, value=0)
        # self.radio_button_3.grid(row=23, column=11, pady=10, padx=20, sticky="n")
        # self.radio_button_4 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="Business", variable=self.radio_var, value=1)
        # self.radio_button_4.grid(row=24, column=11, pady=10, padx=20, sticky="n")


# continue button
        self.continue_button = customtkinter.CTkButton(self,text="Continue",command=self.end_e)
        self.continue_button.grid(row=100, column=15,rowspan=100, padx=20, pady=(10,10))

   
   
# back button
        self.string_input_button = customtkinter.CTkButton(self,text="Back Button", command=self.open_Main_window)
        self.string_input_button.grid(row=1, column=0, padx=20, pady=(10, 10))


    
    def open_Main_window(self):
        self.destroy()            
        import StartPageGUI
        StartPageGUI.Main().mainloop()


        
        
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
        # elif selection=='':
        #     return messagebox.showerror("Error", "choose method of travel")
        # elif selection1=='':
        #     return messagebox.showerror("Error", "choose class of travel") 
        else:
            Query="SELECT CarID,Name,Duration,type,capacity,fare FROM car WHERE FromLocation='{}' AND ToLocation='{}'".format(f1,f2)
            cur.execute(Query)
            availableCAR=cur.fetchall()

            Car1_PNR=availableCAR[0][0]
            Car1_Name=availableCAR[0][1]
            Car1_dur=availableCAR[0][2]
            Car1_type=availableCAR[0][3]
            Car1_cap=availableCAR[0][4]       
            Car1_fare=availableCAR[0][5]

            Car2_ID=availableCAR[1][0]
            Car2_Name=availableCAR[1][1]
            Car2_dur=availableCAR[1][2]
            Car2_type=availableCAR[1][3]
            Car2_cap=availableCAR[1][4]
            Car2_fare=availableCAR[1][5]
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
    app3 = Car()
    app3.mainloop()
    
    
