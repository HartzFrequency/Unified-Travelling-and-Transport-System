import tkinter as tk
import tkinter.messagebox
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter.font import Font
from datetime import datetime
import customtkinter
from PIL import Image, ImageTk
import os
from pymongo import MongoClient
import mysql.connector
import Modules.SQL as sql

# MongoDB connection setup
connection_string = "mongodb+srv://HarshShrivastava:harsh554@cluster0.aghgect.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)
db = client['UTS']  

def query_login_check(username, password):
    """Query to check if a user with the given username and password exists."""
    result = db.Users.find({'First': username, 'Password': password})
    return list(result)

customtkinter.set_appearance_mode("dark")

class Login(customtkinter.CTk):
    """Class representing the login GUI."""
    width = 1240          #helps in image width
    height = 1080         #helps in image height
    def __init__(self):
        super().__init__()

        # Window settings
        self.title("Login")
        self.geometry(f"{1240}x{720}")
        self.bg_image = customtkinter.CTkImage(Image.open("Image/Background_gradient.jpg"),size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # Login frame
        # TEXT : "Welcome!\nUnified Travelling & Transport System"
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=15)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        # Welcome labels
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="Welcome",font=customtkinter.CTkFont(size=24, weight="bold", slant="roman", family="Roboto"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(100, 5))

        self.login_label_UTTS = customtkinter.CTkLabel(self.login_frame, text="Unified Transit System",font=customtkinter.CTkFont(size=20, slant="roman", family="Helvetica"))
        self.login_label_UTTS.grid(row=1, column=0, padx=30, pady=(0, 0))

        #text : Login Page
        self.login_label_2 = customtkinter.CTkLabel(self.login_frame, text="Login Page",font=customtkinter.CTkFont(size=40, weight="bold", family="Roboto"))
        self.login_label_2.grid(row=2, column=0, padx=30, pady=(50, 15))
        
        # Username entry
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=300, placeholder_text="Username")
        self.username_entry.grid(row=3, column=0, padx=30, pady=(15, 15))
        
        # Password entry
        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=300, show="*", placeholder_text="Password")
        self.password_entry.grid(row=4, column=0, padx=30, pady=(0, 15))

        # Show password checkbox
        self.show_password_var = tk.BooleanVar()
        self.show_password_checkbutton = tk.Checkbutton(
            self.login_frame,
            text="Show Password",
            variable=self.show_password_var,
            command=self.toggle_password_visibility,
        )
        self.show_password_checkbutton.grid(
            row=5, column=0, padx=30, sticky="w", pady=(0, 15)
        )
        
        # Login button
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=6, column=0, padx=30, pady=(15, 15))

        
        # Register now label
        self.login_label_3 = customtkinter.CTkLabel(
            self.login_frame,
            text="Register now if you don't have an account.",
            font=customtkinter.CTkFont(size=12, weight="normal"),
        )
        self.login_label_3.grid(row=7, column=0, padx=30, pady=(20, 5))

        # Register button
        self.login_button = customtkinter.CTkButton(
            self.login_frame, text="Register", command=self.register_event, width=200
        )
        self.login_button.grid(row=8, column=0, padx=30, pady=(0, 15))

        # Forgot password label
        self.forgot_password_label = customtkinter.CTkLabel(
            self.login_frame,
            text="Forgot password ?",
            font=customtkinter.CTkFont(underline=True),
            cursor="hand2",
        )
        self.forgot_password_label.grid(
            row=5, column=0, padx=(0, 30), pady=(0, 15), sticky="e"
        )

        # Bind the callback function to the label's click event
        self.forgot_password_label.bind(
            "<Button-1>", lambda event: self.forgot_password_event()
        )


    def toggle_password_visibility(self):
        """Toggle the visibility of the password entry."""
        if self.show_password_var.get():
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")

    def login_event(self):
        """Event handler for the login button."""
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()
        QueryCheckForPassword=query_login_check(entered_username, entered_password)

        if QueryCheckForPassword:
            self.destroy()            
            import StartPageGUI
            StartPageGUI.Main().mainloop()

        else:
            print("error")
            return messagebox.showerror('Error','Incorrect Username or Password')
        
        print("Login pressed - username:", entered_username, "password:",entered_password)

    def register_event(self, event=None):
        """Event handler for the register button."""
        win = tk.Tk()
        win.title("Register")
        win.geometry("350x480")

        label_first = tk.Label(win, text="First Name:")
        label_first.pack()
        entry_first = tk.Entry(win)
        entry_first.pack()

        label_last = tk.Label(win, text="Last Name:")
        label_last.pack()
        entry_last = tk.Entry(win)
        entry_last.pack()

        label_dob = tk.Label(win, text="Date of Birth (DD MM YYYY):")
        label_dob.pack()
        entry_dob = tk.Entry(win)
        entry_dob.pack()

        label_phone = tk.Label(win, text="Phone:")
        label_phone.pack()
        entry_phone = tk.Entry(win)
        entry_phone.pack()

        label_address = tk.Label(win, text="Address:")
        label_address.pack()
        entry_address = tk.Entry(win)
        entry_address.pack()

        label_city = tk.Label(win, text="City:")
        label_city.pack()
        entry_city = tk.Entry(win)
        entry_city.pack()

        label_state = tk.Label(win, text="State:")
        label_state.pack()
        entry_state = tk.Entry(win)
        entry_state.pack()

        label_password = tk.Label(win, text="Password:")
        label_password.pack()
        entry_password = tk.Entry(win, show="*")
        entry_password.pack()

        error_label = tk.Label(win, fg="red")
        error_label.pack()

        def register():
            """Register the user with the provided information."""
            first = entry_first.get()
            last = entry_last.get()
            dob_str = entry_dob.get()
            phone = entry_phone.get()
            address = entry_address.get()
            city = entry_city.get()
            state = entry_state.get()
            password = entry_password.get()

            # Validate Date of Birth format
            try:
                dob = datetime.strptime(dob_str, '%d %m %Y').strftime('%d-%m-%Y')
            except ValueError:
                win.geometry("400x350")
                error_label.config(text="Invalid Date of Birth format! Please enter DD MM YYYY.")
                return


            # Get the last UserID and increment it
            last_user = db.Users.find_one(sort=[("UserID", -1)])
            last_user_id = 0 if last_user is None else last_user['UserID']
            new_user_id = last_user_id + 1

            # Check if the username already exists
            existing_user = db.Users.find_one({'First': first, 'Last': last, 'DOB': dob})

            if existing_user:
                messagebox.showerror(
                    "Registration Error",
                    "User with the same name and Date of Birth already exists.",
                    parent=win
                )
            else:
                # Insert new user into the database
                db.Users.insert_one({
                    'UserID': new_user_id,
                    'First': first,
                    'Last': last,
                    'DOB': dob,
                    'Phone': phone,
                    'Address': address,
                    'City': city,
                    'State': state,
                    'Points': 0,
                    'Password': password
                })
                messagebox.showinfo("Registration", "Registration successful!", parent=win)

        button_register = tk.Button(win, text="Register", command=register)
        button_register.pack()

        win.mainloop()

    def forgot_password_event(self):
        """Event handler for the forgot password link."""
        def send_password():
            """Send the password reset information."""
            username = entry_username.get()
            dob_str = entry_dob.get()

            # Convert the input DOB string to a datetime object
            try:
                dob = datetime.strptime(dob_str, '%d-%m-%Y').strftime('%d-%m-%Y')
            except ValueError:
                messagebox.showerror("Invalid DOB", "Please enter DOB in the format DD-MM-YYYY")
                return

            # Check if the username and DOB combination exists in the database
            user = db.Users.find_one({'First': username, 'DOB': dob})

            if user:
                # Close the current window
                win.destroy()

                # Open a new window to prompt for a new password
                def update_password():
                    """Update the user's password."""
                    new_password = entry_new_password.get()

                    # Check if the password meets the minimum length requirement
                    if len(new_password) < 8:
                        messagebox.showerror(
                            "Invalid Password",
                            "Password must be at least 8 characters long."
                        )
                        return

                    # Update the password in the database
                    db.Users.update_one({'First': username}, {'$set': {'Password': new_password}})
                    messagebox.showinfo(
                        "Password Updated", "Password updated successfully!"
                    )

                    # Close the new window
                    new_win.destroy()

                new_win = tk.Toplevel()
                new_win.title("Reset Password")
                new_win.geometry("300x150")

                label_new_password = tk.Label(new_win, text="New Password:")
                label_new_password.pack()

                entry_new_password = tk.Entry(new_win, show="*")
                entry_new_password.pack()

                btn_update = tk.Button(
                    new_win, text="Update Password", command=update_password
                )
                btn_update.pack()

            else:
                messagebox.showerror(
                    "Forgot Password", "Invalid username or DOB. Please try again."
                )


        win = tk.Tk()
        win.title("Forgot Password")
        win.geometry("300x200")

        label_username = tk.Label(win, text="Username:")
        label_username.pack()

        entry_username = tk.Entry(win)
        entry_username.pack()

        label_dob = tk.Label(win, text="Date of Birth (DD-MM-YYYY):")
        label_dob.pack()

        entry_dob = tk.Entry(win)
        entry_dob.pack()

        btn_send = tk.Button(win, text="Send Password", command=send_password)
        btn_send.pack()

        win.mainloop()


if __name__ == "__main__":
    app9 = Login()
    app9.mainloop()
