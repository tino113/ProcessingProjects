# Back Propegation

# list of inputs and their initial values
inputs = [0,0]
# list of intermediary stages and the number of nodes in each
stages = [3]
stageVals = []
# list of outputs
outputs = [0,0]
# list of all weights
weights = []
# connections do not need to be stored with to and from
# instead they can just be calculated from positions of nodes
# as nodes do not change in this graph
nodeSize = 30
bezierAmt = 50
mutAmt = 0.1
mutChance = 0.5
textHeight = 14

def feedForward(inps,outs,stag,wghts):
    # for each stage take the left multiply 
    # by weights and set to the right
    return outs

def backprop(inps,outs,stag,wghts):
    pass

def mutate(wghts,chance):
    global mutAmt
    for i in range(len(wghts)):
        level = wghts[i]
        for j in range(len(level)):
            if random(0,1) <= chance:
                wghts[i][j] += random(-mutAmt, mutAmt)
                if wghts[i][j] < -1:
                    wghts[i][j] = -1
                elif  wghts[i][j] > 1:
                    wghts[i][j] = 1
    return wghts
    
def setupGraph(inps,outs,stag,wghts):
    global stageVals
    # here we need to generate all the connections between nodes
    # depending on what we set in the beginning
    # and then create all the weights required
    # we'll need a lot of weights, let's split it into levels
    # in order to make it easier to understand
    # the 2 represents the inputs and outputs
    for i in range(2+len(stag)-1):
        wghts.append([])
    # starting with inputs let's create the first level of weights
    for i in range(int(pow(len(inps),stag[0]))):
        wghts[0].append(random(-1,1))
    # now let's create the weights between each of the stages
    for i in range(len(stages)-1):
        one = stag[i]
        two = stag[i+1]
        for j in range(int(pow(one,two))):
            wghts[i+1].append(random(-1,1))
    # now let's create the weights between the last stage and
    # the outputs
    for i in range(int(pow(stag[len(stag)-1],len(outs)))):
        wghts[len(stag)].append(random(-1,1))
    # all finished!
    for i in range(len(stag)):
        stageVals.append([])
        for j in range(stag[i]):
            stageVals[i].append(0)
    '''
    for level in wghts:
        print(level)
        print(" ")
    '''
    return wghts
    
def drawGraph(inps,outs,stag,wghts):
    global nodeSize
    global bezierAmt
    global stageVals
    global textHeight
    clear()
    background(color(20))
    tempList = [len(inps)]
    tempList += stag
    tempList.append(len(outs))
    numInX = 2+len(stages)
    xDist = width/numInX
    inputCol = color(100,255,100) # Light Green
    outputCol = color(255,100,100) # light Red
    stageStartCol = color(50,50,180) # Darker Blue
    stageEndCol = color(150,150,255) # Lighter Blue
    conStartCol = color(200,0,200) 
    conEndCol = color(0,200,200)
    
    # draw all the connections between
    # lerp the colour for the weight between -1 and 1
    noFill()
    for l in range(len(wghts)):
        numLeft = tempList[l]
        numRight = tempList[l+1]
        yDistfrm = height/numLeft
        yDistto = height/numRight
        frmX = xDist * (l+0.5)+nodeSize/2
        toX = xDist * (l+1.5)-nodeSize/2
        for one in range(numLeft):
            frmY = yDistfrm * (one+0.5)
            for two in range(numRight):
                toY = yDistto * (two+0.5)
                w = (wghts[l][one+two]+1)*0.5
                strokeWeight(lerp(1,6,w))
                stroke(lerpColor(conStartCol,conEndCol,w))
                #line(frmX,frmY,toX,toY)
                bezier(frmX,frmY,frmX+bezierAmt,frmY,toX-bezierAmt,toY,toX,toY)
    strokeWeight(nodeSize)
    stroke(inputCol)
    fill(color(0))
    textAlign(CENTER)
    textSize(textHeight)
    # draw all the nodes
    for x in range(numInX):
        numInY = tempList[x]
        yDist = height/numInY
        w = float(x)/len(stag)
        if x > 0:
            stroke(lerpColor(stageStartCol,stageEndCol,w))
        if x == numInX-1:
            stroke(outputCol)
        for y in range(numInY):
            point(xDist * (x+0.5),yDist * (y+0.5))
            if x == 0:
                te = str(inps[y])
            elif x == numInX-1:
                te = str(outs[y])
            else:
                te = str(stageVals[x-1][y])
            text(te,xDist * (x+0.5),yDist * (y+0.5)+textHeight/2)  
            
def setup():
    global inputs
    global outputs
    global stages
    global weights
    size(500,500)
    setupGraph(inputs,outputs,stages,weights)
    drawGraph(inputs,outputs,stages,weights)

def draw():
    global inputs
    global outputs
    global stages
    global weights
    global mutChance
    clear()
    # let's play a game of higher or lower
    # firstly we will create a random integer between
    # a minimum and maximum value
    minimum = 0
    maximum = 100
    randNum = int(random(minimum,maximum))
    print("The number we're guessing for is " + str(randNum))
    # let's start the graph with two inputs
    # a random starting guess
    inputs[0] = int(random(minimum,maximum))
    # and a boolean for higher or lower
    inputs[1] = int(random(0,1))
    # let's start a while loop, which will run while
    # we've not found the correct value
    found = False
    tries = 0
    while not found:
        # now let's use back propegation 
        # to output a new value, this is our guess
        guess = int(feedForward(inputs,outputs,stages,weights)[0])
        weights = mutate(weights,mutChance)
        # if this value equals our guess then we
        # change found to True
        if guess == randNum:
            found = True
            print("Found it after " + str(tries) + " tries!")
        tries += 1
        break
    drawGraph(inputs,outputs,stages,weights)