import customtkinter as ctk
from PIL import Image, ImageTk, ImageSequence
import tkinter as tk
from tkinter import ttk
from Controller.TripController import get_all_upcoming_trips
from Controller.MapController import get_country_name

class TripReminder(ctk.CTk):
    def __init__(self,user):
        super().__init__()
        self.user = user
        self.title("Trip Reminder")
        self.geometry("400x500")

        # Center the window on the screen
        self.center_window()

        # Load the animated GIF using PIL
        self.bg_image = Image.open("View/pictures/airplane-travel.gif")
        self.frames = [ImageTk.PhotoImage(frame.resize((400, 500), Image.LANCZOS)) for frame in
                       ImageSequence.Iterator(self.bg_image)]

        # Create a canvas to place the background image
        self.canvas = tk.Canvas(self, width=400, height=500)
        self.canvas.pack(fill="both", expand=True)
        self.canvas_image = self.canvas.create_image(0, 0, anchor="nw", image=self.frames[0])

        # Start the animation
        self.current_frame = 0
        self.animate()

        # Create and place the widgets
        self.create_widgets()

        self.mainloop()
    def center_window(self):
        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate position x and y coordinates
        x = (screen_width // 2) - (400 // 2)
        y = (screen_height // 2) - (500 // 2)

        self.geometry(f'{400}x{500}+{x}+{y}')

    def animate(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.canvas.itemconfig(self.canvas_image, image=self.frames[self.current_frame])
        self.after(30, self.animate)  # Adjust the delay as needed for the GIF's frame rate

    def create_widgets(self):
        ## Create a Treeview widget
        self.create_table()

        self.button_show = ctk.CTkButton(self, text="Fully awared of my DUTY!", command=self.quit)
        self.button_show.place(x=100, y=350)

    def create_table(self):
        style = ttk.Style()
        style.configure("mystyle.Treeview",
                        background="#ADD8E6",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#ADD8E6")
        style.map('mystyle.Treeview', background=[('selected', '#ADD8E6')])

        columns = ('Departure', 'Destination', 'Departure Time')
        self.tree = ttk.Treeview(self, columns=columns, show='headings', style="mystyle.Treeview")
        self.tree.place(x=50, y=150, width=300, height=100)

        # Define headings
        self.tree.heading('Departure', text='Departure')
        self.tree.heading('Destination', text='Destination')
        self.tree.heading('Departure Time', text='Departure Time')

        # Insert sample data with alternating row colors
        trips = [
            ('New York', 'London', '2024-06-01'),
            ('Paris', 'Berlin', '2024-06-02'),
            ('Tokyo', 'Sydney', '2024-06-03'),
            ('Los Angeles', 'Tokyo', '2024-06-04'),
            ('San Francisco', 'Paris', '2024-06-05')
        ]

        for index, trip in enumerate(trips):
            self.tree.insert('', tk.END, values=trip, tags=('evenrow' if index % 2 == 0 else 'oddrow',))

        # Configure row tags for alternating colors
        self.tree.tag_configure('evenrow', background='#ADD8E6')
        self.tree.tag_configure('oddrow', background='#87CEEB')

        # Adjust column widths
        self.tree.column('Departure', width=60, anchor='center')
        self.tree.column('Destination', width=60, anchor='center')
        self.tree.column('Departure Time', width=60, anchor='center')
    def quit(self):
        self.destroy()


if __name__ == "__main__":
    app = TripReminder()
