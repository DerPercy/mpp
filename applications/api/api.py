import json
import logging
import os
import lib
#from .lib.handler.RootHandler import RootHandler
#from .lib.handler.AbstractHandler import AbstractHandler

log = logging.getLogger("api.Api")


class Api:
	rootHandler = None
	def __init__(self):
		log.debug("Initializing API")
		my_path = os.path.abspath(os.path.dirname(__file__))+"/config/app.json"
		f = open(my_path,"r")
		contents =f.read()
		f.close()
		log.debug(contents)
		jsonData = json.loads(contents)
		self.rootHandler = lib.RootHandler(jsonData)
	def console(self):
		return self.rootHandler.api().console()
		
		
	
