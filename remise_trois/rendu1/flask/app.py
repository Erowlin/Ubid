import sys
import os
from flask import Flask, jsonify, make_response, request, abort, render_template, session
from datetime import timedelta
import helpers

from glob import Models

app = Flask(__name__)

sys.path.insert(0, os.getcwd() + '/models')

import modelmanager
from products import Products
from users import Users
from addresses import Addresses
from payments import Payments
from categories import Categories

import users_api
import products_api
import bids_api
import addresses_api
import payments_api
import categories_api

# Blueprint allow to do "multi-file", by registering collections
app.register_blueprint(users_api.usr, url_prefix="/users")
app.register_blueprint(products_api.prod, url_prefix="/products")
app.register_blueprint(bids_api.bid, url_prefix="/bids")
app.register_blueprint(addresses_api.addr, url_prefix="/addresses")
app.register_blueprint(payments_api.pay, url_prefix="/payments")
app.register_blueprint(categories_api.cat, url_prefix="/categories")

app.secret_key = 'tamere'




# All calls here are executed once, after the first request. 
# This hack is made before of a bug in Flask that initialize 2 times the main application.
# From : https://stackoverflow.com/questions/9449101/how-to-stop-flask-from-initialising-twice-in-debug-mode
@app.before_first_request
def initialize():
	modelmanager.init_models()

@app.after_request
def after_request(data):
	response = make_response(data)
	response.headers['Content-Type'] = 'application/json'
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Headers'] = "Origin, X-Requested-With, Content-Type, Accept"
	response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
	return response

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify( { 'error': 'Bad Request' } ), 400)
	
@app.errorhandler(401)
def bad_request(error):
    return make_response(jsonify( { 'error': 'Unauthorized' } ), 401)
	
@app.errorhandler(403)
def bad_request(error):
    return make_response(jsonify( { 'error': 'Forbidden' } ), 403)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify( { 'error': 'Not Found' } ), 404)

if __name__ == '__main__':
	# We don't do initializations here because of a bug in Flask : 
	# https://stackoverflow.com/questions/9449101/how-to-stop-flask-from-initialising-twice-in-debug-mode
	
	app.run(debug = True)
