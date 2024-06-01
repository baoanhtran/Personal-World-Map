from Repository.MonumentRepository import get_despcriptions_monuments_by_country_id
from Repository.CountryRepository import get_country_id_by_name, get_list_of_countries, get_description_by_name

def get_all_countries_name():
    country_names = []
    for country in get_list_of_countries():
        country_names.append(country.name)

    return country_names

def get_country_id(country_name):
    return get_country_id_by_name(country_name)

def get_despcriptions_monuments(country_id):
    return get_despcriptions_monuments_by_country_id(country_id)

def get_description(country_name):
    return get_description_by_name(country_name)