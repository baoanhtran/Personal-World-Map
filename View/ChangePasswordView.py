import tkinter as tk
import customtkinter as ctk
from Controller.LoginController import login_success

class ChangePasswordView(tk.Tk):
    __slots__ = ["label1", "label2", "label3", "username", "password", "button1", "button2", "title1", "canva"]

    def __init__(self, user):
        ctk.set_appearance_mode("light")

        super().__init__()
        self.user = user # self.user.id self.user.password
        self.title("Your personal travel map")
        self.geometry("500x500")
        self.resizable(False, False)

        # Apply custom color theme
        self.canva = ctk.CTkCanvas(width=500, height=500)
        self.canva.pack()

        # Load the .gif image file.
        img1 = tk.PhotoImage(file="View/pictures/bg_map.png")
        self.canva.create_image(0, 0, image=img1, anchor="nw")


        self.title1 = ctk.CTkLabel(self,text = "Changing password", font = ("Impact", 25), text_color='#354f52', fg_color= "#f5f6f9")
        self.title1.place(x = 140, y = 50)

        self.label1 = ctk.CTkLabel(self,text = "New Password", font = ("Arial", 11, 'bold'), text_color = '#354f52', fg_color= "#f5f6f9")
        self.label1.place(x = 175, y = 150)
        
        self.new_password = ctk.CTkEntry(self, font = ("Arial", 11, 'bold'), width= 150, height = 20, text_color = '#354f52')
        self.new_password.place(x = 175, y = 175)
        
        self.label2 = ctk.CTkLabel(self,text = "Confirmation of new password", font = ("Arial", 11, 'bold'), text_color = '#354f52', fg_color= "#f5f6f9")
        self.label2.place(x = 175, y = 200) 
        
        self.confirmation_of_password = ctk.CTkEntry(self, font = ("Arial", 11, 'bold'), width= 150, height = 20, text_color = '#354f52')
        self.confirmation_of_password.place(x = 175, y = 225)

        self.button1 = ctk.CTkButton(self, text = "Change", font = ("Arial", 11, 'bold'), width = 200, height = 30, fg_color= '#354f52', corner_radius = 10)
        self.button1.place(x = 150, y = 300)
        self.button1.bind('<Button-1>', self.new_password)
        
        '''self.button2 = ctk.CTkButton(self, text = "Create a new Account", font = ("Arial", 11, 'bold'), width = 200, height = 30, fg_color= '#354f52', text_color='#f9f7f3', corner_radius = 10)
        self.button2.place(x = 150, y = 350)
        self.button2.bind('<Button-1>', self.SignUp)'''

        self.mainloop()

    def new_password(self, event):
        username_val = self.username.get().strip()
        password_val = self.password.get().strip()

        if username_val == "" or password_val == "":
            # If error message already exists, destroy it
            if hasattr(self, "label3"):
                self.label3.destroy()

            # Label for error message
            self.label3 = ctk.CTkLabel(self, text = "Please type all fields", font = ("Courier", 15), width = 400, height = 30, bg_color= "red")
            self.label3.place(x = 50, y = 400)
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
            self.label3 = ctk.CTkLabel(self, text = "Wrong username or password", font = ("Courier", 15), width = 400, height = 30, bg_color= "red")
            self.label3.place(x = 50, y = 400)

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

    
    def quit(self):
        self.destroy()
