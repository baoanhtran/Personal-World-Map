class Country:
    __slots__ = ["id", "name", "list_of_monuments"]

    def __init__(self, id, name, list_of_monuments):
        self.id = id
        self.name = name
        self.list_of_monuments = list_of_monuments

    def __str__(self):
        return f"Country {self.name} has the following monuments: {', '.join([monument.name for monument in self.list_of_monuments])}."
    
    def __eq__(self, other):
        return self.id == other.id