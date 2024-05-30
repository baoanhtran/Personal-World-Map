import json
from Model.Country import Country
from Repository.MonumentRepository import get_list_of_monuments_by_country_id

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

def create_object_by_name(country_name):
    with open("Database/Entity/countries.json", "r") as file:
        countries = json.load(file)
        for country in countries:
            if country["name"] == country_name:
                description = country["description"]
    
    country_id = get_country_id_by_name(country_name)
    monuments_list = get_list_of_monuments_by_country_id(country_id)
    return Country(country_id, country_name, monuments_list)

