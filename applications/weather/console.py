import lib

import logging

#logging.basicConfig(level=logging.DEBUG, format='%(message)s')


fParse = lib.getLatestFile()
jsonFile = open(fParse,"r")
parsedFile = lib.parseFile(jsonFile)
jsonFile.close()

def printHourly(hour):
	print(hour.uiTime()+": "+hour.uiTemp()+" "+hour.uiDescription())

def printDaily(daily,index):
    print("Daily forecast: "+daily.uiDate() +"          "+daily.uiTempMax()+"/"+daily.uiTempMin()+" - "+daily.uiDescription())
    print("")
    daily.hourly().each(printHourly)
    print("")
    print("")

print(parsedFile.uiTime())


parsedFile.daily().each(printDaily)



#print("Hourly forecast:")
#for x in range(48):
#	hour = parsedFile.hourly().get(x)
#	print(hour.uiTime()+": "+hour.uiTemp()+" "+hour.uiDescription())
