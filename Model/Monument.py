class Monument:
    __slots__ = ["id", "name", "country", "description"]

    def __init__(self, id, name, country, description):
        self.id = id
        self.name = name
        self.country = country
        self.description = description

    def __str__(self):
        return f"{self.name}\n"
        
    def __eq__(self, other):
        return self.id == other.id