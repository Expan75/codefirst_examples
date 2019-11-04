
# Ye old and trusty web development framework.
from flask import Flask, render_template, request

# this library enables http requests: i.e. to talk to servers via the internet!
import requests

# this library makes it easier to work with json data
import json

# Setup for flask to initalise (don't change this)
app = Flask('apiserver')

# Routes
@app.route("/")
def index():
    return "Hello world!"

# Leads the user to a form where they can put in their location
@app.route("/scootero")
def scooterFormView():
    return render_template("getscooter.html")

# Handles the response when the user submits the form
@app.route("/locatescooters", methods=["POST"])
def closeScooterView():
    """ Handles the user input and retreievs the number of scooters close to the user's given position. """

    # Handle the input from the form
    formData = request.form

    # store the values given (we're converting them to floats as well to make sure that python understands it's numbers)
    lat = formData['lat']
    lng = formData['lng']

    # Set up url to make request (where we want to get data from, what api we want to target)
    url = "https://api.voiapp.io/v1/vehicle/status/ready?lat=%s&lng=%s" % (lat, lng)

    # Make a GET request to the api and store the data
    response = requests.get(url)

    # Extract the JSON data (just a type of data object)
    jsonData = response.json()
    # print(data) # Uncomment this line to see if you actually get what you expected!

    # Luckily, the .json() call parses the data neatly into a python list (full of scooter dictionaries!)
    # This means we can utilise list methods, for example to count the length (i.e. how many scooters are close)
    nScooters = len(jsonData)

    # return some response, in this case the number of scooters close by. We pass the nScooters variable into the response
    return render_template('getscooterresp.html', nearbyNumber=nScooters)


app.run(debug=True)
