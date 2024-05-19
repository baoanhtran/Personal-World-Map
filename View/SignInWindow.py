import customtkinter as ctk
import tkinter as tk
from Controller.LoginController import login_success 
from View.MapWindow import MapWindow
from View.SignUpWindow import SignUpWindow


class SignInWindow(ctk.CTk):
    __slots__ = ["label1", "label2", "username", "password", "button1", "button2", "label3", "title1", "canva"]

    def __init__(self):
        super().__init__()
        self.title("Your personal travel map")
        self.geometry("500x500")

        # Apply custom color theme
        self.canva = ctk.CTkCanvas(width=self.winfo_screenwidth(), height=self.winfo_screenheight(), bg='#f5f6f9')

        # Pack the canvas into the Frame.
        self.canva.pack(expand="YES", fill="both")

        # Load the .gif image file.
        img1 = tk.PhotoImage(file="pictures/bg_map.PNG")
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
        self.button1.bind('<Button-1>', self.checkpassword)
        
        self.button2 = ctk.CTkButton(self, text = "Create a new Account", font = ("Arial", 11, 'bold'), width = 200, height = 30, fg_color= '#354f52', text_color='#f9f7f3', corner_radius = 10)
        self.button2.place(x = 150, y = 350)
        self.button1.bind('<Button-1>', self.SignUp)

        self.mainloop()
    
    def checkpassword(self, event):
        password = self.password.get()
        username = self.username.get()
        success, user = login_success(username, password)
        if success:
            MapWindow(user)
            self.quit()
        else : 
            self.label3= tk.Label(self, text = "Wrong Password or Username", font = ("Courier", 10))
            self.label3.place(x = 50, y = 400, width = 400, height = 30)
    
    def SignUp(self, event):
        SignUpWindow()
        self.quit()
    
    def quit(self):
        self.destroy()
        


