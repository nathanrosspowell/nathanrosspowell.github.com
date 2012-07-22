import os
import datetime
import operator
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
connect_html = "connect.html"
index_html = "index.html"
atom_xml = "atom.xml"
games_html = "games.html"
games_order = (
    "menu/games",
    "games/dirt-showdown",
    "games/dirt-showdown",
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
# Jinja2 additions.
def getkey( dic, key ):
    return dic[ key ]
app.jinja_env.globals.update( getkey = getkey )

def equalto( x, y ):
    return x == y
app.jinja_env.tests.update( equalto = equalto )

#-----------------------------------------------------------------------------
# Helpers.
def directory():
    return os.path.join( app.config[ "ROOT_DIR" ],
        app.config[ "FLATPAGES_ROOT" ]
    )

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

def get_tags( freq_sort = False, take_n = None ):
    tags = {}
    for post in all_pages( directory(), "blog" ):
        for tag in post.meta.get( "tags", [] ):
            if tags.has_key( tag ):
                tags[ tag ] += 1
            else:
                tags[ tag ] = 1
    tag_list = []
    if freq_sort:
        tuple_list = sorted( tags.iteritems(),
            key=operator.itemgetter( 1 ),
            reverse = True
        )
        tag_list = [ tup[ 0 ] for tup in tuple_list ]
    else:
        tag_list = sorted( tags.keys() )
    return ( tag_list, tags ) if take_n is None else ( tag_list[ : take_n ], tags )

def tag_pages( tag ):
    for post in all_pages( directory(), "blog" ):
        if tag in post.meta.get( "tags", [] ):
            yield post
#-----------------------------------------------------------------------------
# Redirects.
@app.route('/')
def index():
    return article_page( index_html, ( "menu/home-page", ) )

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
def blog( select_blogs = None, tag_selection = None ):
    if select_blogs is not None:
        blogs = select_blogs
    else:
        blogs = [ post for post in latest_pages( 5, directory(), "blog" ) ]
    blogroll = pages.get_or_404( "menu/blogroll" )
    tags = get_tags( freq_sort = True, take_n = 5)
    return base_render_template( blog_html,
        pages = blogs,
        blogroll = blogroll,
        tags = tags[ 0 ],
        tag_freq = tags[ 1 ],
        tag_selection = tag_selection
    )

@app.route( "/blog/tag/<path:tag>/" )
def blog_tag( tag ):
    if tag not in get_tags()[ 0 ]:
        return base_render_template( "error.html", error="400" ), 400
    blogs = [ post for post in tag_pages( tag ) ]
    return blog( select_blogs = blogs, tag_selection = tag )


@app.route( "/<path:page_path>/" )
def page( page_path ):
    page = pages.get_or_404( page_path )
    template = page.meta.get( "template", blog_post_html )
    return base_render_template( template, pages=[page] )

@app.route( "/feeds/atom.xml" )
def atom():
    blogs = [ post for post in all_pages( directory(), "blog" ) ]
    w3c_update = get_w3c_date()
    return base_render_template( atom_xml,
        pages = blogs,
        w3c_update = w3c_update
    ), 200, {'Content-Type': 'application/atom+xml; charset=utf-8'}

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
