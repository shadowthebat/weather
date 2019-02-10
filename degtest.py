from random import randint
from feelslike import feels

def direction(wdeg):
    if wdeg > 348.75 or wdeg < 11.25:
        d = 'N'
        print(d)
    elif wdeg > 78.75 and wdeg < 101.25:
        d = 'E'
        print(d)
    elif wdeg > 168.75 and wdeg < 191.25:
        d = 'S'
        print(d)
    elif wdeg > 258.75 and wdeg < 281.25:
        d = 'W'
        print(d)

    elif wdeg <= 348.75 and wdeg >= 281.25:
        d = 'NW'
        print(d)
    elif wdeg >= 11.25 and wdeg <= 78.75:
        d = 'NE'
        print(d)
    elif wdeg <= 168.75 and wdeg >= 101.25:
        d = 'SE'
        print(d)
    elif wdeg >= 191.25 and wdeg <= 258.75:
        d = 'SW'
        print(d)

def calldirection(x):
    for i in range(x):
        d = randint(0,360)
        print(d)
        direction(d)
        print()

def callhumidex(x):
    for i in range(x):
        h = randint(50,101)
        t = randint(20,40)
        w = randint(0,40)
        humidex = feels(w,t,h)
        print(f'temperature:    {t}')
        print(f'windspeed  :    {w}')
        print(f'humidity   :    {h}')
        print(f'humidex    :    {humidex}')
        print('-----------------')
