# -*-coding:Latin-1 -*
from flask import session
from models import Models
import glob
import myjson

class Products(Models): 
	def __init__(self, json=None):
		self.fields = ['buyoutPrice', 'reservePrice', 'imgUrl']
		self.unique = [] # Unique fields are also mandatory
		self.mandatory = ['title', 'description', 'dateStart', 'dateLength', 'startPrice']
		self.editable_fields = ['title', 'description', 'imgUrl']
		Models.__init__(self, json)