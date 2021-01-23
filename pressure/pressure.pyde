# pressure Sim
class particle():
    def __init__(self):
        self.mass = random(3,20)
        self.diam = self.mass * 2
        self.rad = self.diam / 2
        self.pos = PVector(random(self.diam,width-self.diam),random(self.diam,height-self.diam))
        self.vel = PVector(random(-1,1),random(-1,1))
        self.col = color(random(0,255),random(0,255),random(0,255))
    
    def move(self):
        self.pos += self.vel
        
    def collideBounds(self,bounds):
        # bound defined as (x,y,w,h)
        if self.pos.x - self.rad < bounds[0]:
            self.vel.x *= -1
        if self.pos.x + self.rad > bounds[0] + bounds[2]:
            self.vel.x *= -1
        if self.pos.y - self.rad < bounds[1]:
            self.vel.y *= -1
        if self.pos.y + self.rad > bounds[1] + bounds[3]:
            self.vel.y *= -1
    
    def elasticCollision(self,other):
        if self.mass == other.mass:
            self.vel, other.vel = other.vel, self.vel
        
        else:
            combMass = self.mass + other.mass
            mass2A = other.mass*2
            diffVelA = self.vel - other.vel
            diffPosA = self.pos - other.pos
            mass2B = self.mass*2
            diffVelB = other.vel - self.vel
            diffPosB = other.pos - self.pos
            magdiff = diffPosA.mag()
            magdiffSq = magdiff*magdiff
            self.vel -= (mass2A/combMass)*((diffVelA.dot(diffPosA))/magdiffSq)*diffPosA
            other.vel -= (mass2B/combMass)*((diffVelB.dot(diffPosB))/magdiffSq)*diffPosB
    
    def collisionNaive(self,other):
        d = abs(self.pos.dist(other.pos))
        diff = self.rad + other.rad
        return d < diff
    
    def naivePartCollide(self,others):
        for other in others:
            if self.collisionNaive(other):
                self.elasticCollision(other)

def setup():
    global parts,bounds
    size(800,600)
    bounds = (0,0,width,height)
    parts = []
    for i in range(0,50):
        collision = True
        while collision:
            collision = False
            newPart = particle()
            for part in parts:
                if newPart.collisionNaive(part):
                    collision = True
        parts.append(newPart)

def draw():
    background(0)
    # interactivity
    for part in parts:
        # collide with edges
        part.collideBounds(bounds)
        # collide with other particles
        part.naivePartCollide(parts)
        # move
        part.move()
        
    # draw
    for part in parts:
        strokeWeight(part.diam)
        stroke(part.col)
        point(part.pos.x,part.pos.y)
    
                     
