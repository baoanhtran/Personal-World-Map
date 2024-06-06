import tkinter as tk
import customtkinter as ctk
from Controller.MapController import get_description, get_despcriptions_monuments
from View.PlanNewTripWindow import PlanNewTripWindow


class InfoCountryWindow(tk.Toplevel): # ENORA
    __slots__ = ["user", "country_destination"]

    def __init__(self, master, country_destination):
        super().__init__()
        self.master = master
        self.country_destination = country_destination
        self.user = master.user
        self.geometry("500x600")
        self.resizable(False, False)
        self.title("Plan a new trip")
        self.config(bg = "#f5f6f9")
        string_monuments = get_despcriptions_monuments(self.country_destination)

        # Title
        self.title1 = ctk.CTkLabel(self, text=f'{self.country_destination}', text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Impact", 22) ,height=2)
        self.title1.pack(side = "top", padx= 20, pady= 20)


        # Text for the description
        self.description = ctk.CTkLabel(self, text = get_description(self.country_destination), text_color= "#f5f6f9", fg_color= '#354f52', corner_radius= 32,   font=("Arial", 12, "bold") ,height = 180, width = 450, wraplength=400)
        self.description.pack(side = "top")

        # Title for the monuments
        self.title_monuments = ctk.CTkLabel(self, text="Monuments to visit :", text_color= '#354f52', fg_color="#f5f6f9", bg_color= '#f5f6f9', corner_radius= 32,   font=("Impact", 17))
        self.title_monuments.pack(side = "top",padx= 15, pady= 15)

        # Text for the monuments
        self.monuments = ctk.CTkLabel(self, text=string_monuments, text_color= "#f5f6f9", fg_color= '#354f52', bg_color= '#f5f6f9', corner_radius= 32,   font=("Arial", 11, "bold"), height = 100, width = 450, wraplength=400, compound = "center")
        self.monuments.pack(side = "top")

        # Button to plan a trip
        self.button1 = ctk.CTkButton(self, text = f"Plan a trip to {self.country_destination}", font = ("Arial", 14, 'bold'), width = 200, height = 30, fg_color= '#c06848', corner_radius = 10)
        self.button1.pack(side = "top", padx= 20, pady= 20)
        self.button1.bind("<Button-1>", self.plan_new_trip)

        self.mainloop()
    
    def plan_new_trip(self, event):
        # Unbind the button
        self.button1.unbind("<Button-1>")
        self.after(100, self.open_plan_new_trip)

    def open_plan_new_trip(self):
        self.destroy()
        PlanNewTripWindow(self, self.country_destination)

    def quit(self):
        self.destroy()