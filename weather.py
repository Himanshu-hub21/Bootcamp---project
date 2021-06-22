import requests
#import os
from datetime import datetime

api_key = 'b7604e05d5f0c292482b6e28471daa5d'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

report = open('Weather.txt', 'w')

report.write("-------------------------------------------------------------")
report.write(
    "Weather Stats for - {}  || {}".format(location.upper(), date_time))
report.write("-------------------------------------------------------------")

report.write("Current temperature is: {:.2f} deg C".format(temp_city))
report.write("Current weather desc  :", weather_desc)
report.write("Current Humidity      :", hmdt, '%')
report.write("Current wind speed    :", wind_spd, 'kmph')

report.close()
