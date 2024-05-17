import tkinter as tk
from Controller.LoginController import login_success
from View.MapWindow import MapWindow

class LoginWindow(tk.Tk):
    __slots__ = ["user_id"]

    def __init__(self):
        super().__init__()
        self.title("Personal World Map")
        self.geometry("500x500")
        self.create_widgets()
        self.mainloop()

    def create_widgets(self):
        # Username label
        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack()

        # Username entry
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        # Password label
        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()

        # Password entry
        self.password_entry = tk.Entry(self)
        self.password_entry.pack()

        # Login button
        self.login_button = tk.Button(self, text="Login")
        self.login_button.bind("<Button-1>", self.login)
        self.bind("<Return>", self.login)
        self.login_button.pack()

    def login(self, event):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        if login_success(username, password)[0]:
            self.user = login_success(username, password)[1]
            self.destroy()
            MapWindow(self.user)
            
        else:
            # If error message already exists, destroy it
            if hasattr(self, "error_label"):
                self.error_label.destroy()

            # Label for error message
            self.error_label = tk.Label(self, text="Invalid username or password")
            self.error_label.pack()

            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
            self.username_entry.focus()


