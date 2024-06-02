import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from Controller.TripController import get_all_past_trips, get_all_upcoming_trips, delete_planned_trip
from Controller.MapController import get_country_name
from Controller.CountryController import get_country_id
from View.UpdateTripWindow import UpdateTripWindow
from Model.Trip import Trip
from datetime import datetime

class ShowAllTripsWindow(tk.Tk):
    def __init__(self, user):
        ctk.set_appearance_mode("light")

        super().__init__()
        self.user = user
        self.title("All my trips")
        self.resizable(False, False)

        # Title label
        title = ctk.CTkLabel(self, text="All my trips", font=("Arial", 30, "bold"), text_color="#f5f6f9", bg_color="#f5f6f9", fg_color="#354f52")
        title.pack(side="top", fill="x")

        # Show upcoming trips
        self.show_upcoming_trips()

        # Modify trip button
        modify_button = ctk.CTkButton(self, text = "Modify upcoming trip", font = ("Arial", 11, 'bold'), width = 200, height = 30, fg_color= '#354f52', corner_radius = 10)
        modify_button.bind("<Button-1>", self.modify_trip)
        modify_button.pack(side="top", pady=10)

        # Delete trip button
        delete_button = ctk.CTkButton(self, text = "Delete upcoming trip", font = ("Arial", 11, 'bold'), width = 200, height = 30, fg_color= '#354f52', corner_radius = 10)
        delete_button.bind("<Button-1>", self.delete_trip)
        delete_button.pack(side="top", pady=10)

        # Show past trips
        self.show_past_trips()

        self.mainloop()
    
    def show_past_trips(self):
        # Subtitle label
        subtitle = ctk.CTkLabel(self, text="Past trips", font=("Arial", 20, "bold"), text_color="#f5f6f9", bg_color="#f5f6f9", fg_color="#354f52")
        subtitle.pack(side="top", fill="x")

        # Display past trips in form of table
        past_trips = get_all_past_trips(self.user.id)
        self.past_tree = ttk.Treeview(self)
        # Choice not allowed
        self.past_tree["selectmode"] = "none"
        self.past_tree["columns"] = ("departure", "destination", "departure_date", "return_date")
        self.past_tree.column("#0", width=0, stretch=tk.NO)
        self.past_tree.column("departure", anchor=tk.W, width=200)
        self.past_tree.column("destination", anchor=tk.W, width=200)
        self.past_tree.column("departure_date", anchor=tk.W, width=200)
        self.past_tree.column("return_date", anchor=tk.W, width=200)
        self.past_tree.heading("#0", text="", anchor=tk.W)
        self.past_tree.heading("departure", text="Departure", anchor=tk.W)
        self.past_tree.heading("destination", text="Destination", anchor=tk.W)
        self.past_tree.heading("departure_date", text="Departure date", anchor=tk.W)
        self.past_tree.heading("return_date", text="Return date", anchor=tk.W)

        for trip in past_trips:
            departure = get_country_name(trip.departure_id)
            destination = get_country_name(trip.destination_id)
            self.past_tree.insert("", tk.END, text="", values=(departure, destination, trip.departure_date.strftime("%d/%m/%Y"), trip.return_date.strftime("%d/%m/%Y")))

        self.past_tree.pack(side="top", fill="x")

    def show_upcoming_trips(self):
        # Subtitle label
        subtitle = ctk.CTkLabel(self, text="Upcoming trips", font=("Arial", 20, "bold"), text_color="#f5f6f9", bg_color="#f5f6f9", fg_color="#354f52")
        subtitle.pack(side="top", fill="x")

        # Display upcoming trips in form of treeview
        upcoming_trips = get_all_upcoming_trips(self.user.id)
        self.upcoming_tree = ttk.Treeview(self)
        # Single choice
        self.upcoming_tree["selectmode"] = "browse"
        self.upcoming_tree["columns"] = ("departure", "destination", "departure_date", "return_date")
        self.upcoming_tree.column("#0", width=0, stretch=tk.NO)
        self.upcoming_tree.column("departure", anchor=tk.W, width=200)
        self.upcoming_tree.column("destination", anchor=tk.W, width=200)
        self.upcoming_tree.column("departure_date", anchor=tk.W, width=200)
        self.upcoming_tree.column("return_date", anchor=tk.W, width=200)
        self.upcoming_tree.heading("#0", text="", anchor=tk.W)
        self.upcoming_tree.heading("departure", text="Departure", anchor=tk.W)
        self.upcoming_tree.heading("destination", text="Destination", anchor=tk.W)
        self.upcoming_tree.heading("departure_date", text="Departure date", anchor=tk.W)
        self.upcoming_tree.heading("return_date", text="Return date", anchor=tk.W)

        for trip in upcoming_trips:
            departure = get_country_name(trip.departure_id)
            destination = get_country_name(trip.destination_id)
            self.upcoming_tree.insert("", tk.END, text="", values=(departure, destination, trip.departure_date.strftime("%d/%m/%Y"), trip.return_date.strftime("%d/%m/%Y")))
            
        self.upcoming_tree.pack(side="top", fill="x")

    def modify_trip(self, trip):
        # Get the values of the selected item
        selected_item = self.upcoming_tree.selection()
        if selected_item:
            departure, destination, departure_date, return_date = self.upcoming_tree.item(selected_item)["values"]
            departure_date = datetime.strptime(departure_date, "%d/%m/%Y")
            return_date = datetime.strptime(return_date, "%d/%m/%Y")
            trip = Trip(self.user.id, get_country_id(departure), get_country_id(destination), departure_date, return_date)
            self.destroy()
            UpdateTripWindow(self.user, trip)
        else:
            messagebox.showerror("Error", "Please select a trip to modify")
            self.lift()

    def delete_trip(self, trip):
        # Get the values of the selected item
        selected_item = self.upcoming_tree.selection()
        if selected_item:
            departure, destination, departure_date, return_date = self.upcoming_tree.item(selected_item)["values"]
            if not messagebox.askokcancel("Delete trip", f"Do you really want to delete the trip from {departure} to {destination} on {departure_date} ?"):
                return
            
            # Delete the trip
            departure_id = get_country_id(departure)
            destination_id = get_country_id(destination)
            is_deleted = delete_planned_trip(self.user.id, departure_id, destination_id, departure_date, return_date)
            if is_deleted:
                messagebox.showinfo("Success", "The trip has been deleted")
                # Refresh the window
                self.destroy()
                ShowAllTripsWindow(self.user)
        else:
            messagebox.showerror("Error", "Please select a trip to delete")
            self.lift()

    def quit(self, event):
        self.destroy()
