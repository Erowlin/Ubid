# -*-coding:UTF-8 -*
from flask import Blueprint, Flask, jsonify, make_response, request, abort, render_template, session
import helpers
import json
from glob import Models
import base64
import loginmanager

from users import Users

pay = Blueprint('pay', __name__, '')

# ADD
@pay.route('/', methods=['POST'])
def new_pay():
	resp = helpers.get_response(request) 
	loginmanager.verify_token(resp)
	payment = Payments().new(resp)
	payment.save()
	return jsonify({'status':'New payment ok', 'payment':payment._to_json()}), 200 

# EDIT
@pay.route('/<int:pay_id>', methods=['POST'])
def edit_pay(pay_id):
	resp = helpers.get_response(request)
	
	payments = Models().getBy('payments', 'id', pay_id) 
	loginmanager.has_right(payments[0], resp = resp)
	if payments is None:
		return "Payment not found", 404
	payments[0].edit(resp)
	payments[0].save()
	return jsonify({'payment': payments[0].json()}), 200

# GET
@pay.route('/<int:pay_id>', methods=['GET'])
def get_pay(pay_id):
	resp = helpers.get_response(request)

	payments = Models().getBy('payments', 'id', pay_id) 
	if payments is None:
		return "Payment not found", 404
	return jsonify({'payment' : payments[0].json()})

# DELETE
@pay.route('/<int:pay_id>', methods=['DELETE'])
def delete_pay(pay_id):
	resp = helpers.get_response(request)
	loginmanager.verify_token(resp)
	ret = Models().delete('payments', 'id', id=pay_id)
	if ret == False : 
		return 'KO', 401
	return 'OK', 200