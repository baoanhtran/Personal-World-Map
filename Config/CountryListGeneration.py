import json

def country_to_list():
    with open("Database/ExternalData/country_shapes.json", "r") as f:
        data = json.load(f)
        countries = []
        for i, ele in enumerate(data):
            dico = {
                "id": i+1,
                "name": ele["cntry_name"],
                "description": ""
            }
            countries.append(dico)

    with open("Database/Entity/countries.json", "w") as f:
        json.dump(countries, f, indent=4)

if __name__ == "__main__":
    country_to_list()