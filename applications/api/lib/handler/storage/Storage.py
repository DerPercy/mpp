
class AbstractStorage:
	def __init__(self,jsonData):
		pass
	
class DatabaseStorage(AbstractStorage):
	def insert(self,parameter):
		print("Todo: Insert")
		print(parameter)
