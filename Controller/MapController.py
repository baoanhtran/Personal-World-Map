from Repository.TripRepository import get_all_trips_by_user_id
from Repository.CountryRepository import get_country_name_by_id
from datetime import datetime

def get_country_name(country_id):
    return get_country_name_by_id(country_id)

def get_incoming_trips(user_id):
    reminders = []
    for trip in get_all_trips_by_user_id(user_id):
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        if (trip.date - today).days <= 7 and (trip.date - today).days >= 0:
            reminders.append(trip)

    return reminders