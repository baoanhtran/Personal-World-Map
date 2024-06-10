import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk, ImageSequence
from tkinter import messagebox
from Model.Map import Map
from View.InfoCountryWindow import InfoCountryWindow
from View.PlanNewTripWindow import PlanNewTripWindow
from View.ShowAllTripsWindow import ShowAllTripsWindow
from View.TripReminderWindow import TripReminderWindow
from CustomWidget.ZoomableCanvas import ZoomableCanvas
from Controller.MapController import get_incoming_trips, get_all_countries_visited, get_all_countries_to_visit

class MapWindow(tk.Tk):
    """
    A window for displaying the personal world map and providing options for trip planning and management.

    Attributes:
        user: The current user object.
        canevas: The zoomable canvas for displaying the map.
        map: The map object containing country coordinates.
        bg_image: The background image for the animated map.
        frames: The frames of the animated map.
        quit_button: Button to quit the application.
        side_bar: Frame for displaying side bar buttons.
        top_spacer: Spacer frame to position side bar buttons.
        canva: Canvas for displaying icons on the top.
        button1: Button to show all trips.
        button2: Button to plan a new trip.
        button3: Button to change password.
        button4: Button to sign out.
        bottom_spacer: Spacer frame to position side bar buttons.
        current_frame: The current frame of the animated map.
    """
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.attributes("-fullscreen", True)
        self.title("Personal World Map")

        # ICONS
        icon1 = tk.PhotoImage(file="View/pictures/map_icon.png")
        icon2 = Image.open("View/pictures/icon_suitcase.png")
        icon3 = Image.open("View/pictures/plan_icon.png")
        icon4 = Image.open("View/pictures/pw_icon.png")
        icon5 = Image.open("View/pictures/log_out_icon.png")
        icon6 = Image.open("View/pictures/quit_icon.png")

        # Load the animated GIF using PIL
        self.bg_image = Image.open("View/pictures/waves_map.gif")
        self.frames = [ImageTk.PhotoImage(frame.resize((self.winfo_screenwidth(), self.winfo_screenheight()), Image.LANCZOS)) for frame in
                   ImageSequence.Iterator(self.bg_image)]

        # Quit button
        self.quit_button = ctk.CTkButton(self, text="Quit", text_color= "#f5f6f9", fg_color= '#354f52', font=("Arial", 28, "bold"), hover_color = "#e2eafc", border_color = '#354f52',  image = ctk.CTkImage(dark_image=icon6, light_image=icon6))
        self.quit_button.bind("<Button-1>", self.quit)
        self.quit_button.pack(side="top", fill="x")

        # Side bar containing 3 buttons
        self.side_bar = ctk.CTkFrame(self, fg_color='#354f52', border_color = '#354f52')
        self.side_bar.pack(side="right", fill="y")

        # Spacer frame to push buttons to the center
        self.top_spacer = ctk.CTkFrame(self.side_bar, fg_color='#354f52', border_color = '#354f52')
        self.top_spacer.pack(side="top", expand=True)

        # Icon on top
        self.canva = ctk.CTkCanvas(self.top_spacer, bg='#354f52', highlightthickness = 0)
        self.canva.pack(expand="YES")
        self.canva.create_image(self.canva.winfo_reqwidth()/2, self.canva.winfo_reqheight()/2, image=icon1, anchor = "center")

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
        # Start the animation
        self.current_frame = 0
        self.animate()
        self.canevas.pack(side="left")
        
        # Reminders
        self.after(500, self.show_reminders)

        self.mainloop()

    def quit(self, event):
        """Close the window."""
        self.destroy()

    def animate(self):
        """Animate the map."""
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.canevas.itemconfig(self.canvas_image, image=self.frames[self.current_frame])
        self.after(1000, self.animate) # Adjust the delay as needed for the GIF's frame rate

    def draw(self):
        """Draw the map with visited and to visit countries highlighted."""
        visited_countries = get_all_countries_visited(self.user.id)
        to_visit_countries = get_all_countries_to_visit(self.user.id)
        self.canevas.delete("all")
        self.canvas_image = self.canevas.create_image(self.winfo_screenwidth()//2, self.winfo_screenheight()//2, anchor="center", image=self.frames[0])

        for (k, v) in self.map.coordinates_dict.items():
            if k in to_visit_countries:
                color_shape = "#c06848"
            elif k in visited_countries:
                color_shape = "#adb944"
            else:
                color_shape = "#f5f6f9"
                
            if self.map.list_depth(v) == 4: # Country of multiple polygons
                for ele in v:
                    for ele2 in ele:
                        poly = self.canevas.create_polygon(ele2, fill=color_shape, outline="#354f52")
                        self.canevas.tag_bind(poly, "<Double-Button-1>", lambda event, name=k: self.show_country(name))
            elif self.map.list_depth(v) == 3: # Country of one polygon
                for ele in v:
                    poly = self.canevas.create_polygon(ele, fill=color_shape, outline="#354f52")
                    self.canevas.tag_bind(poly, "<Double-Button-1>", lambda event, name=k: self.show_country(name))

    def show_country(self, country):
        """Show the country information window."""
        InfoCountryWindow(self, country)
        
    def show_reminders(self):
        """Show the trip reminders window."""
        reminders = get_incoming_trips(self.user.id)
        if len(reminders) > 0:
            TripReminderWindow(self, reminders)
            
    def show_all_trips(self, event):
        """Show the window with all trips."""
        ShowAllTripsWindow(self)

    def plan_new_trip(self, event):
        """Open the window for planning a new trip."""
        PlanNewTripWindow(self, None) # None for no country selected

    def change_password(self, event):
        """Open the window for changing the password."""
        from View.ChangePasswordWindow import ChangePasswordWindow
        ChangePasswordWindow(self)

    def sign_out(self):
        """Sign out of the application."""
        if not messagebox.askokcancel("Sign out", "Are you sure you want to sign out ?"):
            return

        # Unbind all events
        self.button1.unbind("<Button-1>")
        self.button2.unbind("<Button-1>")
        self.button3.unbind("<Button-1>")
        self.button4.unbind("<Button-1>")
        self.canevas.unbind("<Button-1>")
        self.quit_button.unbind("<Button-1>")

        # Unbind all tag binds
        for tag in self.canevas.find_all():
            self.canevas.tag_unbind(tag, "<Double-Button-1>")

        # Stop the animation
        self.after_cancel(self.animate)

        # Destroy the window
        self.destroy()

        from View.SigninWindow import LoginWindow
        LoginWindow()