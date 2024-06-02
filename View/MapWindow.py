import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk, ImageSequence
from tkinter import messagebox
from Model.Map import Map
from View.InfoCountryWindow import InfoCountryWindow
from View.PlanNewTripWindow import PlanNewTripWindow
from View.ShowAllTripsWindow import ShowAllTripsWindow
from CustomWidget.ZoomableCanvas import ZoomableCanvas
from Controller.MapController import get_country_name, get_incoming_trips, get_all_countries_visited
from datetime import datetime

class MapWindow(tk.Tk):
    __slots__ = ["canevas", "map", "canva"]

    def __init__(self, user):
        super().__init__()
        self.user = user
        self.attributes("-fullscreen", True)
        self.title("Personal World Map")

        # ICONS
        icon2 = Image.open("View/pictures/icon_suitcase.png")
        icon3 = Image.open("View/pictures/plan_icon.png")
        icon4 = Image.open("View/pictures/pw_icon.png")
        icon5 = Image.open("View/pictures/log_out_icon.png")
        icon6 = Image.open("View/pictures/quit_icon.png")

        # Quit button
        quit_button = ctk.CTkButton(self, text="Quit", text_color= "#f5f6f9", fg_color= '#354f52', font=("Arial", 28, "bold"), hover_color = "#e2eafc", border_color = '#354f52',  image = ctk.CTkImage(dark_image=icon6, light_image=icon6))
        quit_button.bind("<Button-1>", self.quit)
        quit_button.pack(side="top", fill="x")

        # Side bar containing 3 buttons
        self.side_bar = ctk.CTkFrame(self, fg_color='#354f52', border_color = '#354f52')
        self.side_bar.pack(side="right", fill="y")

        # Spacer frame to push buttons to the center
        self.top_spacer = ctk.CTkFrame(self.side_bar, fg_color='#354f52', border_color = '#354f52')
        self.top_spacer.pack(side="top", expand=True)

        # Icon1 on top (animated GIF)
        self.canva = ctk.CTkCanvas(self.top_spacer, bg='#354f52', highlightthickness=0, width=150, height=150)
        self.canva.pack(expand="YES")
        self.bg_image = Image.open("View/pictures/globe-world.gif")
        self.frames = [ImageTk.PhotoImage(frame.resize((150, 150), Image.LANCZOS)) for frame in
                       ImageSequence.Iterator(self.bg_image)]
        self.canvas_image = self.canva.create_image(75, 75, anchor="center", image=self.frames[0])
        self.current_frame = 0
        self.animate_globe()

        # Button to show all trips
        self.button1 = ctk.CTkButton(self.side_bar, text="Show all my trips", text_color="#f5f6f9", fg_color= "transparent", border_color = "#f5f6f9", hover_color = "#e2eafc", corner_radius= 32,   font=("Arial", 15, "bold") ,height=2, image = ctk.CTkImage(dark_image=icon2, light_image=icon2))
        self.button1.bind("<Button-1>", self.show_all_trips)
        self.button1.pack(side="top", pady=10, padx=10)

        # Button to plan a new trip
        self.button2 = ctk.CTkButton(self.side_bar, text="Plan a new trip", text_color="#f5f6f9", fg_color= "transparent", font=("Arial", 15, "bold"), hover_color = "#e2eafc",border_color = "#f5f6f9", corner_radius= 32, height=2, image = ctk.CTkImage(dark_image=icon3, light_image=icon3))
        self.button2.bind("<Button-1>", self.plan_new_trip)
        self.button2.pack(side="top", pady=10, padx=10)

        # Button to change password
        self.button3 = ctk.CTkButton(self.side_bar, text="Change password", text_color="#f5f6f9", fg_color= "transparent", font=("Arial", 15, "bold"), hover_color = "#e2eafc",border_color = "#f5f6f9", corner_radius= 32, height=2, image = ctk.CTkImage(dark_image=icon4, light_image=icon4))
        self.button3.bind("<Button-1>", self.change_password)
        self.button3.pack(side="top", pady=10, padx=10)

        # Button to sign out
        self.button4 = ctk.CTkButton(self.side_bar, text="Sign out", text_color="#f5f6f9", fg_color= "transparent", font=("Arial", 15, "bold"), hover_color = "#e2eafc",border_color = "#f5f6f9", corner_radius= 32,  height=2, image = ctk.CTkImage(dark_image=icon5, light_image=icon5))
        self.button4.bind("<Button-1>", lambda event: self.sign_out())
        self.button4.pack(side="bottom", pady=10, padx=10)

        # Spacer frame to keep buttons in the center
        self.bottom_spacer = ctk.CTkFrame(self.side_bar, fg_color='#354f52')
        self.bottom_spacer.pack(side="top", expand=True)

        # Map
        self.canevas = ZoomableCanvas(self, bg="#e2eafc", width=self.winfo_screenwidth(), height=self.winfo_screenheight())
        self.map = Map(self.winfo_screenwidth(), self.winfo_screenheight())
        self.draw()
        self.canevas.pack(side="left")

        # Reminders
        self.show_reminders()

        self.mainloop()
    def animate_globe(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.canva.itemconfig(self.canvas_image, image=self.frames[self.current_frame])
        self.after(100, self.animate_globe)  # Adjust the delay as needed for smoother animation

    def quit(self, event):
        self.destroy()

    def draw(self):
        visited_countries = get_all_countries_visited(self.user.id)
        self.canevas.delete("all")
        for (k, v) in self.map.coordinates_dict.items():
            if k in visited_countries:
                color_shape = "#eb4934"
            else:
                color_shape = "#f5f6f9"

            if self.map.list_depth(v) == 4:
                for ele in v:
                    for ele2 in ele:
                        poly = self.canevas.create_polygon(ele2, fill=color_shape, outline="#354f52")
                        self.canevas.tag_bind(poly, "<Double-Button-1>", lambda event, name=k: self.show_country(name))
            elif self.map.list_depth(v) == 3:
                for ele in v:
                    poly = self.canevas.create_polygon(ele, fill=color_shape, outline="#354f52")
                    self.canevas.tag_bind(poly, "<Double-Button-1>", lambda event, name=k: self.show_country(name))

    def show_country(self, country):
        InfoCountryWindow(self.user, country)

    def show_reminders(self):
        reminders = get_incoming_trips(self.user.id)
        if len(reminders) > 0:
            message = f"Hi {self.user.username} !\n"
            for reminder in reminders:
                departure = get_country_name(reminder.departure_id)
                destination = get_country_name(reminder.destination_id)
                departure_date = datetime.strftime(reminder.departure_date, "%d/%m/%Y")
                return_date = datetime.strftime(reminder.return_date, "%d/%m/%Y")
                today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                if (reminder.departure_date - today).days == 0:
                    message += f"You have a trip from {departure} to {destination} today and you will return on {return_date}.\n"
                else:
                    message += f"You have a trip from {departure} to {destination} on {departure_date} and you will return on {return_date}.\n"
            messagebox.showinfo("Reminders", message)

    def show_all_trips(self, event):
        ShowAllTripsWindow(self.user)

    def plan_new_trip(self, event):
        PlanNewTripWindow(self.user, None)

    def change_password(self, event):
        from View.ChangePasswordWindow import ChangePasswordWindow
        ChangePasswordWindow(self.user)

    def sign_out(self):
        if not messagebox.askokcancel("Sign out", "Are you sure you want to sign out ?"):
            return

        self.destroy()
        from View.SigninWindow import LoginWindow
        LoginWindow()
