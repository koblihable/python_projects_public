import requests
import os

class DataManager:

    def __init__(self):
        self.sheet_end_point = "https://api.sheety.co/5dbef9deb0eb782c5f475ae8da7e7d52/flightDeals/sheet1"
        self._sheet_token = os.environ["SHEETY_TOKEN"]
        self.data = self.get_data()
        self.cities = self.get_cities()

    def get_sheet_header(self):
        return {"Authorization": self._sheet_token}

    def get_data(self):
        return requests.get(url=self.sheet_end_point, headers=self.get_sheet_header()).json()['sheet1']

    def get_cities(self):
        return [line['city'] for line in self.data]

    def populate_iata_codes(self):
        for city in self.data:
            new_body = {
                'sheet1': {'iataCode': city['iataCode']}
            }
            response = requests.put(url=f'{self.sheet_end_point}/{city["id"]}', json=new_body, headers=self.get_sheet_header())

