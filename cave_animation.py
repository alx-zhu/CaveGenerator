from cmu_112_graphics import *
from cave_generator import *

def appStarted(app):
    app.rows = 50
    app.cols = 50
    app.margin = 20
    app.cave = create_initial(app.rows, app.cols, 0.45)
    app.timerDelay = 500
    app.count = 0

def re_generate(app):
    app.cave = create_initial(app.rows, app.cols, 0.45)
    app.count = 0

def getCell(app, x, y):
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth  = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    row = int((y - app.margin) / cellHeight)
    col = int((x - app.margin) / cellWidth)
    return (row, col)

def getCellBounds(app, row, col):
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = app.margin + col * cellWidth
    x1 = app.margin + (col+1) * cellWidth
    y0 = app.margin + row * cellHeight
    y1 = app.margin + (row+1) * cellHeight
    return (x0, y0, x1, y1)

def drawGrid(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            if (app.cave[row][col] == '#'):
                canvas.create_rectangle(x0, y0, x1, y1, fill = "black")
            else:
                canvas.create_rectangle(x0, y0, x1, y1, outline = "white")

def keyPressed(app, event):
    if (event.key == "Enter"):
        re_generate(app)

def timerFired(app):
    if (app.count < 3):
        run_CA_cycle_2step(app.cave, len(app.cave), len(app.cave[0]))
        app.count += 1
    elif (app.count < 5):
        run_CA_cycle_1step(app.cave, len(app.cave), len(app.cave[0]))
        app.count += 1

def redrawAll(app, canvas):
    drawGrid(app, canvas)

runApp(width = 700, height = 700)