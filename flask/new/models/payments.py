# -*-coding:UTF-8 -*
from flask import session
from models import Models
import glob
import myjson


class Payments(Models): 
	def __init__(self, json=None):
		self.belongs_to = ['user']
		self.editable_fields = ['number', 'security', 'date', 'name']
		Models.__init__(self, json)