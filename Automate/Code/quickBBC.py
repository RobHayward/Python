#! python3
# quickBBC.py - prints the latest news from command line
# this is copied from quicWeather.py

import json, requests, sys
# Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: quickBBC.py number')
    sys.exit()
number = ' '.join(sys.argv[1:])

# Download the json data from OpenWeatherMap.org's API
url = 'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=(969ae53245ea0e6992}'
response = requests.get(url)
response.raise_for_status()

BBCData = json.loads(response.text)
# print weather data descriptions
first = BBCData[1]['description'] 
#mintemp = BBCData['main']['temp_min'] - 273.15 
#maxtemp = BBCData['main']['temp_max'] - 273.15 
#pressure = BBCData['main']['pressure']
#humidity = BBCData['main']['humidity']
#description = BBCData['weather'][0]['main'] + ' - ' + BBCData['weather'][0]['description']
#wind_direction = BBCData['wind']['deg'] 
#wind_speed = round(BBCData['wind']['speed'] * 2.2, 2)
#clouds = BBCData['clouds']['all']

print('First new story' % first)
#print('Temperature today is ' + repr(round(temp, 2)))
#print('Maximum temperature today is ' + repr(round(maxtemp, 2)))
#print('Minimum temperature today is ' + repr(round(mintemp,2)))
#print('The weather is ' + description)
#print('Wind directions is ' + repr(wind_direction))
#print('Wind speed ' + repr(wind_speed))
#print('Pressure is ' + repr(pressure))
#print('The humidity is ' + repr(humidity))
#print('The percentage of sky that is cloud covered ' + repr(clouds))

