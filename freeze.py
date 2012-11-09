from flask_frozen import Freezer
from website import app
import website.walk_dates as walk
import os
freezer = Freezer( app )

if __name__ == "__main__":
    freezer.freeze()
