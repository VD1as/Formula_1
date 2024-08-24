class Circuit:
    def __init__(self, circuit_id, name, location, country):
        self.circuit_id = circuit_id
        self.name = name
        self.location = location
        self.country = country

    def __str__(self):
        return f"{self.name} - {self.location}, {self.country}"
