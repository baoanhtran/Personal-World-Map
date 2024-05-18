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
                trip = Trip(i["user_id"], i["country_id"], date)
                trips.append(trip)
                
    return trips

def add_trip(user_id, country_id, date):
    with open("Database/Entity/trips.json", "r") as file:
        trips = json.load(file)
        new_trip = {
            "user_id": user_id,
            "country_id": country_id,
            "date": date
        }
        trips.append(new_trip)
        
    with open("Database/Entity/trips.json", "w") as file:
        json.dump(trips, file, indent=4)

    trip_obj = Trip(user_id, country_id, date)    
    
    return trip_obj

def modify_trip(user_id, country_id, date, new_trip):
    with open("Database/Entity/trips.json", "r") as file:
        trips = json.load(file)
        for i in trips:
            if i["user_id"] == user_id and i["country_id"] == country_id and i["date"] == date:
                i["country_id"] = new_trip.country_id
                i["date"] = new_trip.date
                with open("Database/Entity/trips.json", "w") as file:
                    json.dump(trips, file, indent=4)
                trip_obj = Trip(user_id, country_id, date)
                return trip_obj
            
    return None

def delete_trip(user_id, country_id, date):
    with open("Database/Entity/trips.json", "r") as file:
        trips = json.load(file)
        for i in trips:
            if i["user_id"] == user_id and i["country_id"] == country_id and i["date"] == date:
                trips.remove(i)
                with open("Database/Entity/trips.json", "w") as file:
                    json.dump(trips, file, indent=4)
                return True
                
    return False