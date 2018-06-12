from flask import Flask
from app import app


@app.route('/')
def homepage():
    return """<html>
                    <head> 
                        <title>Hello, People</title>
                    </head>
                    <body>
                        <h3>First, Hello Worldly People</h3>
                        <h4> Peek through what?</h4>
                        <em> The </em> <code>Rabbit MQ ?</code>
                    </body>                    
                </html>"""


@app.route('/peek')
def peek():
    return "<h1> Peek through what?</h1>"
    