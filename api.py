import flask

restaurant={
    "name": "Tasty Bites",
    "location": "123 Main St",
    "cuisine": "Italian",
    "description": "A delightful Italian restaurant",
    "open": True,


    "menu": ["Margherita Pizza", "Spaghetti Carbonara", "Tiramisu"]



    

},{
    "name": "Sushi World",
    "location": "456 Elm St",
    "cuisine": "Japanese",
    "description": "A delicious Japanese restaurant",
    "open": True,
    "menu": ["California Roll", "Dragon Roll", "Miso Soup"]
},
{
    "name": "Burger Haven",
    "location": "789 Oak St",
    "cuisine": "American",
    "description": "A cozy American burger joint",
    "open": False,
    "menu": ["Classic Cheeseburger", "Bacon Burger", "Fries"]
}

app = flask.Flask(__name__)

@app.route('/restaurant', methods=['GET'])
def get_restaurant():
    return flask.jsonify(restaurant)

if __name__ == '__main__':
    app.run(debug=True)

    



