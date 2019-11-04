import requests
from time import sleep

sleep(5)
print("Everything was fine!")

lat = 59.330857
lng = 18.056409

url = "https://api.voiapp.io/v1/vehicle/status/ready?lat=%f&lng=%f" % (lat, lng)

response = requests.get(url)
print(response.json())