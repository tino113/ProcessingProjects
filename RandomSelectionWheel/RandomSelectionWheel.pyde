#Pupil selection wheel
#Click to spin the wheel
import random
from button import button

click = False
spinFor = 0
fade = 0
students = []
colors = []
arcStart = 0
maxSpeed = 0
speed = 0
numStudents = 0
arcAngle = 0
buttons = []

def setup():
    global bl
    global halfWidth
    global halfHeight
    global form
    global wait
    size(500,500)
    halfWidth = width*0.5
    halfHeight = height*0.5
    form = '7I'
    bl = createGraphics(width,height)
    drawWheel()
    wait = 30
    
def drawWheel():
    global buffer
    global arcStart
    buffer = createGraphics(width,height)
    if form == '7D':
        students = ['none','none','none','none','none','none','none','none']
    if form == '7B':
        students = ['none','none','none','none','none','none','none','none']
    if form == '7I':
        students = ['none','none','none','none','none','none','none','none']
    if form == '8D':
        students = ['none','none','none','none','none','none','none','none']
    if form == '8B':
        students = ['none','none','none','none','none','none','none','none']
    if form == '8I':
        students = ['none','none','none','none','none','none','none','none']
    if form == '9D':
        students = ['none','none','none','none','none','none','none','none']
    if form == '9B':
        students = ['none','none','none','none','none','none','none','none']
    if form == '9I':
        students = ['none','none','none','none','none','none','none','none']
    if form == 'Y10':
        students = ['none','none','none','none','none','none','none','none']
    if form == 'Y11':
        students = ['none','none','none','none','none','none','none','none']
    for i in range(len(students)):
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

mode = 'select'

def drawBoxes(bl,txt,fcol = color(64),scol = color(40),txcol = color(230),sdepth = 3,gap = 10,rnd = 10):
  global buttons
  #calcSizes(width,height)
  bl.beginDraw()
  bl.clear()
  bl.noStroke()
  buttons = []
  rows, cols = 0, 0
  remain = len(txt)
  cols = ceil(sqrt(remain))
  rows = ceil(remain/cols)
  if not remain%2 == 0:
    rows += 1
  totalW = width - ((cols+1)*gap)
  totalH = height - ((rows+1)*gap)
  boxW = totalW/cols
  boxH = totalH/rows
  hbW = boxW/2
  hbH = boxH/2
  currX = gap
  currY = gap
  offset = 0
  count = 0
  bl.textAlign(CENTER,CENTER)
  for row in range(rows):
    tcol = cols
    if remain < cols:
      tcol = remain
      offset = (cols - remain) * boxW / 2
    for col in range(tcol):
      text = str(txt[count])
      ttext = text
      if ttext.endswith(' '):
        ttext = str(ttext[:-1])
      # shadow
      bl.fill(scol)
      bl.rect(currX+offset+sdepth,currY+sdepth,boxW-sdepth,boxH-sdepth,rnd,rnd,rnd,rnd)
      # box
      bl.fill(fcol)
      bl.rect(currX+offset,currY,boxW-sdepth,boxH-sdepth,rnd,rnd,rnd,rnd)
      # text
      
      # text Shadow
      bl.fill(scol)
      bl.text(ttext,currX+offset+hbW+sdepth,currY+hbH+sdepth)
      # text
      bl.fill(txcol)
      bl.text(ttext,currX+offset+hbW,currY+hbH)
      # invisible hitbox
      buttons.append(button(lambda: True,text,currX+offset,currY,boxW,boxH,'word'))
      currX += gap + boxW
      remain -= 1
      if count < len(txt):
        count += 1
    currY += gap + boxH
    currX = gap
  bl.endDraw()

def draw():
    global mode
    if mode == 'select':
        select()
    elif mode == 'spin':
        spinner()

def select():
    background(0)
    drawBoxes(bl,['7D','7B','7I','8D','8B','8I','9D','9B','9I','Y10','Y11'])
    image(bl,0,0)
        
def spinner():
    global click
    global spinFor
    global arcStart
    global maxSpeed
    global speed
    global numStudents
    global arcAngle
    global wait
    global mode
    clear()
    noStroke()
    smooth()
    #ellipse(halfWidth,halfHeight,width-10,height-10)

    if click:
        click = False
        spinFor = 80
        maxSpeed = random.uniform(0.02,0.2)
    
    if spinFor >= 20:
        if speed < maxSpeed:
            speed += maxSpeed / 10.0
        spinFor -= 1
    else:
        if speed > 0:
            speed -= maxSpeed / 10.0
        elif speed < 0:
            speed = 0
            wait = 30
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
    global mode
    global click
    if mode == 'spin':
        click = True
    
def mouseReleased():
  global console
  global tl
  global mode
  global form
  if mode == 'select':
    for btn in buttons:
        if btn.over():
            if btn.type == 'word':
                form = btn.word
                drawWheel()
                mode = 'spin'
            else:
                btn.function()