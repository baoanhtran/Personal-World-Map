import tkinter as tk
import customtkinter as ctk
from Controller.LoginController import register_user
from View.MapWindow import MapWindow

class SignUpWindow(tk.Tk):
    __slots__ = ["label1", "label2", "label3", "username", "password", "button1", "title1", "canva"]

    def __init__(self):
        super().__init__()
        self.title("Your personal travel map")
        self.geometry("500x500")
        self.resizable(False, False)

        # Apply custom color theme
        self.canva = ctk.CTkCanvas(width=500, height=500)

        # Pack the canvas into the Frame.
        self.canva.pack()

        # Load the image file.
        img1 = tk.PhotoImage(file="View/pictures/bg_map.png")
        self.canva.create_image(0, 0, image=img1, anchor="nw")


        self.title1 = ctk.CTkLabel(self,text = "Your personal travel map", font = ("Impact", 25), text_color='#354f52', fg_color= "#f5f6f9")
        self.title1.place(x = 130, y = 50)

        self.label1 = ctk.CTkLabel(self,text = "Username", font = ("Arial", 11, 'bold'), text_color = '#354f52', fg_color= "#f5f6f9")
        self.label1.place(x = 175, y = 100)
        
        self.username = ctk.CTkEntry(self, font = ("Arial", 11, 'bold'), width= 150, height = 20, text_color = '#354f52')
        self.username.place(x = 175, y = 125)
        
        self.label2 = ctk.CTkLabel(self,text = "Password", font = ("Arial", 11, 'bold'), text_color = '#354f52', fg_color= "#f5f6f9")
        self.label2.place(x = 175, y = 200) 
        
        self.password = ctk.CTkEntry(self, font = ("Arial", 11, 'bold'), width= 150, height = 20, text_color = '#354f52')
        self.password.place(x = 175, y = 225)

        self.button1 = ctk.CTkButton(self, text = "Create a new Account", font = ("Arial", 11, 'bold'), width = 200, height = 30, fg_color= '#354f52', corner_radius = 10)
        self.button1.place(x = 150, y = 300)
        self.button1.bind('<Button-1>', self.new_account)
        self.bind('<Return>', self.new_account)

        self.mainloop()

    def new_account(self, event):
        username = self.username.get().strip()
        password = self.password.get().strip()

        is_valid, user, error_message = register_user(username, password)

        if is_valid:
            # Unbind events before destruction
            self.button1.unbind('<Button-1>')
            self.unbind('<Return>')

            # Delay destruction to ensure event handler completes
            self.user = user
            self.after(100, self.open_map_window)
        else:
            # If error message already exists, destroy it
            if hasattr(self, "label3"):
                self.label3.destroy()

            self.label3 = ctk.CTkLabel(self, text = error_message, font = ("Courier", 15), width = 400, height = 30, bg_color= "red")
            self.label3.place(x = 50, y = 350)

            # Clear the entry
            self.username.delete(0, 'end')
            self.password.delete(0, 'end')

            # Focus on the username entry
            self.username.focus()

    def open_map_window(self):
        self.destroy()
        MapWindow(self.user)
