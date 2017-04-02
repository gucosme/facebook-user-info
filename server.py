from bottle import delete, get, post, run, request, response, error
from json import dumps

from db_manager import get_all_users, delete_user

@get('/user/<user_id>')
def get_user(user_id):
	response.content_type = 'application/json'
	return dumps({"id": user_id})

@get('/users')
def get_users():
	response.content_type = 'application/json'
	return dumps(get_all_users(request.query.get('limit', '')))

@post('/user')
def save_user():
	fb_id = request.forms.get('facebookId')
	response.status = 201

@delete('/user/<id>')
def del_user(id):
	status = delete_user(id)
	response.status = 204 if status == 1 else 404

@error(404)
def error404(error):
	return 'Not Found' 

run(host='localhost', port=8080, debug=False)
