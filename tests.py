from random import randint
from feelslike import feels
from feelslike import wind_label

def call_wind_label(x):
    for i in range(x):
        d = randint(0,360)
        print(d)
        gimme = wind_label(d)
        print(gimme)
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
