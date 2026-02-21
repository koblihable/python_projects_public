import requests
import datetime as dt
import os


today = dt.date.today().strftime("%Y%m%d")

# create a user at pixela
pixela_url = "https://pixe.la/v1/users"
pixela_username = os.environ.get("OWM_USERNAME")
pixela_token = os.environ.get("OWM_TOKEN")
pixela_params = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#response = requests.post(url=pixela_url, json=pixela_params)
#print(response.text)

# authorization header
headers = {
    "X-USER-TOKEN": pixela_token
}

# create a graph for recording a morning glass of water
graph_config = {
    "id": "graph1",
    "name": "morning drink",
    "unit": "pint",
    "type": "int",
    "color": "momiji"
}

graph_endpoint = f"{pixela_url}/{pixela_username}/graphs"
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

# post a pixel to record the morning glass of water
water_endpoint = f"{graph_endpoint}/graph1"
water_config = {
    "date": today,
    "quantity": "1",
}

response = requests.post(url=water_endpoint, json=water_config, headers=headers)
print(response.text)

