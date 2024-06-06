import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from datetime import datetime
from tkcalendar import DateEntry
from Controller.TripController import update_planned_trip, get_all_countries_without_chosen, get_country_name

class UpdateTripWindow(tk.Toplevel):
    def __init__(self, master, trip):
        ctk.set_appearance_mode("light")
        super().__init__()
        self.master = master
        self.user = master.user
        self.trip = trip
        self.title("Modify trip")
        self.geometry("500x500")
        self.config(bg = "#f5f6f9")
        self.resizable(False, False)
        self.config(bg = "#f5f6f9")

        self.list_countries = get_all_countries_without_chosen(None)

        # Title
        self.title1 = ctk.CTkLabel(self, text='Modify your trip', text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Impact", 24) ,height=2)
        self.title1.pack(side = "top", padx = 30, pady = 30)

        # Label entry for the home country
        self.label1 = ctk.CTkLabel(self, text="Change your departure country", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label1.pack(side = "top", padx= 10, pady = 10)

        # Combo box for the departure country
        self.departure_country = ctk.CTkComboBox(self, font=("Arial", 11, 'bold'), values=self.list_countries, text_color = '#354f52', dropdown_fg_color="#f5f6f9", dropdown_text_color='#354f52')
        self.departure_country.configure(state="readonly")
        self.departure_country.set("")
        self.departure_country.set(get_country_name(trip.departure_id))
        self.departure_country.pack(side = "top")

        # Label entry for the destination country
        self.label2 = ctk.CTkLabel(self, text="Change your destination country", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label2.pack(side = "top", padx= 10, pady = 10)

        # Combo box for the destination country
        self.destination_country = ctk.CTkComboBox(self, font=("Arial", 11, 'bold'), values=self.list_countries, text_color = '#354f52', dropdown_fg_color="#f5f6f9", dropdown_text_color='#354f52')
        self.destination_country.configure(state="readonly")
        self.destination_country.set("")        
        self.destination_country.set(get_country_name(trip.destination_id))
        self.destination_country.pack(side = "top")

        # Label entry for the departure date
        self.label3 = ctk.CTkLabel(self, text="Change the departure date", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label3.pack(side = "top", padx = 20, pady = 20)

        # Date picker for the departure date
        self.departure_date = DateEntry(self, date_pattern="dd/mm/yyyy")
        self.departure_date.configure(state="readonly")
        self.departure_date.set_date(trip.departure_date)
        self.departure_date.pack()

        # Label entry for the return date
        self.label3 = ctk.CTkLabel(self, text="Change the return date", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label3.pack(side = "top", padx = 20, pady = 20)

        # Date picker for the return date
        self.return_date = DateEntry(self, date_pattern="dd/mm/yyyy")
        self.return_date.configure(state="readonly")
        self.return_date.set_date(trip.return_date)
        self.return_date.pack()

        # Button to save the trip
        self.button1 = ctk.CTkButton(self, text = "Save your changes", font = ("Arial", 11), width = 200, height = 30, fg_color= '#354f52', corner_radius = 10)
        self.button1.bind("<Button-1>", self.update_trip)
        self.button1.pack(side = "top", padx = 30, pady = 30)

        self.mainloop()

    def update_trip(self, event):
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

        is_valid, message = update_planned_trip(self.trip, departure_country, destination_country, departure_date, return_date)

        if not is_valid:
            messagebox.showerror("Error", message)
            self.lift()
        else:
            message += ". Update the map !"
            messagebox.showinfo("Success", message)
            self.destroy()

            # Refresh the window
            from View.ShowAllTripsWindow import ShowAllTripsWindow
            ShowAllTripsWindow(self.master)