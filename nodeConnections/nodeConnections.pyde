# node connection diagram
import random

nodes = []
vels = []
maxSpeed = 3
numNodes = 10
maxDist = 200

def setup():
    size(500,500)
    for node in range(numNodes):
        pos = [random.uniform(0,width),random.uniform(0,height)]
        vel = [random.uniform(-maxSpeed,maxSpeed),random.uniform(-maxSpeed,maxSpeed)]
        nodes.append(pos)
        vels.append(vel)
    
def draw():
    clear()
    stroke(color(0,255,255))
    strokeWeight(2)
    for node in nodes:
        point(node[0],node[1])
        for node2 in nodes:
            if dist(node[0],node[1],node2[0],node2[1]) < maxDist:
                line(node[0],node[1],node2[0],node2[1])
    for i in range(numNodes):
        nodes[i][0] += vels[i][0]
        nodes[i][1] += vels[i][1]
        if nodes[i][0] < 0 or nodes[i][0] > width:
            vels[i][0] *= -1
        if nodes[i][1] < 0 or nodes[i][1] > height:
            vels[i][1] *= -1