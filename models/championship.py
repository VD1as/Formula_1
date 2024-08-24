class Championship:
    def __init__(self, year):
        self.year = year
        self.races = []

    def add_race(self, race):
        self.races.append(race)

    def get_races(self):
        return self.races

    def __str__(self):
        return f"Championship {self.year} with {len(self.races)} races"
