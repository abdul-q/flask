import feedparser
from flask import Flask

app = Flask(__name__)

from headline_routes import *
from headline_routes1 import *
from headline_routes2 import *



if __name__ == '__main__':
    app.run()