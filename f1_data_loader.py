import pandas as pd
from models.championship import Championship
from models.drivers import Driver
from models.constructor import Constructor
from models.circuits import Circuit
from models.races import Race

def load_data():
    drivers_df = pd.read_csv('data/drivers.csv')
    constructors_df = pd.read_csv('data/constructors.csv')
    circuits_df = pd.read_csv('data/circuits.csv')
    races_df = pd.read_csv('data/races.csv')
    results_df = pd.read_csv('data/results.csv')

    drivers = {}
    constructors = {}
    circuits = {}
    races = {}
    championships = {}

    for _, row in drivers_df.iterrows():
        driver = Driver(
            driver_id=row['driverId'],
            driver_ref=row['driverRef'],
            name=f"{row['forename']} {row['surname']}",
            nationality=row['nationality'],
            dob=row['dob'],
            number=row.get('number'),
            code=row.get('code')
        )
        drivers[row['driverId']] = driver

    for _, row in constructors_df.iterrows():
        constructor = Constructor(
            constructor_id=row['constructorId'],
            name=row['name'],
            nationality=row['nationality']
        )
        constructors[row['constructorId']] = constructor

    for _, row in circuits_df.iterrows():
        circuit = Circuit(
            circuit_id=row['circuitId'],
            name=row['name'],
            location=row['location'],
            country=row['country']
        )
        circuits[row['circuitId']] = circuit

    for _, row in races_df.iterrows():
        circuit = circuits.get(row['circuitId'])
        race = Race(
            race_id=row['raceId'],
            year=row['year'],
            round=row['round'],
            circuit=circuit,
            date=row['date']
        )
        races[row['raceId']] = race

        if row['year'] not in championships:
            championships[row['year']] = Championship(year=row['year'])

        championships[row['year']].add_race(race)

    for _, row in results_df.iterrows():
        race = races.get(row['raceId'])
        driver = drivers.get(row['driverId'])
        race.add_result(driver, row['positionOrder'])

    return drivers, constructors, circuits, races, championships
