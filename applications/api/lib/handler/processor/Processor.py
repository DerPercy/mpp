#import lib

class AbstractProcessor:
	jsonData = None
	rootHandler = None
	def __init__(self,jsonData,rootHandler):
		self.jsonData = jsonData
		self.rootHandler = rootHandler

	def process(self,parameter):
#		print("AbstractProcessor.process")
#		print(self.jsonData)
		if self.jsonData["type"] == "entity.create":
			self.rootHandler.entity(self.jsonData["entity"]).build(parameter).create()
#		print(parameter)

class StorageCreateProcessor(AbstractProcessor):
	pass
