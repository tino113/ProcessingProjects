particles = []
prevPart = []
numParticles = 10
partCol = []
newPoint = []

def setup():
    global particles
    global prevPart
    global partCol
    global newPoint
    global numParticles
    size(300,300)
    for i in range(numParticles):
        particles.append(PVector(random(0,width),random(0,height)))
        prevPart.append(particles[i])
        partCol.append(color(random(0,255),random(0,255),random(0,255)))
        newPoint.append(True)
    strokeWeight(5)
    
def draw():
    clear()
    global particles
    global prevPart
    global partCol
    global numParticles
    global newPoint
    
    for i in range(numParticles):
        #trail = ((prevPart[i]-particles[i]) * 10) + particles[i]
        if not newPoint[i]:
            line(particles[i].x,particles[i].y,prevPart[i].x,prevPart[i].y)
        stroke(color(partCol[i]))
        #point(particles[i].x,particles[i].y)
        
    
    centre = PVector(width/2,height/2)
    
    for i in range(numParticles):
        particles[i] += (particles[i]-centre) * 0.05
        prevPart[i] = particles[i]
        newPoint[i] = False
        if particles[i].x > width or particles[i].x < 0:
            particles[i] = PVector(random(0,width),random(0,height))
            newPoint[i] = True
        if particles[i].y > height or particles[i].y < 0:
            particles[i] = PVector(random(0,width),random(0,height))
            newPoint[i] = True