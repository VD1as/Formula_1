class Race:
    def __init__(self, race_id, year, round, circuit, date):
        self.race_id = race_id
        self.year = year
        self.round = round
        self.circuit = circuit
        self.date = date
        self.results = []  

    def add_result(self, driver, position):
        self.results.append((driver, position))

    def get_results(self):
        return sorted(self.results, key=lambda x: x[1]) 

    def __str__(self):
        return f"Race {self.round} - {self.circuit} ({self.date})"
