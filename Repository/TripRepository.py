import json
from Model.Trip import Trip
from datetime import datetime

def get_all_trips_by_user_id(user_id):
    trips = []
    with open("Database/Entity/trips.json", "r") as file:
        data = json.load(file)
        for i in data:
            if i["user_id"] == user_id:
                date = datetime.strptime(i["date"], "%d/%m/%Y")
                trip = Trip(i["user_id"], i["departure_id"], i["destination_id"], date)
                trips.append(trip)
                
    return trips

def add_trip(user_id, departure_id, destination_id, date):
    with open("Database/Entity/trips.json", "r") as file:
        trips = json.load(file)
        new_trip = {
            "user_id": user_id,
            "departure_id": departure_id,
            "destination_id": destination_id,
            "date": date.strftime("%d/%m/%Y")
        }
        trips.append(new_trip)
        
    with open("Database/Entity/trips.json", "w") as file:
        json.dump(trips, file, indent=4)

    trip_obj = Trip(user_id, departure_id, destination_id, date)    
    
    return trip_obj

def modify_trip(user_id, departure_id, destination_id, date, new_trip):
    with open("Database/Entity/trips.json", "r") as file:
        trips = json.load(file)
        for i in trips:
            if i["user_id"] == user_id and i["departure_id"] == departure_id and i["destination_id"] == destination_id and i["date"] == date:
                i["departure_id"] = new_trip.departure_id
                i["destination_id"] = new_trip.destination_id
                i["date"] = new_trip.date.strftime("%d/%m/%Y")
                with open("Database/Entity/trips.json", "w") as file:
                    json.dump(trips, file, indent=4)
                return True
                
    return False

def delete_trip(user_id, departure_id, destination_id, date):
    with open("Database/Entity/trips.json", "r") as file:
        trips = json.load(file)
        for i in trips:
            if i["user_id"] == user_id and i["departure_id"] == departure_id and i["destination_id"] == destination_id and i["date"] == date:
                trips.remove(i)
                with open("Database/Entity/trips.json", "w") as file:
                    json.dump(trips, file, indent=4)
                return True
                
    return False