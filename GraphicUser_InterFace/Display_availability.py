import customtkinter
import Modules.SQL as sql
import Modules.FileHandling as File

class Available(customtkinter.CTk):
    """
    Class representing the Route Information Page GUI.

    Attributes:
        textbox: Textbox to display available routes.
        combobox: ComboBox to select a specific route.
        button: Button to proceed with the selected route.
    """
    def __init__(self):
        super().__init__()

        self.geometry("700x300")
        self.title("Route Information Page")
        self.minsize(300, 200)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Textbox for displaying available routes
        self.textbox = customtkinter.CTkTextbox(master=self)
        self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
        self.textbox.configure(font=("Arial", 18))

        # Fetching available routes from the file and displaying them
        AvailableList = sql.Query_FetchFromFile()
        AvailableList.reverse()
        list=[]
        indexing_Choices=len(AvailableList)
        for i in range(AvailableList.__len__()):
            self.textbox.insert("0.0",str(indexing_Choices)+"). "+AvailableList[i]+"\n")
            indexing_Choices=indexing_Choices-1
            list.append("Choice "+ str(indexing_Choices+1))  
        list.append("Select")
        list.reverse()

        # ComboBox for route selection
        self.combobox = customtkinter.CTkComboBox(master=self, values=list)
        self.combobox.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        # Button to proceed with the selected route
        self.button = customtkinter.CTkButton(master=self, command=self.button_callback, text="Proceed")
        self.button.grid(row=1, column=1, padx=20, pady=20, sticky="ew")
        

    def button_callback(self):
        """
        Callback function for the button to handle the selected route and proceed to the payment page.
        """
        selection = self.combobox.get()
        File.Handle_Selection(selection)
        self.destroy()            
        import Payment
        Payment.mainloop()
    

if __name__ == "__main__":
    Available = App()
    Available.mainloop()
