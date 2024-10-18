import customtkinter as ctk
import Modules.SQL as sql
import Modules.FileHandling as File

class Available(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.setup_window()
        self.create_widgets()
        self.populate_textbox()

    def setup_window(self):
        self.geometry("700x300")
        self.title("Route Information Page")
        self.minsize(300, 200)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

    def create_widgets(self):
        self.textbox = ctk.CTkTextbox(master=self, font=("Arial", 18))
        self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
        
        self.combobox = ctk.CTkComboBox(master=self, values=self.get_combobox_values())
        self.combobox.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.button = ctk.CTkButton(master=self, command=self.button_callback, text="Proceed")
        self.button.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

    def populate_textbox(self):
        try:
            available_list = sql.Query_FetchFromFile()
            available_list.reverse()
            indexing_choices = len(available_list)

            for item in available_list:
                self.textbox.insert("0.0", f"{indexing_choices}). {item}\n")
                indexing_choices -= 1
        except Exception as e:
            self.textbox.insert("0.0", f"Error fetching data: {e}\n")

    def get_combobox_values(self):
        try:
            available_list = sql.Query_FetchFromFile()
            values = [f"Choice {i+1}" for i in range(len(available_list))]
            values.append("Select")
            return values[::-1]
        except Exception as e:
            return [f"Error fetching data: {e}"]

    def button_callback(self):
        selection = self.combobox.get()
        try:
            File.Handle_Selection(selection)
        except Exception as e:
            print(f"Error handling selection: {e}")
        finally:
            self.destroy()
            import Payment
            Payment.mainloop()

if __name__ == "__main__":
    app = Available()
    app.mainloop()
