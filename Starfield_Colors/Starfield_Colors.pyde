# Starfield
def setup():
    global posX, posY, dirX, dirY, col
    size(300,300)
    background(0)
    posX, posY = [], []
    dirX, dirY = [], []
    for i in range(0,300):
        p2x = random(0,300)
        p2y = random(0,300)
        posX.append(p2x)
        posY.append(p2y)
        dirX.append((150 - p2x)/100)
        dirY.append((150 - p2y)/100)
    
def draw():
    global posX, posY, dirX, dirY
    clear()
    strokeWeight(5)
    for i in range(0,300):
        stroke(color(255,255,255))
        point(posX[i],posY[i])
        posX[i] = posX[i] - dirX[i]
        posY[i] = posY[i] - dirY[i] 
        if posX[i] > 300 or posX[i] < 0 or posY[i] > 300 or posY[i] < 0:
            p2x = random(0,300)
            p2y = random(0,300)
            posX[i] = p2x
            posY[i] = p2y
            dirX[i] =(150 - p2x)/10
            dirY[i] =(150 - p2y)/10
                
                