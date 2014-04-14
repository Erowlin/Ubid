# -*-coding:Latin-1 -*
from flask import session
from models import Models
import glob
import myjson

class Products(Models): 
	def __init__(self, json=None):
		self.fields = ['buyoutPrice', 'reservePrice', 'imgUrl']
		self.unique = [] # Unique fields are also mandatory
		self.mandatory = ['title', 'description', 'dateStart', 'dateLength', 'startPrice'] # Champs obligatoires
		self.editable_fields = ['title', 'description', 'imgUrl'] # Champs éditables par l'utilisateur 
		self.belongs_to = ['user'] # Est rattaché à un utilisateur, crée un champ 'user_id'
		Models.__init__(self, json)