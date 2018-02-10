#Pupil selection wheel
#Click to spin the wheel
import random

click = False
spinFor = 0
students = []
colors = []
arcStart = 0
maxSpeed = 0
speed = 0
numStudents = 0
arcAngle = 0

def setup():
    global students
    global colors
    global numStudents
    global arcAngle
    global arcStart
    global halfWidth
    global halfHeight
    global buffer
    size(600,600)
    buffer = createGraphics(width,height)
    halfWidth = width*0.5
    halfHeight = height*0.5
    for i in range(21):
        students.append("name")
        colors.append(color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    numStudents = len(students)
    arcAngle = TWO_PI / float(numStudents)
    arcStart -= arcAngle * 0.5
    
    buffer.beginDraw()
    i = 0
    #textAlign(CENTER)
    for student in students:
        buffer.fill(colors[i])
        arcEnd = arcStart + arcAngle
        buffer.arc(halfWidth,halfHeight,width-20,height-20,arcStart-0.01,arcEnd+0.01)
        arcStart += arcAngle
        i += 1 
    
    i = 0 
    for student in students:
        buffer.fill(color(255))
        buffer.textSize(20)
        buffer.pushMatrix()
        buffer.translate(halfWidth,halfHeight)
        buffer.rotate(arcStart+arcAngle)
        buffer.rotate(arcAngle*float(i))
        buffer.translate(2,-halfHeight+15)
        buffer.rotate(HALF_PI)
        buffer.text(student,0,0)
        buffer.popMatrix()
        i += 1
    buffer.endDraw()
    
def draw():
    global click
    global spinFor
    global arcStart
    global maxSpeed
    global speed
    global numStudents
    global arcAngle
    clear()
    noStroke()
    smooth()
    #ellipse(halfWidth,halfHeight,width-10,height-10)

    if click:
        click = False
        spinFor = 80
        maxSpeed = random.uniform(0.02,0.2)
    
    if spinFor >= 0:
        if speed < maxSpeed:
            speed += maxSpeed / 10.0
        spinFor -= 1
    else:
        if speed > 0:
            speed -= maxSpeed / 10.0
        elif speed < 0:
            speed = 0
    arcStart += speed
    
    pushMatrix()
    translate(halfWidth,halfHeight)
    rotate(arcStart)
    translate(-halfWidth,-halfHeight)
    
    image(buffer,0,0)
    popMatrix()
    
    stroke(color(0))
    fill(color(255))
    triangle(halfWidth-10,5,halfWidth+10,5,halfWidth,30)

        
    
def mouseClicked():
    global click
    click = True
    