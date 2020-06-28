import lib

fParse = lib.getLatestFile()
jsonFile = open(fParse,"r")
parsedFile = lib.parseFile(jsonFile)
jsonFile.close()


print(parsedFile.uiTime())
