# -*-coding:UTF-8 -*
from flask import abort, make_response, jsonify
from models import Models
import glob
import myjson
import base64
import copy


class Users(Models): 
	def __init__(self, json=None):
		self.fields = ['name'] #Default fields, can be blank in the request.
		self.unique = ['email', 'username', 'rate', 'rateNumber'] #Unique fields are also mandatory // Rate = note de l'utilisateur & rate_number = nombre de vote (pour le calcul coté client)
		self.mandatory = ['password'] # Mandatory fields.
		self.intern_fields = ['token']
		self.editable_fields = ['name', 'password', 'email']
		self.has_many = ['products', 'bids', 'addresses', 'payments']
		self.__password = None # Special field with a callback
		Models.__init__(self, json)

	# We set the special functions, they should not be called directly.
	# When we do User.password = 'abcdef', 
	# the method __set_password is automatically called
	def __get_password(self):
		return self.__password

	# When we set the password, we encode it with base64
	def __set_password(self, password):
		if len(password) < 6:
			abort(make_response('Password too short, should be 6 characters minimum', 400))
		self.__password = base64.b64encode(password)

	# Define the delete callback
	def __del_password(self):
		del self.__password

	# We define the callback, and say :
	# Hey password field, when I set you like "user.password = abcdef", I want you to call the method "__get_password()" for me !
	password = property(__get_password, __set_password, __del_password, '')
	
	# Public profile
	def public(self):
		ret = copy.deepcopy(self)
		del ret.password
		del ret.token
		del ret.name
		return ret._to_json()

	# Private profile, we remove password.
	def secured(self):
		ret = copy.deepcopy(self)
		del ret.password
		return ret._to_json()

