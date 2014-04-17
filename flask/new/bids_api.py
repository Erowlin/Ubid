# -*-coding:UTF-8 -*
from flask import Blueprint, Flask, jsonify, make_response, request, abort, render_template, session
import helpers
import json
from glob import Models
import base64
import loginmanager

from users import Users
from products import Products
from bids import Bids

bid = Blueprint('bid', __name__, '')

# ADD
@bid.route('/', methods=['POST'])
def new_bid():
	resp = helpers.get_response(request) 
	loginmanager.verify_token(resp)
	newbid = Bids().new(resp)
	newbid.save()
	return jsonify({'status':'New bid ok', 'bid':newbid._to_json()}), 200 

# EDIT
@bid.route('/<int:bid_id>', methods=['POST'])
def edit_bid(bid_id):
	resp = helpers.get_response(request)
	
	editBid = Models().getBy('bids', 'id', bid_id) 
	loginmanager.has_right(editBid[0], resp = resp)
	if editBid is None:
		return "Bid not found", 404
	editBid[0].edit(resp)
	editBid[0].save()
	return jsonify({'bid': product[0].json()}), 200

# GET
@bid.route('/<int:bid_id>', methods=['GET'])
def get_bid(bid_id):
	resp = helpers.get_response(request)

	getBid = Models().getBy('bids', 'id', bid_id) 
	if getBid is None:
		return "Bid not found", 404
	return jsonify({'bid' : getBid[0].json()})

# DELETE
@bid.route('/<int:bid_id>', methods=['DELETE'])
def delete_bid(bid_id):
	resp = helpers.get_response(request)
	loginmanager.verify_token(resp)
	ret = Models().delete('bids', 'id', id=bid_id)
	if ret == False : 
		return 'KO', 401
	return 'OK', 200