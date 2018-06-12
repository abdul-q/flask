from flask import Flask
app = Flask(__name__)

from routes import *
from routes_with_variables import *
from routes_links import *

#gateway interface
wsgi_app = app.wsgi_app



'''
Has been moved to the route file
 @app.route('/')
def homepage():
    return "This is a Primer!" '''


if __name__ == '__main__':
    app.run()