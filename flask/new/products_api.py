# -*-coding:UTF-8 -*
from flask import Blueprint, Flask, jsonify, make_response, request, abort, render_template, session
import helpers
import json
from glob import Models
import base64
import loginmanager

from users import Users
from products import Products

prod = Blueprint('prod', __name__, '')

@prod.route('/', methods=['POST'])
def new_product():
	resp = helpers.get_response(request)
	product = Products().new(resp)
	product.save()
	return jsonify({'product' : product._to_json()})

@prod.route('/<int:product_id>', methods=['POST'])
def edit_product(product_id):
	resp = helpers.get_response(request)
	product = Models().getBy('products', 'id', product_id) # Retourne une liste
	if product is None:
		return "Product not found", 404
	product[0].edit(resp)
	product[0].save()
	return jsonify({'product': product[0].json()}), 200

@prod.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
	resp = helpers.get_response(request)
	product = Models().getBy('products', 'id', product_id) # Retourne une liste
	if product is None:
		return "Product not found", 404
	return jsonify({'product' : product[0].json()})

@prod.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
	resp = helpers.get_response(request) 
	ret = Models().delete('products', 'id', id=product_id) # Rajouter un paramètre pour vérifier le token de l'utilisateur et le droit qu'il a de delete.
	if ret == False : 
		return 'KO', 401
	return 'OK', 200

