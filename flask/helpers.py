from flask import abort, make_response

import base64
import myjson
import copy
import re

# Verify the presence of mandatory fields.
# If mandatory fields are missing or empty, abort with 400 and list all the missing fields
# fields : List of mandatory fields ['field1', 'field2']
# request : The original request
def verify_mandatory_field_form(fields, request):
	missing_fields = ''
	for param in fields:
		if param not in request.form or request.form[param] == '':
			missing_fields += (' ' + param)			
	if len(missing_fields):
		abort(make_response('Missing fields :'+  missing_fields, 400))

def get_by(model, value_to_match, field_to_search="id", public_fields=None, test=""):
	model_entry = filter(lambda u: u[field_to_search] == value_to_match, model)
	if model_entry:
		if public_fields:
			model_copy_entry = copy.deepcopy(model_entry)
			for public_field in public_fields:
				r = re.search('(assoc_)a-z(_)_(a-z)')
				if r:
					print r
				model_copy_entry[public_field] = model_entry[0][public_field]
		return model_entry[0]
	print "Return None from " + test
	return None


# Update the json object and save it in database.
###
# model : the global model to modify
# save_path : The file path for the json model
# value_model : the model_entry to modify
# exclude_fields : Exclude fields, even if they are in the form
# null_fields : Don't set fields if they are empty
# mandatory_fields : Check if all fields are presents
def update_object(model, value_model, request, save_path, exclude_fields=None, null_fields=None, mandatory_fields=None):
	model_entry = get_by(model, value_model, test="update_object")
	if model_entry: # If the model_entry exist
		new_model = {}
		if mandatory_fields:
			verify_mandatory_field_form(mandatory_fields, request)
		for param in request.form:
			can_set = 1
			if exclude_fields and param in exclude_fields:
				can_set = 0
			if null_fields and param in null_fields and request.form[param] is not None:
				if param == 'password' :
					new_model[param] = base64.b64encode(request.form[param])
				can_set = 0
			if can_set == 1 and param in model_entry:
				new_model[param] = request.form[param]
	
		for param in new_model:
			if param in model_entry:
				model_entry[param] = new_model[param]
		myjson.save_json(model, save_path)
	else: # If the model_entry does not exist
		abort(make_response('Object not found', 400))
	return model_entry


# Create a new object for the given model
###
# model : the global model to modify
# save_path : The file path for the json model
# allowed_fields : The allowed fields for the model
# mandatory_fields : Check if the mandatory fields are present and not empty
# special fields : Special behaviour for special fields
# Association : Allow association between 2 models. association = [{association_field : 'field_name', association_entry: entry, association_name: 'name'}]
def new_object(model, request, save_path, allowed_fields, mandatory_fields=None, special_fields=None, associations=None):
	new_model = {}
	if mandatory_fields:
		verify_mandatory_field_form(mandatory_fields, request)

	for param in allowed_fields:
		if special_fields and param in special_fields and param in request.form:
			if param == 'password' :
				new_model[param] = base64.b64encode(request.form[param])
		else:
			if param in request.form:
				new_model[param] = request.form[param]
			else: 
				new_model[param] = ''
	if association:
		for association in associations:
			pass
	new_model['id'] = len(model) + 1
	model.append(new_model)
	myjson.save_json(model, save_path)

def delete_object(model, request, save_path):
	model_entry = get_by(model, request.form['id'])
	if model_entry is None:
		abort(make_response('Object not found', 400))
	model.delete(model_entry)
	myjson.save(model, save_path)


