import customtkinter
from tkinter import Label
import tkinter as tk
# import customtkinter

class MyGUI:
    def __init__(self, master):
        self.master = master
        self.image = customtkinter.CTkImage("Image/BUS.png")
        self.label = Label(master, image=self.image)
        self.label.pack()


root = tk.Tk()
app = MyGUI(root) # Pass in root as the master argument
root.mainloop()