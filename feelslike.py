import sys
from key import *
import requests
import json
from datetime import datetime
import math
import os

# -- Classes --
class Weather:
    ''' Weather class '''
    def __init__(self):
        # pull data from api
        self.apiurl = create_url(sys.argv,key)
        self.source = requests.get(self.apiurl) # response RAW
        self.data = self.source.json() # response --> Python Dictionary

        # create variables with desired values from data
        # datetime
        self.dt = datetime.fromtimestamp(self.data['dt'])
        self.time = self.dt.time()
        self.date = self.dt.date()

        # location info
        self.city = self.data['name']
        self.country = self.data['sys']['country']
        self.lat = self.data['coord']['lat']
        self.lon = self.data['coord']['lon']

        # temperature and conditions
        self.temp = round(self.data['main']['temp'])
        self.conditions = self.data['weather'][0]['main']
        self.description = self.data['weather'][0]['description']
        self.visibility = self.data['visibility']
        self.visibility = round(self.visibility/1000)
        self.humidity = self.data['main']['humidity']
        self.pressure = self.data['main']['pressure']
        self.pressure = round(self.pressure/10)

        # wind
        self.wspeed = self.data['wind']['speed']
        self.w_speed = converter(self.wspeed) # from meter/sec to km/h
        self.feels = feels(self.w_speed, self.temp, self.humidity)
        self.w_deg = round(self.data['wind']['deg'])
        self.w_label = wind_label(self.w_deg)

        # sunrise/sunset
        self.sunrise = self.data['sys']['sunrise']
        self.sunrise = datetime.fromtimestamp(self.sunrise)
        self.riseh = self.sunrise.hour
        self.risem = self.sunrise.minute
        self.riseh = t_format(self.riseh)
        self.risem = t_format(self.risem)
        self.sunrise = f'{self.riseh}:{self.risem}'
        self.sunset = self.data['sys']['sunset']
        self.sunset = datetime.fromtimestamp(self.sunset)
        self.seth = self.sunset.hour
        self.setm = self.sunset.minute
        self.seth = t_format(self.seth)
        self.setm = t_format(self.setm)
        self.sunset = f'{self.seth}:{self.setm}'

    def display(self):
        '''
            prints redable weather info
        '''
        os.system('clear')
        print(f'{self.city}, {self.country}\n{self.lat}, {self.lon}')
        print(f'Temperature:    {self.temp} C°')
        print(f'Conditions :    {self.conditions}')
        print('-------------------------')
        print()
        print(f'Feels Like :    {self.feels} C°')
        print(f'Description:    {self.description}')
        print('-------------------------')
        print()
        print(f'Wind       :    {self.w_label}, {self.w_deg}°')
        print(f'W. Speed   :    {self.w_speed} km/h')
        print(f'Humidity   :    {self.humidity} %')
        print(f'Visibility :    {self.visibility} km')
        print(f'Pressure   :    {self.pressure} kPa')
        print(f'Sunrise    :    {self.sunrise}')
        print(f'Sunset     :    {self.sunset}')
        print('-------------------------')
        print()
        print(f'Last Update:    {self.time}')
        print(f'                {self.date}')
        print()

    def attributes(self):
        '''
            lists class attributes
        '''
        list_data = 'city country lat lon temp conditions feels description w_label w_deg w_speed humidity visibility pressure sunrise sunset time date'
        list_data = list_data.split()
        print(list_data)


# -- Functions --
def create_url(y,key):
    '''
        Creates appropriate url based on sys.argv(y)
    '''
    if len(y) == 1:
        return f'http://api.openweathermap.org/data/2.5/weather?id=6077243&appid={key}&units=metric'
    else:
        if len(y) == 2:
            city = y[1]
            return f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'
        else:
            if y[1] == 'find':
                id_dic = {}
                if len(y) <= 3:
                    x = y[2].upper()
                    choice = findid(x, id_dic)
                    id = id_dic[choice]
                    return f'http://api.openweathermap.org/data/2.5/weather?id={id}&appid={key}&units=metric'
                else:
                    x = y[2:]
                    x = ' '.join(x)
                    x = x.upper()
                    choice = findid(x, id_dic)
                    id = id_dic[choice]
                    return f'http://api.openweathermap.org/data/2.5/weather?id={id}&appid={key}&units=metric'

            else:
                city = y[1:]
                city = '%20'.join(city)
                return f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'

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
    if wind >= 5 and temp > -50 and temp <= 15:
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

def t_format(x):
    '''
        adds 0 infront min or hour given is single digit
    '''
    if x < 10:
        time = f'0{x}'
        return time
    else:
        return x

def findid(x, id_dic):
    '''
        Offers a choice between similar named cities
    '''
    os.system('clear')
    with open(find_id_path,'r') as f:
        cities = f.read()
    cities = json.loads(cities)
    choose_count = 1
    for i in cities:
        if x == i['name'].upper():
            n = i['name']
            c = i['country']
            lt = round(i['coord']['lat'], 2)
            ln = round(i['coord']['lon'], 2)
            print(f'{n}, {c}')
            print(f'{lt}, {ln}')
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
