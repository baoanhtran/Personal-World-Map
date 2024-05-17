import tkinter as tk
from Controller.LoginController import check_user_existence, login_success 
from View.MapWindow import MapWindow
from View.SignUpWindow import SignUpWindow


class SignInWindow(tk.Tk):
    __slots__ = ["label1", "label2", "username", "password", "button1", "button2", "label3"]

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

        self.button1 = tk.Button(self, text = "Connect", font = ("Courier", 10))
        self.button1.place(x = 150, y = 300, width = 200, height = 30)
        self.button1.bind('<Button-1>', self.checkpassword)
        
        self.button2 = tk.Button(self, text = "Create a new Account", font = ("Courier", 10))
        self.button2.place(x = 150, y = 350, width = 200, height = 30)
        self.button2.bind('<Button-1>', self.SignUp)

    
    def checkpassword(self, event):
        password = self.password.get()
        username = self.username.get()
        if login_success(username, password):
            map_window = MapWindow()
            self.quit()
            MapWindow.mainloop()
        else : 
            self.label3= tk.Label(self, text = "Wrong Password or Username", font = ("Courier", 10))
            self.label3.place(x = 50, y = 400, width = 400, height = 30)
    
    def SignUp(self, event):
        sign_up_window = SignUpWindow()
        self.quit()
    
    def quit(self,):
        self.destroy()
        


