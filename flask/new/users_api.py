from flask import Blueprint, Flask, jsonify, make_response, request, abort, render_template, session
import helpers
import json
from glob import Models
import base64
import loginmanager

from users import Users

usr = Blueprint('usr', __name__, '')

# Register the user.
@usr.route('/register', methods=['POST'])
def new_user():
	resp = helpers.get_response(request)
	u = Users().new(resp)
	u.save()
	return jsonify({'status':'User Registration ok', 'user':u.public()}), 200

# Try to login the user. If the username and passwords match, a token is returned. This token must be returned on all requests, for POST and GET.
@usr.route('/login', methods=['POST'])
def login():
	resp = helpers.get_response(request)
	if not 'username' in resp or not 'password' in resp:
		return "Bad request, missing username or password in request", 400
	user = loginmanager.check_credentials(resp['username'], resp['password'])
	if user != False:
		token = loginmanager.generate_token(user)
		return jsonify({'status': 'Logged in successfully', 'token':token}), 200
	else:
		return 'Bad credentials', 401

# Logout the user.
# Param post : "token"
@usr.route('/logout', methods=['POST'])
def logout():
	resp = helpers.get_response(request)
	loginmanager.logout(resp)
	return 'Logged out', 200

# Return the profil of the user. 
# If "token" is specified in the URL, and the token match the profil asked, it's the secured profil that is returned.
# If "token" is specified in the URL, and the token DOES NOT match the profil asked, it's the public profile that is returned.
# If "token" is NOT specified in the URLm it's the public profile that is returned.
@usr.route('/<int:user_id>', methods=['GET'])
def profil(user_id):
	resp = helpers.get_response(request)
	user = Models().getBy('users', 'id', user_id)
	if user is None:
		return 'User not found', 404
	if 'token' in resp:
		if loginmanager.has_right(user[0], resp['token']):
			return jsonify({'status':'User connected', 'user':user[0].secured()}), 200
		return jsonify({'user' : user[0].public()}), 200
	else:
		return jsonify({'user' : user[0].public()}), 200

