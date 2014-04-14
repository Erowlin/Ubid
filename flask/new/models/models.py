from flask import abort, make_response, session

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
				if self.verify_errors(key, attributes[key]) >= 0:
					setattr(self, key, attributes[key])

		setattr(self, "id", modelmanager.model_size(self.__class__.__name__))
		return self

	def edit(self, attributes):
		self.__edit_fields__(attributes)
		return self

	def save(self):
		self._verify_mandatory_fields()
		modelmanager.save(self)

	def json(self):
		return self._to_json()


## Fonction privees en dessous, ne devraient jamais etre appele directement par l'API

	def __set_fields__(self, json=None):
		if json is not None:
			for j in json:
				setattr(self, j, json[j])
		else:
			for field in self.fields:
				setattr(self, field, '') # Set the  fields to default value
			if hasattr(self, 'unique'):
				for uniq in self.unique: # Set the Unique field to default value
					setattr(self, uniq, '')
			if hasattr(self, 'mandatory'):
				for mandatory in self.mandatory: # Set the Unique field to default value
					if mandatory != 'password':
						setattr(self, mandatory, '')
			if hasattr(self, 'intern_fields'):
				for intern_field in self.intern_fields: # Set the Unique field to default value
					setattr(self, intern_field, '')
			if hasattr(self, 'belongs_to'):
				for relation in self.belongs_to:
					if relation == "user":
						setattr(self, relation + "_id", session['user_id'])
					else:
						setattr(self, relation + "_id", -1)
		return self

	def __edit_fields__(self, attributes):
		for attribute in attributes:
			if attribute in self.editable_fields:
				print 'Setattr on : ' + attribute + '= ' + attributes[attribute]
				setattr(self, attribute, attributes[attribute])

	def verify_errors(self, key, value):
		status = self._attribute_exist_(key)
		if status == 1: #Normal field
			return 0
		elif status == 2: # Unique (Is also mandatory)
			if value is '' or value is None or len(value) == 0:
				abort(make_response('Mandatory field : ' + key, 400))
			if  glob.Models().getBy(self.__class__.__name__, key, value) is not None:
				abort(make_response(key + ' Already taken.', 400))
		elif status == 3 : # Mandatory field
			if value is '' or value is None or len(value) == 0:
				abort(make_response('Mandatory field : ' + key, 400))
		elif status == -1 :
			abort(make_response('Forbiden field : ' + key + ".\nAuthorized fields : " + self._authorized_fields(), 400))
		elif status == -2:
			return -2
		return 0

	def _attribute_exist_(self, attribute):
		if (hasattr(self, 'fields') and attribute in self.fields):
			return 1
		elif hasattr(self, 'unique') and attribute in self.unique:
			return 2
		elif hasattr(self, 'mandatory') and attribute in self.mandatory:
			return 3
		elif attribute == 'token':
			return -2
		else:
			return -1

	def _verify_mandatory_fields(self):
		if hasattr(self, 'mandatory'):
			for mandatory in self.mandatory:
				value = eval('self.' + mandatory)
				if  value is  None or value is '' or len(value) is 0:
					abort(make_response('Mandatory field : ' + mandatory, 400))
		return 0

	def _authorized_fields(self):
		authorized_fields = ""
		if hasattr(self, 'fields'):
			for f in self.fields:
				authorized_fields += " " + f
		if hasattr(self, 'unique'):
			for f in self.unique:
				authorized_fields += " " + f
		if hasattr(self, 'mandatory'):
			for f in self.mandatory:
				authorized_fields += " " + f
		return authorized_fields

	

	def _to_json(self):
		to_remove = ['fields', 'unique', 'mandatory', 'intern_fields', 'editable_fields', 'belongs_to', 'has_many']
		if hasattr(self, 'has_many'): # Remove the has many fields
			for many in self.has_many:
				print many
				to_remove.append(many)
		if hasattr(self, 'belongs_to'):  # Remove the belongs_to fields
			for belongs in self.belongs_to:
				to_remove.append(belongs)
		obj_copy = copy.deepcopy(self) #We dont want to work directly on the object, but rather on a copy of it
		for remove in to_remove:
			if hasattr(obj_copy, remove):
				delattr(obj_copy, remove)

		js = json.loads(json.dumps(obj_copy.__dict__))
		return js