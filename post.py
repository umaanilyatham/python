import requests

url = "http://127.0.0.1:5000/restaurants"

restaurant = {
    "id": 6,
    "name": "Food Palace",
    "location": "Pune",
    "cuisine": "Indian",
    "rating": 4.3,
    "price_for_two": 600,
    "phone": "9876543215",
    "is_open": True
}

response = requests.post(url, json=restaurant)

print(response.status_code)
print(response.json())