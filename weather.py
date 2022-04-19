import requests
import json
import os

#https://api.openweathermap.org/data/2.5/weather?lat=36.973104608831015&lon=-122.02457319050546&appid=220d1548676e502c191ec0a35711040e

#response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")
#print(response.status_code)

#new_file_path = os.path.join(os.getcwd(), "config.json")
#print(new_file_path)

try:
  with open("config.json", "r") as read_file:
    data = json.load(read_file)
  apikey = data["SECRET_API_KEY"]
  if apikey == None:
    print("API Key not found in config.json file.")
    apikey = input("Please Enter your Openweathermap API Key:")
    data = {"SECRET_API_KEY": apikey}
    with open("config.json", "w") as write_file:
      json.dump(data, write_file)
    print("Saved API Key in config.json")
except FileNotFoundError:
  apikey = input("Please Enter your Openweathermap API Key:")
  data = {"SECRET_API_KEY": apikey}
  with open("config.json", "w") as write_file:
      json.dump(data, write_file)
  print("Saved API Key in config.json")


lat = '36.972837'
lon = '-122.0309346'

query = {'lat':lat, 'lon':lon, 'appid':apikey}
response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=query)
#print(response.json())

weatherdata = response.json()
print("The Temperature is: {:0.2f} ºC".format(weatherdata["main"]["temp"] - 273.15))