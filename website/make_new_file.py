import datetime
import os
import re
from time_stamp import get_w3c_date

#-----------------------------------------------------------------------------
# Globals.
datefolders = ( "blog", )
base_url = "http://github.com/nathanrosspowell/nathanrosspowell.github.com/blob/dev/website/pages/"

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
    folder = input ( "Top folder>" )
    title = input( "Title>" )
    template = input( "Template (.html)>" )
    comments = input( "Comments> y/n>" )
    if comments == 'n' or comments == 'N':
        comments = False
    else:
        comments = True
    titlename = slugify( title )
    responce = input ( "Create '%s' y/n>" % ( titlename, ) )
    if responce != "y" and responce != "Y":
        return "Bailed"
    dir_folder = os.path.join( dir, folder )
    if not os.path.exists( dir_folder ):
        os.mkdir( dir_folder )
    now = datetime.datetime.now()
    date = now.strftime( "%Y/%m/%d" )
    time = now.strftime( "%H:%M:%S" )
    if folder in datefolders:
        urlpath = "blog/%s/" % ( date,)
        path = os.path.join( dir, urlpath )
        url = os.path.join( folder, os.path.join( date, titlename ) )
    else:
        path = os.path.join( dir, folder )
        url = os.path.join( folder, titlename )
    if not os.path.exists( path ):
        os.makedirs( path )
    titlepath = os.path.join( path, titlename )
    source = "%s%s" % ( base_url, url )
    body = """source: "%s.md"
named: "%s"
title: "%s"
published: "%s"
time: "%s"
w3c: "%s"
url: "%s"
template: "%s"
comments: %s
short: "Here is the post short."
tags:
- %s

Heres is the post body.""" % (
        source,
        titlename,
        title,
        date,
        time,
        get_w3c_date(),
        url,
        template,
        comments,
        folder
    )
    with open( titlepath+".md", 'w' ) as file:
        file.write( body )

#-----------------------------------------------------------------------------
# Run using this files directory as the root.
if __name__ == "__main__":
    dir = os.path.split( os.path.realpath( __file__ ) )[ 0 ]
    main( os.path.join( dir, "pages" ) )
