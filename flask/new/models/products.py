from models import Models
import glob
import myjson

class Products(Models): 
	def __init__(self, json=None):
		self.fields = ['description']
		self.unique = ['title']
		Models.__init__(self, json)

