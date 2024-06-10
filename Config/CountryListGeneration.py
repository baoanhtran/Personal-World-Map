import json
from openai import OpenAI
client = OpenAI()

def country_to_list():
    """
    Reads country shapes data from a JSON file, extracts country names,
    assigns each an ID, sorts the list alphabetically by country name,
    and writes the data to a new JSON file.
    """
    with open("Database/ExternalData/country_shapes.json", "r") as f:
        data = json.load(f)
        countries = []
        for i, ele in enumerate(data):
            dico = {
                "id": i + 1,
                "name": ele["cntry_name"],
                "description": ""
            }
            countries.append(dico)

    countries.sort(key=lambda x: x["name"])  # Sort countries by name

    # Update the id of each country
    for i, ele in enumerate(countries):
        ele["id"] = i + 1

    with open("Database/Entity/countries.json", "w") as f:
        json.dump(countries, f, indent=4)

def generate_description(country):
    """
    Generates a brief description for a given country using the OpenAI API.
    
    Args:
        country (str): The name of the country to generate a description for.
        
    Returns:
        str: A description of the country suitable for tourists.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Generate a brief description of the following country or territory. The description should be for tourists who are planning to visit the place."},
            {"role": "user", "content": country}
        ]
    )

    return response.choices[0].message.content

def update_descriptions():
    """
    Reads the country list from a JSON file, generates descriptions for each country,
    updates the list with the descriptions, and writes the updated data back to the JSON file.
    """
    with open("Database/Entity/countries.json", "r") as f:
        countries = json.load(f)
        for country in countries:
            country["description"] = generate_description(country["name"])

    with open("Database/Entity/countries.json", "w") as f:
        json.dump(countries, f, indent=4)

if __name__ == "__main__":
    country_to_list()
    update_descriptions()