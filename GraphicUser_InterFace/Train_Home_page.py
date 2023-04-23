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


window4 = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue") 


class Train(customtkinter.CTk):

    
    def __init__(self):
        super().__init__()
        self.title("Train Home Page")
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
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame0, text="Train Booking Services", font=customtkinter.CTkFont(size=50, weight="bold"))
        self.logo_label.grid(row=0, column=15, padx=600, pady=50)



# # from button
        self.sidebar_frame1=customtkinter.CTkFrame(self,width=200,height=100)
        self.sidebar_frame1.grid(row=15,column=15,rowspan=50, padx=20, pady=10)
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="FROM",font=customtkinter.CTkFont(size=20),anchor="w")
        self.to_label.grid(row=15, column=15, padx=100, pady=10)
        self.from_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1,values=["-Select-","GWL", "BHP","MUM", "DLH"])
        self.from_optionemenu.grid(row=16, column=15, padx=100, pady=10)

# # to button
        self.to_label = customtkinter.CTkLabel(self.sidebar_frame1, text="TO",font=customtkinter.CTkFont(size=20), anchor="w")
        self.to_label.grid(row=15, column=19, padx=20, pady=(10,0))
        self.to_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame1, values=["-Select-","GWL", "BHP","MUM", "DLH"])
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
            Train1_PNR = 0
            Train2_PNR = 0
            Query="SELECT PNR,Name,Duration,type,capacity,fare FROM train WHERE FromLocation='{}' AND ToLocation='{}'".format(f1,f2)
            cur.execute(Query)
            availableTRAIN=cur.fetchall()


            
            travel_vehicle = "Railway"
            os.environ['TRAVEL_VEHICLE'] = str(travel_vehicle)
            os.environ['F1'] = str(f1)
            os.environ['F2'] = str(f2)
            
            Number_of_train = len(availableTRAIN)
            print(Number_of_train)
            os.environ['NUMBER_OF_TRAIN'] = str(Number_of_train)
            if Number_of_train == 2:
               Train1_PNR=availableTRAIN[0][0]
               Train1_Name=availableTRAIN[0][1]
               Train1_dur=availableTRAIN[0][2]
               Train1_type=availableTRAIN[0][3]
               Train1_cap=availableTRAIN[0][4]       
               Train1_fare=availableTRAIN[0][5]
   
               os.environ['TRAIN1_PNR'] =  str(Train1_PNR)
               os.environ['TRAIN1_NAME']  = str(Train1_Name)
               os.environ['TRAIN1_DUR']  = str(Train1_dur)
               os.environ['TRAIN1_TYPE']  = str(Train1_type)
               os.environ['TRAIN1_CAP']  = str(Train1_cap)
               os.environ['TRAIN1_FARE']  = str(Train1_fare)
   
   
               Train2_PNR=availableTRAIN[1][0]
               Train2_Name=availableTRAIN[1][1]
               Train2_dur=availableTRAIN[1][2]
               Train2_type=availableTRAIN[1][3]
               Train2_cap=availableTRAIN[1][4]
               Train2_fare=availableTRAIN[1][5]
               
               os.environ['TRAIN2_PNR'] =  str(Train2_PNR)
               os.environ['TRAIN2_PNR'] =  str(Train2_PNR)
               os.environ['TRAIN2_NAME']  = str(Train2_Name)
               os.environ['TRAIN2_DUR']  = str(Train2_dur)
               os.environ['TRAIN2_TYPE']  = str(Train2_type)
               os.environ['TRAIN2_CAP']  = str(Train2_cap)
               os.environ['TRAIN2_FARE'] =  str(Train2_fare)
            elif Number_of_train == 1:
               Train1_PNR=availableTRAIN[0][0]
               Train1_Name=availableTRAIN[0][1]
               Train1_dur=availableTRAIN[0][2]
               Train1_type=availableTRAIN[0][3]
               Train1_cap=availableTRAIN[0][4]       
               Train1_fare=availableTRAIN[0][5]
   
               os.environ['TRAIN1_PNR'] =  str(Train1_PNR)
               os.environ['TRAIN1_NAME']  = str(Train1_Name)
               os.environ['TRAIN1_DUR']  = str(Train1_dur)
               os.environ['TRAIN1_TYPE']  = str(Train1_type)
               os.environ['TRAIN1_CAP']  = str(Train1_cap)
               os.environ['TRAIN1_FARE']  = str(Train1_fare)
            else:
                return messagebox.showerror("Error", "No trian for this Route ")

        
            self.open_Info_window()


    
    def open_Info_window(self):
        self.destroy()            
        import Train_Route_Info
        Train_Route_Info.Route().mainloop()


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
    
    
