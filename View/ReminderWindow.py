import customtkinter as ctk
from PIL import Image, ImageTk, ImageSequence
import tkinter as tk


class TripReminder(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Trip Reminder")
        self.geometry("400x450")

        # Center the window on the screen
        self.center_window()

        # Load the animated GIF using PIL
        self.bg_image = Image.open("pictures/airplane-travel.gif")
        self.frames = [ImageTk.PhotoImage(frame.resize((400, 450), Image.LANCZOS)) for frame in
                       ImageSequence.Iterator(self.bg_image)]

        # Create a canvas to place the background image
        self.canvas = tk.Canvas(self, width=450, height=450)
        self.canvas.pack(fill="both", expand=True)
        self.canvas_image = self.canvas.create_image(0, 0, anchor="nw", image=self.frames[0])

        # Start the animation
        self.current_frame = 0
        self.animate()

        # Create and place the widgets
        self.create_widgets()

    def center_window(self):
        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate position x and y coordinates
        x = (screen_width // 2) - (400 // 2)
        y = (screen_height // 2) - (450 // 2)

        self.geometry(f'{400}x{450}+{x}+{y}')

    def animate(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.canvas.itemconfig(self.canvas_image, image=self.frames[self.current_frame])
        self.after(30, self.animate)  # Adjust the delay as needed for the GIF's frame rate

    def create_widgets(self):
        # Create labels and entry directly on the canvas
        self.label_country = ctk.CTkLabel(self, text="Destination Country:", bg_color="#ADD8E6")
        self.label_country.place(x=50, y=120)

        # self.entry_country = ctk.CTkLabel(self, text=f"{destination_country}")
        # self.entry_country.place(x=200, y=120)

        self.label_city = ctk.CTkLabel(self, text="Departure Country:", bg_color="#ADD8E6")
        self.label_city.place(x=50, y=180)

        # self.entry_city = ctk.CTkLabel(self, text=f"{departure_country}")
        # self.entry_city.place(x=200, y=180)

        self.label_time = ctk.CTkLabel(self, text="Scheduled Time:", bg_color="#ADD8E6")
        self.label_time.place(x=50, y=240)

        self.entry_time = ctk.CTkEntry(self)
        self.entry_time.place(x=200, y=240)

        self.button_show = ctk.CTkButton(self, text="Fully aware of my DUTY!", command=self.quit)
        self.button_show.place(x=100, y=300)

    def quit(self):
        self.destroy()


if __name__ == "__main__":
    app = TripReminder()
    app.mainloop()
