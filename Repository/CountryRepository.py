import json
from Model.Country import Country

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