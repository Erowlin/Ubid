def get_response(request):
	if len(request.form) > 0: # If POST from WEb Browser
        		resp = request.form
    	elif request.json is not None and len(request.json) > 0: # If POST from Angular
          		resp = request.json
	else:
		resp = request.args # If GET Values
    	return resp