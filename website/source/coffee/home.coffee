drawingCanvas = document.getElementById('headingCanvas')
# Check the element is in the DOM and the browser supports canvas
if drawingCanvas.getContext
    # Initaliase a 2-dimensional drawing context
    context = drawingCanvas.getContext('2d')
    # Canvas commands go here

    my_gradient = context.createLinearGradient(0, 0, 320, 0)
    my_gradient.addColorStop(0, "black")
    my_gradient.addColorStop(1, "white")
    context.fillStyle = my_gradient
    context.fillRect(0, 0, 320, 320)
    context.fillRect(50, 25, 150, 100)
    
    # Yellow circle.
    context.strokeStyle = "#000000"
    context.fillStyle = "#FFFF00"
    context.beginPath()
    context.arc(100,100,50,0,Math.PI*2,true)
    context.closePath()
    context.stroke()
    context.fill()
