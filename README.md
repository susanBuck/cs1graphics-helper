# cs1graphicsHelper.py

<img src='screenshot.png' alt='Screenshot of cs1graphicshelper'>

This script includes 3 helper functions which will make drawing in cs1graphics easier:

1. `drawReferencePoints(canvas)`: Marks the reference point of any objects on the canvas with a small orange circle; Layers have a small `x` inside the circle.
2. `drawGrid(canvas, dimension)`: Draws a labeled grid on the canvas to help pick coordinate points. Param `dimension` indicates the spacing of the grid; defaults to 100.
3. `markClicks(canvas)`: Prints the coordinates of every mouse click; can slow things down, so toggle it on/off as needed.


## Instructions
Put [cs1graphicsHelper.py](https://raw.githubusercontent.com/wellesleycs111/cs1graphicsHelper/master/cs1graphicsHelper.py) in your working folder, then import after cs1graphics.

```py
from cs1graphics import *
from cs1graphicsHelper import *
```

At the __end__ of your script, invoke 1 or more of the helper functions on your canvas:

```py
paper = Canvas(500, 500, 'yellow')

drawReferencePoints(paper)
drawGrid(paper, 100)
markClicks(paper)
```

__Basic example:__

```py
from cs1graphics import *
from cs1graphicsHelper import *

paper = Canvas(500, 500, 'yellow')

# Draws a green polygon (cone)
# Note the reference point is the first point in the polygon
poly = Polygon(Point(-50,0), Point(50,0), Point(0,200))
poly.setFillColor('green')
poly.moveTo(100,100)
paper.add(poly)

# Invoke the helper functions
drawReferencePoints(paper)
drawGrid(paper,100)
markClicks(paper)
```

## Demo
Run [demo.py](https://raw.githubusercontent.com/wellesleycs111/cs1graphicsHelper/master/demo.py) for a full demonstration.
