from flask import Flask
from flask import request
from flask import current_app,g,make_response,redirect,abort

app = Flask(__name__)
@app.route('/post/<int:post_id>')
def post(post_id):
    if post_id == 1:
        abort(404)
    return '<h1>Hello {}!<h1>'.format(post_id)
@app.route('/login')
def login():
    return '<h1>Hello World!<h1>'
@app.route('/logout')
def logout():
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
@app.route('/cookie')
def cookie():
    response = make_response('<hi>This site contains cookie</h1>')
    response.set_cookie('name', 'Rithul')
    return response
@app.route('/happyfappy')
def happyfappy():
    return redirect('https://www.happyfappy.net/')
@app.route('/test')
def test():
    abort(404)
if __name__ == '__main__':
    app.run(debug=True)
