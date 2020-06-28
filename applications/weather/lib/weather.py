import glob
import os

def getLatestFile():
	my_path = os.path.abspath(os.path.dirname(__file__))
	#path = os.path.join(my_path, "../data/test.csv")
	list_of_files = glob.glob(my_path+'/../data/*.json') # * means all if need specific format then *.json
	latest_file = max(list_of_files, key=os.path.getctime)
	#print(latest_file)
	return latest_file
