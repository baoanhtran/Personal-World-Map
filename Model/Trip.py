class Trip:
    __slots__ = ["user_id", "country_id", "date"]

    def __init__(self, user_id, country_id, date):
        self.user_id = user_id
        self.country_id = country_id
        self.date = date

    def __str__(self):
        return f"Trip from {self.departure} to {self.destination} on {self.date}."
    
    def distance(self):
        """
        Calculate the distance between the departure and the destination
        """