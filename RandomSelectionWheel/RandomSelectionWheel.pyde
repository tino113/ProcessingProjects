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
    size(500,500)
    for i in range(20):
        students.append("name")
        colors.append(color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    numStudents = len(students)
    arcAngle = TWO_PI / numStudents
    arcStart -= arcAngle/2
    
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
    #ellipse(width/2,height/2,width-10,height-10)
    
    
    i = 0
    #textAlign(CENTER)
    
    for student in students:
        fill(colors[i])
        arcEnd = arcStart + arcAngle
        arc(width/2,height/2,width-20,height-20,arcStart-0.01,arcEnd+0.01)
        arcStart += arcAngle
        i += 1 
    
    i = 0 
    for student in students:
        fill(color(255))
        textSize(20)
        pushMatrix()
        translate(width/2,height/2)
        rotate(arcStart+arcAngle)
        rotate(arcAngle*i)
        translate(0,-height/2+15)
        rotate(radians(90))
        text(student,0,0)
        popMatrix()
        i += 1 
    
    stroke(color(0))
    fill(color(255))
    triangle(width/2-10,5,width/2+10,5,width/2,30)    
    
    if click:
        click = False
        spinFor = 50
        maxSpeed = random.uniform(0.02,0.2)
    
    if spinFor >= 0:
        if speed < maxSpeed:
            speed += maxSpeed / 10
        spinFor -= 1
    else:
        if speed > 0:
            speed -= maxSpeed / 10
        elif speed < 0:
            speed = 0
    arcStart += speed
        
    
def mouseClicked():
    global click
    click = True
    