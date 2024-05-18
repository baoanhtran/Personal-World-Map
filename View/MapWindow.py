import tkinter as tk
from tkinter import messagebox
from Model.Map import Map
from CustomWidget.ZoomableCanvas import ZoomableCanvas
from Controller.MapController import get_country_name, get_incoming_trips, get_all_countries_visited, get_description
from datetime import datetime

class MapWindow(tk.Tk):
    __slots__ = ["canevas", "map"]

    def __init__(self, user):
        super().__init__()
        self.user = user
        self.attributes("-fullscreen", True)
        self.title("Personal World Map")

        # Quit button
        quit_button = tk.Button(self, text="Quit", background="cyan", foreground="black", font=("Courier", 10))
        quit_button.bind("<Button-1>", self.quit)
        quit_button.pack(side="top", fill="x")

        # Side bar containing 3 buttons
        self.side_bar = tk.Frame(self, bg="cyan")
        self.side_bar.pack(side="right", fill="y")

        # Button to show all trips
        self.button1 = tk.Button(self.side_bar, text="Show all my trips", foreground="black", font=("Courier", 10),height=2)
        self.button1.pack(side="top", fill="x", pady=10, padx=10)

        # Button to plan a new trip
        self.button2 = tk.Button(self.side_bar, text="Plan a new trip", foreground="black", font=("Courier", 10), height=2)
        self.button2.pack(side="top", fill="x", pady=10, padx=10)

        # Button to change password
        self.button3 = tk.Button(self.side_bar, text="Change password", foreground="black", font=("Courier", 10), height=2)
        self.button3.pack(side="top", fill="x", pady=10, padx=10)

        # Button to sign out
        self.button4 = tk.Button(self.side_bar, text="Sign out", foreground="black", font=("Courier", 10), height=2)
        self.button4.bind("<Button-1>", lambda event: self.sign_out())
        self.button4.pack(side="top", fill="x", pady=10, padx=10)

        # Map
        self.canevas = ZoomableCanvas(self, bg="#%02x%02x%02x" % (182, 255, 246), width=self.winfo_screenwidth(), height=self.winfo_screenheight())
        self.map = Map(self.winfo_screenwidth(), self.winfo_screenheight())
        self.draw()
        self.canevas.pack(side="left")

        # Reminders
        self.show_reminders()

        self.mainloop()

    def quit(self, event):
        self.destroy()

    def draw(self):
        visited_countries = get_all_countries_visited(self.user.id)
        self.canevas.delete("all")
        for (k, v) in self.map.coordinates_dict.items():
            if self.map.list_depth(v) == 4:
                for ele in v:
                    for ele2 in ele:
                        if k in visited_countries:
                            poly = self.canevas.create_polygon(ele2, fill="green", outline="black")
                            self.canevas.tag_bind(poly, "<Button-1>", lambda event, name=k: self.show_country(name))
                        else:
                            poly = self.canevas.create_polygon(ele2, fill="white", outline="black")
                            self.canevas.tag_bind(poly, "<Button-1>", lambda event, name=k: self.show_country(name))
            elif self.map.list_depth(v) == 3:
                for ele in v:
                    if k in visited_countries:
                        poly = self.canevas.create_polygon(ele, fill="green", outline="black")
                        self.canevas.tag_bind(poly, "<Button-1>", lambda event, name=k: self.show_country(name))
                    else:
                        poly = self.canevas.create_polygon(ele, fill="white", outline="black")
                        self.canevas.tag_bind(poly, "<Button-1>", lambda event, name=k: self.show_country(name))


    def show_country(self, country):
        messagebox.showinfo(country, get_description(country))

    def show_reminders(self):
        reminders = get_incoming_trips(self.user.id)
        if len(reminders) > 0:
            message = f"Hi {self.user.username} !\n"
            for reminder in reminders:
                departure = get_country_name(reminder.departure_id)
                destination = get_country_name(reminder.destination_id)
                date = datetime.strftime(reminder.date, "%d/%m/%Y")
                today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                if (reminder.date - today).days == 0:
                    message += f"You have a trip from {departure} to {destination} today.\n"
                else:
                    message += f"You have a trip from {departure} to {destination} on {date}.\n"
            messagebox.showinfo("Reminders", message)

    def sign_out(self):
        if not messagebox.askokcancel("Sign out", "Are you sure you want to sign out ?"):
            return

        self.destroy()
        from View.SigninWindow import LoginWindow
        LoginWindow()