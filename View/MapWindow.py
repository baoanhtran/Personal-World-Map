import tkinter as tk
from tkinter import messagebox
from Model.Map import Map
from CustomWidget.ZoomableCanvas import ZoomableCanvas
from Controller.MapController import get_country_name, get_incoming_trips
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

        # Toggle side bar visibility
        # self.side_bar_visible = True
        # self.toggle_button = tk.Button(self, text="Hide action menu", background="cyan", foreground="black", font=("Courier", 10))
        # self.toggle_button.bind("<Button-1>", self.toggle_side_bar)
        # self.toggle_button.pack(side="top", fill="x")

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
        self.button4.pack(side="top", fill="x", pady=10, padx=10)

        # Map
        self.canevas = ZoomableCanvas(self, bg="#%02x%02x%02x" % (182, 255, 246), width=self.winfo_screenwidth(), height=self.winfo_screenheight())
        self.map = Map(self.winfo_screenwidth(), self.winfo_screenheight())
        self.draw()
        self.canevas.pack(side="left")

        # Reminders
        self.show_reminders()

    #     self.mainloop()

    # def toggle_side_bar(self, event):
    #     if self.side_bar_visible:
    #         # change the button text
    #         self.toggle_button.config(text="Show action menu")

    #         self.side_bar.pack_forget() # Hide the side bar
    #         self.side_bar_visible = False
    #     else:
    #         # change the button text
    #         self.toggle_button.config(text="Hide action menu")
            
    #         self.side_bar.pack(side="right", fill="y")
    #         self.side_bar_visible = True

            # Make the side bar on top of the canvas
            # self.canevas.pack_forget()
            # self.canevas.pack(side="left", fill="both")

    def quit(self, event):
        self.destroy()

    def draw(self):
        self.canevas.delete("all")
        for (k, v) in self.map.coordinates_dict.items():
            if self.map.list_depth(v) == 4:
                for ele in v:
                    for ele2 in ele:
                        poly = self.canevas.create_polygon(ele2, fill="white", outline="black")
                        self.canevas.tag_bind(poly, "<Button-1>", lambda event, name=k: self.show_country(name))
            elif self.map.list_depth(v) == 3:
                for ele in v:
                    poly = self.canevas.create_polygon(ele, fill="white", outline="black")
                    self.canevas.tag_bind(poly, "<Button-1>", lambda event, name=k: self.show_country(name))


    def show_country(self, country):
        print(country)

    def show_reminders(self):
        reminders = get_incoming_trips(self.user.id)
        if len(reminders) > 0:
            message = f"Hi {self.user.username} !\n"
            for reminder in reminders:
                country_name = get_country_name(reminder.country_id)
                date = datetime.strftime(reminder.date, "%d/%m/%Y")
                today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                if (reminder.date - today).days == 0:
                    message += f"You have a trip to {country_name} today.\n"
                else:
                    message += f"You have an incoming trip to {country_name} on {date}.\n"
            messagebox.showinfo("Reminders", message)