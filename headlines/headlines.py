import feedparser
from flask import Flask

app = Flask(__name__)


from headline_route3 import *



if __name__ == '__main__':
    app.run()
