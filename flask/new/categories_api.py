# -*-coding:UTF-8 -*
from flask import Blueprint, Flask, jsonify, make_response, request, abort, render_template, session
import helpers
import json
from glob import Models
import base64
import loginmanager

from products import Products
from categories import Categories

cat = Blueprint('cat', __name__, '')

@cat.route('/', methods=['POST'])
def new_category():
	resp = helpers.get_response(request)
	loginmanager.verify_token(resp)
	category = Categories().new(resp)
	category.save()
	return jsonify({'category' : category._to_json()})

@cat.route('/<int:cat_id>', methods=['POST'])
def edit_category(cat_id):
	resp = helpers.get_response(request)
	
	categories = Models().getBy('categories', 'id', cat_id) # Retourne une liste
	if categories is None:
		return "Category not found", 404
	categories[0].edit(resp)
	categories[0].save()
	return jsonify({'category': categories[0].json()}), 200

@cat.route('/<int:cat_id>', methods=['GET'])
def get_category(cat_id):
	resp = helpers.get_response(request)

	categories = Models().getBy('categories', 'id', cat_id) # Retourne une liste
	if categories is None:
		return "Category not found", 404
	return jsonify({'category' : categories[0].json()})

@cat.route('/<int:cat_id>', methods=['DELETE'])
def delete_category(cat_id):
	resp = helpers.get_response(request)
	loginmanager.verify_token(resp)
	ret = Models().delete('categories', 'id', id=cat_id) # Rajouter un paramètre pour vérifier le token de l'utilisateur et le droit qu'il a de delete.
	if ret == False : 
		return 'KO', 401
	return 'OK', 200

@cat.route('/<int:cat_id>/products', methods=['GET']) # Liste des enchères d'un objet
def get_category_products(cat_id):
	resp = helpers.get_response(request)
	categories = Models().getBy('categories', 'id', cat_id)
	return jsonify({'category' : categories[0].id, 'products' : helpers.list_to_json(categories[0].products)}), 200