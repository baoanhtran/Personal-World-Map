from Model.Monument import Monument
import json

def get_monument_name_by_id(monument_id):
    """
    Retrieves the name of a monument given its ID.

    Args:
        monument_id (int): The ID of the monument.

    Returns:
        str: The name of the monument, or None if not found.
    """
    with open("Database/Entity/monuments.json", "r") as file:
        monuments = json.load(file)
        for monument in monuments:
            if monument["id"] == monument_id:
                return monument["name"]
    return None

def get_list_of_monuments_by_country_id(country_id):
    """
    Retrieves a list of monuments for a given country ID.

    Args:
        country_id (int): The ID of the country.

    Returns:
        list: A list of Monument objects.
    """
    with open("Database/Entity/monuments.json", "r") as file:
        monuments = json.load(file)
        monuments_list = []
        for monument in monuments:
            if monument["country_id"] == country_id:
                monuments_list.append(Monument(monument["id"], monument["name"], monument["description"], monument["country_id"]))
        return monuments_list
