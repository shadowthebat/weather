import requests
import json
from key import key

url = f'http://api.openweathermap.org/data/2.5/weather?q=montreal,ca{id}&appid={key}&units=metric'
source = requests.get(url)
data = source.json()

name = data['name']
country = data['sys']['country']
lat = data['coord']['lat']
lon = data['coord']['lon']
temp = data['main']['temp']
weather = data['weather'][0]['main']
min = data['main']['temp_min']
max = data['main']['temp_max']
humidity = data['main']['humidity']
pressure = data['main']['pressure']
sunrise = data['sys']['sunrise']
sunset = data['sys']['sunset']
wdeg = data['wind']['deg']
wspeed = data['wind']['speed']

print()
print(name, country, lat, lon)
print('-------------------------')
print(f'Weather    :    {weather}')
print(f'Temperature:    {temp}')
print('-------------------------')
print(f'Min Temp   :    {min}')
print(f'Max Temp   :    {max}')
print(f'Humidity   :    {humidity}')
print(f'Pressure   :    {pressure}')
print(f'Sunrise    :    {sunrise}')
print(f'Sunset     :    {sunset}')
print(f'Wind deg.  :    {wdeg}')
print(f'Wind Speed :    {wspeed}')
print()
