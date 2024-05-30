from Model.Monument import Monument
import json

def get_monument_name_by_id(monument_id):
    with open("Database/Entity/monuments.json", "r") as file:
        monuments = json.load(file)
        for monument in monuments:
            if monument["id"] == monument_id:
                return monument["name"]
            
    return None

def get_list_of_monuments_by_country_id(country_id):
    with open("Database/Entity/monuments.json", "r") as file:
        monuments = json.load(file)
        monuments_list = []
        for monument in monuments:
            if monument["country_id"] == country_id:
                monuments_list.append(Monument(monument["id"], monument["name"],monument["country_id"], monument["description"]))
                
        return monuments_list
def get_despcriptions_monuments_by_country_id(country_id):
    monuments_list = get_list_of_monuments_by_country_id(country_id)
    text = "\n\n"
    for Monument in monuments_list:
        text += Monument.__str__()+"\n"
    return text