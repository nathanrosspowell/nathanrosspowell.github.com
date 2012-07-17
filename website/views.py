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
games_html = "games.html"
games_order = (
    "dirt-showdown",
    "operation-flashpoint-red-river",
    "ferrari-the-race-experience",
    "ride-to-hell",
    "hot-wheels-beat-that",
)

#-----------------------------------------------------------------------------
# Helpers.
def latest_pages( n, dir, subdir ):
    for page_path in walk.take( n, os.path.join( dir, subdir ), walk.newest ):
        urlpath = os.path.splitext( page_path.replace( dir, "" )[1:] )[ 0 ]
        yield pages.get_or_404( urlpath )

def get_pages( page_path ):
    return [page]

def base_render_template( template, **kwargs ):
    kwargs[ "credits" ] = pages.get_or_404( "menu/credits-short" )
    kwargs[ "bio" ] = pages.get_or_404( "menu/bio" )
    return render_template( template, **kwargs )

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
    games = pages.get_or_404( "menu/games" )
    games_list = list( pages.get_or_404( "games/%s" % ( name, ) ) for name in games_order )
    games_list.insert( 0, games )
    return base_render_template( games_html,
            pages = games_list, 
            comment_override_id = "/menu/games/",
            comment_override_title = "games"
    )

@app.route("/credits/")
def credits():
    return page( "menu/credits" )

@app.route("/career/")
def career():
    return page( "menu/career" )

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
