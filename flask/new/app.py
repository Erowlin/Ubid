from flask import Flask, jsonify, make_response, request, abort, render_template, session
from datetime import timedelta

from products import Products

products_path = 'files/products.json'
users_path = 'files/users.json'

app = Flask(__name__)


# Blueprint allow to do "multi-file", by registering collections

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

@app.route("/products", methods=['POST'])
def new_product():
	print "New Product"
	product = Products().new("toto")
	product.save()
	return "ok", 200

if __name__ == '__main__':
	app.run(debug = True)
