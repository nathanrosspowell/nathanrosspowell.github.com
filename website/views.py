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
blogs_per_page = 5
article_html = "article.html"
blog_html = "blog.html"
blog_all_html = "blog_all.html"
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

def compare( x, type, y ):
    return eval( "x %s y " % ( type, ) )
app.jinja_env.tests.update( compare = compare )

def makedate( value ):
    ret = ""
    year = ""
    month = ""
    day = ""
    for i, part in enumerate( value.split( "/" ) ):
        if i == 0:
            year = part
        elif i == 1:
            month = ", %s" % getdate( part, "month" )
        elif i == 2:
            day = getdate( part, "day" )
    return "%s%s %s" % ( year, month, day )
app.jinja_env.globals.update( makedate = makedate )

def getdate( value, type ):
    if type == "month":
        return [ "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ][ int( value ) - 1 ]
    elif type == "day":
        day = str( int( value ) )
        post = "th"
        if day != "11" and day != "12" and day != "13":
            if day[ -1 ] == "1":
                post = "st"
            elif day[ 0 ] == "2":
                post = "nd"
            elif day[ 0 ] == "3":
                post = "rd"
        return "%s%s" % ( day, post, )

    return "_ERROR_"
app.jinja_env.globals.update( getdate = getdate )

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
        if page_path[ -1 ] != "~":
            urlpath = os.path.splitext( page_path.replace( dir, "" )[1:] )[ 0 ]
            yield pages.get_or_404( urlpath )

def archive_pages_dated( date, dir, subdir ):
    for page_path in walk.walk( os.path.join( dir, subdir ), walk.newest ):
        urlpath = os.path.splitext( page_path.replace( dir, "" )[1:] )[ 0 ]
        if page_path.split( "/blog/" )[ 1 ].startswith( date ):
            yield pages.get_or_404( urlpath )

def all_pages( dir, subdir ):
    for page_path in walk.walk( os.path.join( dir, subdir ), walk.newest ):
        urlpath = os.path.splitext( page_path.replace( dir, "" )[1:] )[ 0 ]
        yield pages.get_or_404( urlpath )

def page_count( dir, subdir ):
    return len( [ a for a in walk.walk( os.path.join( dir, subdir ) ) ] )

def get_pages( page_path ):
    return [page]

def base_render_template( template, **kwargs ):
    kwargs[ "credits" ] = pages.get_or_404( "menu/credits-short" )
    kwargs[ "bio" ] = pages.get_or_404( "menu/bio" )
    return render_template( template, **kwargs )

def article_page( template, page_list ):
    pages_list = list( pages.get_or_404( name ) for name in page_list )
    title = pages_list[ 0 ]
    if pages_list[ 0 ].meta.get( "comments", False ):
        comment_id = "/%s/" % page_list[ 0 ]
        comment_title = title.meta.get( "title", "No Title" )
    else:
        comment_id = None
        comment_title = None
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
def blog( template = blog_html,
          page_list = None,
          select_blogs = None,
          tag_selection = None, **kwargs ):
    if select_blogs is not None:
        blogs = select_blogs
    elif page_list is not None:
        blogs = page_list
    else:
        blogs = [ post for post in latest_pages( ( 0, blogs_per_page ), directory(), "blog" ) ]
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

@app.route( "/blog/" )
def blog_page_0():
    return blog_page( 0 )

@app.route( "/blog/<int:page>/" )
def blog_page( page ):
    lower = 0
    higher = blogs_per_page
    if page > 1:
        lower = blogs_per_page * ( page - 1 )
        higher = blogs_per_page * page
    page_list = [ post for post in latest_pages( ( lower, higher ), directory(), "blog" ) ]
    print "PL>>>", page_list, ( lower, higher ), directory()
    num_pages = page_count( directory(), "blog" )
    navpages =  num_pages / blogs_per_page
    if num_pages % blogs_per_page != 0:
        navpages += 1
    return blog( template = blog_all_html,
        page_list = page_list,
        currentpage = page if page > 0 else 1,
        navpages = navpages,
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
    dates = {}
    for key, value in get_archive()[ 1 ].items():
        date = ""
        parts = key.split( "/" )
        d = dates
        for part in parts:
            date = os.path.join( date, part )
            if not d.has_key( part):
                d[ part ] = ( date, {} )
            d = d[ part ][ 1 ]
    return blog(
        template = archive_html,
        arcs = dates
    )

@app.route( "/blog/tag/<path:item>/" )
def blog_tag( item ):
    if item not in get_tags()[ 0 ]:
        return base_render_template( "error.html", error="400" ), 400
    blogs = [ post for post in tag_pages( item ) ]
    return blog( select_blogs = blogs, tag_selection = item )

@app.route( "/blog/archive/<path:item>/" )
def blog_archive( item ):
    select_blogs = [ post for post in archive_pages_dated( item, directory(), "blog" ) ]
    return blog( select_blogs = select_blogs, date_selection = item )

@app.route( "/blog/all/" )
def blog_all():
    select_blogs = [ post for post in all_pages( directory(), "blog" ) ]
    return blog( select_blogs = select_blogs, custom_blog_title = "All Blogs" )

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
    get_w3c_date()
    blogs = [ post for post in all_pages( directory(), "blog" ) ]
    with open( "website/feed_content.txt", 'r' ) as feed_cache:
        cache_blogs = feed_cache.readlines()
    changed = False
    if len( blogs ) != len( cache_blogs ):
        changed = True
    if not changed:
        for index, blog in enumerate( blogs ):
            if blog.path != cache_blogs[ index ].strip():
                changed = True
                break
    if changed:
        w3c_update = get_w3c_date()
        with open( "website/feed_content.txt", 'w' ) as new_feed:
            new_feed.writelines( [ blog.path+"\n" for blog in blogs ] )
        with open( "website/feed_time.txt", 'w' ) as new_time:
            new_time.write( w3c_update )
    else:
        with open( "website/feed_time.txt", 'r' ) as cache_time:
            w3c_update = cache_time.read().strip()
    return base_render_template( atom_xml,
        pages = blogs,
        w3c_update = w3c_update
    ), 200, {'Content-Type': 'application/atom+xml; charset=utf-8'}

#-----------------------------------------------------------------------------
# Error pages.
@app.errorhandler( 404 )
def page_not_found( e ):
    return base_render_template( "error.html", details = e, error="404" )
@app.route( "/404.html" )
def error404():
    return base_render_template( "error.html", error="404" )

@app.errorhandler( 403 )
def page_not_found( e ):
    return base_render_template( "error.html", details = e, error="403" )
@app.route( "/403.html" )
def error403():
    return base_render_template( "error.html", error="403" )

@app.errorhandler( 410 )
def page_not_found( e ):
    return base_render_template( "error.html", details = e, error="410" )
@app.route( "/410.html" )
def error410():
    return base_render_template( "error.html", error="410" )

@app.errorhandler( 500 )
def page_not_found( e ):
    return base_render_template( "error.html", details = e, error="500" )
@app.route( "/500.html" )
def error500():
    return base_render_template( "error.html", error="500" )

