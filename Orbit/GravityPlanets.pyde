# gravity
import random

planet = [0,0]
planetVel = [0,0]
planetSize = 20
planetColor = color(255)
planetMaxSpeed = 10

def setup():
    size(800,800)
    global planet
    global planetVel
    planet = [width/2,height/2]
    planetVel = [random.uniform(-1,1),random.uniform(-1,1)]
    planetColor = color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    strokeWeight(planetSize)

def draw():
    clear()
    global planet
    global planetVel
    strokeWeight(planetSize)
    stroke(planetColor)
    point(planet[0],planet[1])
    #planetVel = [random.uniform(-1,1),random.uniform(-1,1)]
    
    
    #attract to mouse
    vecToMouse = PVector(mouseX-planet[0],mouseY-planet[1]).normalize()
    
    planetVel[0] += vecToMouse.x
    planetVel[1] += vecToMouse.y
    
    planet[0] += planetVel[0]
    planet[1] += planetVel[1]
    
    if planetVel[0] > planetMaxSpeed:
        planetVel[0] = planetMaxSpeed
    if planetVel[1] > planetMaxSpeed:
        planetVel[1] = planetMaxSpeed
    if planetVel[0] < -planetMaxSpeed:
        planetVel[0] = -planetMaxSpeed
    if planetVel[1] < -planetMaxSpeed:
        planetVel[1] = -planetMaxSpeed