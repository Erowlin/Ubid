# -*-coding:UTF-8 -*
from flask import session
from models import Models
import glob
import myjson


class Bids(Models): 
	def __init__(self, json=None):
		self.mandatory = ['date']
		self.belongs_to = ['user', 'product'] # Est rattaché à un utilisateur et un produit
		self.editable_fields = ['price']
		Models.__init__(self, json)