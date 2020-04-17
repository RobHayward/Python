import urllib2

# Define a string variable called 'filepath' pointing to the location of the data
filepath = ''
baseurl = 'http://www.metoffice.gov.uk'

# Read in cleaned csv data on weather station information from WeatherStations.txt

# For each line in the cleaned file, 
# 		get url
#       get name 
#       get data via url
#		write data to disk with a file name = station name