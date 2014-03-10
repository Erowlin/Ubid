from flask import Blueprint, Flask, jsonify, make_response, request, abort, render_template, session
import myjson

pdt = Blueprint('pdt', __name__, '')

products_path = 'files/products.json'



@pdt.route('/', methods= ['POST'])
def add_product():
	## To complete
    
    allowed_fields = ['title', 'description', 'dateStart', 'dateLength', 'startPrice', 'buyoutPrice', 'reservePrice', 'imgUrl']
    mandatory_fields = ['title', 'description', 'dateStart', 'dateLength', 'startPrice']
    
    helpers.new_object(users, request, users_path, allowed_fields, mandatory_fields)
    return jsonify( { 'products' : products } ), 201

@pdt.route('/')
def get_products():
	return jsonify( { 'products' : products } )
	
@pdt.route('/products/<int:product_id>')
def get_product(product_id):
    product = filter(lambda p: p['id'] == product_id, products)
    if len(product) == 0:
        abort(404)
    return jsonify( { 'product': product[0] } )