from flask import abort, make_response, session
from users import Users
from glob import Models
import os
import base64

def check_credentials(username, password):
	user = Models().getBy('users', 'username', username)
	if user == None:
		abort(make_response('Username not found', 401))
	if base64.b64encode(password) == user[0].password:
		return user[0]
	return False
		# Create token

def verify_token(resp = None, token= None):
	if resp is not None and 'token' in resp:
		token = resp['token']
	if token is None:
		abort(make_response('Bad token', 401))
	u = Models().getBy('users', 'token', token)
	if u:
		return u[0]
	else:
		abort(make_response('Bad token', 401))

def generate_token(user):
	token = base64.b64encode(str(os.urandom(10)))
	session['token'] = token
	user.token = token
	user.save()
	return token

def logout(resp):
	u = verify_token(resp)
	u.token = ''
	u.save()
	return True

def has_right(model, token):
	u = verify_token(token = token)
	if model.__class__.__name__ == 'Users':
		if model.id == u.id:
			return True
		else:
			return False
	if model is not None and u.id == model.user_id:
		return True
	return False

