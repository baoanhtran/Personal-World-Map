import json
from Model.Trip import Trip
from datetime import datetime

def get_all_trips_by_user_id(user_id):
    trips = []
    with open("Database/Entity/trips.json", "r") as file:
        data = json.load(file)
        for i in data:
            if i["user_id"] == user_id:
                departure_date = datetime.strptime(i["departure_date"], "%d/%m/%Y")
                return_date = datetime.strptime(i["return_date"], "%d/%m/%Y")
                trip = Trip(i["user_id"], i["departure_id"], i["destination_id"], departure_date, return_date)
                trips.append(trip)
                
    return trips

def add_trip(user_id, departure_id, destination_id, departure_date, return_date):
    with open("Database/Entity/trips.json", "r") as file:
        trips = json.load(file)
        new_trip = {
            "user_id": user_id,
            "departure_id": departure_id,
            "destination_id": destination_id,
            "departure_date": departure_date.strftime("%d/%m/%Y"),
            "return_date": return_date.strftime("%d/%m/%Y")
        }
        trips.append(new_trip)
        
    with open("Database/Entity/trips.json", "w") as file:
        json.dump(trips, file, indent=4)

    # trip_obj = Trip(user_id, departure_id, destination_id, departure_date, return_date)    
    
    return True

def modify_trip(old_trip, new_departure_id, new_destination_id, new_departure_date, new_return_date):
    with open("Database/Entity/trips.json", "r") as file:
        trips = json.load(file)
        for i in trips:
            if i["user_id"] == old_trip.user_id and i["departure_id"] == old_trip.departure_id and i["destination_id"] == old_trip.destination_id and i["departure_date"] == old_trip.departure_date.strftime("%d/%m/%Y") and i["return_date"] == old_trip.return_date.strftime("%d/%m/%Y"):
                i["departure_id"] = new_departure_id
                i["destination_id"] = new_destination_id
                i["departure_date"] = new_departure_date.strftime("%d/%m/%Y")
                i["return_date"] = new_return_date.strftime("%d/%m/%Y")
                with open("Database/Entity/trips.json", "w") as file:
                    json.dump(trips, file, indent=4)
                return True
                
    return False

def delete_trip(user_id, departure_id, destination_id, departure_date, return_date):
    with open("Database/Entity/trips.json", "r") as file:
        trips = json.load(file)
        for i in trips:
            if i["user_id"] == user_id and i["departure_id"] == departure_id and i["destination_id"] == destination_id and i["departure_date"] == departure_date and i["return_date"] == return_date:
                trips.remove(i)
                with open("Database/Entity/trips.json", "w") as file:
                    json.dump(trips, file, indent=4)
                return True
                
    return False