# -*-coding:UTF-8 -*
from flask import session
from models import Models
import glob
import myjson


class Addresses(Models): 
	def __init__(self, json=None):
		self.belongs_to = ['user']
		self.editable_fields = ['street1', 'street2', 'country', 'zipcode', 'city']
		Models.__init__(self, json)