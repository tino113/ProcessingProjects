# tornado
partPos = []
partC = []
def setup():
    clear()
    global partPos
    size(500,500)
    for i in range(1000):
        partPos.append(PVector(random(0,width),random(0,height)))
        partC.append(random(0,255))
        
def draw():
    global partPos
    #clear()
    strokeWeight(3)
    i = 0
    for p in partPos:
        c = partC[i]
        stroke(color(c,c,c,20))
        point(p.x,p.y)
        i+=1
        
    furthest = 0
    centre = PVector(width/2,height/2)
    for i in range(len(partPos)):
        p = partPos[i]
        dirToCentre = centre - p
        distance = dirToCentre.mag()
        if distance > furthest:
            furthest = distance
        tangent = dirToCentre.rotate(HALF_PI)
        partPos[i] = p + tangent * ((dirToCentre.mag()/furthest)-1)*2 * 0.04
        if distance > height*2:
            partPos[i] = PVector(random(0,width),random(0,height))
    
    
    
    