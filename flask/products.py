from flask import Blueprint, Flask, jsonify, make_response, request, abort, render_template, session
import myjson
import decorator

import copy
import helpers
import glob
import users

pdt = Blueprint('pdt', __name__, '')

products_path = 'files/products.json'

@pdt.route('/', methods= ['POST', 'OPTIONS'])
@decorator.crossdomain(origin='*')
def add_product():
	## To complete
    resp = helpers.get_response(request)
    allowed_fields = ['title', 'description', 'dateStart', 'dateLength', 'startPrice', 'buyoutPrice', 'reservePrice', 'imgUrl']
    mandatory_fields = ['title', 'description', 'dateStart', 'dateLength', 'startPrice']
    user = helpers.get_by(glob.users, resp['user_id'])
    association_field = [{'association_name': 'user_id', 'association_value': user['id']}]
    product = helpers.new_object(glob.products, resp, products_path, allowed_fields, mandatory_fields, associations=association_field)
    return show(product['id'])

@pdt.route('/', methods=['GET'])
@decorator.crossdomain(origin="*")
def list_products():
    return jsonify({'products': glob.products}), 200

@pdt.route('/<int:product_id>')
@decorator.crossdomain(origin='*')
def show(product_id):
            product = helpers.get_by(glob.products, product_id)
            p = copy.deepcopy(product)
            iduser = p['user_id']
            user = users.get_user_by_id(int(iduser))
            p['user'] = user
            if not p:
                return 'Product Not found', 401
            return jsonify( { 'product' : p } )

@pdt.route('/<int:product_id>', methods=['POST', 'OPTIONS'])
@decorator.crossdomain(origin='*')
def update(product_id):
    resp = helpers.get_response(request) 
    product = helpers.get_by(glob.products, product_id)
    users.has_right_abort(resp, product['user_id'])
    resp = helpers.get_response(request)
    exclude_field = ['reservePrice', 'startPrice', 'id', 'user_id', 'user']
    null_fields = ['title', 'description', 'buyoutPrice', 'dateLength', 'dateStart']
    product = helpers.update_object(glob.products, product_id, resp, glob.products_path, null_fields=null_fields, exclude_fields=exclude_field)
    return show(product_id)

@pdt.route('/<int:product_id>', methods=['DELETE', 'OPTIONS'])
@decorator.crossdomain(origin='*')
def destroy(product_id):
    resp = helpers.get_response(request) 
    product = helpers.get_by(glob.products, product_id)
    if product is None:
        return 'No such product', 400
    users.has_right_abort(resp, product['user_id'])
    helpers.delete_object(glob.products, product_id, products_path)
    return 'Delete ok', 200

@pdt.route('/products/<int:product_id>')
@decorator.crossdomain(origin='*')
def get_product(product_id):
    product = filter(lambda p: p['id'] == product_id, products)
    if len(product) == 0:
        abort(404)
    return jsonify( { 'product': product[0] } )