class Trip:
    __slots__ = ["user_id", "departure_id", "destination_id", "date"]

    def __init__(self, user_id, departure_id, destination_id, date):
        self.user_id = user_id
        self.departure_id = departure_id
        self.destination_id = destination_id
        self.date = date
    
    def distance(self):
        """
        Calculate the distance between the departure and the destination
        """