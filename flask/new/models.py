
class Models(object):
	def __init__(self, json=None):
		self.__set_fields__(json)

	def new(self, attributes):
		# Attributes var is type of dict.
		for key in attributes:
			setattr(self, key, attributes[key])
		return self

	def save(self):
		for field in self.fields:
			print(eval("self."+field))
		print 'TAMERE'
		print products[0].title

	def __set_fields__(self, json=None):
		if json is not None:
			for field in json:
				setattr(self, field, json[field]) # Set the  fields to default value
		else :
			for field in self.fields:
				setattr(self, field, '') # Set the  fields to default value
			if hasattr(self, 'unique'):
				for uniq in self.unique: # Set the Unique field to default value
					setattr(self, uniq, '')
		return self

	def _is_unique(self, attribute):
		if hasattr(self, 'unique'):
			if attribute in self.unique:
				pass