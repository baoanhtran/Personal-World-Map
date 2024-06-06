import json
from Model.Country import Country

def get_list_of_countries():
    with open("Database/Entity/countries.json", "r") as file:
        countries = json.load(file)
        countries_list = []
        for country in countries:
            countries_list.append(Country(country["id"], country["name"], country["description"]))
            
        return countries_list

def get_country_name_by_id(country_id):
    with open("Database/Entity/countries.json", "r") as file:
        countries = json.load(file)
        for country in countries:
            if country["id"] == country_id:
                return country["name"]
            
    return None

def get_country_id_by_name(country_name):
    with open("Database/Entity/countries.json", "r") as file:
        countries = json.load(file)
        for country in countries:
            if country["name"] == country_name:
                return country["id"]
            
    return None

def get_description_by_name(country_name):
    with open("Database/Entity/countries.json", "r") as file:
        countries = json.load(file)
        for country in countries:
            if country["name"] == country_name:
                return country["description"]
            
    return None

def get_all_countries_name():
    country_names = []
    for country in get_list_of_countries():
        country_names.append(country.name)
        
    # Sort the list of countries
    country_names.sort()
    
    return country_names