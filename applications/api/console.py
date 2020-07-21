import api
import logging

#logging.basicConfig(level=logging.DEBUG, format='%(message)s')


apiInst = api.Api()

parameter = {
	"email": "mail",
	"password": "passwd"
}
result = apiInst.console().request("createUser",parameter)
