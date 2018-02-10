import random

fishies = []
numFish = 80
flockViewDist = 40
flockMaxLocal = 4
flockAlignment = 0.1
flockSeparation = 0.3
flockCohesion = 0.1
flockMinDist = 5
edgeAvoidance = 0.15
maxSpeed = 3
minSpeed = 0.8

def setup():
    size(500,500)
    for fish in range(numFish):
        pos = PVector(random.uniform(0,width),random.uniform(0,height))
        vel = PVector(random.uniform(-maxSpeed,maxSpeed),random.uniform(-maxSpeed,maxSpeed))
        fishies.append([pos,vel])
        
def flock(fishies):
    #for each fish in fishies
    friends = 0
    friendAverage = PVector(0,0)
    friendAverageVel = PVector(0,0)
    for fish1 in fishies:
        #for each other fish in fishies
        friends = 0
        friendAverage = PVector(0,0)
        friendAverageVel = PVector(0,0)
        for fish2 in fishies:
            #if the two fish are close enough
            between = PVector.sub(fish2[0],fish1[0])
            betweenMag = between.mag()
            between.normalize()
            if betweenMag < flockViewDist and friends < flockMaxLocal:
                #move towards other fish
                friends += 1
                friendAverage += fish2[0]
                friendAverageVel += fish2[1]
            if betweenMag <= flockMinDist:
                fish1[1] -= between * flockSeparation
        friendAverage /= friends
        friendAverageVel /= friends
        fish1[1] += friendAverageVel.normalize() * flockAlignment
        vecToAverage = PVector.sub(friendAverage,fish1[0])
        fish1[1] += vecToAverage.normalize() * flockCohesion
        #ensure that the velocity is not greater than max speed
        if fish1[1].mag() > maxSpeed:
            fish1[1] = fish1[1].normalize() * maxSpeed
        if fish1[1].mag() < minSpeed:
            fish1[1] = fish1[1].normalize() * minSpeed
        #add velocity to position
        fish1[0] += fish1[1]
        
def loopWorld(fishies):
    for fish1 in fishies:
        if fish1[0].x < 0:
            fish1[0].x += width
        elif fish1[0].x > width:
            fish1[0].x -= width
        if fish1[0].y < 0:
            fish1[0].y += height
        elif fish1[0].y > height:
            fish1[0].y -= height
            
def avoidEdges(fishies, distance):
    for fish1 in fishies:
        if fish1[0].x < distance:
            fish1[1].x += edgeAvoidance
        elif fish1[0].x > width - distance:
            fish1[1].x -= edgeAvoidance
        if fish1[0].y < distance:
            fish1[1].y += edgeAvoidance
        elif fish1[0].y > height - distance:
            fish1[1].y -= edgeAvoidance

def draw():
    clear()
    stroke(color(255))
    strokeWeight(5)
    for fish in fishies:
        point(fish[0].x,fish[0].y)
    flock(fishies)
    avoidEdges(fishies,50)