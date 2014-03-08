from flask import Blueprint, Flask, jsonify, make_response, request, abort, render_template, session
import myjson

pdt = Blueprint('pdt', __name__, '')

products_path = 'files/products.json'
products = myjson.load_json(products_path)



@pdt.route('/', methods= ['POST'])
def add_product():
    # if not 'current_price' in request.json or int(request.json['current_price']) < 0:
    #     abort(400)
    # if not 'shipping_cost' in request.json or int(request.json['shipping_cost']) < 0:
    #     abort(400)
    # if 'duration' in request.json and int(request.json['duration']) < 0:
    #     abort(400)
		
	
	## To complete
    product = {
        'id': len(products) + 1,
        'name': request.json['name'],
    }
    products.append(product)
    save_json(products, products_path)

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