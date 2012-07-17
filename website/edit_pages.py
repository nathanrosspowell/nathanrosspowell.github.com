import os
import sys

#-----------------------------------------------------------------------------
# Globals.
root_dir = os.path.split( os.path.realpath( __file__ ) )[ 0 ]
root = os.path.join( root_dir, "pages" )
base_url = "http://github.com/nathanrosspowell/nathanrosspowell.github.com/blob/dev/website/pages"

#-----------------------------------------------------------------------------
# Edit all files.
def edit_files( function, dry_run = True ):
    openwith = 'r+'
    if dry_run:
        openwith = 'r'
    for path, dirs, files in os.walk( root ): 
        for file in files:
            filename = os.path.join( path, file )
            with open( filename, 'r' ) as read:
                lines = function( path, file, read.readlines() )
            if dry_run:
                for line in lines:
                    print "\t%s" % ( line, )
            else:
                with open( filename, 'w' ) as write:
                    write.writelines( lines )

#-----------------------------------------------------------------------------
# Edit functions.
def add_named( path, name, lines ):
    stripped = os.path.splitext( name )[ 0 ]
    lines.insert( 0, "named: %s\n" % ( stripped, ) )
    return lines

def add_github_source( path, name, lines ):
    short_path = os.path.join( path, name).replace( root, "" )
    url = "%s%s" % ( base_url, short_path, )
    source = 'source: "%s"\n' % ( url, )
    #print source
    lines.insert( 0, source )
    return lines

def edit_github_source( path, name, lines ):
    for i, line in enumerate( lines ):
        if line.startswith( 'source:'): 
            lines[ i ] = lines[ i ][ :-2 ] + ".md\n"
    return lines

if __name__ == "__main__":
    dry_run = True
    edit_files( edit_github_source, dry_run )
