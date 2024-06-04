import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from datetime import datetime
from tkcalendar import DateEntry
from Controller.TripController import update_planned_trip
from Controller.CountryController import get_country_id, get_all_countries_name
from Controller.MapController import get_country_name

class UpdateTripWindow(tk.Toplevel):
    def __init__(self, master, trip):
        ctk.set_appearance_mode("light")
        super().__init__()
        self.master = master
        self.user = master.user
        self.trip = trip
        self.title("Modify trip")
        self.resizable(False, False)
        self.config(bg = "#f5f6f9")

        self.list_countries = get_all_countries_name()
        
        # Load the background image
        self.background_image = tk.PhotoImage(file="View/pictures/bg_map.png")
        
        # Create a canvas and set the background image
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        # Title
        self.title1 = tk.Label(self, text="Modify your trip", bg="#f5f6f9", fg="#354f52", font=("Impact", 25, "bold"))
        self.canvas.create_window(250, 50, window=self.title1)

        # Label entry for the home country
        self.label1 = tk.Label(self, text="Choose your departure country", bg="#f5f6f9", fg="#354f52", font=("Arial", 11, "bold"))
        self.canvas.create_window(250, 100, window=self.label1)

        # Combo box for the departure country
        self.departure_country = ttk.Combobox(self, font=("Arial", 11, 'bold'), values=self.list_countries)
        self.departure_country.configure(state="readonly")
        self.departure_country.set("")
        self.departure_country.set(get_country_name(trip.departure_id))
        self.canvas.create_window(250, 130, window=self.departure_country)

        # Label entry for the destination country
        self.label2 = tk.Label(self, text="Choose the destination country", bg="#f5f6f9", fg="#354f52", font=("Arial", 11, "bold"))
        self.canvas.create_window(250, 170, window=self.label2)

        # Combo box for the destination country
        self.destination_country = ttk.Combobox(self, font=("Arial", 11, 'bold'), values=self.list_countries)
        self.destination_country.configure(state="readonly")
        self.destination_country.set("")
        self.destination_country.set(get_country_name(trip.destination_id))
        self.canvas.create_window(250, 200, window=self.destination_country)

        # Label entry for the departure date
        self.label3 = tk.Label(self, text="Choose the departure date", bg="#f5f6f9", fg="#354f52", font=("Arial", 11, "bold"))
        self.canvas.create_window(250, 240, window=self.label3)

        # Date picker for the departure date
        self.departure_date = DateEntry(self, date_pattern="dd/mm/yyyy")
        self.departure_date.configure(state="readonly")
        self.departure_date.set_date(trip.departure_date)
        self.canvas.create_window(250, 270, window=self.departure_date)

        # Label entry for the return date
        self.label4 = tk.Label(self, text="Choose the return date", bg="#f5f6f9", fg="#354f52", font=("Arial", 11, "bold"))
        self.canvas.create_window(250, 310, window=self.label4)

        # Date picker for the return date
        self.return_date = DateEntry(self, date_pattern="dd/mm/yyyy")
        self.return_date.configure(state="readonly")
        self.return_date.set_date(trip.return_date)
        self.canvas.create_window(250, 340, window=self.return_date)

        # Button to save the trip
        self.button1 = tk.Button(self, text="Modify your trip", font=("Arial", 11, 'bold'), bg='#354f52', fg="#f5f6f9", command=self.update_trip)
        self.canvas.create_window(250, 400, window=self.button1)

        self.mainloop()

    def update_trip(self):
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
            messagebox.showerror("Error", "Please type all fields")
            self.lift() 
        elif departure_country == destination_country:
            messagebox.showerror("Error", "Departure and destination countries must be different")
            self.lift() 
        elif return_date <= departure_date:
            messagebox.showerror("Error", "Return date must be after departure date")
            self.lift() 
        elif departure_date < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
            messagebox.showerror("Error", "Departure date must be in the future")
            self.lift() 
        else:
            departure_id = get_country_id(departure_country)
            destination_id = get_country_id(destination_country)
            is_added = update_planned_trip(self.trip, departure_id, destination_id, departure_date, return_date)
            if not is_added:
                messagebox.showerror("Error", "This trip conflicts with another trip")
                self.lift() 
            else:
                messagebox.showinfo("Success", "Trip added successfully")
                self.destroy()

                # Refresh the window
                from View.ShowAllTripsWindow import ShowAllTripsWindow
                ShowAllTripsWindow(self)
