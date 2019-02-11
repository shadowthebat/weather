import math
import json
import os
import sys


class Weather:
    def __init__(self, name, country, lat, lon, temp, weather, feels, weather_d,
                 label, deg, wspeed, humidity, vis, pressure, sunrise, sunset, time, date):
        self.name = name
        self.country = country
        self.lat = lat
        self.lon = lon
        self.temp = temp
        self.weather = weather
        self.feels = feels
        self.weather_d = weather_d
        self.label = label
        self.deg = deg
        self.wspeed = wspeed
        self.humidity = humidity
        self.vis = vis
        self.pressure = pressure
        self.sunrise = sunrise
        self.sunset = sunset
        self.time = time
        self.date = date

    def display_weather(self):
        '''
            prints redable weather info
        '''
        os.system('clear')
        print(f'{self.name}, {self.country}\n{self.lat}, {self.lon}')
        print(f'Temperature:    {self.temp} C°')
        print(f'Conditions :    {self.weather}')
        print('-------------------------')
        print()
        print(f'Feels Like :    {self.feels} C°')
        print(f'Description:    {self.weather_d}')
        print('-------------------------')
        print()
        print(f'Wind       :    {self.label}, {self.deg}°')
        print(f'W. Speed   :    {self.wspeed} km/h')
        print(f'Humidity   :    {self.humidity} %')
        print(f'Visibility :    {self.vis} km')
        print(f'Pressure   :    {self.pressure} kPa')
        print(f'Sunrise    :    {self.sunrise}')
        print(f'Sunset     :    {self.sunset}')
        print('-------------------------')
        print()
        print(f'Last Update:    {self.time}')
        print(f'                {self.date}')
        print()


def t_format(x):
    '''
        adds 0 infront min or hour given is single digit
    '''
    if x < 10:
        time = f'0{x}'
        return time
    else:
        return x

def intervols():
    '''
        used to determin direction labels
    '''
    x = 0
    while x < 360:
        print(x)
        x += 22.5

def converter(x):
    '''
        converts from meter/sec to km/hour
    '''
    x = (x*60)*60
    x = x/1000
    return round(x)

def feels(wind,temp, humidity):
    '''
        Calculates feels like conditions windchill/humidex
    '''
    if wind >= 6 and temp > -50 and temp <= 5:
        chill=(13.12+0.6215*temp-11.37*(wind**0.16)+0.3965*temp*(wind**0.16))
        return round(chill)
    else:
        kelvin = temp + 273
        eTs = 10 ** ((-2937.4 / kelvin) - 4.9283 * math.log(kelvin) / 2.30258509299 + 23.5471)
        eTd=eTs * humidity / 100
        humidex = round(temp + ((eTd-10)*5/9))
        if humidex < temp:
            humidex = temp
        return humidex

def findid(x, id_dic):
    '''
        Offers a choice between similar named cities
    '''
    with open('cityid.json','r') as f:
        cities = f.read()
    cities = json.loads(cities)
    choose_count = 1
    for i in cities:
        if x == i['name'].upper():
            print(i['name'])
            print(i['country'])
            print(i['coord']['lat'])
            print(i['coord']['lon'])
            print(f'CHOICE: {choose_count}')
            print()
            id_dic[str(choose_count)] = i['id']
            choose_count += 1
    if choose_count == 1:
        print(f'Sorry, no results found for {x}')
        return sys.exit()
    else:
        choice = input('Enter choice: ')
        return choice

def wind_label(wdeg):
    """
        compares degree of wind to determin appropriate label
        """
    if wdeg >= 338 or wdeg < 23:
        return 'N'
    elif wdeg in range(23, 68):
        return 'NE'
    elif wdeg in range(68, 113):
        return 'E'
    elif wdeg in range(113, 158):
        return 'SE'
    elif wdeg in range(158, 203):
        return 'S'
    elif wdeg in range(203, 248):
        return 'SW'
    elif wdeg in range(248, 293):
        return 'W'
    elif wdeg in range(293, 338):
        return 'NW'


def create_url(y,key):
    '''
        Creates appropriate url based on sys.argv(y)
    '''
    if len(y) > 1:
        if len(y) > 2:
            if y[1] == 'find':
                id_dic = {}
                if len(y) > 3:
                    x = y[2:]
                    x = ' '.join(x)
                    x = x.upper()
                    choice = findid(x, id_dic)
                    id = id_dic[choice]
                    return f'http://api.openweathermap.org/data/2.5/weather?id={id}&appid={key}&units=metric'
        
                else:
                    x = y[2].upper()
                    choice = findid(x, id_dic)
                    id = id_dic[choice]
                    return f'http://api.openweathermap.org/data/2.5/weather?id={id}&appid={key}&units=metric'
            
            else:
                city = y[1:]
                city = '%20'.join(city)
                return f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'

        else:
            city = y[1]
            return f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'
    else:
        return f'http://api.openweathermap.org/data/2.5/weather?id=6077243&appid={key}&units=metric'
