import myjsonobject
import glob

class Models(object):
	def __init__(self, json=None):
	self.save_path = "files/" + str(self.__class__.__name__.lower()) + ".json"
		print self.save_path
		self.__set_fields__(json)
		print "Init Models"

	def new(self, attributes):
		# Attributes is type of dict.
		for key in attributes:
			setattr(self, key, attributes[key])
		return self

	def save(self):
		print self.fields
		for field in self.fields:
			print field
			print(eval("self."+field))

	def json_to_object(self, json):
		for json in jsons:
			print json


	def __set_fields__(self, json=None):
		print self.fields
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
