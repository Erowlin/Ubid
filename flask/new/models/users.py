from models import Models
import glob
import myjson

class Users(Models): 
	def __init__(self, json=None):
		self.fields = ['name']
		self.unique = ['email', 'username']
		Models.__init__(self, json)



