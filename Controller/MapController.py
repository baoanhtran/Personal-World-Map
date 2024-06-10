from Repository.TripRepository import get_all_trips_by_user_id
from Repository.CountryRepository import get_country_name_by_id, get_description_by_name, get_country_id_by_name
from Repository.MonumentRepository import get_list_of_monuments_by_country_id
from datetime import datetime

def get_country_name(country_id):
    """
    Retrieves the name of a country given its ID.
    
    Args:
        country_id (int): The ID of the country.
        
    Returns:
        str: The name of the country.
    """
    return get_country_name_by_id(country_id)

def get_description(country_name):
    """
    Retrieves the description of a country given its name.
    
    Args:
        country_name (str): The name of the country.
        
    Returns:
        str: The description of the country.
    """
    return get_description_by_name(country_name)

def get_incoming_trips(user_id):
    """
    Retrieves a list of upcoming trips for a user within the next 7 days.
    
    Args:
        user_id (int): The ID of the user.
        
    Returns:
        list: A list of upcoming trips.
    """
    reminders = []
    for trip in get_all_trips_by_user_id(user_id):
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        if 0 <= (trip.departure_date - today).days <= 7:
            reminders.append(trip)

    return reminders

def get_all_countries_visited(user_id):
    """
    Retrieves a list of all countries a user has visited.
    
    Args:
        user_id (int): The ID of the user.
        
    Returns:
        list: A list of names of countries visited.
    """
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
    """
    Retrieves a list of all countries a user plans to visit.
    
    Args:
        user_id (int): The ID of the user.
        
    Returns:
        list: A list of names of countries to visit.
    """
    countries = []
    for trip in get_all_trips_by_user_id(user_id):
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        if trip.departure_date >= today:
            destination = get_country_name(trip.destination_id)
            if destination not in countries:
                countries.append(destination)

    return countries

def get_descriptions_monuments(country_name):
    """
    Retrieves descriptions of all monuments in a given country.
    
    Args:
        country_name (str): The name of the country.
        
    Returns:
        str: A formatted string of descriptions of monuments in the country.
    """
    country_id = get_country_id_by_name(country_name)
    monuments_list = get_list_of_monuments_by_country_id(country_id)
    text = "\n\n"
    for monument in monuments_list:
        text += str(monument) + "\n"
    return text
