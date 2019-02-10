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

def feels(wind,temp):
    # Calculations from official canada website
    if wind >= 6 and temp > -50 and temp <= 5:
        chill=(13.12+0.6215*temp-11.37*(wind**0.16)+0.3965*temp*(wind**0.16))
        return round(chill)
