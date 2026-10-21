import requests
import json

url = "http://api.weatherapi.com/v1/current.json?key=638ba7c08aa4460794393515231104&q=Raipur"

req = requests.get(url) 
data = json.loads(req.content)
print("Location = " ,data["location"]["name"])
print("Temperature in celcius = ",data["current"]["temp_c"])
print("Temperature in Ferenehite = ",data["current"]["temp_f"])
print("Humidity = ",data["current"]["humidity"])