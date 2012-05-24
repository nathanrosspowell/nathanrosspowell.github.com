import os
import datetime
import walk_dates as walk
from website import \
app,                \
pages
from flask import   \
Flask,              \
request,            \
session,            \
g,                  \
redirect,           \
url_for,            \
abort,              \
render_template,    \
flash

#-----------------------------------------------------------------------------
# Helpers.
def latest_pages( n, dir, subdir ):
    for page_path in walk.take( n, os.path.join( dir, subdir ), walk.newest ):
        urlpath = os.path.splitext( page_path.replace( dir, "" )[1:] )[ 0 ]
        yield pages.get_or_404( urlpath ) 

#-----------------------------------------------------------------------------
# Stuff.
@app.route('/')
def index():
    return render_template( "index.html", pages=pages )

@app.route( "/blog/" )
def blog():
    dir = os.path.join( app.config[ "ROOT_DIR" ], app.config[ "FLATPAGES_ROOT" ] )
    blogs = [ post for post in latest_pages( 5, dir, "blog" ) ]
    return render_template( "blog.html", pages = blogs  )

@app.route( "/<path:page_path>/" )
def page( page_path ):
    print "page_path", page_path
    page = pages.get_or_404( page_path )
    template = page.meta.get( "template", "blog_post.html" )
    return render_template( template, pages=[page] ) 
