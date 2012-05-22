import sqlite3
from flask import \
Flask, \
request, \
session, \
g, \
redirect, \
url_for, \
abort, \
render_template, \
flash

# Configuration.
DATABASE = "/tmp/website.db"
DEBUG = True
SECRET_KEY = "huge_secret"
USERNAME = "admin"
PASSWORD = "default"

app = Flask( __name__ )
app.config.from_object( __name__ )

def connect_db():
    return sqlite3.connect( app.config[ "DATABASE" ] )

@app.route('/')
def index():
    return render_template( "index.html" )

@app.route( "/blog/" )
def blog():
    return "Blog home"

@app.route( "/blog/<int:post_id>" )
def blog_post( post_id ):
    return "Blog post %d" % ( post_id, )

if __name__ == "__main__":
    app.run()
