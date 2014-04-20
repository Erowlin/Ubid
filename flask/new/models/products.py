# -*-coding:Latin-1 -*
from flask import session
from models import Models
import glob
import myjson

class Products(Models): 
	def __init__(self, json=None):
		self.fields = ['buyoutPrice', 'reservePrice', 'imgUrl', 'status', 'user', 'categorie', 'lat', 'long']
		self.unique = [] # Unique fields are also mandatory
		self.mandatory = ['title', 'description', 'dateStart', 'dateLength', 'startPrice'] # Champs obligatoires // status : encherissable, en envoi, envoyé ?
		self.editable_fields = ['title', 'description', 'imgUrl', 'lat', 'long'] # Champs éditables par l'utilisateur 
		self.belongs_to = ['user', 'categorie'] # Est rattaché à un utilisateur, crée un champ 'user_id'
		self.has_many = ['bids'] 
		Models.__init__(self, json)