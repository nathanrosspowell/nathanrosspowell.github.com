import os
import sys

#-----------------------------------------------------------------------------
# Globals.
root_dir = os.path.split( os.path.realpath( __file__ ) )[ 0 ]
root = os.path.join( root_dir, "pages" )

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
                lines = function( file, read.readlines() )
            if dry_run:
                for line in lines:
                    print "\t%s" % ( line, )
            else:
                with open( filename, 'w' ) as write:
                    write.writelines( lines )

                    


#-----------------------------------------------------------------------------
# Edit functions.
def add_named( name, lines ):
    stripped = os.path.splitext( name )[ 0 ]
    print stripped
    lines.insert( 0, "named: %s\n" % ( stripped, ) )
    return lines

if __name__ == "__main__":
    edit_files( add_named, False )
