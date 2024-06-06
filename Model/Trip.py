class Trip:
    __slots__ = ["user_id", "departure_id", "destination_id", "departure_date", "return_date"]

    def __init__(self, user_id, departure_id, destination_id, departure_date, return_date):
        self.user_id = user_id
        self.departure_id = departure_id
        self.destination_id = destination_id
        self.departure_date = departure_date
        self.return_date = return_date

    def distance(self):
        """
        Calculate the distance between the departure and the destination
        """

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Trip):
            return False

        return self.user_id == value.user_id and self.departure_id == value.departure_id and self.destination_id == value.destination_id and self.departure_date == value.departure_date and self.return_date == value.return_date