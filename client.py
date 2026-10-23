import requests

url="http://127.0.0.1:5000/restaurants"


response = requests.get(url)

print(response.json())    



for restaurant in response.json():
    if restaurant["id"]==1:
        print(restaurant["name"],restaurant["location"],restaurant["cuisine"],restaurant["rating"],restaurant["price_for_two"],restaurant["phone"],restaurant["is_open"])
