# -*-coding:UTF-8 -*
from flask import abort, make_response, session
from users import Users
from glob import Models
import os
import base64

# Vérification des crédentials de l'utilisateur, on provide son username et password.
# Retourne l'utilisateur si les credentials sont bons
def check_credentials(username, password): 
	user = Models().getBy('users', 'username', username)
	if user == None:
		abort(make_response('Username not found', 401))
	if base64.b64encode(password) == user[0].password:
		return user[0]
	return False
		# Create token

# Vérification du token de l'utilisateur, on regarde par rapport au token qui est stocké en session. 
# Si aucun token n'est stocké en session, ou si le token ne correspond à aucun utilisateur, on envoie un message d'erreur. 
# Si le token correspond à un utilisateur, on retourne l'utilisateur concerné. 
def verify_token(resp = None, token= None):
	if resp is not None and 'token' in resp:
		token = resp['token']
	if token is None:
		abort(make_response('No token provided', 401))
	if 'token' not in session: 
		abort(make_response('No session on server', 500))
	if session['token'] == token:
		u = Models().getBy('users', 'id', session['user_id'])
		return u[0]
	else:
		print session['token']
		print token
		abort(make_response('Bad token', 401))

# Génère un token, sauvegarde en session le token (session['token']), son id (session['user_id']) et retourne le token généré. 
# Sauvegarde également le token dans la base de donnée.
def generate_token(user):
	token = base64.b64encode(str(os.urandom(10)))
	session['token'] = token
	session['user_id'] = user.id
	user.token = token
	user.save()
	return token

# Logout l'utilisateur en supprimant sa session et en supprimant le token. 
def logout(resp):
	u = verify_token(resp)
	u.token = ''
	session.clear()
	u.save()
	return True

# Vérifie si l'utilisateur a le droit de modifier le modèle actuel, retourne True s'il peut le modifier, sinon retourne False.
def has_right(model, token = None, resp=None):
	if resp is not None : 
		if 'token' in resp:
			token = resp['token']
		else:
			abort(make_response('No token provided', 401))
	elif token is None:
		abort(make_response('No token provided', 401))
	u = verify_token(token = token)
	if model.__class__.__name__ == 'Users':
		if model.id == session['id']:
			return True
		else:
			return False
	if model is not None and u.id == model.user_id:
		return True
	return False

