from flask import Flask, jsonify, request, g
from flask_httpauth import  HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from adl_user.adl_user import get, get_id, put, post, delete
from DB_Example.Ref.urusan import get_urusan, get_urusan_id
from DB_Example.Ref.bidang import get_bidang, get_bidang_id
from DB_Example.Ref.program import get_program, get_program_id
from DB_Example.Ref.fungsi import get_fungsi, get_fungsi_id

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
#token_serializer = Serializer(app.config['SECRET_KEY'], expires_in=3600)
token_serializer = Serializer(app.config['SECRET_KEY'], expires_in=3600)

auth = HTTPTokenAuth('Bearer')


users = ['token1', 'token2', 'token3']
for user in users:
    token = token_serializer.dumps({'username': user}).decode('utf-8')
    print('*** token for {}: {}\n'.format(user, token))


@auth.verify_token
def verify_token(token):
    g.user = None
    try:
        data = token_serializer.loads(token)
    except:  # noqa: E722
        return False
    if 'username' in data:
        g.user = data['username']
        return True
    return False


@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % g.user


### adl_user.adl_user ###
@app.route('/users')
@auth.login_required
def get_users():
	get()
	return get()
@app.route('/users/<int:id>')
@auth.login_required
def get_user(id):
	get_id(id)
	return get_id(id)
@app.route('/users/add', methods = ['POST'])
@auth.login_required
def add_user():
	post()
	return post()
@app.route('/users/update', methods = ['POST'])
@auth.login_required
def update_user():
	put()
	return put()
@app.route('/users/delete/<int:id>')
@auth.login_required
def del_user(id):
	delete(id)
	return delete(id)

### Ref.urusan ###
@app.route('/ref_urusan')
@auth.login_required
def get_ref_urusan():
	get_urusan()
	return get_urusan()
@app.route('/ref_urusan/<int:id>')
@auth.login_required
def get_urusan_(id):
	get_urusan_id(id)
	return get_urusan_id(id)

### Ref.bidang ###
@app.route('/ref_bidang')
@auth.login_required
def get_ref_bidang():
	get_bidang()
	return get_bidang()
@app.route('/ref_bidang/<id>')
@auth.login_required
def get_bidang_(id):
	get_bidang_id(id)
	return get_bidang_id(id)

### Ref.program ###
@app.route('/ref_program')
@auth.login_required
def get_ref_program():
	get_program()
	return get_program()
@app.route('/ref_program/<id>')
@auth.login_required
def get_program_(id):
	get_program_id(id)
	return get_program_id(id)

### Ref.fungsi ###
@app.route('/ref_fungsi')
@auth.login_required
def get_ref_fungsi():
	get_fungsi()
	return get_fungsi()
@app.route('/ref_fungsi/<id>')
@auth.login_required
def get_fungsi_(id):
	get_fungsi_id(id)
	return get_fungsi_id(id)




@app.errorhandler(404)
def not_found(error = None):
	message = {
		'status': 404,
		'message': 'Not Found: ' + request.url,
	}
	resp = jsonify(message)
	resp.status_code = 404

	return resp


if __name__ == "__main__":
	app.run(debug = True)