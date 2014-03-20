from models import Models
import glob
import myjson

print 'Users loaded'

class Users(Models): 
	def __init__(self, json=None):
		self.fields = ['name']
		self.unique = ['email']
		self.void
		Models.__init__(self, json)



