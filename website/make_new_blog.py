import datetime
import os
import re

#-----------------------------------------------------------------------------
# URL slug creation via http://djangosnippets.org/snippets/29/
def slugify(inStr):
    removelist = ["a", "an", "as", "at", "before", "but",   \
        "by", "for","from","is", "in", "into", "like", "of",\
        "off", "on", "onto","per","since", "than", "the",   \
        "this", "that", "to", "up", "via","with"]
    for a in removelist:
        aslug = re.sub(r'\b'+a+r'\b','',inStr)
    aslug = re.sub('[^\w\s-]', '', aslug).strip().lower()
    aslug = re.sub('\s+', '-', aslug)
    return aslug

# Clean input.
def input( output ):
    return raw_input( output ).strip()

#-----------------------------------------------------------------------------
# Create a new file of the given name in the correct folder.
# Sets the YAML metadata including URL.
def main( dir ):
    title = input( "Blog title>" )
    titlename = slugify( title )
    responce = input ( "Create '%s' y/n>" % ( titlename, ) )
    if responce != "y" and responce != "Y":
        return "Bailed"
    if not os.path.exists( "blog" ):
        os.mkdir( "blog" )
    now = datetime.datetime.now()
    date = now.strftime( "%Y/%m/%d" )
    urlpath = "blog/%s/" % ( date,)
    path = os.path.join( dir, urlpath )
    if not os.path.exists( path ):
        os.makedirs( path )
    url = os.path.join( date, titlename )
    titlepath = os.path.join( path, titlename )
    body = """title: %s
published: %s
url: %s
comments: True
tags:
- blog

Heres is the post body.""" % ( title, date, url )
    with open( titlepath+".md", 'w' ) as file:
        file.write( body )

#-----------------------------------------------------------------------------
# Run using this files directory as the root.
if __name__ == "__main__":
    dir = os.path.split( os.path.realpath( __file__ ) )[ 0 ]
    main( os.path.join( dir, "pages" ) )
