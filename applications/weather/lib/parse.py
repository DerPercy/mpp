import json
from datetime import datetime
import logging

log = logging.getLogger("weather.parse")


class Parser:
	jsonData = ""
	hourlyList = ""
	dailyList = None
	def __init__(self, content):
		log.debug(content)
		self.jsonData = json.loads(content)
		self.hourlyList = WeatherDataList(self.jsonData["hourly"])
		self.dailyList = WeatherDataDailyList(self.jsonData["daily"],self.jsonData["hourly"])

	def uiTime(self):
		dt_object = datetime.fromtimestamp(self.jsonData["current"]["dt"])
		return dt_object.strftime("%H:%M")

	def hourly(self):
		return self.hourlyList

	def daily(self):
		return self.dailyList

def parseFile(f):
	contents =f.read()
	return Parser(contents)


# ========== Daily ==========

class WeatherDataDailyList:
	jsonDataList = None
	jsonDataHourlyList = None

	def __init__(self,jsonDataList,jsonDataHourlyList):
		log.debug("Init WeatherDataDailyList")
		self.jsonDataList = jsonDataList
		self.jsonDataHourlyList = jsonDataHourlyList

	def each(self,_callback):
		index = 0
		for jsonData in self.jsonDataList:
			dt_daily = datetime.fromtimestamp(jsonData["dt"])
			jdHourly = []
			for jdh in self.jsonDataHourlyList:
				dt_hourly = datetime.fromtimestamp(jdh["dt"])
				if dt_hourly.date() == dt_daily.date():
					jdHourly.append(jdh)
			wdd = WeatherDataDaily(jsonData,WeatherDataList(jdHourly))
			_callback(wdd,index)
			index = index + 1


class WeatherDataDaily:
	jsonData = None
	weatherDataHourlyList = None
	def __init__(self,jsonData,weatherDataHourlyList):
		self.jsonData = jsonData
		self.weatherDataHourlyList = weatherDataHourlyList
	def uiDate(self):
		dt_object = datetime.fromtimestamp(self.jsonData["dt"])
		return dt_object.strftime("%a %d.%m.%Y")
	def uiTempMax(self):
		tempValue = round(self.jsonData["temp"]["max"],0)
		return str(int(tempValue)) + "°C"
	def uiTempMin(self):
		tempValue = round(self.jsonData["temp"]["min"],0)
		return str(int(tempValue)) + "°C"
	def uiDescription(self):
		return self.jsonData["weather"][0]["description"]
	def hourly(self):
		return self.weatherDataHourlyList


# ========== Hourly ==========

class WeatherDataList:
	jsonDataList = []
	weatherDataList = []
	def __init__(self,jsonDataList):
		log.debug("Init WeatherDataList")
		self.weatherDataList = []
		self.jsonDataList = jsonDataList
		for jsonData in jsonDataList:
			self.weatherDataList.append(WeatherData(jsonData))
#			print(len(self.weatherDataList))
	def get(self,index):
		return self.weatherDataList[index]
	def each(self,_callback):
		log.debug(len(self.weatherDataList))
		for wdl in self.weatherDataList:
			_callback(wdl)


class WeatherData:
	jsonData = []
	def __init__(self,jsonData):
		self.jsonData = jsonData
	def uiTemp(self):
		tempValue = round(self.jsonData["temp"],0)
		return str(int(tempValue)) + "°C"
	def uiTime(self):
		dt_object = datetime.fromtimestamp(self.jsonData["dt"])
		return dt_object.strftime("%H:%M")
	def uiDescription(self):
		return self.jsonData["weather"][0]["description"]
