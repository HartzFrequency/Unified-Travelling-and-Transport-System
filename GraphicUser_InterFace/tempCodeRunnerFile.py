        self.title("Login Page")
        self.geometry(f"{1700}x{580}")
        self.bg_image = customtkinter.CTkImage(Image.open("Image/Background_gradient.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)