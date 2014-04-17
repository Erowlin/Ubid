# -*-coding:Latin-1 -*
from flask import session
from models import Models
import glob
import myjson

class Categories(Models): 
	def __init__(self, json=None):
		self.fields = ['name']
		self.has_many = ['products'] 
		Models.__init__(self, json)