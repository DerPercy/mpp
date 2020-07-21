from .AbstractHandler import AbstractHandler
import abc
import logging
#from .processor.Processor import AbstractProcessor
from .processor.Processor import StorageCreateProcessor
from .storage.Storage import DatabaseStorage

log = logging.getLogger("api.roothandler")

#import AbstractHandler

class RootHandler(AbstractHandler):
	storageHandler = None
	apiHandler = None
	entityHandler = None
	@abc.abstractmethod
	def build_handler_by_key(self,key,jsonData):
		if key == "storage":
			self.storageHandler = StorageHandler(jsonData)
			return self.storageHandler
		if key == "api":
			self.apiHandler = ApiHandler(jsonData,self)
			return self.apiHandler
		if key == "entities":
			self.entityHandler = EntityHandler(jsonData,self)
			return self.entityHandler
		pass
	def storage(self):
		return self.storageHandler
	def api(self):
		return self.apiHandler


class EntityHandler(AbstractHandler):
	pass



class ApiHandler(AbstractHandler):
	consoleHandler = None
	def build_handler_by_key(self,key,jsonData):
		if key == "console":
			self.consoleHandler = ConsoleHandler(jsonData,self.rootHandler)
			return self.consoleHandler
		if key == "http":
			return HTTPHandler(jsonData,self.rootHandler)
	def console(self):
		return self.consoleHandler

class AbstractRequestHandler(AbstractHandler):
	def request(self,key,parameter):
		print("Request")
	def read_json_data(self,jsonData):
		for key in jsonData:
			if jsonData[key]["type"] == "storage.create":
				StorageCreateProcessor(jsonData[key])
			else:
				print("Unknown processor for "+key)

class ConsoleHandler(AbstractRequestHandler):
	pass


class HTTPHandler(AbstractRequestHandler):
	pass

class StorageHandler(AbstractHandler):
	def build_handler_by_key(self,key,jsonData):
		if jsonData["type"] == "database":
			return DatabaseStorage(jsonData)
