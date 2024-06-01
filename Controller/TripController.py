from Repository.TripRepository import add_trip, modify_trip, delete_trip, get_all_trips_by_user_id
from datetime import datetime

def add_new_trip(user_id, departure_id, destination_id, departure_date, return_date):
    return add_trip(user_id, departure_id, destination_id, departure_date, return_date)

def update_planned_trip(user_id, country_id, date, new_date):
    # Check if the new date is in the future
    if new_date < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
        return False
    
    return modify_trip(user_id, country_id, date, new_date)

def delete_planned_trip(user_id, country_id, date):
    return delete_trip(user_id, country_id, date)