import time
import random

im = createImage(50,50, RGB)
scl = 0
bot = PVector()
# 0: North 1: East 2: South 3: West
botDir = 3
hasStarted = False
verbosity = 0
timedelay = 0 # slow time in seconds per frame
repeats = 10
finished = False
maze = "maze.gif"
moves = 0
startPoint = PVector()

def setup():
    global im
    global scl
    global bot
    global path
    global hasStarted
    global verbosity
    global finished
    global maze
    global moves
    global startPoint
    size(1000,1000)
    im = loadImage(maze)
    scl = width/float(im.width)
    bot = PVector(0,0)
    path = createGraphics(width, height)
    hasStarted = False
    finished = False
    moves = 0
    
    found = False
    while not found:
        found = findFirstWall()
    startPoint.x = bot.x
    startPoint.y = bot.y

def isEdge(im,x,y,w,h):
    global verbosity
    if verbosity >= 4:
        print("looking at x: " + str(x) + " y: " + str(y))
    if y < 0:
        if verbosity >= 3:
            print("top")
        return True
    if y >= h:
        if verbosity >= 3:
            print("bottom")
        return True
    if x < 0:
        if verbosity >= 3:
            print("left")
        return True
    if x >= w:
        if verbosity >= 3:
            print("right")
        return True
    return False

def isWall(im,x,y,w,h):
    global verbosity
    if verbosity >= 4:
        print("looking at x: " + str(x) + " y: " + str(y))
    if y < 0:
        if verbosity >= 3:
            print("top")
        return True
    if y >= h:
        if verbosity >= 3:
            print("bottom")
        return True
    if x < 0:
        if verbosity >= 3:
            print("left")
        return True
    if x >= w:
        if verbosity >= 3:
            print("right")
        return True
    if verbosity >= 3:
        print("index is: " + str(int(y*w + x)))
    return im.pixels[int(y*w + x)] == color(0)

def findFirstWall():
    global im
    global scl
    global bot
    global path
    global botDir
    global hasStarted
    global verbosity
    global moves
    
    left = PVector()
    forward = PVector()
    # check to the left
    if botDir == 0: # N
        left.x = -1
        left.y = 0
        forward.x = 0
        forward.y = -1
    elif botDir == 1: # E
        left.x = 0
        left.y = -1
        forward.x = 1
        forward.y = 0
    elif botDir == 2: # S
        left.x = 1
        left.y = 0
        forward.x = 0
        forward.y = 1
    else: # W
        left.x = 0
        left.y = 1
        forward.x = -1
        forward.y = 0
        
    checkLeft = bot + left
    checkRight = bot - left
    checkFront = bot + forward
    checkBack = bot - forward

    wallLeft  = False
    wallFront = False
    wallRight = False
    wallBack  = False

    if isWall(im,checkLeft.x,checkLeft.y,im.width,im.height):
        if not isEdge(im,checkLeft.x,checkLeft.y,im.width,im.height):
            wallLeft  = True
    if isWall(im,checkFront.x,checkFront.y,im.width,im.height):
        if not isEdge(im,checkFront.x,checkFront.y,im.width,im.height):
            wallFront = True
    if isWall(im,checkBack.x,checkBack.y,im.width,im.height):
        if not isEdge(im,checkBack.x,checkBack.y,im.width,im.height):
            wallBack  = True
    if isWall(im,checkRight.x,checkRight.y,im.width,im.height):
        if not isEdge(im,checkRight.x,checkRight.y,im.width,im.height):
            wallRight = True
    
    if wallLeft:
        pass
    elif wallRight:
        botDir -= 2
    elif wallFront:
        botDir +=1
    elif wallRight:
        botDir -=1
    else:
        bot += random.choice([forward,left,forward*-1,left*-1])
        if bot.x < 0:
            bot.x = 0
        if bot.y < 0:
            bot.y = 0
        return False

    # loop the direction
    if botDir < 0:
        botDir = 4 + botDir
    elif botDir > 3:
        botDir = botDir - 4
    return True

def leftSolve():
    """
    Left move solve
    bot checks all squares around it, if a square to the left
    is white, then move left, however if a square infront is
    white then move infront, if neither left or front are white
    turn back, ignore right..
    do this until we've gone more than one pixel from the outside
    maze is complete when we arrive back at one pixel from the outside.
    """
    global im
    global scl
    global bot
    global path
    global botDir
    global hasStarted
    global verbosity
    global moves
    global startPoint
    
    left = PVector()
    forward = PVector()
    # check to the left
    if botDir == 0: # N
        left.x = -1
        left.y = 0
        forward.x = 0
        forward.y = -1
    elif botDir == 1: # E
        left.x = 0
        left.y = -1
        forward.x = 1
        forward.y = 0
    elif botDir == 2: # S
        left.x = 1
        left.y = 0
        forward.x = 0
        forward.y = 1
    else: # W
        left.x = 0
        left.y = 1
        forward.x = -1
        forward.y = 0
        
    checkLeft = bot + left
    checkRight = bot - left
    checkFront = bot + forward
    checkBack = bot - forward
    
    turnedLeft = False

    wallLeft  = False
    wallFront = False
    wallRight = False
    wallBack  = False

    if isWall(im,checkLeft.x,checkLeft.y,im.width,im.height):
        wallLeft  = True
    if isWall(im,checkFront.x,checkFront.y,im.width,im.height):
        wallFront = True
    if isWall(im,checkBack.x,checkBack.y,im.width,im.height):
        wallBack  = True
    if isWall(im,checkRight.x,checkRight.y,im.width,im.height):
        wallRight = True
    
    if verbosity >= 2:
        print("I'm at x: " + str(bot.x) + " y: " + str(bot.y))
    dirToText = "North"
    if verbosity >= 1:
        if botDir == 0:
            dirToText = "North"
        elif botDir == 1:
            dirToText = "East"
        elif botDir == 2:
            dirToText = "South"
        elif botDir == 3:
            dirToText = "West"
        print("I'm facing " + dirToText)
    if verbosity >= 2:
        if wallLeft:
            print("There's a wall to my left")
        if wallFront:
            print("There's a wall in front")
        if wallBack:
            print("There's a wall behind")
        if wallRight:
            print("There's a wall to my right")

    if wallLeft and not wallFront:
        bot += forward
        if verbosity >= 1:
            print("I'm moving Forward")
        if verbosity >= 2:
            print("Forward is x: " + str(forward.x) + " y: " + str(forward.y))
    elif not wallLeft:
        bot += left
        botDir -=1
        turnedLeft = True
        if verbosity >= 1:
            print("I'm moving Left")
        if verbosity >= 2:
            print("Left is x: " + str(left.x) + " y: " + str(left.y))
    elif wallLeft and wallFront and not wallRight:
        bot -= left
        botDir +=1
        if verbosity >= 1:
            print("I'm moving Right")
        if verbosity >= 2:
            print("Right is x: " + str(-left.x) + " y: " + str(-left.y))
    elif wallLeft and wallFront and wallRight and not wallBack:
        bot -= forward
        botDir +=2
        if verbosity >= 1:
            print("I'm moving Back")
        if verbosity >= 2:
            print("Back is x: " + str(-forward.x) + " y: " + str(-forward.y))
    else:
        if verbosity >= 1:
            print("Nowhere to go!")
        
    # loop the direction
    if botDir < 0:
        botDir = 4 + botDir
    elif botDir > 3:
        botDir = botDir - 4
    
    if verbosity >= 2:
        print("Now I'm at x: " + str(bot.x) + " y: " + str(bot.y))
        if botDir == 0:
            dirToText = "North"
        elif botDir == 1:
            dirToText = "East"
        elif botDir == 2:
            dirToText = "South"
        elif botDir == 3:
            dirToText = "West"
        print("Now I'm facing " + dirToText)
    
    moves += 1
    
    # Check if we've actually entered the maze!
    if hasStarted == False and bot.x > 0 and bot.y > 0:
        hasStarted = True
        if verbosity >= 1:
            print("I've found the entrance to the maze!")
    
    # reched end
    if hasStarted == True and moves > 3 and (bot.x == 0 or bot.x == im.width-1 or bot.y == 0 or bot.y == im.height-1 or startPoint == bot):
        if verbosity >= 1:
            print("I've reached the end!")
        return True
    
def drawSolver():
    global scl
    global bot
    # Draw the Maze Solver
    halfScl = scl/2
    path.beginDraw()
    #path.clear()
    #path.strokeWeight(scl)
    #path.stroke(color(255,0,0,100))
    path.noStroke()
    path.fill(color(255,0,0,100))
    #path.rect(bot.x*scl,bot.y*scl,scl,scl)
    path.translate(bot.x*scl,bot.y*scl)
    path.translate(halfScl,halfScl)
    path.rotate(radians(botDir*90-90))
    path.triangle(-halfScl,-halfScl,-halfScl,halfScl,halfScl,0)
    path.endDraw()

def draw():
    global im
    global scl
    global bot
    global path
    global botDir
    global hasStarted
    global verbosity
    global finished
    global moves
    clear()
    
    # Draw the maze
    imageMode(CORNERS)
    #scl = 2
    image(im,0,0,im.width *scl,im.height*scl)
    halfscl = scl/2
    if verbosity >= 4:
        print("image w: " + str(im.width) + " h: " + str(im.height))
    
    if not finished:
        for i in range(repeats):
            finished = leftSolve()
            if finished:
                break
            drawSolver()
    else:
        print("Completed in " + str(moves) + " moves")
        time.sleep(5)
                
    image(path,0,0)
    if verbosity >= 1:
        print("")
    if timedelay > 0:
        time.sleep(timedelay)
    