import customtkinter as ctk
from tkinter import PhotoImage
from Controller.MapController import get_incoming_trips,get_country_name

class TripReminder(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Trip Reminder")
        self.geometry("400x600")

        # Set the background color to light blue
        self.configure(bg="#ADD8E6")

        # Center the window on the screen
        self.center_window()

        # Load and place the reminder symbol
        self.reminder_symbol = PhotoImage(file="pictures/map_icon.png")  # Make sure this path is correct
        self.symbol_label = ctk.CTkLabel(self, image=self.reminder_symbol, bg_color="#ADD8E6")
        self.symbol_label.grid(row=0, column=0, padx=20, pady=10, columnspan=2)

        # Create and place the widgets
        self.create_widgets()

    def center_window(self):
        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate position x and y coordinates
        x = (screen_width // 2) - (400 // 2)
        y = (screen_height // 2) - (600 // 2)

        self.geometry(f'400x600 + {x}+{y}')

    def create_widgets(self):

        # Label for destination Country
        self.label_country = ctk.CTkLabel(self, text="Destination Country:", bg_color="#ADD8E6")
        self.label_country.grid(row=1, column=0, padx=20, pady=10)
        destination_country = get_incoming_trips(self.user_id)
        self.entry_country = ctk.CTkLabel(self,text= f"{destination_country}")
        self.entry_country.grid(row=1, column=1, padx=20, pady=10)

        # Label and entry for departure country
        self.label_city = ctk.CTkLabel(self, text="Departure Country:", bg_color="#ADD8E6")
        self.label_city.grid(row=2, column=0, padx=20, pady=10)
        departure_country = get_country_name(self.country_id)
        self.entry_city = ctk.CTkLabel(self, text= f"{departure_country}")
        self.entry_city.grid(row=2, column=1, padx=20, pady=10)

        # Label and entry for Scheduled Time
        self.label_time = ctk.CTkLabel(self, text="Scheduled Time:", bg_color="#ADD8E6")
        self.label_time.grid(row=3, column=0, padx=20, pady=10)
        self.entry_time = ctk.CTkEntry(self)
        self.entry_time.grid(row=3, column=1, padx=20, pady=10)

        # Button to show the entered information
        self.button_show = ctk.CTkButton(self, text="Fullywared of my DUTY !!!!", command=self.quit)
        self.button_show.grid(row=4, column=0, columnspan=2, pady=20)

        # Label to acknowlage the result
        self.label_result = ctk.CTkLabel(self, text="ok", bg_color="#ADD8E6")
        self.label_result.grid(row=5, column=0, columnspan=2, pady=10)
    def quit(self):
        self.destroy()

if __name__ == "__main__":
    app = TripReminder()
    app.mainloop()
