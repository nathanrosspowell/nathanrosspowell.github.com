from flask_frozen import Freezer
from website import app
import website.walk_dates as walk
import os
freezer = Freezer( app )

@freezer.register_generator
def blogs():
    dir = os.path.join( app.config[ "ROOT_DIR" ], app.config[ "FLATPAGES_ROOT" ] )
    for page_path in walk.walk( os.path.join( dir, "blog" ), walk.newest ):
        urlpath = os.path.splitext( page_path.replace( dir, "" )[1:] )[ 0 ]
        yield { "page_path" : urlpath }

if __name__ == "__main__":
    freezer.freeze()
