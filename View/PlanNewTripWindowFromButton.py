import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
from Controller.TripController import add_new_trip, get_all_countries_without_chosen

class PlanNewTripWindowFromButton(tk.Toplevel):
    __slots__ = ["user", "country_destination", "return_date", "departure_date", "list_countries"]

    def __init__(self, master, country_destination):
        super().__init__()
        
        self.master = master
        self.user = master.user
        self.country_destination = country_destination
        self.list_countries = get_all_countries_without_chosen(country_destination)
        self.geometry("500x500")
        self.config(bg = "#f5f6f9")
        self.resizable(False, False)
        self.title("Plan a new trip")

        # Title
        self.title1 = ctk.CTkLabel(self, text='Plan a new trip', text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Impact", 24) ,height=2)
        self.title1.pack(side = "top", padx = 30, pady = 30)

        # Label entry for the home country
        self.label1 = ctk.CTkLabel(self, text="Choose your departure country", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label1.pack(side = "top", padx= 10, pady = 10)

        # Combo box for the departure country
        self.departure_country = ctk.CTkComboBox(self, font=("Arial", 11, 'bold'), values=self.list_countries, text_color = '#354f52', dropdown_fg_color="#f5f6f9", dropdown_text_color='#354f52')
        self.departure_country.configure(state="readonly")
        self.departure_country.set("")
        self.departure_country.pack(side = "top")

        # Label entry for the destination country
        self.label2 = ctk.CTkLabel(self, text="Choose your destination country", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label2.pack(side = "top", padx= 10, pady = 10)

        # Combo box for the destination country
        self.destination_country = ctk.CTkComboBox(self, font=("Arial", 11, 'bold'), values=self.list_countries, text_color = '#354f52', dropdown_fg_color="#f5f6f9", dropdown_text_color='#354f52')
        self.destination_country.configure(state="readonly")
        self.destination_country.set("")
        if country_destination is not None:
            self.destination_country.set(country_destination)
            self.destination_country.configure(state="disabled")
        self.destination_country.pack(side = "top")

        # Label entry for the departure date
        self.label3 = ctk.CTkLabel(self, text="Choose the departure date", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label3.pack(side = "top", padx = 10, pady = 10)

        # Date picker for the departure date
        self.departure_date = DateEntry(self, date_pattern="dd/mm/yyyy")
        self.departure_date.configure(state="readonly")
        self.departure_date.pack(side = "top")

        # Label entry for the return date
        self.label3 = ctk.CTkLabel(self, text="Choose the return date", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label3.pack(side = "top", padx = 10, pady = 10)


        # Date picker for the return date
        self.return_date = DateEntry(self, date_pattern="dd/mm/yyyy")
        self.return_date.configure(state="readonly")
        self.return_date.pack(side = "top")

        # Button to save the trip
        self.button1 = ctk.CTkButton(self, text = "Save your trip", font = ("Arial", 11), width = 200, height = 30, fg_color= '#354f52', corner_radius = 10)
        self.button1.bind("<Button-1>", self.save_new_trip)
        self.button1.pack(side = "top", padx = 30, pady = 30)

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
        
        is_valid, message = add_new_trip(self.user.id, departure_country, destination_country, departure_date, return_date)

        if not is_valid:
            messagebox.showerror("Error", message)
            self.lift() 
        else:
            message += ". Update the map !"
            self.destroy()
            messagebox.showinfo("Success", message)
