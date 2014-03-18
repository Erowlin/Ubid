import json

def load_json(path):
	data = []
	with open(path, 'r') as json_data:
		data = json.load(json_data)
	return data