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
# Global template names
article_html = "article.html"
blog_html = "blog.html"
blog_post_html = "blog_post.html"

#-----------------------------------------------------------------------------
# Helpers.
def latest_pages( n, dir, subdir ):
    for page_path in walk.take( n, os.path.join( dir, subdir ), walk.newest ):
        urlpath = os.path.splitext( page_path.replace( dir, "" )[1:] )[ 0 ]
        yield pages.get_or_404( urlpath ) 

def get_pages( page_path ):
    return [page]

def bio():
    return pages.get_or_404( "menu/bio" )

#-----------------------------------------------------------------------------
# Stuff.
@app.route('/')
def index():
    return page( "menu/home_page" )

@app.route("/connect/")
def connect():
    return page( "menu/connect" )

@app.route("/code/")
def code():
    return page( "menu/code" )

@app.route("/games")
def games():
    return page( "menu/games" )

@app.route("/career/")
def career():
    return page( "menu/career" )

@app.route( "/blog/" )
def blog():
    print "Blog start"
    dir = os.path.join( app.config[ "ROOT_DIR" ], app.config[ "FLATPAGES_ROOT" ] )
    blogs = [ post for post in latest_pages( 5, dir, "blog" ) ]
    print "Blog end", blogs, "NOPE"
    return render_template( blog_html, pages = blogs, bio = bio() ) 

@app.route( "/<path:page_path>/" )
def page( page_path ):
    page = pages.get_or_404( page_path )
    template = page.meta.get( "template", blog_post_html )
    print "####", page_path, template
    return render_template( template, pages=[page], bio = bio() ) 
