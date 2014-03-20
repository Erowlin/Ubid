import myjson

import modelmanager

products_path = 'files/products.json'

models = {}

class Models():
	def __init__(self):
		self.models = models
		
	def get(self, name, id=None):
		if name in self.models:
			model = self.models[name]
			for m in model:
				print m["title"]
			return self.models[name]
		else:
			return None

	def insert(self, name, obj):
		print name
		print obj
		self.get(name).append(obj)

	def initialise_model(self, name):
		self.models[name] = []








@app.route('/products/<integer:id>' methods=["GET"]):
def get_product(id):
	product = modelmanager.get("products", id)
	product.title