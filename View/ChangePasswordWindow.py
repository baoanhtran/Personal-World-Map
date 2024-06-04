import tkinter as tk
import customtkinter as ctk
from Controller.LoginController import change_password
from tkinter import messagebox

class ChangePasswordWindow(tk.Toplevel):
    __slots__ = ["label1", "label2", "label3", "username", "password", "button1", "button2", "title1", "canva"]

    def __init__(self, master):
        ctk.set_appearance_mode("light")

        super().__init__()
        self.master = master
        self.user = master.user
        self.title("Your personal travel map")
        self.resizable(False, False)

        # Apply custom color theme
        self.canva = tk.Canvas(self, width=500, height=500)
        self.canva.pack(fill="both", expand=True)

        # Load the image file.
        self.img1 = tk.PhotoImage(file="View/pictures/bg_map.png")
        self.canva.create_image(0, 0, image=self.img1, anchor="nw")


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
        self.button1.bind('<Button-1>', self.change_password)
        self.bind('<Return>', self.change_password)

        self.mainloop()

    def change_password(self, event):
        new_password = self.new_password.get().strip()
        password_confirmation = self.confirmation_of_password.get().strip()

        is_valid, message = change_password(self.user.id, new_password, password_confirmation)

        if not is_valid:
            if hasattr(self, "label3"):
                self.label3.destroy()

            self.label3 = ctk.CTkLabel(self, text = message, font = ("Courier", 15), width = 400, height = 30, bg_color= "red")
            self.label3.place(x = 50, y = 400)
        else:
            self.button1.unbind('<Button-1>')
            self.unbind('<Return>')
            self.quit()
            messagebox.showinfo("Success", "Password changed successfully")
    
    def quit(self):
        self.destroy()
