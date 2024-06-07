from Repository.TripRepository import get_all_trips_by_user_id
from Repository.CountryRepository import get_country_name_by_id, get_description_by_name, get_country_id_by_name
from Repository.MonumentRepository import get_list_of_monuments_by_country_id
from datetime import datetime

def get_country_name(country_id):
    return get_country_name_by_id(country_id)

def get_description(country_name):
    return get_description_by_name(country_name)

def get_incoming_trips(user_id):
    reminders = []
    for trip in get_all_trips_by_user_id(user_id):
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        if (trip.departure_date - today).days <= 7 and (trip.departure_date - today).days >= 0:
            reminders.append(trip)

    return reminders

def get_all_countries_visited(user_id):
    countries = []
    for trip in get_all_trips_by_user_id(user_id):
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        if trip.departure_date < today:
            departure = get_country_name(trip.departure_id)
            destination = get_country_name(trip.destination_id)
            if departure not in countries:
                countries.append(departure)
            if destination not in countries:
                countries.append(destination)

    return countries

def get_all_countries_to_visit(user_id):
    countries = []
    for trip in get_all_trips_by_user_id(user_id):
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        if trip.departure_date >= today:
            destination = get_country_name(trip.destination_id)
            if destination not in countries:
                countries.append(destination)

    return countries

def get_despcriptions_monuments(country_name):
    country_id = get_country_id_by_name(country_name)
    monuments_list = get_list_of_monuments_by_country_id(country_id)
    text = "\n\n"
    for monument in monuments_list:
        text += monument.__str__() + "\n"
    return text   