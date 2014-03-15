
import myjson

secret_key = 'a43%@3'

products_path = 'files/products.json'
users_path = 'files/users.json'

public_users_field = ['username', 'city', 'postalcode', 'id']
public_products_field = []

products = myjson.load_json(products_path)
users = myjson.load_json(users_path)

