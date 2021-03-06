from flask import Blueprint, Flask, jsonify, make_response, request, abort, session
import myjson


import json
import decorator
import os

import glob
import base64
import copy

import helpers


# We create Blueprint with name "usr"
usr = Blueprint('usr', __name__, '')

users_path = 'files/users.json'

@usr.route('/login', methods=['POST', 'OPTIONS'])
@decorator.crossdomain(origin='*')
def login():
    resp = helpers.get_response(request)
    mandatory_fields = ["username", "password"]
    helpers.verify_mandatory_field_form(mandatory_fields, resp)
    username = resp['username']
    password = resp['password']
    user = filter(lambda u: u['username'] == username, glob.users)
    if len(user) == 0:
        return 'No such username', 401	
    if password != base64.b64decode(user[0]['password']):
        return 'Wrong password', 403
    generate_token(user[0])
    return jsonify({'user_id': user[0]["id"], 'token': user[0]['token']}), 200
	
@usr.route('/logout', methods=['POST', 'OPTIONS'])
@decorator.crossdomain(origin='*')
def logout():
    resp = helpers.get_response(request)
    has_right_abort(resp, resp['user_id'])
    user = helpers.get_by(glob.users, resp['user_id'])
    destroy_token(user)
    return 'Logout successful', 201

@usr.route('/', methods=['POST', 'OPTIONS'])
@decorator.crossdomain(origin='*')
def register():
    resp = helpers.get_response(request)
    if len(resp['password']) < 6:
    	return 'password too short', 406
    usersMatch = filter(lambda u: u['username'] == resp['username'], glob.users)
    if len(usersMatch) != 0 :
    	return 'Username already taken', 409
    allowed_fields = ['username', 'password', 'email', 'address1', 'address2', 'city', 'firstname', 'lastname', 'postalcode', 'country', 'token']
    mandatory_fields = ['username', 'password', 'email', 'address1', 'city', 'firstname', 'lastname', 'postalcode', 'country']
    special_fields = ['password', 'token']
    helpers.new_object(glob.users, resp, users_path, allowed_fields, mandatory_fields, special_fields)
    return 'Register successful', 201

@usr.route('/<int:user_id>', methods=['POST', 'OPTIONS'])
@decorator.crossdomain(origin='*')
def update(user_id):
    resp = helpers.get_response(request)
    has_right_abort(resp, user_id)
    user = helpers.update_object(glob.users, user_id, resp, users_path, null_fields=['password'])
    u = copy.deepcopy(user)
    del u['password']
    return jsonify({"user": u}), 200

@usr.route('/<int:user_id>', methods=['GET', 'OPTIONS'])
@decorator.crossdomain(origin='*')
def show(user_id):
    resp = helpers.get_response(request)
    user = helpers.get_by(glob.users, user_id)
    if user is None:
        abort(make_response("User not found",400))
    u = copy.deepcopy(user)        
    del u['password']
    if not 'user_id' in resp or int(resp['user_id']) != user_id or not 'token' in resp or u['token'] != resp['token']: # Public profil
        del u['address1']
        del u['address2']
        del u['email']
        del u['firstname']
        del u['lastname']
        del u['token']
    if (len(u) != 0):
        return jsonify({'user': u})
    return 'User Not found', 401


# Function to check if the token is expired or not.
@usr.route('/islogged', methods=['POST'])
@decorator.crossdomain(origin='*')
def is_logged():
    resp = helpers.get_response(request)
    if has_right(resp, resp['user_id']):
        return 'Ok', 200
    return 'Ko', 403

# Check if the user is authenticated and if he has the right to access ressource.
# If it's not the same user, abort 400
def has_right_abort(resp, user_id=None):
    if not resp or not 'user_id' in resp or not 'token' in resp:
        abort(make_response('Missing Token or User Id',400))
    id = has_right(resp, user_id)
    if id != False:
        return id
    else:
        abort(401)

# Return true if same user and token, otherwise return false
def has_right(resp, user_id):
    if  not resp or not 'user_id' in resp or not 'token' in resp:
        return 0
    token = resp['token']
    user = helpers.get_by(glob.users, user_id)
    if int(resp['user_id']) != int(user_id) or resp['token'] != user['token']:
        return False
    else:
        return True

def generate_token(user):
    user = helpers.get_by(glob.users, user['id'])
    user['token'] = base64.b64encode(str(user['id']) + str(os.urandom(5)) + str(glob.secret_key))
    myjson.save_json(glob.users, users_path)

def destroy_token(user):
    user['token'] = ''
    myjson.save_json(glob.users, users_path)

def get_user_by_id(user_id, token=None):
    user = helpers.get_by(glob.users, user_id)
    if user is None:
        abort(make_response("User not found",400))
    u = copy.deepcopy(user)
    del u['password']
    if  user_id != u['id'] or 'token' is None or u['token'] != token: # Public profil
        del u['address1']
        del u['address2']
        del u['email']
        del u['firstname']
        del u['lastname']
        del u['token']
    return u

