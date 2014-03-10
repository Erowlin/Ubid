from flask import Blueprint, Flask, jsonify, make_response, request, abort, session
import myjson

import json
import decorator

import glob
import base64
import copy
import pprint

import helpers

# We create Blueprint with name "usr"
usr = Blueprint('usr', __name__, '')

users_path = 'files/users.json'

@usr.route('/login', methods=['POST', 'OPTIONS'])
@decorator.crossdomain(origin='*')
def login():
    mandatory_fields = ["username", "password"]
    print base64.b64encode('tata')
    helpers.verify_mandatory_field_form(mandatory_fields, request)
    username = request.json['username']
    print username
    password = request.json['password']
    usersMatch = filter(lambda u: u['username'] == username, glob.users)
    if len(usersMatch) == 0:
        return 'No such username', 401	
    if password != base64.b64decode(usersMatch[0]['password']):
        return 'Wrong password', 403
    session['id'] = usersMatch[0]["id"]
    return jsonify({'userId': usersMatch[0]["id"]}), 200
	
@usr.route('/logout', methods=['POST'])
def logout():
	session.pop('id', None)
	return 'Logout successful', 201

@usr.route('/', methods=['POST', 'OPTIONS'])
@decorator.crossdomain(origin='*')
def register():
    if len(request.json['password']) < 6:
    	return 'password too short', 406
    usersMatch = filter(lambda u: u['username'] == request.json['username'], glob.users)
    if len(usersMatch) != 0 :
    	return 'Username already taken', 409
    allowed_fields = ['username', 'password', 'email', 'address1', 'address2', 'city', 'firstname', 'lastname', 'postalcode', 'country']
    mandatory_fields = ['username', 'password', 'email', 'address1', 'city', 'firstname', 'lastname', 'postalcode', 'country']
    special_fields = ['password']
    helpers.new_object(glob.users, request, users_path, allowed_fields, mandatory_fields, special_fields)
    return 'Register successful', 201

@usr.route('/<int:user_id>', methods=['POST'])
def update(user_id):
    has_right(user_id)
    form_entry = ["email", "address1", "address2"]
    user = helpers.update_object(glob.users, user_id, request, users_path, mandatory_fields=form_entry, null_fields=['password'])
    u = copy.deepcopy(user)
    del u['password']
    return jsonify({"user": u}), 200

@usr.route('/<int:user_id>', methods=['GET'])
def show(user_id):
	user = get_user_by_id(user_id)
	if (len(user) != 0):
                u = copy.deepcopy(user[0])
                del u['password'] # We don't want the client to get the password
                if (not has_right(user_id)): # Access public profil
                    del u['address1']
                    del u['address2']
                    del u['email']
                    del u['firstname']
                    del u['lastname']
                return jsonify({'user': u})
	return 'User Not found', 401

@usr.route('/islogged', methods=['GET'])
def loge():
	if 'id' in session: 
		return str(session["id"])
	return '0'

@usr.route('/test', methods=['GET'])
def testee():
    public_fields = ['assoc_user_id']
    helpers.test_regexp("assoc_user_id")
    return '', 200

# Check if the user is authenticated and if he has the right to access ressource.
# If it's not the same user, abort 400
def has_right_abort(user_id):
	if is_authenticated() and has_right(user_id):
		return
	else:
		abort(401)

# Return true if same user, otherwise return false
def has_right(user_id):
    if is_authenticated() and int(user_id) == int(session["id"]):
        return 1
    else:
        return 0



## Utilities.
def is_authenticated():
	if 'id' not in session or helpers.get_by(glob.users, session['id'], test="User Authentification") is  None:
		return 0
	return 1
def get_user_by_id(id):
    user = filter(lambda u:u['id'] == id, glob.users)
    return user

