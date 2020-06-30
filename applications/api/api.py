import json
import logging
import os

log = logging.getLogger("api.Api")


class Api:
	def __init__(self):
		log.debug("Initializing API")
		my_path = os.path.abspath(os.path.dirname(__file__))+"/config/app.json"
		f = open(my_path,"r")
		contents =f.read()
		f.close()
		log.debug(contents)
	
