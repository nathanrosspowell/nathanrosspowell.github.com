import os
import sqlite3
from contextlib import closing
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

#-----------------------------------------------------------------------------
# The root folder for this project.
root_dir = os.path.split( os.path.realpath( __file__ ) )[ 0 ]

# Configuration.
DATABASE = os.path.join( root_dir, "database/website.db" )
DEBUG = True
SECRET_KEY = "huge_secret"
USERNAME = "admin"
PASSWORD = "default"

app = Flask( __name__ )
app.config.from_object( __name__ )

#-----------------------------------------------------------------------------
# Database specific code.
def init_db():
    with closing( connect_db() ) as db:
        with app.open_resource( "schema.sql" ) as sql:
            db.cursor().executescript( sql.read() )
        db.commit()

def connect_db():
    return sqlite3.connect( app.config[ "DATABASE" ] )

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request( exception ):
    g.db.close()

#-----------------------------------------------------------------------------
# Views.
@app.route('/')
def index():
    return render_template( "index.html" )

@app.route( "/blog/" )
def blog():
    rows = g.db.execute( \
"select title, post, author, posted, tags from posts order by id desc" )
    posts = [ dict(title=r[0],post=r[1],author=r[2]) for r in rows.fetchall() ]
    return render_template( "blog.html", blog_posts=posts )

@app.route( "/blog/<int:post_id>" )
def blog_post( post_id ):
    return render_template( "blog_post.html" )

#-----------------------------------------------------------------------------
# Run the app.
if __name__ == "__main__":
    app.run()
