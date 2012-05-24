import os

#-----------------------------------------------------------------------------
# Walk from a dir returning the results of function.
# The path below the dir should be set out in date format.
# path example: /YYYY/MM/DD/file.ext
# path example: /2012/01/30/file.txt
def walk( dir, function, desc = True ):
    for walking in os.walk( dir, topdown = desc ):
        walking[ 1 ].sort( reverse = desc )
        for result in function( *walking, desc = desc ):
            yield result

# Talke n from walk.
def take( n, dir, function, desc = True ):
    for f in walk( dir, function, desc ):
        if n > 0:
            yield f
            n -= 1
        else:
            break;

# Example function for returning latest/'up to date' files.
def newest( dirname, dirnames, filenames, desc = True ):
    paths = [ os.path.join( dirname, x ) for x in filenames if x[0] != "." ]
    t = os.path.getmtime
    paths.sort( reverse = desc, cmp = lambda x,y: int( t( x ) - t( y ) ) )
    for file in paths:
        yield file

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    # Print out all of the file paths, newest to oldest.
    for f in take( 1, "pages/blog", newest, True ):
        print f
