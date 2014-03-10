from flask import Blueprint, Flask, jsonify, make_response, request, abort, render_template, session
from flask.ext import login
import myjson

import helpers
import glob

pdt = Blueprint('pdt', __name__, '')

products_path = 'files/products.json'



@pdt.route('/', methods= ['POST'])
def add_product():
	## To complete
    resp = helpers.get_response(request)
    allowed_fields = ['title', 'description', 'dateStart', 'dateLength', 'startPrice', 'buyoutPrice', 'reservePrice', 'imgUrl']
    mandatory_fields = ['title', 'description', 'dateStart', 'dateLength', 'startPrice']
    user = helpers.get_by(glob.users, session["id"])
    association_field = [{'association_name': 'user_id', 'association_value': 'id'}]
    product = helpers.new_object(users, resp, products_path, allowed_fields, mandatory_fields, associations=association_field)
    return jsonify( { 'product' : product } ), 201

@pdt.route('/')
def get_products():
	return jsonify( { 'products' : products } )
	
@pdt.route('/products/<int:product_id>')
def get_product(product_id):
    product = filter(lambda p: p['id'] == product_id, products)
    if len(product) == 0:
        abort(404)
    return jsonify( { 'product': product[0] } )