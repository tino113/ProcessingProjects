
def setup():
    size(400,400)
    b = color(0)
    w = color(255)
    background(w)
    set(width/2,height-1,b)
    
def draw():
    
    loadPixels();
    lastRow = (height-1)*width 
    for i in range(lastRow):
        pixels[i] = pixels[i+width];
    for x in range(width):
        pixels[lastRow + x] = color(255)
    updatePixels();
       
    rule90()
        
def rule90():
    b = color(0)
    w = color(255)
    y = height - 1
    maxX = width + 2
    for x in range(maxX):
        p1 = get(x-1,y-1)
        p2 = get(x,y-1)
        p3 = get(x+1,y-1)
        if p1 == b and p2 == b and p3 == w:
            set(x,y,b)
        elif p1 == b and p2 == w and p3 == w:
            set(x,y,b)
        elif p1 == w and p2 == b and p3 == b:
            set(x,y,b)
        elif p1 == w and p2 == w and p3 == b:
            set(x,y,b)
        else:
            continue
        
def rule30():
    b = color(0)
    w = color(255)
    y = height - 1
    maxX = width + 2
    for x in range(maxX):
        p1 = get(x-1,y-1)
        p2 = get(x,y-1)
        p3 = get(x+1,y-1)
        if p1 == b and p2 == w and p3 == w:
            set(x,y,b)
        elif p1 == w and p2 == b and p3 == b:
            set(x,y,b)
        elif p1 == w and p2 == b and p3 == w:
            set(x,y,b)
        elif p1 == w and p2 == w and p3 == b:
            set(x,y,b)
        else:
            continue
   
    
    
    