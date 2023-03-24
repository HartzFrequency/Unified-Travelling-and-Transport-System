import tkinter as tk

class Window1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Window 1")
        self.geometry("200x100")
        tk.Button(self, text="Open Window 2", command=self.open_window2).pack()

    def open_window2(self):
        self.destroy()  # close current window
        Window2().mainloop()  # open next window

class Window2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Window 2")
        self.geometry("200x100")
        tk.Button(self, text="Open Window 1", command=self.open_window1).pack()

    def open_window1(self):
        self.destroy()  # close current window
        Window1().mainloop()  # open previous window

if __name__ == '__main__':
    Window1().mainloop()  # start with the first window
