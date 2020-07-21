class AbstractHandler:
	childNodes = {}
	rootHandler = None
	def __init__(self,jsonData, rootHandler = None):
		self.rootHandler = rootHandler
		self.read_json_data(jsonData)
		
	def read_json_data(self,jsonData):
		for key in jsonData:
			handler = self.build_handler_by_key(key,jsonData[key])
			if not handler:
				print(self.__class__.__name__+": No Handler for:"+key)
			else:
				self.childNodes[key] = handler
	
	# Abstract
	def build_handler_by_key(self,key,jsonData):
		pass
			
