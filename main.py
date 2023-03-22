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


        self.upper_name_frame = customtkinter.CTkFrame(self, width=140, corner_radius=5)
        self.upper_name_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.upper_name_frame.grid_rowconfigure(4, weight=0)
        
        self.project_name = customtkinter.CTkLabel(self.upper_name_frame, text="Unified Traveling and Transportation System (UTTS)", font=customtkinter.CTkFont(size=50, weight="bold"))
        self.project_name.grid(row=0, column=0, padx=200, pady=(50, 10))
        

        self.lower_frame = customtkinter.CTkFrame(self, width=140, corner_radius=5)
        self.lower_frame.grid(row=4, column=0, rowspan=4, sticky="nsew")
        self.lower_frame.grid_rowconfigure(4, weight=0)
        
        self.transport_name = customtkinter.CTkLabel(self.lower_frame, text="Hellllllllllllo", font=customtkinter.CTkFont(size=50, weight="bold"))
        self.transport_name.grid(row=0, column=0, padx=200, pady=(50, 10))

    






if __name__ == "__main__":
    app = App()
    app.mainloop()
