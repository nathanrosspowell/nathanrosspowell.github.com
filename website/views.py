import os
import datetime
import walk_dates as walk
from time_stamp import get_w3c_date
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
atom_xml = "atom.xml"
games_html = "games.html"
games_order = (
    "menu/games",
    "games/dirt-showdown",
    "games/operation-flashpoint-red-river",
    "games/ferrari-the-race-experience",
    "games/ride-to-hell",
    "games/hot-wheels-beat-that",
)
career_order = (
    "menu/career",
    "career/other-experience",
    "career/cv",
)

#-----------------------------------------------------------------------------
# Helpers.
def latest_pages( n, dir, subdir ):
    for page_path in walk.take( n, os.path.join( dir, subdir ), walk.newest ):
        urlpath = os.path.splitext( page_path.replace( dir, "" )[1:] )[ 0 ]
        yield pages.get_or_404( urlpath )

def all_pages( dir, subdir ):
    for page_path in walk.walk( os.path.join( dir, subdir ), walk.newest ):
        urlpath = os.path.splitext( page_path.replace( dir, "" )[1:] )[ 0 ]
        yield pages.get_or_404( urlpath )

def get_pages( page_path ):
    return [page]

def base_render_template( template, **kwargs ):
    kwargs[ "credits" ] = pages.get_or_404( "menu/credits-short" )
    kwargs[ "bio" ] = pages.get_or_404( "menu/bio" )
    return render_template( template, **kwargs )

def article_page( template, page_list ):
    pages_list = list( pages.get_or_404( name ) for name in page_list )
    title = pages_list[ 0 ] 
    comment_id = "/%s/" % page_list[ 0 ]
    comment_title = title.meta.get( "title", "No Title" )
    return base_render_template( template,
            pages = pages_list, 
            comment_override_id = comment_id,
            comment_override_title = comment_title,
    )
    
#-----------------------------------------------------------------------------
# Redirects.
@app.route('/')
def index():
    return page( "menu/home-page" )

@app.route("/connect/")
def connect():
    return page( "menu/connect" )

@app.route("/code/")
def code():
    return page( "menu/code" )

@app.route("/games/")
def games():
    return article_page( games_html, games_order )

@app.route("/credits/")
def credits():
    return page( "menu/credits" )

@app.route("/career/")
def career():
    return article_page( article_html, career_order )

#-----------------------------------------------------------------------------
# Dynamic pages.
@app.route( "/blog/" )
def blog():
    dir = os.path.join( app.config[ "ROOT_DIR" ], app.config[ "FLATPAGES_ROOT" ] )
    blogs = [ post for post in latest_pages( 5, dir, "blog" ) ]
    blogroll = pages.get_or_404( "menu/blogroll" )
    return base_render_template( blog_html, pages = blogs, blogroll = blogroll )

@app.route( "/<path:page_path>/" )
def page( page_path ):
    page = pages.get_or_404( page_path )
    template = page.meta.get( "template", blog_post_html )
    return base_render_template( template, pages=[page] )

@app.route( "/feeds/atom.xml" )
def atom():
    dir = os.path.join( app.config[ "ROOT_DIR" ], app.config[ "FLATPAGES_ROOT" ] )
    blogs = [ post for post in all_pages( dir, "blog" ) ]
    w3c_update = get_w3c_date()
    return base_render_template( atom_xml, pages = blogs, w3c_update = w3c_update ), 200, {'Content-Type': 'application/xml; charset=utf-8'}

#-----------------------------------------------------------------------------
# Error pages.
@app.errorhandler( 404 )
def page_not_found( e ):
    return base_render_template( "error.html", details = e, error="404" )

@app.errorhandler( 403 )
def page_not_found( e ):
    return base_render_template( "error.html", details = e, error="403" )

@app.errorhandler( 410 )
def page_not_found( e ):
    return base_render_template( "error.html", details = e, error="410" )

@app.errorhandler( 500 )
def page_not_found( e ):
    return base_render_template( "error.html", details = e, error="500" )
