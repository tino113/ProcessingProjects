
def setup():
    size(800,600)
    
def draw():
    b = color(0)
    w = color(255)
    background(w)
    set(width/2,0,b)
    
    maxX = width-2
    for y in range(height):
        for x in range(maxX):
            p1 = get(x,y)
            p2 = get(x+1,y)
            p3 = get(x+2,y)
            
            if p1 == b and p2 == b and p3 == b: #rule 1
                #do nothing
                continue
            elif p1 == b and p2 == b and p3 == w: #rule 2
                # set middle pixel on next line to be black
                set(x+1,y+1,b)
            elif p1 == b and p2 == w and p3 == b: #rule 3
                #do nothing
                continue
            elif p1 == b and p2 == w and p3 == w: #rule 4
                # set middle pixel on next line to be black
                set(x+1,y+1,b)
            elif p1 == w and p2 == b and p3 == b: #rule 5
                # set middle pixel on next line to be black
                set(x+1,y+1,b)
            elif p1 == w and p2 == b and p3 == w: #rule 6
                #do nothing
                continue
            elif p1 == w and p2 == w and p3 == b: #rule 7
                # set middle pixel on next line to be black
                set(x+1,y+1,b)
            else:
                continue