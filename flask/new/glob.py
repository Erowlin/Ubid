import myjson

products_path = 'files/products.json'

models = {}

class Models():
	def __init__(self):
		self.models = models
		
	def get(self, name):
		name = name.lower()
		if name in self.models:
			return self.models[name]
		else:
			return None

	def getBy(self, modelName, field, fieldValue):
		models = self.get(modelName)
		model = []
		if models is not None and len(models) is not 0 and hasattr(models[0], field):
			model = filter(lambda u: eval("u." + field) == fieldValue, models)
		if len(model) is 0:
			return None
		return model

	def delete(self, modelName, modele = None, id=None):
		models = self.get(modelName)
		if id is not None:
			model = filter(lambda u: u.id== id, models)
			if len(model) is 0:
				return False
			models.remove(model[0])
		else:
			models.remove(modele)
		return True

	def insert(self, name, obj):
		self.get(name).append(obj)

	def initialise_model(self, name):
		self.models[name] = []


