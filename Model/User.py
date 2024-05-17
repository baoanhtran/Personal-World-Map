import datetime

class User:
    __slots__ = ["id", "username", "password", "carbon_footprint"]

    def __init__(self, id, username, password, carbon_footprint):
        self.id = id
        self.username = username
        self.password = password
        self.carbon_footprint = carbon_footprint

    def __str__(self):
        return f"User {self.username} with id {self.id} has a carbon footprint of {self.carbon_footprint}."
    
    def __eq__(self, other):
        return self.id == other.id
    
    # def add_trip(self, trip):
    #     self.trips.append(trip)
    
    def add_carbon_footprint(self, carbon_footprint):
        self.carbon_footprint += carbon_footprint