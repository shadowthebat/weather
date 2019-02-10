import requests
import json
from key import key
from datetime import datetime
import os
from feelslike import *

def t_format(x):
    # adds 0 infront min or hour given is single digit
    if x < 10:
        time = f'0{x}'
        return time
    else:
        return x

apiurl = f'http://api.openweathermap.org/data/2.5/weather?q=montreal,ca{id}&appid={key}&units=metric'
source = requests.get(apiurl) # response RAW
data = source.json() # response --> Python Dictionary

# create variables with desired values from data
dt = datetime.fromtimestamp(data['dt'])
time = dt.time()
date = dt.date()
name = data['name']
country = data['sys']['country']
lat = data['coord']['lat']
lon = data['coord']['lon']
temp = data['main']['temp']
weather = data['weather'][0]['main']
weather_d = data['weather'][0]['description']
vis = data['visibility']
vis = round(vis/1000)
humidity = data['main']['humidity']
pressure = data['main']['pressure']
pressure = round(pressure/10)

# sunrise/sunset
sunrise = data['sys']['sunrise']
sunrise = datetime.fromtimestamp(sunrise)
riseh = sunrise.hour
risem = sunrise.minute
riseh = t_format(riseh)
risem = t_format(risem)
sunset = data['sys']['sunset']
sunset = datetime.fromtimestamp(sunset)
seth = sunset.hour
setm = sunset.minute
seth = t_format(seth)
setm = t_format(setm)

# wind
wspeed = data['wind']['speed']
wspeed = converter(wspeed) # from meter/sec to km/h
feels = feels(wspeed, temp)
wdeg = data['wind']['deg']
deg = wdeg
# compares degree of wind to determin appropriate label
if wdeg >= 338 or wdeg < 23:
    d = 'N'
elif wdeg in range(23, 68):
    d = 'NE'
elif wdeg in range(68, 113):
    d = 'E'
elif wdeg in range(113, 158):
    d = 'SE'
elif wdeg in range(158, 203):
    d = 'S'
elif wdeg in range(203, 248):
    d = 'SW'
elif wdeg in range(248, 293):
    d = 'W'
elif wdeg in range(293, 338):
    d = 'NW'
wdeg = d
os.system('clear')
# prints redable weather info
print(f'{name}, {country}\n{lat}, {lon}')
print(f'Temperature:    {temp} C°')
print(f'Conditions :    {weather}')
print('-------------------------')
print()
print(f'Feels Like :    {feels} C°')
print(f'Description:    {weather_d}')
print('-------------------------')
print()
print(f'Wind       :    {d}, {deg}°')
print(f'W. Speed   :    {wspeed} km/h')
print(f'Humidity   :    {humidity} %')
print(f'Visibility :    {vis} km')
print(f'Pressure   :    {pressure} kPa')
print(f'Sunrise    :    {riseh}:{risem}')
print(f'Sunset     :    {seth}:{setm}')
print('-------------------------')
print()
print(f'Last Update:    {time}')
print(f'                {date}')
print()
