import tkinter as tk
from Controller.LoginController import login_success
from View.SignUpWindow import SignUpWindow
from View.MapWindow import MapWindow

class LoginWindow(tk.Tk):
    __slots__ = ["username", "password"]

    def __init__(self):
        super().__init__()
        self.title()
        self.geometry("500x500")

        self.label1 = tk.Label(self,text = "Username", font = ("Courier", 11))
        self.label1.place(x = 175, y = 100)

        self.username = tk.Entry(self, font = ("Courier", 10))
        self.username.place(x = 175, y = 125, width= 150, height = 20)

        self.label2 = tk.Label(self,text = "Password", font = ("Courier", 11))
        self.label2.place(x = 175, y = 200) 

        self.password = tk.Entry(self, font = ("Courier", 10))
        self.password.place(x = 175, y = 225, width= 150, height = 20)

        self.btn1 = tk.Button(self, text = "Connect", font = ("Courier", 10))
        self.btn1.place(x = 150, y = 300, width = 200, height = 30)
        self.btn1.bind('<Button-1>', self.login)

        self.btn2 = tk.Button(self, text = "Create a new Account", font = ("Courier", 10))
        self.btn2.place(x = 150, y = 350, width = 200, height = 30)
        self.btn2.bind('<Button-1>', self.SignUp)

        self.mainloop()

    def login(self, event):
        username_val = self.username.get().strip()
        password_val = self.password.get().strip()
        if login_success(username_val, password_val)[0]:
            self.user = login_success(username_val, password_val)[1]

            # Unbind events before destruction
            self.btn1.unbind('<Button-1>')
            self.btn2.unbind('<Button-1>')

            # Delay destruction to ensure event handler completes
            self.after(100, self.open_map_window)
        else :
            # If error message already exists, destroy it
            if hasattr(self, "label3"):
                self.label3.destroy()

            # Label for error message
            self.label3 = tk.Label(self, text = "Wrong Password or Username", font = ("Courier", 10), fg="red")
            self.label3.place(x = 50, y = 400, width = 400, height = 30)

            # Clear the entry
            self.username.delete(0, 'end')
            self.password.delete(0, 'end')

            # Focus on username entry
            self.username.focus()

    def SignUp(self, event):
        # Unbind events before destruction
        self.btn1.unbind('<Button-1>')
        self.btn2.unbind('<Button-1>')

        # Delay destruction to ensure event handler completes
        self.after(100, self.open_sign_up_window)

    def open_map_window(self):
        self.destroy()
        MapWindow(self.user)

    def open_sign_up_window(self):
        self.destroy()
        SignUpWindow()