from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1>Hello World!<h1>'
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello {}!<h1>'.format(name)
@app.route('/post/<int:post_id>')
def post(post_id):
    return '<h1>Hello {}!<h1>'.format(post_id)
@app.route('/login')
def login():
    return '<h1>Hello World!<h1>'
@app.route('/logout')
def logout():
    return '<h1>Hello World!<h1>'
if __name__ == '__main__':
    app.run(debug=True)
