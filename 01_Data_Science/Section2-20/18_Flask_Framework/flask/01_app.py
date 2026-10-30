from flask import Flask

# basic skeleton

# creates an instance of the flask class, which will be your WSGI application.

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home page, which is made using Flask.'

@app.route('/index')
def index():
    return 'Welcome to the Index page'

if __name__ == '__main__':
    app.run(debug=True)
