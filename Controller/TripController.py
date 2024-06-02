from Repository.TripRepository import add_trip, modify_trip, delete_trip, get_all_trips_by_user_id
from datetime import datetime

def add_new_trip(user_id, departure_id, destination_id, departure_date, return_date):
    # Check if the departure date, return date have conflict with other trips
    all_trips = get_all_trips_by_user_id(user_id)
    for trip in all_trips:
        if (departure_date >= trip.departure_date and departure_date <= trip.return_date) \
            or (return_date >= trip.departure_date and return_date <= trip.return_date) \
            or (departure_date <= trip.departure_date and return_date >= trip.return_date):

            return False
            
    return add_trip(user_id, departure_id, destination_id, departure_date, return_date)

def update_planned_trip(user_id, departure_id, destination_id, departure_date, return_date, new_trip):
    # Check if the departure date, return date have conflict with other trips
    all_trips = get_all_trips_by_user_id(user_id)
    for trip in all_trips:
        if (new_trip.departure_date >= trip.departure_date and new_trip.departure_date <= trip.return_date) \
            or (new_trip.return_date >= trip.departure_date and new_trip.return_date <= trip.return_date) \
            or (new_trip.departure_date <= trip.departure_date and new_trip.return_date >= trip.return_date):

            return False
        
    return modify_trip(user_id, departure_id, destination_id, departure_date, return_date, new_trip)

def delete_planned_trip(user_id, departure_id, destination_id, departure_date, return_date):
    return delete_trip(user_id, departure_id, destination_id, departure_date, return_date)

def get_all_past_trips(user_id):
    all_trips = get_all_trips_by_user_id(user_id)
    past_trips = []
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    for trip in all_trips:
        if trip.departure_date < today:
            past_trips.append(trip)

    # Sort the list of past trips by departure date
    past_trips.sort(key=lambda x: x.departure_date, reverse=True) # Reverse the list to have the most recent trip first
            
    return past_trips

def get_all_upcoming_trips(user_id):
    all_trips = get_all_trips_by_user_id(user_id)
    upcoming_trips = []
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    for trip in all_trips:
        if trip.departure_date >= today:
            upcoming_trips.append(trip)

    # Sort the list of upcoming trips by departure date
    upcoming_trips.sort(key=lambda x: x.departure_date, reverse=True) # Reverse the list to have the most recent trip first
            
    return upcoming_trips