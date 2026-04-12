import requests
import json


url_end_point = " https://api.npoint.io/91997184c10bd8cfb48f"
blog_response = requests.get(url_end_point).json()
for blog in blog_response:
    print(blog)
