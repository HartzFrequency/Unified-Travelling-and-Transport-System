import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage


window1 = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Home page")
        self.geometry(f"{1700}x{580}")
        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()
        # self.geometry("%dx%d" % (screen_width, screen_height))

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        

        # self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Profile", font=customtkinter.CTkFont(size=35, weight="bold"))
        # self.logo_label.grid(row=0, column=0, padx=20, pady=20, sticky ="ew")


        self.sidebar_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0)
        self.sidebar_frame.grid(row=9, column=0, rowspan=4, sticky="ew")
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


        
        
        self.upper_name_frame = customtkinter.CTkFrame(self, width=140, corner_radius=5)
        self.upper_name_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
        self.upper_name_frame.grid_rowconfigure(6, weight=1)
        
        self.project_name = customtkinter.CTkLabel(self.upper_name_frame, text="Unified Traveling and Transportation System (UTTS)", font=customtkinter.CTkFont(size=50, weight="bold"))
        self.project_name.grid(row=0, column=2, padx=200, pady=50)



        
      
        
        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=500, height= 250)
        self.tabview.grid(row=8, column=2, padx=(20, 0), pady=(20, 0))
        self.tabview.add("Travel")
        self.tabview.add("Transport")
    
        self.tabview.tab("Travel").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Transport").grid_columnconfigure(0, weight=1)

        # self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Travel"))
        # self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        
        self.Bus_button = customtkinter.CTkButton(self.tabview.tab("Travel"), text="Bus",command=self.open_Bus_window)
        self.Bus_button.grid(row=4, column=0, padx=20, pady=(10, 10))

        self.Car_button = customtkinter.CTkButton(self.tabview.tab("Travel"), text="Car",command=self.open_Car_window)
        self.Car_button.grid(row=4, column=1, padx=20, pady=(10, 10))

        self.Train_button = customtkinter.CTkButton(self.tabview.tab("Travel"), text="Train",command=self.open_Train_window)
        self.Train_button.grid(row=4, column=2, padx=20, pady=(10, 10))

        self.Airplane_button = customtkinter.CTkButton(self.tabview.tab("Travel"), text="Airplane",command=self.open_Airplane_window)
        self.Airplane_button.grid(row=4, column=3, padx=20, pady=(10, 10))


        
        
        
        
        
        
        # image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Images")

        # self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "BUS.png")),
        #                                              dark_image=Image.open(os.path.join(image_path, "BUS.png")), size=(20, 20))
        
        



        # self.bus_image = customtkinter.CTkLabel(self.label_tab_2)
        # self.image = customtkinter.CTkImage("Image/BUS.png")
        # self.bus_image.configure(image = self.image)
        # self.bus_image.pack()
        # self.tabview.add(self.label_tab_2)
        # self.tabview.pack()

        
        
        
        
        
        
        
        
        
        
        
        
        # image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Image")

        # self.bus_image = customtkinter.CTkImage(Image.open(os.path.join(image_path,"BUS.png")),size=(30,30))


        # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Travel"), dynamic_resizing=True,
        #                                                 values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))


        # bus_image = self.label_tab_2()
        # photo = self.PhotoImage(file = "Image/BUS.jpg")
        # bus_image.config(image = photo)
        # bus_image.pack()


        # # self.label_tab_2 = customtkinter.CTkImage(Image.open("Image/ss11.png"), size=(26, 26))
    
        # self.label_tab_2 = customtkinter.CTkButton(master=window)
        # # self.label_tab_2.pack()
        # self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Travel"),
        #                                             values=["Value 1", "Value 2", "Value Long....."])
        # self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.label_tab_3 = customtkinter.CTkLabel(self.tabview.tab("Transport"))
        self.label_tab_3.grid(row=0, column=0, padx=20, pady=20)
        

        # self.lower_frame = customtkinter.CTkFrame(self, width=140, corner_radius=5)
        # self.lower_frame.grid(row=4, column=10, rowspan=4, sticky="nsew")
        # self.lower_frame.grid_rowconfigure(4, weight=0)
        
        # self.transport_name = customtkinter.CTkLabel(self.lower_frame, text="Hellllllllllllo", font=customtkinter.CTkFont(size=50, weight="bold"))
        # self.transport_name.grid(row=0, column=0, padx=200, pady=(50, 10))
    

        self.tabview = customtkinter.CTkTabview(self, width=250, height= 100)
        self.tabview.grid(row=10, column=2, padx=(20, 0), pady=(20, 0))
        self.tabview.add("Feedback")

        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Feedback"), text="Feedback Button",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=10, column=19, padx=20, pady=(10, 10), sticky="ew")
        self.string_input_button.pack(side="bottom", anchor="center")




    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Please enter your valuable Feedback :", title="Feedback Window")
        print("Feedback :", dialog.get_input())


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)



    def open_Bus_window(self):
        self.destroy()            
        import Bus_Home_page
        Bus_Home_page.Bus().mainloop()

    def open_Car_window(self):
        self.destroy()            
        import Car_Home_page
        Car_Home_page.Car().mainloop()

    def open_Train_window(self):
        self.destroy()            
        import Train_Home_page
        Train_Home_page.Train().mainloop()

    def open_Airplane_window(self):
        self.destroy()            
        import Airplane_Home_page
        Airplane_Home_page.Airplane().mainloop()


        
        


if __name__ == "__main__":
    app1 = Main()
    app1.mainloop()

    