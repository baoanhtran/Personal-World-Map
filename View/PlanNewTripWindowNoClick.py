import tkinter as tk
import customtkinter as ctk
from PIL import Image
from Controller.TripController import add_new_trip
from Repository.CountryRepository import get_country_id_by_name
from tkinter import messagebox

class PlanNewTripWindowNoClick(ctk.CTk):
    __slots__ = ["user", "country_destination", "arrival_date", "departure_date"]

    def __init__(self, user, country_destination):
        super().__init__()
        self.country_destination = country_destination
        self.country_destination_id = get_country_id_by_name(country_destination)
        self.geometry("500x500")
        self.title("Plan a new trip")
        self.config(bg = "#f5f6f9")
        self.user = user
    
        # Quit button
        quit_button = ctk.CTkButton(self, text="Quit", text_color= "#f5f6f9", fg_color= '#354f52', font=("Arial", 28, "bold"), hover_color = "#74a098", border_color = '#354f52', width = 500)
        quit_button.place(x = 0, y = 0)
        quit_button.bind("<Button-1>", self.quit)

        # Title
        self.title1 = ctk.CTkLabel(self, text=f'Plan your trip to {self.country_destination}', text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Impact", 25, "bold") ,height=2)
        self.title1.place(x = 130, y = 50)

        # Label entry for the home country
        self.label1 = ctk.CTkLabel(self, text="Enter your country of departure (in English)", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label1.place(x = 150, y = 100)
        
        # Entry for the home country
        self.home_country = ctk.CTkEntry(self, font = ("Arial", 11, 'bold'), width= 150, height = 20, text_color = '#354f52')
        self.home_country.place(x = 175, y = 125)

        # Label entry for the departure date
        self.label2 = ctk.CTkLabel(self, text="Enter the departure date (DD/MM/YYYY format)", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label2.place(x = 150, y = 175)
        
        # Entry for the home country
        self.departure_date = ctk.CTkEntry(self, font = ("Arial", 11, 'bold'), width= 150, height = 20, text_color = '#354f52')
        self.departure_date.place(x = 175, y = 200)

        # Label entry for the arrival date
        self.label3 = ctk.CTkLabel(self, text="Enter the arrival date (DD/MM/YYYY format)", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label3.place(x = 150, y = 250)
        
        # Entry for the home country
        self.arrival_date = ctk.CTkEntry(self, font = ("Arial", 11, 'bold'), width= 150, height = 20, text_color = '#354f52')
        self.arrival_date.place(x = 175, y = 275)

        # Label for the Mean of transport
        self.label4 = ctk.CTkLabel(self, text="What is your main mean of transport", text_color='#354f52', fg_color= "#f5f6f9", corner_radius= 32,   font=("Arial", 11, "bold") ,height=2)
        self.label4.place(x = 150, y = 325)
        
        # Combo box for the mean of transport
        self.transport = ctk.CTkComboBox(self, font = ("Arial", 11, 'bold'), width= 150, height = 20, text_color = '#354f52', values = ["Train", "Car", "Plane", "Boat", "Bike"], dropdown_fg_color="#f5f6f9", dropdown_text_color='#354f52')
        self.transport.place(x = 175, y = 350)

        # Button to save the trip
        self.button1 = ctk.CTkButton(self, text = "Save your trip", font = ("Arial", 11, 'bold'), width = 200, height = 30, fg_color= '#354f52', corner_radius = 10)
        self.button1.place(x = 150, y = 410)
        self.button1.bind("<Button-1>", self.save_new_trip)
        self.mainloop()

    def save_new_trip(self, event):
        date = self.departure_date.get()
        departure_id = get_country_id_by_name(self.home_country.get())
        if add_new_trip(self.user.id, departure_id, self.country_destination_id, date):
            messagebox.showinfo(title = "Save your new trip", message = "Your new trip was added !")
        self.destroy()
    
    def quit(self, event):
        self.destroy()

        
