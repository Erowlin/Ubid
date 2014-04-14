# Permet de transformer n'importe quelle requête en entrée vers un format unique. Permet d'avoir un format standard, que ce soit du POST, PUT, DELETE, GET, et depuis ANgular ou Postman.
def get_response(request):
	if len(request.form) > 0: # If POST from WEb Browser
        		resp = request.form
    	elif request.json is not None and len(request.json) > 0: # If POST from Angular
          		resp = request.json
	else:
		resp = request.args # If GET Values
    	return resp


# Permet de transformer une liste de Model en json. Sérialize chaque objet dans la liste en Json, puis retourne une nouvelle liste au format Json
def list_to_json(liste):
	json = []
	for elem in liste:
		print "toto"
		json.append(elem.json())
	return json
