import tkinter as tk
from Controller.LoginController import register_user
from View.MapWindow import MapWindow

class SignUpWindow(tk.Tk):
    __slots__ = ["username", "password"]

    def __init__(self):
        super().__init__()
        self.title()
        self.geometry("500x500")
        
        self.label1 = tk.Label(self, text = "Username", font = ("Courier", 11))
        self.label1.place(x = 175, y = 100)
        
        self.username = tk.Entry(self, font = ("Courier", 10))
        self.username.place(x = 175, y = 125, width= 150, height = 20)
        
        self.label2 = tk.Label(self,text = "Password", font = ("Courier", 11))
        self.label2.place(x = 175, y = 200) 
        
        self.password = tk.Entry(self, font = ("Courier", 10))
        self.password.place(x = 175, y = 225, width= 150, height = 20)

        self.btn1 = tk.Button(self, text = "Create New Account", font = ("Courier", 10))
        self.btn1.place(x = 150, y = 300, width = 200, height = 30)
        self.btn1.bind('<Button-1>', self.new_account)



    def new_account(self, event):
        username = self.username.get()
        password = self.password.get()
        isAdded, user = register_user(username, password)
        if isAdded:
            MapWindow(user)
            self.quit()
        else:
            # If error message already exists, destroy it
            if hasattr(self, "label3"):
                self.label3.destroy()

            self.label3 = tk.Label(self, text = "This username is already taken", font = ("Courier", 10), fg="red")
            self.label3.place(x = 50, y = 350, width = 400, height = 30)

            # Clear the entry
            self.username.delete(0, 'end')
            self.password.delete(0, 'end')

            # Focus on the username entry
            self.username.focus()

    def quit(self):
        self.destroy()
