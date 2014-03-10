from flask import Flask, jsonify, make_response, request, abort, render_template, session
from datetime import timedelta


import myjson
import json

import users
import products


products_path = 'files/products.json'
users_path = 'files/users.json'

app = Flask(__name__)

# Blueprint allow to do "multi-file", by registering collections
app.register_blueprint(products.pdt, url_prefix="/products")
app.register_blueprint(users.usr, url_prefix="/user")

 
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.permanent_session_lifetime = timedelta(minutes=60)

users = []

@app.after_request
def after_request(data):
	response = make_response(data)
	response.headers['Content-Type'] = 'application/json'
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Headers'] = "Origin, X-Requested-With, Content-Type, Accept"
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
	products = myjson.load_json(products_path)
	users = myjson.load_json(users_path)
	app.run(debug = True)