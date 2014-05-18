title: "Functional One Liner"
date: "2012-08-15T23:06:56-04:00"
comments: True
short: A little Project Euler solution that I'm fond of. I'm also currently taking a smallish python script and trying to make it into a more full featured program with a GUI. 
showInFeed: True
tags:
- project-euler
- python
- gui
- functional
- programming
- pycast

I'd like to share a Project Euler solution [(I'll not say which)*][sol] that I am particularly fond of. Like all true wonders of code, it is a mighty one liner:

    :::python
    sum( map( int, str( reduce( operator.mul, xrange( 2, 101 ) ) ) ) )

While I'm still very much a novice with functional programming, I'm using a few tricks that I picked up when I last sat down and tried to ['Learn *me* a Haskell'][luah] by using a range generator, folds and an anonymous function.

I managed to power through a couple of the easier P.E problems a few ahead of my current sticking point, using the python language. It made me want to try and do something a little more **useful** with the language. Enter the last big python [gist][gist] I created `podcast.py` - a crude but configurable mass podcast downloader.

### [`podcast.py`][gistpy]

    :::python
    # Snippet from jumbo file podcast.py

    def downloadAll( newDict, priority, verbose, dryRun ):
        for key in priority:
            value = newDict.get( key, None)
            if not value:
                continue
            print "Downloading %s from: %s" %( len( value ), key )
            value.sort( reverse=True, key=lambda v: v[ "date" ] )
            for item in value:
                download( item[ "url" ], item[ "fullFilePath" ], verbose, dryRun )

    def main( xmlFile, verbose, dryRun ):
        settings, priority = getSettingsAndPriority( xmlFile )
        newFiles = {}
        for key, value in settings[ "feeds" ].iteritems():
            new = listNewFiles( settings[ "folder" ], value )
            if new != []:
                newFiles[ key ] = new
        if newFileStatus( newFiles, priority, verbose ):
            downloadAll( newFiles, priority, verbose, dryRun )

    if __name__ == "__main__":
        if len( sys.argv ) < 2:
            print "Usage: <podcast: xml file> <verbose: 1 or 0> <dryrun: 1 or 0>"
        else:
            podcastXML = sys.argv[ 1 ]
            try:
                verbose = sys.argv[ 2 ]
            except:
                verbose = False
            try:
                dryRun = sys.argv[ 3 ]
            except:
                dryRun = False
            main( podcastXML, verbose, dryRun )

Being very anti-iTunes (due to it being a system resource hog) and failing to find a suitable alternative for 'managing' podcasts I decided to grab the favourite feeds straight from the source and download ALL the things at once. Running the script whenever I booted my computer to get all the latest audio treats for myself to keep.

An example of my config that powered the script (note the embedded python code used to format the titles!).

### [`podcast.xml`][gistxml]

    :::xml
    <?xml version="1.0" encoding="UTF-8"?>
    <podcast>
        <!-- Root folder to download to. -->
        <folder value="Z:\Media\Podcast\" />
        <!-- RSS feeds to download, listed highest priority to lowest. 
            Fields to set:
                name= print out name of the feed 
                folder= sub folder used
                rss= RSS URI
            Optional Fields:
                seperator= '-'
                space= '_'
                dateFormat= how the datetime will be displayed
                nameFormat= tuple for custom file name format: %s+seperator+%s
                            can use title (string) and dateFormat (string)
                            e.g "JRE+title, dateFormat
        -->
        <feeds>
            <feed name="Lavender Hour" 
                  folder="Lavender Hour" 
                  rss="http://lavenderhour.libsyn.com/rss"
                  nameFormat="dateFormat, title"
                  dateFormat="%Y-%m-%d"
            />
            <feed name="Joe Rogan Experience" 
                  folder="JRE" 
                  rss="http://joeroganexp.joerogan.libsynpro.com/irss"
                  nameFormat="title[ title.find('#')+1: ], dateFormat"
            />
        </feeds>
    </podcast>


After not looking at the actual script for a good few months I totally forget how I wired it up and **oh my GLOB**... debugging python scripts is about as much fun as ironing wrinkly parts of your body. After a few hours of self.torture I managed to split up core parts of the functionality with the final aim of using the code inside of an actual GUI of some kind. The functionality I'd like would be to pick (or filter) the podcasts that I download instead of just ending up with tens of GBs of files sitting on my NAS.

So, I'm learning about real world *best practices* for python and also looking into the Qt/PySide GUI framework. Look out for an operational [PyCast][pycast] <s>app</s> program some time soon!

<a id="solution"></a>

_*if you manage to reverse engineer the code and figure out which problem this is the solution to, SPOILER ALERT, I guess..._

[sol]: #solution "If you manage to reverse engineer the code and figure out which problem this is the solution too, SPOILER ALERT, I guess..."
[luah]: http://learnyouahaskell.com/ "Learn You a Haskell for Great Good"
[gistpy]: https://gist.github.com/2603334#file_podcast.py "podcast.py - Gist powered by GitHub"
[gistxml]: https://gist.github.com/2603334#file_podcast.xml "podcast.xml - Gist powered by GitHub"
[gist]: https://gist.github.com/2603334 "Gist powered by Github"
[pycast]: https://github.com/nathanrosspowell/pycast
