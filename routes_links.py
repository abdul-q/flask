from flask import Flask, url_for
from app import app
#from routes import peek

#Creating Links
@app.route('/link')
def hello():
    createTheLink = "<a href='" + url_for('creates') + "'>Create Something</a>"
    return """<html>
                    <head> 
                        <title>Hello, People</title>
                    </head>
                    <body>
                        """ + createTheLink + """
                    </body>                    
                </html>"""


@app.route('/creates')
def creates():
    return "<h4> Flee </h4>"