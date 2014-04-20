# -*-coding:UTF-8 -*
from flask import Blueprint, Flask, jsonify, make_response, request, abort, render_template, session
import helpers
import json
from glob import Models
import base64
import loginmanager

from users import Users
from addresses import Addresses

addr = Blueprint('addresse', __name__, '')

# ADD
@addr.route('/', methods=['POST'])
def new_addr():
	resp = helpers.get_response(request) 
	loginmanager.verify_token(resp)
	addresse = Addresses().new(resp)
	addresse.save()
	return jsonify({'status':'New addresse ok', 'addresse':addresse._to_json()}), 200 

# EDIT
@addr.route('/<int:addr_id>', methods=['POST'])
def edit_addr(addr_id):
	resp = helpers.get_response(request)
	
	addresses = Models().getBy('addresses', 'id', addr_id) 
	loginmanager.has_right(addresses[0], resp = resp)
	if addresses is None:
		return "Addresse not found", 404
	addresses[0].edit(resp)
	addresses[0].save()
	return jsonify({'addresse': addresses[0].json()}), 200

# GET
@addr.route('/<int:addr_id>', methods=['GET'])
def get_addr(addr_id):
	resp = helpers.get_response(request)

	addresses = Models().getBy('addresses', 'id', addr_id) 
	if addresses is None:
		return "Addresse not found", 404
	return jsonify({'addresse' : addresses[0].json()})

# DELETE
@addr.route('/<int:addr_id>', methods=['DELETE'])
def delete_addr(addr_id):
	resp = helpers.get_response(request)
	loginmanager.verify_token(resp)
	ret = Models().delete('addresses', 'id', id=addr_id)
	if ret == False : 
		return 'KO', 401
	return 'OK', 200