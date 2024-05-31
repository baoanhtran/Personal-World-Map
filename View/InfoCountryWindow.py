import tkinter as tk
import customtkinter as ctk
from PIL import Image
from Repository.CountryRepository import get_description_by_name, get_country_id_by_name
from Repository.MonumentRepository import get_list_of_monuments_by_country_id, get_despcriptions_monuments_by_country_id
from View.PlanNewTripWindow import PlanNewTripWindow


class InfoCountryWindow(ctk.CTk): # ENORA
    __slots__ = ["user", "country_destination", "icon1"]

    def __init__(self, user, country_destination):
        super().__init__()
        self.country_destination = country_destination
        self.user = user
        self.geometry("500x500")
        self.title("Plan a new trip")
        self.config(bg = "#f5f6f9")
        self.country_id = get_country_id_by_name(country_destination)
        string_monuments = get_despcriptions_monuments_by_country_id(self.country_id)

        # Image import
        # self.icon1 = tk.PhotoImage(file="View/pictures/map_icon.png")

        # Background canva
        # self.canva = ctk.CTkCanvas(self, bg='#f5f6f9', highlightthickness = 0)
        # self.canva.create_image(self.canva.winfo_reqwidth()/2, self.canva.winfo_reqheight()/2, image=self.icon1, anchor = "center")
        # self.canva.pack(expand="YES")

        # Title
        self.title1 = ctk.CTkLabel(self, text=f'{self.country_destination}', text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Impact", 25, "bold") ,height=2)
        self.title1.pack(side = "top", padx= 20, pady= 20)


        # Text for the description
        self.description = ctk.CTkLabel(self, text = get_description_by_name(self.country_destination), text_color= "#f5f6f9", fg_color= '#354f52', corner_radius= 32,   font=("Arial", 12, "bold") ,height = 180, width = 450, wraplength=400)
        self.description.pack(side = "top")

        # Title for the monuments
        self.title_monuments = ctk.CTkLabel(self, text="Monuments to visit :", text_color= '#354f52', fg_color="#f5f6f9", bg_color= '#f5f6f9', corner_radius= 32,   font=("Impact", 17, "bold"))
        self.title_monuments.pack(side = "top",padx= 15, pady= 15)

        # Text for the monuments
        self.monuments = ctk.CTkLabel(self, text=string_monuments, text_color= "#f5f6f9", fg_color= '#354f52', bg_color= '#f5f6f9', corner_radius= 32,   font=("Arial", 11, "bold"), height = 100, width = 450, wraplength=400, compound = "center")
        self.monuments.pack(side = "top")

        # Button to plan a trip
        self.button1 = ctk.CTkButton(self, text = f"Plan a trip to {self.country_destination}", font = ("Arial", 11, 'bold'), width = 200, height = 30, fg_color= '#354f52', corner_radius = 10)
        self.button1.pack(side = "top", padx= 20, pady= 20)
        self.button1.bind("<Button-1>", self.plan_new_trip)

        self.mainloop()
    
    def plan_new_trip(self, event):
        PlanNewTripWindow(self.user, self.country_destination)
        self.destroy()
