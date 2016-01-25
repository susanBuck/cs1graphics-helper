from cs1graphics import *
from cs1graphicsHelper import *

# Reference points:
# Layer: 0,0
# Polygon: First point of the polygon.
# Square: Center
# Rectangle: Center
# Circle: Center

paper = Canvas(500,500,'yellow')

# Draws a green polygon (cone)
# Note the reference point is the first point in the polygon
def example0():
    poly = Polygon(Point(-50,0), Point(50,0), Point(0,200))
    poly.setFillColor('green')
    poly.moveTo(100,100)
    paper.add(poly)

example0()

# Draws an blue polygon (cone) in a Layer
# Note reference point is 0,0
def example1():
    toybox = Layer()
    cone = Polygon(Point(-50,0), Point(50,0), Point(0,200))
    cone.setFillColor('blue')
    toybox.add(cone)
    paper.add(toybox)

#example1()


# Draws a blue polygon (cone) and a red circle on a Layer
# Note the reference point is 0,0 
def example2():
    toybox = Layer()

    circ = Circle(100)
    circ.setFillColor('red')
    toybox.add(circ)

    cone = Polygon(Point(-50,0), Point(50,0), Point(0,200))
    cone.setFillColor('blue')
    toybox.add(cone)

    paper.add(toybox)

#example2()


# Invoke helper functions as the last step
drawReferencePoints(paper)
drawGrid(paper,100)
markClicks(paper)



