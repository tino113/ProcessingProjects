#Pong

paddle1Y = 0
paddle2Y = 0

ballPos = PVector(0,0)
ballVel = PVector(0,0)

paddleWidth = 50
paddleThickness = 10
ballDiam = 20

score1 = 0
score2 = 0

speed = 4
player2AI = True
player1AI = True

moveUp = False
moveDown = False

def setup():
    global ballPos
    global ballVel
    global paddle1Y
    global paddle2Y
    global speed
    global score1
    global score2
    size(500,500)
    score1 = 0
    score2 = 0
    ballPos = PVector(width/2,height/2)
    ballVel = PVector(random(-1,1),0)
    ballVel = ballVel.normalize() * speed
    paddle1Y = random(paddleWidth,height-paddleWidth)
    paddle2Y = random(paddleWidth,height-paddleWidth)
    
def reset():
    global ballPos
    global ballVel
    global speed
    ballPos = PVector(width/2,height/2)
    ballVel = PVector(0,0)
    while abs(ballVel.x) < 0.2:
        ballVel = PVector(random(-1,1),0)
    speed += 0.2
    
def keyPressed():
    global moveUp
    global moveDown

    if not player2AI:
        if key == 'q' or key == 'Q':
            moveUp = True
        elif key == 'a' or key == 'A':
            moveDown = True
        else:
            pass
    
    if not player2AI:
        if key == 'o' or key == 'O':
            paddle2Y -= speed*2
        elif key == 'l' or key == 'L':
            paddle2Y += speed*2
        else:
            pass
def keyReleased():
    global moveUp
    global moveDown
    if key == 'q' or key == 'Q':
        moveUp = False
    elif key == 'a' or key == 'A':
        moveDown = False
    else:
        pass

def control():
    global paddle1Y
    global paddle2Y
    global speed
    global moveUp
    global moveDown
    if moveUp:
        paddle1Y -= speed*2
    elif moveDown:
        paddle1Y += speed*2
    else:
        pass
    
def draw():
    global ballPos
    global ballVel
    global paddle1Y
    global paddle2Y
    global score1
    global score2
    global ballDiam
    global player2AI
    
    clear()
    stroke(color(255))
    strokeWeight(ballDiam)
    point(ballPos.x,ballPos.y)
    
    control()
    
    halfPaddleW = paddleWidth/2
    
    strokeWeight(0)
    #player1
    rect(0,paddle1Y,paddleThickness,paddleWidth)
    #player2
    rect(width-paddleThickness,paddle2Y,paddleThickness,paddleWidth)
    
    if player1AI:
        if ballVel.x < 0.1:
            if paddle1Y+halfPaddleW >= ballPos.y:
                paddle1Y -= speed
            if paddle1Y+halfPaddleW <= ballPos.y:
                paddle1Y += speed
    
    if player2AI:
        if ballVel.x > -0.1:
            if paddle2Y+halfPaddleW >= ballPos.y:
                paddle2Y -= speed
            if paddle2Y+halfPaddleW <= ballPos.y:
                paddle2Y += speed
    
    ballPos += ballVel
    
    if paddle1Y > height-paddleWidth:
        paddle1Y = height-paddleWidth
    elif paddle1Y < 0:
        paddle1Y = 0
    if paddle2Y > height-paddleWidth:
        paddle2Y = height-paddleWidth
    elif paddle2Y < 0:
        paddle2Y = 0
    
    textSize(32)
    text("P1:"+ str(score1),0,30)
    text("P2:"+ str(score2),width - 80,30)
    
    #ball bounces if it touches the paddles
    if ballPos.x < paddleThickness + ballDiam/2:
        if ballPos.y > paddle1Y and ballPos.y < paddle1Y + halfPaddleW:
            ballVel.x = -ballVel.x
            ballVel.y -= random(0,1)
        if ballPos.y > paddle1Y + halfPaddleW and ballPos.y < paddle1Y + paddleWidth:
            ballVel.x = -ballVel.x
            ballVel.y += random(0,1)
    if ballPos.x > width - paddleThickness - ballDiam/2 :
        if ballPos.y > paddle2Y and ballPos.y < paddle2Y + halfPaddleW:
            ballVel.x = -ballVel.x
            ballVel.y -= random(0,1)
        if ballPos.y > paddle2Y + halfPaddleW and ballPos.y < paddle2Y + paddleWidth:
            ballVel.x = -ballVel.x
            ballVel.y += random(0,1)
            
    ballVel = ballVel.normalize() * speed
    
    #players score points if hit other side
    if ballPos.x > width:
        score1 += 1
        reset()
    if ballPos.x < 0:
        score2 += 1
        reset()
    #bounce if the ball is on an upper edge.
    if ballPos.y < 0 or ballPos.y > height:
        ballVel.y = -ballVel.y
    