import json

def load_json(path):
	data = []
	with open(path, 'r') as json_data:
		data = json.load(json_data)
	return data
	
def save_json(data, path):
	with open(path, 'w') as outfile:
	 	json.dump(data, outfile)