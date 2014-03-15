from models import Models

class Products(Models): 
	def __init__(self):
		self.fields = ['description']
		self.unique = ['title']
		Models.__init__(self)
		print self.save_path
		print self.title