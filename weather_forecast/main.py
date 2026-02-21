import requests
from twilio.rest import Client
import os


OWM_API_KEY = os.environ.get("OWM_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
MY_LATITUDE = 49.195061
MY_LONGITUDE = 16.606836

TWILIO_FROM_FN = os.environ.get("TWILIO_FROM_FN")
TWILIO_TO_FN = os.environ.get("TWILIO_TO_FN")

params = {
    "lat": 49.195061,
    "lon": 16.606836,
    "appid": OWM_API_KEY,
    "cnt": 4,
    "units": "metric"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()

data = response.json()

will_rain = False
for segment in data['list']:
    if segment['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    message = client.messages.create(
        body="bring an umbrella today",
        from_=TWILIO_FROM_FN,
        to=TWILIO_TO_FN
    )
    print(message.status)
