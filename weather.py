import requests
import json
from key import key
from datetime import datetime
import sys
from feelslike import *


apiurl = create_url(sys.argv,key)
source = requests.get(apiurl) # response RAW
data = source.json() # response --> Python Dictionary

# create variables with desired values from data
# datetime
dt = datetime.fromtimestamp(data['dt'])
time = dt.time()
date = dt.date()

# location info
name = data['name']
country = data['sys']['country']
lat = data['coord']['lat']
lon = data['coord']['lon']

# temperature and conditions
temp = round(data['main']['temp'])
weather = data['weather'][0]['main']
weather_d = data['weather'][0]['description']
vis = data['visibility']
vis = round(vis/1000)
humidity = data['main']['humidity']
pressure = data['main']['pressure']
pressure = round(pressure/10)

# wind
wspeed = data['wind']['speed']
wspeed = converter(wspeed) # from meter/sec to km/h
feels = feels(wspeed, temp, humidity)
deg = round(data['wind']['deg'])
label = wind_label(deg)

# sunrise/sunset
sunrise = data['sys']['sunrise']
sunrise = datetime.fromtimestamp(sunrise)
riseh = sunrise.hour
risem = sunrise.minute
riseh = t_format(riseh)
risem = t_format(risem)
sunrise = f'{riseh}:{risem}'
sunset = data['sys']['sunset']
sunset = datetime.fromtimestamp(sunset)
seth = sunset.hour
setm = sunset.minute
seth = t_format(seth)
setm = t_format(setm)
sunset = f'{seth}:{setm}'

# current weather class
current = Weather(name, country, lat, lon, temp, weather, feels, weather_d,
                  label, deg, wspeed, humidity, vis, pressure, sunrise, sunset, time, date)

# display current weather
current.display_weather()
