import tkinter as tk
import customtkinter as ctk
from Controller.LoginController import login_success
from View.SignUpWindow import SignUpWindow
from View.MapWindow import MapWindow

class LoginWindow(ctk.CTk):
    __slots__ = ["label1", "label2", "label3", "username", "password", "button1", "button2", "title1", "canva"]

    def __init__(self):
        super().__init__()
        self.title("Your personal travel map")
        self.geometry("500x500")

        # Apply custom color theme
        self.canva = ctk.CTkCanvas(width=500, height=500, bg='#f5f6f9')
        self.canva.pack(expand="YES", fill="both")

        # Load the .gif image file.
        img1 = tk.PhotoImage(file="View/pictures/bg_map.png")
        self.canva.create_image(50, 50, image=img1, anchor="nw")


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

        self.button1 = ctk.CTkButton(self, text = "Connect", font = ("Arial", 11, 'bold'), width = 200, height = 30, fg_color= '#354f52', corner_radius = 10)
        self.button1.place(x = 150, y = 300)
        self.button1.bind('<Button-1>', self.login)
        
        self.button2 = ctk.CTkButton(self, text = "Create a new Account", font = ("Arial", 11, 'bold'), width = 200, height = 30, fg_color= '#354f52', text_color='#f9f7f3', corner_radius = 10)
        self.button2.place(x = 150, y = 350)
        self.button2.bind('<Button-1>', self.SignUp)

        self.mainloop()

    def login(self, event):
        username_val = self.username.get().strip()
        password_val = self.password.get().strip()

        if username_val == "" or password_val == "":
            # If error message already exists, destroy it
            if hasattr(self, "label3"):
                self.label3.destroy()

            # Label for error message
            self.label3 = ctk.CTkLabel(self, text = "Please type all fields", font = ("Courier", 10), fg="red")
            self.label3.place(x = 50, y = 400, width = 400, height = 30)
        elif login_success(username_val, password_val)[0]:
            self.user = login_success(username_val, password_val)[1]

            # Unbind events before destruction
            self.button1.unbind('<Button-1>')
            self.button2.unbind('<Button-1>')

            # Delay destruction to ensure event handler completes
            self.after(100, self.open_map_window)
        else :
            # If error message already exists, destroy it
            if hasattr(self, "label3"):
                self.label3.destroy()

            # Label for error message
            self.label3 = ctk.CTkLabel(self, text = "Wrong username or password", font = ("Courier", 10), fg="red")
            self.label3.place(x = 50, y = 400, width = 400, height = 30)

            # Clear the entry
            self.username.delete(0, 'end')
            self.password.delete(0, 'end')

            # Focus on username entry
            self.username.focus()

    def SignUp(self, event):
        # Unbind events before destruction
        self.button1.unbind('<Button-1>')
        self.button2.unbind('<Button-1>')

        # Delay destruction to ensure event handler completes
        self.after(100, self.open_sign_up_window)

    def open_map_window(self):
        self.destroy()
        MapWindow(self.user)

    def open_sign_up_window(self):
        self.destroy()
        SignUpWindow()
    
    def quit(self):
        self.destroy()
        


