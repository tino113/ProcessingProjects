# DLA
# Diffusion Limited Aggregation

stuckParts = []
furthestDist = 0

# smaller diam results in more detailed but slower DLAs
diam = 0.4

# bias controls how much force is applied towards the centre.
# A higher number will mean faster generation, but also less random
biasAmount = 0.2

# bias2 controls how much rotation the particles should have around the centre.
# negative numbers will make it rotate the other way.
# generally shouldn't be bigger than the biasAmount...
# otherwise particals may continually spin around the outside and never hit anything...
bias2Amount = 0.0

# only search the last maxSearch number particles... 
# smaller numbers are faster but cause errors...
maxSearch = 300
maxSearchPerc = 0

# If the program has searched more than searchLimit times,
# something probably went wrong, just generate a new particle
searchLimit = 100000000

# increase this number to reduce the size of the inner limit
# this will slow down the program but make it more 'accirate'
# change to 0 to turn off the inner limit
# put inner limit to 1 to force only particles on the outside.
# numbers closer to 1 tend to create long thin arms of particles
innerLimitDivider = 1.8

# decreasing this number will speed up generation, but make it
# less random, larger numbers result in slower generation but more random results.
outerLimitMultiplier = 6

colors = [color(0,100,255),color(0,255,255),color(255,0,255),color(100,0,255)]
colorDistDivider = 1000

numPartsDivider = 5000

useDistForCol = False
useWalkingCentre = False

avesum = 0

def DLA(particles):
    global diam
    global biasAmount
    global bias2Amount
    global maxSearch
    global maxSearchPerc
    global searchLimit
    global furthestDist
    global colorDistDivider
    global numPartsDivider
    global colors
    global avesum
    
    fails = 0
    realCentre = PVector(width/2,height/2)
    centre = realCentre
    # loop until a sticking location is found.
    while True:
        # generate a new random particle location
        outerLimit = diam * outerLimitMultiplier
        # generate particles that are close to the existing maximum radius..
        # more likely to walk randomly towards the centre and get stuck
        # therefore speeding up the process
        part1 = PVector(1,0)
        part1 = part1.rotate(random(0,TWO_PI))
        part1 *= (furthestDist + outerLimit)
        part1 += centre
        quaterDiam = diam/4
        checks = 0
        innerLimit = 0
        doubleOuterLimit = outerLimit*2
        if not innerLimitDivider == 0:
            innerLimit = furthestDist/innerLimitDivider
        
        while checks < searchLimit:
            # walk the particle in a random direction
            part1 += PVector(random(-1,1),random(-1,1)).normalize()*quaterDiam
            bias = centre - part1
            bias.normalize()
            bias2 = PVector(0,0)
            if not bias2Amount <= 0.001:
                bias2 = PVector.cross(bias,PVector(0,0,1)) * bias2Amount
            bias *= biasAmount
    
            part1 += bias + bias2
            
            # only start searching to see if it's touching another particle
            # when it's within the radius of the furthest particle.
            # saves a lot of computation and therefore time.
            distance = PVector.dist(part1,centre)
            if distance < furthestDist + outerLimit:
                # if we're more than halfway to the centre
                # it's unlikely that it will touch one of the particles
                # within the search limit, so let's just break out of the loop.
                if distance < innerLimit:
                    print("Particle is inside the inner limit...")
                    break
                
                if distance > (doubleOuterLimit) + furthestDist:
                    print("Particle is outside the outer limit...")
                    break
                # when the particle touches the seed or another stuck particle, stick it
                numParts = len(particles)
                # go through particles in reverse order
                # newer particles are more likely to be at the outer edges of the DLA
                to = -1
                if maxSearchPerc != 0 and numParts > maxSearch:
                    maxSearch = numParts/100 * maxSearchPerc
                if numParts > maxSearch:
                    to = numParts - maxSearch
                for i in range(numParts-1,to,-1):
                    part2 = particles[i]
                    if PVector.dist(part1,part2) <= diam:
                        particles.append(part1)
                        if useWalkingCentre:
                            avesum += part1
                            centre = avesum/numParts
                        # Once the particle is stuck, draw it then exit the function
                        colorDistDivider = float(colorDistDivider)
                        numPartsDivider = float(numPartsDivider)
                        if useDistForCol:
                            d = PVector.dist(part1,realCentre)
                            cnum = int((d / colorDistDivider) % len(colors))
                            perc = d / colorDistDivider - cnum
                        else:
                            d = numParts
                            cnum = int((d / numPartsDivider) % len(colors))
                            perc = d / numPartsDivider - cnum                        
                        c = colors[cnum]
                        if cnum < len(colors)-1:
                            c1 = colors[cnum+1]
                        else:
                            c1 = colors[0]
                        stroke(lerpColor(c,c1,perc))
                        point(part1.x,part1.y)
                        if distance > furthestDist:
                            furthestDist = distance
                        #print('searched ' + str(checks) + ' times before stuck')
                        return
                    checks += 1
        if checks == searchLimit:
            print('Reached searchLimit of ' + str(searchLimit) + ', something probably went wrong!')
        print('Generating a new particle...')
        fails += 1
        if fails >= 3:
            print('Failed ' + str(fails) + ' times, perhaps try increasing maxSearch or innerLimitDivider...')
        print(' ')

# a slower way to draw, required if clearing the screen every draw call..
def drawParts(particles):
    for part in particles:
        point(part.x,part.y)
    
def setup():
    global stuckParts
    global diam
    global avesum
    
    avesum = PVector(0,0)
    clear()
    strokeWeight(diam)
    # the colour of the particles
    stroke(color(0,255,255))
    # size of the canvas (window)
    size(1500,1300)
    stuckParts.append(PVector(width/2,height/2))
    # uncomment this and change the value in range to generate
    # some existing particles before you even start drawing.
    '''
    for i in range(100):
        DLA(stuckParts)
    '''


def draw():
    #clear()
    global stuckParts
    global bias2Amount
    # only required if clearing the screen on the draw call.
    # slow...
    #drawParts(stuckParts)
    # uncomment to change the spin over time
    #bias2Amount += 0.0001
    DLA(stuckParts)

    
    