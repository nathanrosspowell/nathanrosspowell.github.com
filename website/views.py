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
tag_html = "tag.html"
archive_html = "archive.html"
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
def getkey( d, key ):
    e = "_ERROR_"
    r = d.get( key, e )
    if r == e:
        print "\tDEBUG: asked for", key 
        print "\tDEBUG: dic:", dic 
        return "0"
    return r
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

def add_to_dict( d, key ):
    if d.has_key( key ):
        d[ key ] += 1
    else:
        d[ key ] = 1

def get_tags( freq_sort = False, take_n = None ):
    tags = {}
    for post in all_pages( directory(), "blog" ):
        for tag in post.meta.get( "tags", [] ):
            add_to_dict( tags, tag )
    tag_list = []
    if freq_sort:
        tuple_list = sorted( tags.iteritems(),
            key=operator.itemgetter( 1 ),
            reverse = True
        )
        tag_list = [ tup[ 0 ] for tup in tuple_list ]
    else:
        tag_list = sorted( tags.keys() )
    return (tag_list, tags) if take_n is None else (tag_list[ :take_n ], tags)

def tag_pages( tag ):
    for post in all_pages( directory(), "blog" ):
        if tag in post.meta.get( "tags", [] ):
            yield post

def get_archive( specific = None, take_n = None ):
    years = {}
    months = {}
    days = {}
    for post in all_pages( directory(), "blog" ):
        path = post.path.replace( "blog", "" )
        year, month, day, title = [ x for x in path.split( "/" ) if x ]
        add_to_dict( years, year )
        month_path = os.path.join( year, month )
        add_to_dict( months, month_path )
        day_path = os.path.join( month_path, day )
        add_to_dict( days, day_path )
    arcs = dict( 
        years.items() +
        months.items() +
        days.items()
    )
    if specific == "years":
        arc_list = years.keys()
    elif specific == "months":
        arc_list = months.keys()
    elif specific == "days":
        arc_list = days.keys()
    else:
        arc_list = arcs.keys()
    arc_list = sorted( arc_list, reverse = True )
    return (arc_list, arcs) if take_n is None else (arc_list[ :take_n], arcs)

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
def blog( template = blog_html, page_list = None, select_blogs = None, tag_selection = None, **kwargs ):
    if select_blogs is not None:
        blogs = select_blogs
    elif page_list is not None:
        blogs = page_list
    else:
        blogs = [ post for post in latest_pages( 5, directory(), "blog" ) ]
    blogroll = pages.get_or_404( "menu/blogroll" )
    take_n = 20 
    all_tags = get_tags( take_n = take_n )
    top_tags = get_tags( freq_sort = True, take_n = take_n )
    arc_years = get_archive( specific = "years", take_n = take_n )
    arc_months = get_archive( specific = "months", take_n = take_n )
    arc_days = get_archive( specific = "days", take_n = take_n )
    return base_render_template( template,
        pages = blogs,
        blogroll = blogroll,
        all_tags_n = all_tags[ 0 ],
        top_tags_n = top_tags[ 0 ],
        tag_freq = all_tags[ 1 ],
        tag_selection = tag_selection,
        arc_years_n = arc_years[ 0 ],
        arc_months_n = arc_months[ 0 ],
        arc_days_n = arc_days[ 0 ],
        arc_freq = arc_years[ 1 ],
        **kwargs
    )

@app.route( "/blog/tag/" )
def blog_tags():
    all_tags = get_tags()
    top_tags = get_tags( freq_sort = True )
    return blog( 
        template = tag_html,
        all_tags = all_tags[ 0 ],
        top_tags = top_tags[ 0 ],
    )

@app.route( "/blog/archive/" )
def blog_archives():
    arcs = get_archive()
    return blog( 
        template = archive_html,
        arcs = arcs[ 0 ],
    )

@app.route( "/blog/tag/<path:item>/" )
def blog_tag( item ):
    if item not in get_tags()[ 0 ]:
        return base_render_template( "error.html", error="400" ), 400
    blogs = [ post for post in tag_pages( item ) ]
    return blog( select_blogs = blogs, tag_selection = item )

@app.route( "/blog/archive/<path:item>/" )
def blog_archive( item ):
    return blog()


@app.route( "/<path:page_path>/" )
def page( page_path ):
    page = pages.get_or_404( page_path )
    template = page.meta.get( "template", blog_post_html )
    return blog( 
        template = template,
        page_list = [ page ] 
    )

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
