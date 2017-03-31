from bottle import delete, get, post, run, request, response, error
from json import dumps

import db_manager

@get('/user/<user_id>')
def getUser(user_id):
	response.content_type = 'application/json'
	return dumps({"id": user_id})

@get('/user')
def getUsers():
	return

@post('/user')
def saveUser():
	fb_id = request.forms.get('facebookId')
	response.status = 201
	return fb_id

@error(404)
def error404(error):
	return 'Not Found' 

run(host='localhost', port=8080, debug=True)
