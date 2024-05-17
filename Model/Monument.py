class Monument:
    __slots__ = ["id", "name", "country", "description"]

    def __init__(self, id, name, country, description):
        self.id = id
        self.name = name
        self.country = country
        self.description = description

    def __str__(self):
        return f"Monument {self.name} in {self.country} is {self.description}."
    
    def __eq__(self, other):
        return self.id == other.id