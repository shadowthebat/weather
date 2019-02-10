import math
import json

def t_format(x):
    # adds 0 infront min or hour given is single digit
    if x < 10:
        time = f'0{x}'
        return time
    else:
        return x

def intervols():
    # used to determin direction labels
    x = 0
    while x < 360:
        print(x)
        x += 22.5

def converter(x):
    # converts from meter/sec to km/hour
    x = (x*60)*60
    x = x/1000
    return round(x)

def feels(wind,temp, humidity):
    # Calculations from official canada website
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

def findid(x):
    with open('cityid.json','r') as f:
        cities = f.read()
    cities = json.loads(cities)
    for i in cities:
        if x == i['name'].upper():
            print(i['name'])
            print(i['country'])
            print(i['id'])
            print()















