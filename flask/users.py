from flask import Blueprint, Flask, jsonify, make_response, request, abort, render_template, session
import myjson

import base64

# We create Blueprint with name "usr"
usr = Blueprint('usr', __name__, '')

users_path = 'files/users.json'
users = myjson.load_json(users_path)

@usr.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	usersMatch = filter(lambda u: u['name'] == username, users)
	if len(usersMatch) == 0:
		return 'No such username', 401	
	if password != base64.b64decode(usersMatch[0]['password']):
		return 'Wrong password', 403
	session['username'] = request.form['username']
	return 'Login successful', 200
	
@usr.route('/logout', methods=['POST'])
def logout():
	session.pop('username', None)
	return 'Logout successful', 201

@usr.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    if len(request.form['password']) < 6:
    	return 'password too short', 406
    password = base64.b64encode(request.form['password'])
    usersMatch = filter(lambda u: u['name'] == username, users)
    if len(usersMatch) != 0 :
    	return 'Username already taken', 409

    user = {
    	'id':  len(users) + 1,
    	'name': username, 
    	'password': password,
    	'cart_total': 0
    }
    users.append(user)
    myjson.save_json(users, users_path)
    return 'Register successful', 201

## Utilities.
def is_authenticated():
	if 'username' not in session:
		abort(401)
