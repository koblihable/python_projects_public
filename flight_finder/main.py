import requests
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

for line in data_manager.data:
    print(line)
    if line['iataCode'] == '':
        line['iataCode'] = flight_search.get_iata_code(line['city'])

print(data_manager.data)

data_manager.populate_iata_codes()

flight_search.find_flights(data_manager.data)


