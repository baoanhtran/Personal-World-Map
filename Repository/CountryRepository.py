import json
from Model.Country import Country

def get_list_of_countries():
    """
    Retrieves a list of Country objects from the countries.json file.

    Returns:
        list: A list of Country objects.
    """
    with open("Database/Entity/countries.json", "r") as file:
        countries = json.load(file)
        countries_list = []
        for country in countries:
            countries_list.append(Country(country["id"], country["name"], country["description"]))
        return countries_list

def get_country_name_by_id(country_id):
    """
    Retrieves the name of a country given its ID.

    Args:
        country_id (int): The ID of the country.

    Returns:
        str: The name of the country, or None if not found.
    """
    with open("Database/Entity/countries.json", "r") as file:
        countries = json.load(file)
        for country in countries:
            if country["id"] == country_id:
                return country["name"]
    return None

def get_country_id_by_name(country_name):
    """
    Retrieves the ID of a country given its name.

    Args:
        country_name (str): The name of the country.

    Returns:
        int: The ID of the country, or None if not found.
    """
    with open("Database/Entity/countries.json", "r") as file:
        countries = json.load(file)
        for country in countries:
            if country["name"] == country_name:
                return country["id"]
    return None

def get_description_by_name(country_name):
    """
    Retrieves the description of a country given its name.

    Args:
        country_name (str): The name of the country.

    Returns:
        str: The description of the country, or None if not found.
    """
    with open("Database/Entity/countries.json", "r") as file:
        countries = json.load(file)
        for country in countries:
            if country["name"] == country_name:
                return country["description"]
    return None

def get_all_countries_name():
    """
    Retrieves a sorted list of all country names.

    Returns:
        list: A sorted list of country names.
    """
    country_names = []
    for country in get_list_of_countries():
        country_names.append(country.name)
    country_names.sort()
    return country_names
