'''
Snow!
A project to create snowfall
'''

particles = []
particleSizes = []
maxParticles = 4000
speed = 0.2
wind = 0
windEffect = 0.1

def setup():
    global particles
    global particleSizes
    global maxParticles
    global wind
    
    size(1920,1080)
    
    for i in range(maxParticles):
        particles.append(PVector(random(-width,width*2),random(-height,0)))
        particleSizes.append(random(2,8))
        
    wind = random(-1,1)
        
def draw():
    global particles
    global particleSizes
    global maxParticles
    global speed
    global wind
    global windEffect
    
    clear()
    stroke(color(255))
    
    for i in range(maxParticles):
        strokeWeight(particleSizes[i])
        point(particles[i].x,particles[i].y)
        
    for i in range(maxParticles):
        particles[i].y += particleSizes[i] * speed
        particles[i].x += wind * particleSizes[i] * windEffect
        if particles[i].y > height:
            particles[i] = PVector(random(-width,width),random(-10,0))
            
    if frameCount % random(50,1000) == 0:
        wind = random(-1,1)