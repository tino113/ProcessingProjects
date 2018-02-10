from random import uniform
positions = []
velocities = []
colors = []
numPlanets = 50

def setup():
    global positions
    global velocities
    size(1400,800)
    for i in range(numPlanets):
        pos = PVector(uniform(0,width),uniform(0,height))
        vel = PVector(uniform(-1,1),uniform(-1,1))
        positions.append(pos)
        velocities.append(vel)
        colors.append(color(uniform(0,255),uniform(0,255),uniform(0,255)))
    
def draw():
    global positions
    global velocities
    #clear()
    
    for i in range(numPlanets):
        stroke(colors[i])
        strokeWeight(20)
        point(positions[i].x,positions[i].y)
        
        vec = PVector(mouseX,mouseY) - positions[i] 
        velocities[i] += vec.normalize()
        
        if velocities[i].mag() > 20:
            velocities[i] = velocities[i].normalize() * 20
        
        positions[i] += velocities[i]