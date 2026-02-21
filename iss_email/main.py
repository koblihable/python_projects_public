import requests
from datetime import datetime
import smtplib
import time
import os

#Brno location
MY_LATITUDE = 49.195061
MY_LONGITUDE = 16.606836
MY_EMAIL = os.environ.get("ETEST_EMAIL")
PASSWORD = os.environ.get("ETEST_EMAIL_PWD")

def is_dark():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    return hour_now > sunset or hour_now < sunrise

def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_latitude = float(response.json()["iss_position"]["latitude"])
    iss_longitude = float(response.json()["iss_position"]["longitude"])

    return MY_LATITUDE-5 <= iss_latitude <= MY_LATITUDE+5 and MY_LONGITUDE-5 <= iss_longitude <= MY_LONGITUDE+5

while True:
    time.sleep(60)
    if is_dark() and is_iss_close():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:ISS overhead\n\nLOOK UP"
            )
