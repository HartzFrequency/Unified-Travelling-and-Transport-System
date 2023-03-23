import tkinter
import tkinter.messagebox
import customtkinter


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Home page")
        self.geometry(f"{1100}x{580}")

        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()
        # self.geometry("%dx%d" % (screen_width, screen_height))


        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Profile", font=customtkinter.CTkFont(size=35, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=20, pady=(20, 10))
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(700, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                  command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        
        
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        
        
        # self.upper_name_frame = customtkinter.CTkFrame(self, width=140, corner_radius=5)
        # self.upper_name_frame.grid(row=0, column=10, rowspan=4, sticky="nsew")
        # self.upper_name_frame.grid_rowconfigure(6, weight=1)
        
        # self.project_name = customtkinter.CTkLabel(self.upper_name_frame, text="Unified Traveling and Transportation System (UTTS)", font=customtkinter.CTkFont(size=50, weight="bold"))
        # self.project_name.grid(row=0, column=0, padx=200, pady=(50, 10))
        

        # self.lower_frame = customtkinter.CTkFrame(self, width=140, corner_radius=5)
        # self.lower_frame.grid(row=4, column=10, rowspan=4, sticky="nsew")
        # self.lower_frame.grid_rowconfigure(4, weight=0)
        
        # self.transport_name = customtkinter.CTkLabel(self.lower_frame, text="Hellllllllllllo", font=customtkinter.CTkFont(size=50, weight="bold"))
        # self.transport_name.grid(row=0, column=0, padx=200, pady=(50, 10))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

   

    






if __name__ == "__main__":
    app = App()
    app.mainloop()
