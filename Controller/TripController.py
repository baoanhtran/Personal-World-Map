from Repository.TripRepository import add_trip, modify_trip, delete_trip
from Repository.CountryRepository import get_country_id_by_name
from datetime import datetime

def get_country_id_by_name(country_name):
    return get_country_id_by_name(country_name)

def add_new_trip(user_id, country_id, date):
    # Check if the date is in the future
    if date < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
        return False
    
    add_trip(user_id, country_id, date)
    return True

def update_planned_trip(user_id, country_id, date, new_trip):
    # Check if the date is in the future
    if new_trip.date <= datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
        return False
    
    return modify_trip(user_id, country_id, date, new_trip)

def delete_planned_trip(user_id, country_id, date):
    return delete_trip(user_id, country_id, date)