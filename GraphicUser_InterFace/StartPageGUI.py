import tkinter as tk
import tkinter.messagebox
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage
from colorama import Fore, Style

import pickle as pk

import urllib.request
from urllib.request import Request
import pickle as pk
from discord_webhook import DiscordWebhook, DiscordEmbed 


window1 = customtkinter.CTk()
# AVAILABLE MODES->"System", "Dark", "Light"
customtkinter.set_appearance_mode("System") 
#AVAILABLE THEMES->"blue", "green", "dark-blue" 
customtkinter.set_default_color_theme("blue")

WINX = 1440
WINY = 540
SCALE = 100
THEME = 'Dark'

def update_config():
    global WINX, WINY, SCALE, THEME
    try:
        with open('LocalDATA/config.ini', 'rb') as file:
            WINX, WINY, SCALE, THEME = pk.load(file)
    except:
        with open('LocalDATA/config.ini', 'wb') as file:
            pk.dump([WINX,WINY,SCALE,THEME], file)

update_config()

class Main(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        #DEFINING WINDOW NAME AND SIZE
        self.title("Home Page")
        self.geometry(f"{WINX}x{WINY}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=0)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=120, corner_radius=15)
        self.sidebar_frame.grid(row=9, column=0, rowspan=4, sticky="ns")
        self.sidebar_frame.grid_rowconfigure(1, weight=1)
        
        # PROFILE BUTTON
        self.profile_button = customtkinter.CTkButton(self.sidebar_frame,text="Profile")
        self.profile_button.grid(row=0,column=0,padx=10,pady=15)

        # LOGIN BUTTON
        self.back_to_loginPage_button = customtkinter.CTkButton(self.sidebar_frame,text="Log Out", command=self.open_Login_window)
        self.back_to_loginPage_button.grid(row=1, column=0, padx=10, pady=15)

        # APPEARANCE TEXT
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=10, pady=(5,0))
        # APPEARANCE BUTTON
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady =(10,10))
        
        # SCALING TEXT
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10,0))
        # SCALING BUTTON
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["70%", "80%", "90%", "100%", "110%", "120%", "130%"],command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(5,20))
        try:
            with open('runtimevars.dat', 'rb') as file:
                theme_selection = pk.load(file)
        except:
            theme_selection = 'Dark'
        self.appearance_mode_optionemenu.set(theme_selection)
        self.change_appearance_mode_event(theme_selection)
        self.scaling_optionemenu.set("100%")

        self.upper_name_frame = customtkinter.CTkFrame(self, width=140,height=50, corner_radius=15)
        self.upper_name_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
        self.upper_name_frame.grid_rowconfigure(6, weight=1)
        
        self.project_name = customtkinter.CTkLabel(self.upper_name_frame, text="UTS\nUnified Transit System", font=customtkinter.CTkFont(size=38, weight="bold"))
        self.project_name.grid(row=0, column=2, padx=400, pady=6)

        #PROGRESS BAR TO BE COMPLETED
        # self.slider_progressbar_frame = customtkinter.CTkFrame(self, width=200, height=20, fg_color="transparent")
        # self.slider_progressbar_frame.grid(row=6, column=2, padx=(20, 0), pady=(20, 0))
        # self.slider_progressbar_frame.grid_columnconfigure(0, weight=4)
        # self.slider_progressbar_frame.grid_rowconfigure(14, weight=4)
        # self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_1.grid(row=6, column=2, padx=(20, 10), pady=(10, 10))
        # self.progressbar_1.configure(mode="indeterminate")
        # self.progressbar_1.start()
        # self.slider_progressbar_frame = customtkinter.CTkFrame(self, width=100,height=20,fg_color="transparent")
        # self.slider_progressbar_frame.grid(row=6, column=2, padx=(20, 0), pady=(20, 0))
        # self.slider_progressbar_frame.grid_columnconfigure(0, weight=4)
        # self.slider_progressbar_frame.grid_rowconfigure(14, weight=4)
        # self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, width=200)
        # self.progressbar_1.grid(row=6, column=2, padx=(20, 10), pady=(10, 10))
        # self.progressbar_1.configure(mode="indeterminnate")
        # self.progressbar_1.start()


        #CREATING TAB VIEW
        self.tabview = customtkinter.CTkTabview(self, width=1240, height= 50, corner_radius=10)
        self.tabview.grid(row=4, column=2, padx=0, pady=(5, 10))
        self.tabview.add("Travel")
        self.tabview.tab("Travel").grid_columnconfigure(0, weight=0)  # configure grid of individual tabs
        self.tabview.add("Transport")
        self.tabview.tab("Transport").grid_columnconfigure(0, weight=1)

        #TRAVEL
        self.Bus_button = customtkinter.CTkButton(self.tabview.tab("Travel"), text="Bus",command=self.open_Bus_window)
        self.Bus_button.grid(row=4, column=0, padx=(0,110), pady=(10, 10),sticky="w")

        self.Car_button = customtkinter.CTkButton(self.tabview.tab("Travel"), text="Car",command=self.open_Car_window)
        self.Car_button.grid(row=4, column=1, padx=(110,110), pady=(10, 10),sticky="nsew")

        self.Train_button = customtkinter.CTkButton(self.tabview.tab("Travel"), text="Train",command=self.open_Train_window)
        self.Train_button.grid(row=4, column=2, padx=(110,110), pady=(10, 10),sticky="nsew")

        self.Airplane_button = customtkinter.CTkButton(self.tabview.tab("Travel"), text="Airplane",command=self.open_Airplane_window)
        self.Airplane_button.grid(row=4, column=3, padx=(110,0), pady=(10, 10),sticky="e")


        #TRANSPORT
        self.Truck_button = customtkinter.CTkButton(self.tabview.tab("Transport"), text="Truck",command=self.open_Truck_window)
        self.Truck_button.grid(row=4, column=0, padx=20, pady=(10, 10),sticky="w")
        
        self.Ship_button = customtkinter.CTkButton(self.tabview.tab("Transport"), text="Railways",command=self.open_Ship_window)
        self.Ship_button.grid(row=4, column=1, padx=20, pady=(10, 10),sticky="e")
            

        self.tabview = customtkinter.CTkTabview(self, width=240, height= 80)
        self.tabview.grid(row=10, column=2, padx=0, pady=0,sticky="s")
        self.tabview.add("Error Encountered")

        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Error Encountered"), text="Feedback Button",command=self.open_input_dialog_event)
        self.string_input_button.grid(row=10, column=19, padx=20, pady=(10, 10), sticky="nsew")
        self.string_input_button.pack(side="top", anchor="center")


    def open_input_dialog_event(self):
        # Get feedback from the user through a dialog
        # dialog = customtkinter.CTkInputDialog(text="Please enter your valuable Feedback :", title="Feedback Window")
        # feedback = dialog.get_input()

        win = tk.Tk()
        win.title("Register")
        win.geometry("400x200")

        label_first = tk.Label(win, text="Email/Github")
        label_first.pack()
        ContactOpt = tk.Entry(win)
        ContactOpt.pack()

        label_last = tk.Label(win, text="Feedback")
        label_last.pack()
        Feedback = tk.Entry(win)
        Feedback.pack()

        def Submit():
            # Get the text entered by the user in the Entry fields
            contact_text = ContactOpt.get()
            feedback_text = Feedback.get()

            # Setting up Discord webhook URL
            webhook_url = "https://discord.com/api/webhooks/1174817583216726088/1NF3FdBKaxH5jsaMdayOkN2qNEdsl9V8SsWJZ6XN2unTxbk4QNRL1crZPCB7AY-pZjq0"

            req = Request(
                url=webhook_url,
                headers={"User-Agent": "Mozilla/5.0"}
            )
            try:
                # Trying to open the Discord webhook URL to ensure connectivity
                with urllib.request.urlopen(req) as response:
                    txt = response.read()
            except Exception as e:
                # Exit with an error message if there is a connection error
                messagebox.showerror("Error", f"Contact system error: {e}")
                return

            # Create a Discord embed with contact information, subject, and message
            embed = DiscordEmbed(title="UTS Feedback", color="03b2f8")
            embed.add_embed_field(name="Contact method", value=contact_text, inline=False)
            embed.add_embed_field(name="Subject", value="Feedback", inline=False)
            embed.add_embed_field(name="Message", value=feedback_text, inline=False)

            # Set up a proxy for the Discord webhook (if needed)
            proxy = {
                "http": "14.97.216.232:80"
            }
            webhook = DiscordWebhook(url=webhook_url, proxies=proxy)
            # Add the embed to the Discord webhook and execute the request
            webhook.add_embed(embed)
            response = webhook.execute()
            # Show a success message after the message is sent
            messagebox.showinfo("Success", "Feedback sent successfully")
            win.mainloop()
        button_submit = tk.Button(win, text="Submit", command=Submit)
        button_submit.pack()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        global WINX, WINY, SCALE, THEME
        THEME = new_appearance_mode
        customtkinter.set_appearance_mode(THEME)
        update_config()

    def change_scaling_event(self, new_scaling: str):
        global WINX, WINY, SCALE, THEME
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        SCALE = new_scaling_float
        WINX = int((WINX)*new_scaling_float)
        WINY = int((WINY)*new_scaling_float)
        self.geometry(f"{WINX}x{WINY}")
        customtkinter.set_widget_scaling(SCALE)
        update_config()

    def open_Login_window(self):
        self.destroy()            
        import Login_page
        Login_page.Login().mainloop()

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

    def open_Truck_window(self):
        self.destroy()            
        import Truck_Home_page
        Truck_Home_page.Truck().mainloop()

    def open_Ship_window(self):
        self.destroy()            
        import Railway_Home_page
        Railway_Home_page.Railway().mainloop()


if __name__ == "__main__":
    app1 = Main()
    app1.mainloop()    
