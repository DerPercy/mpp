import json
from datetime import datetime
import logging

log = logging.getLogger("weather.parse")


class Parser:
	jsonData = ""
	hourlyList = ""
	def __init__(self, content):
		log.debug(content)
		self.jsonData = json.loads(content)
		self.hourlyList = WeatherDataList(self.jsonData["hourly"])
		
	def uiTime(self):
		dt_object = datetime.fromtimestamp(self.jsonData["current"]["dt"])
		return dt_object.strftime("%H:%M")
	
	def hourly(self):
		return self.hourlyList
		
	
def parseFile(f):
	contents =f.read()
	return Parser(contents)



class WeatherDataList:
	jsonDataList = []
	weatherDataList = []
	def __init__(self,jsonDataList):
		self.jsonDataList = jsonDataList
		for jsonData in jsonDataList:
			self.weatherDataList.append(WeatherData(jsonData))
	def get(self,index):
		return self.weatherDataList[index]
		

class WeatherData:
	jsonData = []
	def __init__(self,jsonData):
		self.jsonData = jsonData
	def uiTemp(self):
		tempValue = round(self.jsonData["temp"],0)
		return str(int(tempValue)) + " °C"
