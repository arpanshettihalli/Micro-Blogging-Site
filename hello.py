from flask import Flask
from flask import request
from flask import current_app,g
app = Flask(__name__)
@app.route('/post/<int:post_id>')
def post(post_id):
    return '<h1>Hello {}!<h1>'.format(post_id)
@app.route('/login')
def login():
    return '<h1>Hello World!<h1>'
@app.route('/logout')
def logout():
    return '<h1>Hello World!<h1>'
@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Hello World!<h1>'
@app.errorhandler(500)
def server_error(e):
    return '<h1>Hello World!<h1>'

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    current = current_app.name
    print('User-Agent:', user_agent)
    print('Current:', current)
    return '<p>Your browser is {}</p>'.format(user_agent)
@app.route('/user')
def user():
    name = request.args.get('name')
    print('method=',request.method)
    return '<h1>Hello {}!<h1>'.format(name)
@app.before_request
def load_user():
    g.user = 'Rithul'

@app.route('/profile')
def profile():
    return '<hi>Profile {}</hi>'.format(g.user)
if __name__ == '__main__':
    app.run(debug=True)
