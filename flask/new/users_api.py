# -*-coding:Latin-1 -*
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
	# Request contient la requête qui a été envoyée au serveur.
	resp = helpers.get_response(request) # Formate les réponses, que ce soit en POST, en GET, ou avec Postman.
	u = Users().new(resp) #Créer un nouvel utilisateur, on passe les paramètres de la requête en params, l'objet est automatiquement crée.
	u.save() # On sauvegarde l'objet dans le .json
	return jsonify({'status':'User Registration ok', 'user':u.public()}), 200 # On fait une réponse au client en envoyant le status de la requête, et on lui retourne l'user avec son profil public

# Try to login the user. If the username and passwords match, a token is returned. This token must be returned on all requests, for POST and GET.
@usr.route('/login', methods=['POST'])
def login():
	resp = helpers.get_response(request)
	if not 'username' in resp or not 'password' in resp: # Si username et / ou password ne sont pas dans la requête, erreur
		return "Bad request, missing username or password in request", 400 # Retourne au client le code d'erreur 400
	user = loginmanager.check_credentials(resp['username'], resp['password']) # On vérifie les identifiants
	print user.products
	if user != False:  # Si identifiants OK
		token = loginmanager.generate_token(user) # On génère le token de l'utilisateur, et on stock en session l'id et le token
		return jsonify({'status': 'Logged in successfully', 'token':token}), 200 # On retourne au client le token
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
	user = Models().getBy('users', 'id', user_id) # Retourne une liste d'utilisateurs. Vu qu'on demande une ID, et que l'id est unique, on peut sans problème faire user[0] pour accéder au premier élément
	if user is None: # Si la liste retournée est vide, c'est que  aucun utilsiateur n'a cet id
		return 'User not found', 404
	if 'token' in resp:
		if loginmanager.has_right(user[0], resp['token']): # On vérifie le token 
			return jsonify({'status':'User connected', 'user':user[0].secured()}), 200 # On retourne le profil utilisateur en supprimant le champ "Mot de passe", c'est l'utilisateur qui consulte son propre profil
		return jsonify({'user' : user[0].public()}), 200 # On retourne le profil utilisateur, comme si l'utilisateur A voulait consulter le profil de l'utilisateur B
	else:
		return jsonify({'user' : user[0].public()}), 200

@usr.route('/<int:user_id>', methods=['POST'])
def edit_user(user_id):
	resp = helpers.get_response(request)
	user = loginmanager.verify_token(resp) # On vérifie le token en envoyant la request
	user.edit(resp) #On édite l'utilisateur en passant la requête à la fonction edit
	user.save() # On sauvegarde en BDD
	return jsonify({'user' : user.secured()}), 200 # On retourne à l'utilisateur son profil secured.

@usr.route('/<int:user_id>/products', methods=['GET']) # Liste des produits d'un utilisateur
def get_user_products(user_id):
	resp = helpers.get_response(request)
	user = Models().getBy('users', 'id', user_id)
	return jsonify({'user' : user[0].id, 'products' : helpers.list_to_json(user[0].products)}), 200

@usr.route('/<int:user_id>/bids', methods=['GET']) # Liste des enchères d'un utilisateur
def get_user_products(user_id):
	resp = helpers.get_response(request)
	user = Models().getBy('users', 'id', user_id)
	return jsonify({'user' : user[0].id, 'bids' : helpers.list_to_json(user[0].bids)}), 200