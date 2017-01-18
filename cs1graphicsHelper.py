from cs1graphics import *

# Example usage:
#   drawReferencePoints(canvas)
#   drawGrid(canvas,100)
#   markClicks(canvas)
#
# markClicks can slow things down, so toggle it on/off as needed
#
# Read more: https://github.com/susanBuck/cs1graphics-helper


def drawReferencePoints(canvas):
    ''' Loops through every element on a given canvas and marks the
    reference point of that element with a small orange circle '''

    for el in canvas.getContents():

        refPoint = el.getReferencePoint()
        refMarker = Circle(5, refPoint)
        refMarker.setDepth(-998)
        refMarker.setFillColor('orange')
        canvas.add(refMarker)

        if 'Layer' in str(type(el)):
            refMarker.setBorderColor('black')
            label = Text('x', fontsize=8)
            labelDimensions = label.getDimensions()
            label.adjustReference(-labelDimensions[0]/2, -labelDimensions[1]/2)
            label.moveTo(refPoint.getX()-4, refPoint.getY()-5)
            label.setDepth(-999)
            canvas.add(label)


def drawGrid(canvas, division = 100):
    ''' Draws a grid on the canvas of width/height division '''

    width = canvas.getWidth()
    height = canvas.getHeight()

    totalCols = width/division
    totalRows = height/division

    # Rows
    row, startY = 0,0
    for i in range(totalRows):

        startX, startY = 0,row * division
        endX, endY = width,startY

        line = Polygon(Point(startX, startY), Point(endX, endY))

        label = makeLabel(startX, startY)

        canvas.add(line)
        canvas.add(label)
        row += 1

    # Cols
    col,startX = 0,0
    for i in range(totalCols):

        startX,startY = col * division,0
        endX,endY = startX,height

        line = Polygon(Point(startX, startY),Point(endX, endY))
        label = makeLabel(startX, startY)

        canvas.add(label)
        canvas.add(line)
        col += 1


def makeLabel(startX,startY):
    ''' Helper function used to produce a text label at an x,y coord. '''
    fontSize = 10
    label = Text(str(startX) + ',' + str(startY),fontSize)
    labelDimensions = label.getDimensions()
    label.adjustReference(-labelDimensions[0]/2, -labelDimensions[1]/2)
    label.moveTo(startX,startY)

    return label


def markClicks(canvas):
    ''' Marks the x,y coordinates of wherever the mouse clicks;
    good for finding exact pixel coordinates on the canvas. '''

    while True:

        clickListener = canvas.wait();
        click = clickListener.getMouseLocation()

        x = int(click.getX())
        y = int(click.getY())

        label = Layer()

        cords = Text(str(x) + "," + str(y),10)
        cordDimensions = cords.getDimensions()
        cords.moveTo(x + cordDimensions[0]/2, y + cordDimensions[1]/2)
        cords.setFontColor('red')

        point = Circle(1, Point(x,y))

        label.add(cords)
        label.add(point)
        label.setDepth(-999)

        canvas.add(label)
