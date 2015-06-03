'''add_library( "video" )
add_library( "opencv_processing" )

import json

video = None
opencv = None
points = []
jsonPoints = {}
jsonIndex = 0
movieLength = 40

def setup ():
    global video, opencv
    
    #size( 960, 540 )
    size( 640, 370 )
    
    video = Movie( this, "test.mp4" )
    opencv = OpenCV( this, width, height )
    opencv.startBackgroundSubtraction( 5, 3, 0.5 )
    
    video.play()
    
def draw ():
    global jsonIndex, jsonPoints, video
    
    #noStroke()
    #fill( 0, 0, 0 )
    #rect( 0, 0, width, height )
    
    #image(video, 0, 0);
    opencv.loadImage( video )
    opencv.updateBackground()
    opencv.threshold( 50 )
    opencv.dilate()
    opencv.erode()
    
    noFill()
    stroke( 255, 0, 0 )
    strokeWeight( 1 )
    
    contours = opencv.findContours( False, True )
    
    if contours.size() > 0:
        point = contours.get( 0 ).getBoundingBox()
        ellipse( point.x, point.y, 10, 10 )
        points.append( [ point.x, point.y ] )
        
        jsonPoints[ str( jsonIndex ) ] = [ point.x, point.y ]
        
    jsonIndex += 1
    
    if movieLength < millis() / 1000:
        videoEnded()
        
def videoEnded ():
    global video, jsonPoints
    
    println( "VIDEO ENDED" )
    println( "JSON SAVED" )
    
    with open( 'data/exported.json', 'w' ) as outfile:
        str( json.dump(jsonPoints, outfile, sort_keys = True, indent = 4, ensure_ascii = False ) )
    
    noLoop()
        
def movieEvent ( movie ):
    movie.read()
'''

# new

# imports
add_library( "video" )
add_library( "opencv_processing" )

import json

# global vars
opencv = None
video = None
snapshot = None
points = {}
movieLength = 45

def setup():
    global video, opencv
    
    size( 608, 1080 )
    frameRate(1)
    
    video = Movie( this, "test.mov" )
    
    opencv = OpenCV( this, width, height )
    opencv.findCannyEdges( 1, 10 )
    
    video.play()
    
    draw()
    
def draw():
    global video, snapshot, points
    
    points[ str( frameCount ) ] = []
    
    opencv.loadImage( video )
    opencv.findCannyEdges( 0, 100 )
    snapshot = opencv.getSnapshot()
    
    image( snapshot, 0, 0 )
    
    saveFrame("line-######.png"); 
    
    for x in range( 0, width / 2 ):
        for y in range( 0, height / 2 ):
            pixelColor = color( get( x * 2, y * 2 ) )
            
            if pixelColor > -16777216:
                points[ str( frameCount ) ].append( [ x * 2, y * 2 ] )
    
    if movieLength < millis() / 1000:
        videoEnded()
    
def videoEnded():
    global points
    
    println( "VIDEO ENDED" )
    println( "JSON SAVED" )
    
    with open( 'data/exportedv2.json', 'w' ) as outfile:
        str( json.dump( points, outfile, sort_keys = True, indent = 4, ensure_ascii = False ) )
    
    noLoop()
    
def movieEvent ( movie ):
    movie.read()
