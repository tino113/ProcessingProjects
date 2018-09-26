def setup():
    size(300,300)
    background(color(0,0,0))
    
def draw():
    fill(color(255,0,255))
    strokeWeight(10)
    stroke(color(mouseX,mouseY,-mouseX))
    
def mouseDragged():
    line(mouseX,mouseY,pmouseX,pmouseY)

def keyReleased():
    if key == 'b':
       stroke(color(0,0,0))
    if key == 'y':
       stroke(color(255,255,0))
