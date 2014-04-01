from flask import abort, make_response

import modelmanager
import json
import copy
import glob

class Models(object):
	def __init__(self, json=None):
		self.__set_fields__(json)

	def new(self, attributes = None):
		# Attributes var is type of dict.
		if attributes is not None :
			for key in attributes:
				attribute_status = self._attribute_exist_(key) 
				print "Verifications : [" + key + "]=[" + str(attribute_status)+"]"
				if attribute_status == 1:
					setattr(self, key, attributes[key])
				elif attribute_status == 2:
					if attributes[key] is '' or attributes[key] is None or len(attributes[key]) == 0:
						abort(make_response('Mandatory field : ' + key, 400))
					if  glob.Models().getBy(self.__class__.__name__, key, attributes[key]) is not None:
						abort(make_response(key + ' Already taken.', 400))
					else:
					 	setattr(self, key, attributes[key])
				elif attribute_status == 3 and attribute[key] == '':
					abort(make_response('Mandatory field : ' + key, 400))
		setattr(self, "id", modelmanager.model_size(self.__class__.__name__))
		return self

	def save(self):
		modelmanager.save(self)

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

	def _attribute_exist_(self, attribute):
		if hasattr(self, 'fields') and attribute in self.fields:
			return 1
		elif hasattr(self, 'unique') and attribute in self.unique:
			return 2
		elif hasattr(self, 'mandatory') and attribute in self.unique:
			return 3
		else:
			abort(make_response('Forbiden field : ' + attribute, 400))

	def _to_json(self):
		to_remove = ['fields', 'unique']
		obj_copy = copy.deepcopy(self) #We dont want to work directly on the object, but rather on a copy of it
		for remove in to_remove:
			if hasattr(obj_copy, remove):
				delattr(obj_copy, remove)

		js = json.loads(json.dumps(obj_copy.__dict__))
		return js