from random import uniform 

pos = [0,0]
vel = [0,0]

def setup():
    global pos
    global vel
    size(500,500)
    
    pos = [width/2,height/2]
    vel = [uniform(-10,10),uniform(-10,10)]
    print(vel)
    
    
def draw():
    global pos
    global vel
    #clear()
    
    fill(color(255,0,0))
    stroke(color(0,255,255))
    strokeWeight(2)
    ellipse(pos[0],pos[1],30,30)
    
    if pos[0] < 0 or pos[0] > width:
        vel[0] = -vel[0]
    if pos[1] < 0 or pos[1] > height:
        vel[1] = -vel[1]
    
    pos[0] += vel[0]
    pos[1] += vel[1]
    
    
    
    
    
    
    
    
    
    
    