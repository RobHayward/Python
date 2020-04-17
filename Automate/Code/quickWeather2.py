#! python3
# quickWeather.py - prints the weather for a location from command line

import json, requests, sys
# Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the json data from OpenWeatherMap.org's API
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s,uk&&APPID=b1004a393be3814aa1388dfd23f05120' % (location)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
# print weather data descriptions
temp = weatherData['main']['temp'] - 273.15 
mintemp = weatherData['main']['temp_min'] - 273.15 
maxtemp = weatherData['main']['temp_max'] - 273.15 
pressure = weatherData['main']['pressure']
humidity = weatherData['main']['humidity']
description = weatherData['weather'][0]['main'] + ' - ' + weatherData['weather'][0]['description']
wind_direction = weatherData['wind']['deg']
wind_speed = weatherData['wind']['speed']
clouds = weatherData['clouds']['all']

print('Current weather in %s:' % (location))
print('Temperature today is ' + repr(round(temp, 2)))
print('Maximum temperature today is ' + repr(round(maxtemp, 2)))
print('Minimum temperature today is ' + repr(round(mintemp,2)))
print('The weather is ' + description)
print('Wind directions is ' + repr(wind_direction))
print('Wind speed ' + repr(wind_speed))
print('Pressure is ' + repr(pressure))
print('The humidity is ' + repr(humidity))
print('The percentage of sky that is cloud covered ' + repr(clouds))

