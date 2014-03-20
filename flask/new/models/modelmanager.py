from os import path, listdir
from os.path import isfile, join
from imp import load_source
import importlib

import myjson
from glob import Models



# This function initialize the glob model with all the json data.
def init_module_models(name, module):
	Models().initialise_model(name)
	json = myjson.load_json("files/"+ name+ ".json")
	for j in json:
		to_exec = "module." + name.title() + "(" + str(j) + ")"
		p = eval(to_exec)
		Models().insert(name, p)

# This function initialize the models, load the class, prepare the 
def init_models():
	print "Loading Model Manager..."
	file_path = path.dirname(path.abspath(__file__))
	ls = listdir(file_path)
	files = []
	for f in ls:
		if str(f).endswith('.py') and isfile(join(file_path, f)):
			files.append(f.split('.')[0])
	files.remove('modelmanager')
	files.remove('models')
	for f in files:
		module = importlib.import_module(f)
		if hasattr(module, f.title()):
 			init_module_models(f, module)
 	#print products
 	p = models['products'][0]
 	#glob.Models("products")
	print "Model Manager Loaded !"