# Drawing Program

prevPos = PVector()
brushSize = 20

def setup():
    global prevPos
    size(300,300)
    prevPos = PVector(0,0)
    
def draw():
    global prevPos
    global brushSize
    
    if keyPressed:
        if key == 'p':
            brushSize += 1
        if key == 'o':
            if brushSize > 1:
                brushSize -= 1
            
    stroke(color(0,255,255))
    strokeWeight(brushSize)
    if mousePressed:
       line(mouseX,mouseY,prevPos.x,prevPos.y) 
    
    prevPos = PVector(mouseX,mouseY)