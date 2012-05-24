@loadStartCSS = loadStartCSS = ( rootPath, json ) ->
    files = [
        {
            load : rootPath + "css/style.css"
        },
        {
            load : rootPath + "css/nrp.css"
        }
    ]
    files = files.concat( json ) if json != null
    Modernizr.load( files )
    
@loadStartJs = loadStartJs = ( rootPath, load1, load3 ) ->
    load2 = [
        # Load JQuerey.
        {
            load: '//ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.js',
            complete: -> 
                if ( !window.jQuery )
                    Modernizr.load(rootPath+'js/libs/jquery-1.6.1.min.js')
        },
        # Load FlashCanvas.
        {
            # Logical list of things we would normally need
            test : Modernizr.canvas,
            # Modernizr.load loads css and js by default
            nope : rootPath+'flash/flashcanvas.js'
        },
    ]
    files = []
    files = files.concat load1 if load1 != null
    files = files.concat load2 
    files = files.concat load3 if load3 != null
    Modernizr.load( files )
