from flask import Flask
from app import app

@app.route('/question/<name>')
def create(name):
    """ With a Variable/parameter"""
    return "<h3>" + name + "</h3>"
