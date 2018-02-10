#Chaotic Pendulum

vector1 = PVector()
vector2 = PVector()
angle1 = 0
angle2 = 0
angleMax = 20
vec2End = PVector()
prevVec2End = PVector()
pen = PGraphics()

def setup():
    global vector1
    global vector2
    global angle1
    global angle2
    global pen
    size(500,500)
    
    vector1 = PVector(random(-width/4,width/4),random(-height/4,height/4))
    vector2 = PVector(random(-width/8,width/8),random(-height/8,height/8))
    angle1 = radians(random(-angleMax, angleMax))
    angle2 = radians(random(-angleMax, angleMax))
    pen = createGraphics(width,height)
    
def draw():
    clear()
    global pen
    global vec2End
    global prevVec2End
    
    stroke(color(255))
    strokeWeight(2)
    vec2End = PVector(width/2+vector1.x+vector2.x,height/2+vector1.y+vector2.y)
    line(width/2,height/2,width/2+vector1.x,height/2+vector1.y)
    line(width/2+vector1.x,height/2+vector1.y,vec2End.x,vec2End.y)
    
    vector1.rotate(angle1)
    vector2.rotate(angle2)
    
    pen.beginDraw()
    pen.stroke(color(255,255,255,150))
    pen.strokeWeight(2)
    vecBetween =  vec2End - prevVec2End
    vecBetween = vecBetween.normalize() * 1.8
    if prevVec2End.mag() != 0:
        pen.line(prevVec2End.x,prevVec2End.y,vec2End.x -vecBetween.x,vec2End.y-vecBetween.y)
    pen.endDraw()
    image(pen,0,0)
    prevVec2End = vec2End
