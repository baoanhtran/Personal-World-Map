from Repository.TripRepository import add_trip, modify_trip, delete_trip, get_all_trips_by_user_id
from Repository.CountryRepository import get_country_id_by_name, get_all_countries_name, get_country_name_by_id
from datetime import datetime

def add_new_trip(user_id, departure_country, destination_country, departure_date, return_date, transport, duration):
    if departure_country == "" or destination_country == "" or transport == "" or duration == "":
        return False, "Please type all fields"
    
    if departure_country == destination_country:
        return False, "Departure and destination countries must be different"
    
    if return_date < departure_date:
        return False, "Return date must be after departure date"
    
    if departure_date < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
        return False, "Departure date must be in the future"
    
    for trip in get_all_trips_by_user_id(user_id): # Check if the departure date, return date have conflict with other trips
        if (departure_date >= trip.departure_date and departure_date <= trip.return_date) \
            or (return_date >= trip.departure_date and return_date <= trip.return_date) \
            or (departure_date <= trip.departure_date and return_date >= trip.return_date):

            return False, "You already have a trip planned at this date"
        
    try:
        duration = float(duration)
    except ValueError:
        return False, "Duration must be a number"
    
    if duration <= 0:
        return False, "Duration must be positive"
    
    departure_id = get_country_id_by_name(departure_country)
    destination_id = get_country_id_by_name(destination_country)
    duration = float(duration)

    # Calculate the carbon footprint
    if transport == "Plane":
        carbon_footprint = 17.825 * duration
    elif transport == "Train":
        carbon_footprint = 1.77 * duration
    elif transport == "Car":
        carbon_footprint = 9.89 * duration
    elif transport == "Bus":
        carbon_footprint = 1.5 * duration
    elif transport == "Ferry":
        carbon_footprint = 1.8 * duration
    elif transport == "Bike":
        carbon_footprint = 0
    elif transport == "Foot":
        carbon_footprint = 0

    # Round the carbon footprint to 1 decimal places
    carbon_footprint = round(carbon_footprint, 1)

    return add_trip(user_id, departure_id, destination_id, departure_date, return_date, transport, duration, carbon_footprint), "Trip added successfully"

def update_planned_trip(old_trip, new_departure_country, new_destination_country, new_departure_date, new_return_date, new_transport, new_duration):

    if new_departure_country == "" or new_destination_country == "" or new_transport == "" or new_duration == "":
        return False, "Please type all fields"
    
    if new_departure_country == new_destination_country:
        return False, "Departure and destination countries must be different"
    
    if new_return_date < new_departure_date:
        return False, "Return date must be after departure date"
    
    if new_departure_date < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
        return False, "Departure date must be in the future"
    
    for trip in get_all_trips_by_user_id(old_trip.user_id):
        if trip.__eq__(old_trip):
            continue
        if (new_departure_date >= trip.departure_date and new_departure_date <= trip.return_date) \
            or (new_return_date >= trip.departure_date and new_return_date <= trip.return_date) \
            or (new_departure_date <= trip.departure_date and new_return_date >= trip.return_date):

            return False, "You already have a trip planned at this date"
        
    try:
        new_duration = float(new_duration)
    except ValueError:
        return False, "Duration must be a number"
    
    if new_duration <= 0:
        return False, "Duration must be positive"
        
    departure_id = get_country_id_by_name(new_departure_country)
    destination_id = get_country_id_by_name(new_destination_country)

    # Calculate the carbon footprint
    if new_transport == "Plane":
        carbon_footprint = 17.825 * new_duration
    elif new_transport == "Train":
        carbon_footprint = 1.77 * new_duration
    elif new_transport == "Car":
        carbon_footprint = 9.89 * new_duration
    elif new_transport == "Bus":
        carbon_footprint = 1.5 * new_duration
    elif new_transport == "Ferry":
        carbon_footprint = 1.8 * new_duration
    elif new_transport == "Bike":
        carbon_footprint = 0
    elif new_transport == "Foot":
        carbon_footprint = 0

    # Round the carbon footprint to 1 decimal places
    carbon_footprint = round(carbon_footprint, 1)

    return modify_trip(old_trip, departure_id, destination_id, new_departure_date, new_return_date, new_transport, new_duration, carbon_footprint), "Trip modified successfully"

def delete_planned_trip(user_id, departure_country, destination_country, departure_date, return_date, transport, duration, carbon_footprint):
    departure_id = get_country_id_by_name(departure_country)
    destination_id = get_country_id_by_name(destination_country)

    # Convert duration and carbon_footprint to float
    duration = float(duration)
    carbon_footprint = float(carbon_footprint)

    return delete_trip(user_id, departure_id, destination_id, departure_date, return_date, transport, duration, carbon_footprint), "Trip deleted successfully"

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
    upcoming_trips.sort(key=lambda x: x.departure_date, reverse=False)
            
    return upcoming_trips

def get_all_countries_without_chosen(country):
    all_countries = get_all_countries_name()
    if country is not None:
        all_countries.remove(country)
    return all_countries

def get_country_name(country_id):
    return get_country_name_by_id(country_id)

def get_country_id(country_name):
    return get_country_id_by_name(country_name)