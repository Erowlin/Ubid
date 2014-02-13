from flask import Flask, jsonify, make_response, request, abort, render_template, session
from datetime import timedelta

import json
import base64

products_path = 'files/products.json'
users_path = 'files/users.json'

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.permanent_session_lifetime = timedelta(minutes=60)

products = []
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
	
@app.route('/products', methods = ['POST'])
def add_product():
    is_authenticated()
    if not request.json or not 'name' in request.json:
        abort(400)
    if not 'current_price' in request.json or int(request.json['current_price']) < 0:
        abort(400)
    if not 'shipping_cost' in request.json or int(request.json['shipping_cost']) < 0:
        abort(400)
    if 'duration' in request.json and int(request.json['duration']) < 0:
        abort(400)
		
	duration = request.json.get('duration', 0)
	
	## To complete
    product = {
        'id': len(products) + 1,
        'current_price': request.json['current_price'],
        'name': request.json['name'],
        'shipping_cost': request.json['shipping_cost'],
        'description': request.json.get('description', ""),
        'categories': request.json.get('categories', ""),
		'duration' : request.json.get('duration', 0),
		'is_buy_it_now' : request.json.get('duration', 0) == 0
    }
    products.append(product)
    save_json(products, products_path)

    return jsonify( { 'products' : products } ), 201

@app.route('/products')
def get_products():
	return jsonify( { 'products' : products } )
	
@app.route('/products/<int:product_id>')
def get_product(product_id):
    product = filter(lambda p: p['id'] == product_id, products)
    if len(product) == 0:
        abort(404)
    return jsonify( { 'product': product[0] } )
	
@app.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	usersMatch = filter(lambda u: u['name'] == username, users)
	if len(usersMatch) == 0:
		abort(401)
	if usersMatch[0]['password'] != base64.b64decode(password):
		abort(403)
	
	session['username'] = request.form['username']
	return 'Login successful', 201
	
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return 'Logout successful', 201

## Utilities.
def is_authenticated():
	if 'username' not in session:
		abort(401)

def load_json(path):
	with open(path, 'r') as json_data:
	  data = json.load(json_data)
	return data
	
def save_json(data, path):
	with open(path, 'w') as outfile:
	  json.dump(data, outfile)
	

if __name__ == '__main__':
	products = load_json(products_path)
	users = load_json(users_path)
	app.run(debug = True)