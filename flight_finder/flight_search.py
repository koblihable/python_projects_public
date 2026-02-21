import requests
from datetime import datetime as dt
from datetime import timedelta
import os


# flight search API
class FlightSearch:
    def __init__(self):
        self._api_key = os.environ[AMADEUS_API_KEY]
        self._secret = os.environ[AMADEUS_SECRET]
        self.base_url = 'https://test.api.amadeus.com/v1'
        self._token = self._get_new_token()

    def _get_new_token(self):
        auth_body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._secret
        }
        auth_header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        token_endpoint = f'{self.base_url}/security/oauth2/token'

        response = requests.post(url=token_endpoint, data=auth_body, headers=auth_header)
        return response.json()['access_token']

    def get_auth_header(self):
        return {'Authorization': f'Bearer {self._token}'}

    def get_iata_code(self, city):
        cities_endpoint = f'{self.base_url}/reference-data/locations/cities'
        params = {'keyword': city}
        response = requests.get(url=cities_endpoint, params=params, headers=self.get_auth_header())
        return response.json()['data'][0]['iataCode']

    def find_flights(self, data):
        flights_endpoint = f'{self.base_url}/shopping/flight-dates'
        start_date = dt.today().strftime('%Y-%m-%d')
        end_date = (dt.today() - timedelta(days=180)).strftime('%Y-%m-%d')
        departure_date = start_date + end_date

        for line in data:
            params = {
                'origin': 'PRG',
                'destination': line['iataCode'],
                'departure_date': departure_date,
                'oneWay': 'false',
                'nonStop': 'false',
                'max_price': line['lowestPrice']
            }
            response = requests.get(url=flights_endpoint, params=params, headers=self.get_auth_header())
            if response:
                print(response.json())
            else:
                print('no flights found')











