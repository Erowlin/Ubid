from os import path, listdir
from os.path import isfile, join
from imp import load_source
import importlib

import copy
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

def set_has_many(modele, field):
	setattr(modele, field, Models().getBy(field, modele.__class__.__name__.lower()[:-1] + "_id", modele.id))

def set_belongs_to(modele, field):
	setattr(modele, field, Models().getBy(field + "s", "id", eval("modele." + field + "_id")))

# Define the references between 2 models, the 'belongs_to' and the 'has_many'.
def init_references(models):
	for model_name in models:
		mods = Models().get(model_name)
		for model in mods: # All models in "user"
			if hasattr(model, 'has_many'): 
				for field in model.has_many: # All fields in "has_many"
					set_has_many(model, field)
			if hasattr(model, 'belongs_to'):
				for field in model.belongs_to : 
					set_belongs_to(model, field)

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
	print files
	for f in files:
		module = importlib.import_module(f)
		if hasattr(module, f.title()):
 			init_module_models(f, module)
 			print f + " Loaded"
 	init_references(files)
	print "Models successfully Loaded !"

def model_size(model):
	minimum = 0
	models = Models().get(model)
	if models is not None:
		for m in models:
			if m.id > minimum:
				minimum = m.id
	minimum += 1
	return minimum

def save(obj):
	models = Models().get(obj.__class__.__name__)
	model = filter(lambda u: u.id == int(obj.id), models)
	
	if len(model) is 0:
		models.append(obj)
	else:
		model[0] = copy.deepcopy(obj)
	final = []
	for m in models:
		final.append(m._to_json())
	myjson.save_json(final, obj.__class__.__name__)
