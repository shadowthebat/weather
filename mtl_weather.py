import requests
import json
from key import key
from datetime import datetime

url = f'http://api.openweathermap.org/data/2.5/weather?q=montreal,ca{id}&appid={key}&units=metric'
source = requests.get(url)
data = source.json()

def t_format(x):
    if x < 10:
        time = f'0{x}'
        return time
    else:
        return x

name = data['name']
country = data['sys']['country']
lat = data['coord']['lat']
lon = data['coord']['lon']
temp = data['main']['temp']
weather = data['weather'][0]['main']
min = data['main']['temp_min']
max = data['main']['temp_max']
vis = data['visibility']
humidity = data['main']['humidity']
pressure = data['main']['pressure']
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

wspeed = data['wind']['speed']
wdeg = data['wind']['deg']

if wdeg > 348.75 and wdeg < 11.25:
    d = 'N'
elif wdeg > 78.75 and wdeg < 101.25:
    d = 'E'
elif wdeg > 168.75 and wdeg < 191.25:
    d = 'S'
elif wdeg > 258.75 and wdeg < 281.25:
    d = 'W'
elif wdeg <= 348.75 and wdeg >= 281.25:
    d = 'NW'
elif wdeg <= 11.25 and wdeg >= 78.75:
    d = 'NE'
elif wdeg <= 101.25 and wdeg >= 168.75:
    d = 'SW'
elif wdeg <= 191.25 and wdeg >= 258.75:
    d = 'SE'
wdeg = d

print()
print(f'{name}, {country}\n{lat}, {lon}')
print('-------------------------')
print(f'Temperature:    {temp} C')
print(f'Conditions :    {weather}')
print('-------------------------')
print(f'Wind       :    {d}')
print(f'W. Speed   :    {wspeed} km/h')
print(f'Humidity   :    {humidity} %')
print(f'Visibility :    {vis} km')
print(f'Pressure   :    {pressure} kPa')
print(f'Sunrise    :    {riseh}:{risem}')
print(f'Sunset     :    {seth}:{setm}')
print()
