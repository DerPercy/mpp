import configparser
import logging
import urllib.request
from datetime import datetime



logging.basicConfig(level=logging.DEBUG, format='%(message)s')

config = configparser.ConfigParser()                                     
config.read('./config.ini')

# Read config
apikey = config.get('OPENWEATHERMAP', 'APIKEY')
lat = config.get('OPENWEATHERMAP', 'LAT')
lon = config.get('OPENWEATHERMAP', 'LON')

log = logging.getLogger("weather.fetch")

apiurl = "https://api.openweathermap.org/data/2.5/onecall?lat=" + lat + "&lon=" + lon + "&exclude=minute&appid=" + apikey + "&units=metric&lang=de"
log.debug(apiurl)

# Fetching data
contents = urllib.request.urlopen(apiurl).read()
#contentString = bytes(contents,'utf-8')
#log.debug(contents)

dt_object = datetime.now()

file1 = open("./data/"+dt_object.strftime("%Y%m%d_%H%M")+".json","wb")
file1.write(contents) 
file1.close() 
