import json
from Model.Trip import Trip
from datetime import datetime

def get_all_trips_by_user_id(user_id):
    """
    Retrieves all trips for a given user ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: A list of Trip objects.
    """
    trips = []
    with open("Database/Entity/trips.json", "r") as file:
        data = json.load(file)
        for i in data:
            if i["user_id"] == user_id:
                departure_date = datetime.strptime(i["departure_date"], "%d/%m/%Y")
                return_date = datetime.strptime(i["return_date"], "%d/%m/%Y")
                trip = Trip(i["user_id"], i["departure_id"], i["destination_id"], departure_date, return_date, i["transport"], i["duration"], i["carbon_footprint"])
                trips.append(trip)
    return trips

def add_trip(user_id, departure_id, destination_id, departure_date, return_date, transport, duration, carbon_footprint):
    """
    Adds a new trip to the database.

    Args:
        user_id (int): The ID of the user.
        departure_id (int): The ID of the departure country.
        destination_id (int): The ID of the destination country.
        departure_date (datetime): The departure date.
        return_date (datetime): The return date.
        transport (str): The mode of transport.
        duration (float): The duration of the trip.
        carbon_footprint (float): The carbon footprint of the trip.

    Returns:
        bool: True if the trip was added successfully, False otherwise.
    """
    with open("Database/Entity/trips.json", "r") as file:
        trips = json.load(file)
        new_trip = {
            "user_id": user_id,
            "departure_id": departure_id,
            "destination_id": destination_id,
            "departure_date": departure_date.strftime("%d/%m/%Y"),
            "return_date": return_date.strftime("%d/%m/%Y"),
            "transport": transport,
            "duration": duration,
            "carbon_footprint": carbon_footprint
        }
        trips.append(new_trip)
    with open("Database/Entity/trips.json", "w") as file:
        json.dump(trips, file, indent=4)
    return True

def modify_trip(old_trip, new_departure_id, new_destination_id, new_departure_date, new_return_date, new_transport, new_duration, new_carbon_footprint):
    """
    Modifies an existing trip.

    Args:
        old_trip (Trip): The old Trip object to be modified.
        new_departure_id (int): The new departure country ID.
        new_destination_id (int): The new destination country ID.
        new_departure_date (datetime): The new departure date.
        new_return_date (datetime): The new return date.
        new_transport (str): The new mode of transport.
        new_duration (float): The new duration of the trip.
        new_carbon_footprint (float): The new carbon footprint of the trip.

    Returns:
        bool: True if the trip was modified successfully, False otherwise.
    """
    with open("Database/Entity/trips.json", "r") as file:
        trips = json.load(file)
        for i in trips:
            if i["user_id"] == old_trip.user_id and i["departure_id"] == old_trip.departure_id and i["destination_id"] == old_trip.destination_id and i["departure_date"] == old_trip.departure_date.strftime("%d/%m/%Y") and i["return_date"] == old_trip.return_date.strftime("%d/%m/%Y") and i["transport"] == old_trip.transport and i["carbon_footprint"] == old_trip.carbon_footprint:
                i["departure_id"] = new_departure_id
                i["destination_id"] = new_destination_id
                i["departure_date"] = new_departure_date.strftime("%d/%m/%Y")
                i["return_date"] = new_return_date.strftime("%d/%m/%Y")
                i["transport"] = new_transport
                i["duration"] = new_duration
                i["carbon_footprint"] = new_carbon_footprint
                with open("Database/Entity/trips.json", "w") as file:
                    json.dump(trips, file, indent=4)
                return True
    return False

def delete_trip(user_id, departure_id, destination_id, departure_date, return_date, transport, duration, carbon_footprint):
    """
    Deletes a trip from the database.

    Args:
        user_id (int): The ID of the user.
        departure_id (int): The ID of the departure country.
        destination_id (int): The ID of the destination country.
        departure_date (str): The departure date (in the format "%d/%m/%Y").
        return_date (str): The return date (in the format "%d/%m/%Y").
        transport (str): The mode of transport.
        duration (float): The duration of the trip.
        carbon_footprint (float): The carbon footprint of the trip.

    Returns:
        bool: True if the trip was deleted successfully, False otherwise.
    """
    with open("Database/Entity/trips.json", "r") as file:
        trips = json.load(file)
        for i in trips:
            if i["user_id"] == user_id and i["departure_id"] == departure_id and i["destination_id"] == destination_id and i["departure_date"] == departure_date and i["return_date"] == return_date and i["transport"] == transport and i["duration"] == duration and i["carbon_footprint"] == carbon_footprint:
                trips.remove(i)
                with open("Database/Entity/trips.json", "w") as file:
                    json.dump(trips, file, indent=4)
                return True
    return False
