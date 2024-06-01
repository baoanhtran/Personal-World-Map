import tkinter as tk
import customtkinter as ctk
from tkcalendar import DateEntry
from Controller.TripController import add_new_trip
from Controller.CountryController import get_country_id, get_all_countries_name
from tkinter import messagebox
from datetime import datetime

class PlanNewTripWindow(tk.Tk):
    __slots__ = ["user", "country_destination", "return_date", "departure_date", "list_countries"]

    def __init__(self, user, country_destination):
        super().__init__()
        self.country_destination = country_destination
        self.list_countries = get_all_countries_name()
        if country_destination is not None:
            # Remove the country from the list of countries
            self.list_countries.remove(country_destination)
        self.geometry("400x500")
        self.resizable(False, False)
        self.title("Plan a new trip")
        self.config(bg = "#f5f6f9")
        self.user = user

        # Title
        self.title1 = ctk.CTkLabel(self, text="Plan your trip", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Impact", 25, "bold") ,height=2)
        self.title1.pack(padx= 10, pady= 10)

        # Label entry for the home country
        self.label1 = ctk.CTkLabel(self, text="Choose your departure country", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label1.pack(padx= 10, pady= 10)

        # Combo box for the departure country
        self.departure_country = ctk.CTkComboBox(self, font = ("Arial", 11, 'bold'), width= 150, height = 20, text_color = '#354f52', values = self.list_countries, dropdown_fg_color="#f5f6f9", dropdown_text_color='#354f52')
        self.departure_country.pack(padx= 10, pady= 10)
        self.departure_country.configure(state="readonly")
        self.departure_country.set("")

        # Label entry for the destination country
        self.label2 = ctk.CTkLabel(self, text="Choose the destination country", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label2.pack(padx= 10, pady= 10)

        # Combo box for the destination country
        self.destination_country = ctk.CTkComboBox(self, font=("Arial", 11, 'bold'), width=150, height=20, text_color='#354f52', values=self.list_countries, dropdown_fg_color="#f5f6f9", dropdown_text_color='#354f52')
        self.destination_country.pack(padx=10, pady=10)
        self.destination_country.configure(state="readonly")
        self.destination_country.set("")
        if country_destination is not None:
            self.destination_country.set(country_destination)
            self.destination_country.configure(state="disabled")

        # Label entry for the departure date
        self.label2 = ctk.CTkLabel(self, text="Choose the departure date", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label2.pack(padx= 10, pady= 10)

        # Date picker for the departure date
        self.departure_date = DateEntry(self, date_pattern="dd/mm/yyyy")
        self.departure_date.pack(padx= 10, pady= 10)
        self.departure_date.configure(state="readonly")

        # Label entry for the return date
        self.label3 = ctk.CTkLabel(self, text="Choose the return date", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label3.pack(padx= 10, pady= 10)

        # Date picker for the return date
        self.return_date = DateEntry(self, date_pattern="dd/mm/yyyy")
        self.return_date.pack(padx= 10, pady= 10)
        self.return_date.configure(state="readonly")

        # Button to save the trip
        self.button1 = ctk.CTkButton(self, text = "Save your trip", font = ("Arial", 11, 'bold'), width = 200, height = 30, fg_color= '#354f52', corner_radius = 10)
        self.button1.pack(padx= 10, pady= 10)
        self.button1.bind("<Button-1>", self.save_new_trip)
        self.mainloop()

    def save_new_trip(self, event):
        departure_country = self.departure_country.get()
        destination_country = self.destination_country.get()
        departure_date = self.departure_date.get_date()
        return_date = self.return_date.get_date()

        # Convert the date to a string
        departure_date = departure_date.strftime("%Y-%m-%d")
        return_date = return_date.strftime("%Y-%m-%d")

        # Convert the date to a datetime object
        departure_date = datetime.strptime(departure_date, "%Y-%m-%d")
        return_date = datetime.strptime(return_date, "%Y-%m-%d")
        

        if departure_country == "" or destination_country == "":
            if hasattr(self, "label4"):
                self.label4.destroy()

            self.label4 = ctk.CTkLabel(self, text="Please type all fields", text_color='#eb4934', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
            self.label4.pack(padx= 10, pady= 10)

        elif departure_country == destination_country:
            if hasattr(self, "label4"):
                self.label4.destroy()

            self.label4 = ctk.CTkLabel(self, text="Departure and destination countries must be different", text_color='#eb4934', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
            self.label4.pack(padx= 10, pady= 10)

        elif return_date <= departure_date:
            if hasattr(self, "label4"):
                self.label4.destroy()

            self.label4 = ctk.CTkLabel(self, text="Return date must be after departure date", text_color='#eb4934', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
            self.label4.pack(padx= 10, pady= 10)

        elif departure_date < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
            if hasattr(self, "label4"):
                self.label4.destroy()

            self.label4 = ctk.CTkLabel(self, text="Departure date must be in the future", text_color='#eb4934', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
            self.label4.pack(padx= 10, pady= 10)

        else:
            departure_id = get_country_id(departure_country)
            destination_id = get_country_id(destination_country)
            add_new_trip(self.user.id, departure_id, destination_id, departure_date, return_date)
            messagebox.showinfo("Success", "Trip added successfully")

            # Unbind events before destruction
            self.button1.unbind('<Button-1>')
            self.after(100, self.destroy)