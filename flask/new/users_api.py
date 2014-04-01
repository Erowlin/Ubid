from flask import Blueprint, Flask, jsonify, make_response, request, abort, render_template, session
import helpers
from glob import Models

from users import Users

usr = Blueprint('usr', __name__, '')

@usr.route('/', methods=['GET'])
def user():
	return 'okk', 200

@usr.route('/', methods=['POST'])
def new_user():
	resp = helpers.get_response(request)
	u = Users().new(resp)
	if u == None:
		return 'KO', 400
	u.save()
	return 'okk', 200