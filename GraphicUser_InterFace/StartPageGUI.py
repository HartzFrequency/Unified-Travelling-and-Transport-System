import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk

window = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Home page")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        

        # self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Profile", font=customtkinter.CTkFont(size=35, weight="bold"))
        # self.logo_label.grid(row=0, column=0, padx=20, pady=20, sticky ="ew")
        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()
        # self.geometry("%dx%d" % (screen_width, screen_height))


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
        self.tabview.grid(row=8, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Travel")
        self.tabview.add("Transport")
    
        self.tabview.tab("Travel").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Transport").grid_columnconfigure(0, weight=1)

        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Travel"))
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        # self.label_tab_2 = customtkinter.CTkImage(Image.open("Image/ss11.png"), size=(26, 26))
    
        # self.label_tab_2 = customtkinter.CTkButton(master=window)
        # # self.label_tab_2.pack()

        # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Travel"), dynamic_resizing=True,
        #                                                 values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
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
        self.tabview.grid(row=10, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Feedback")
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Feedback"), text="Feedback Button",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=10, column=6, padx=20, pady=(10, 10))




    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Please enter your valuable Feedback :", title="CTkInputDialog")
        print("Feedback :", dialog.get_input())


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

   

    






if __name__ == "__main__":
    app = App()
    app.mainloop()
