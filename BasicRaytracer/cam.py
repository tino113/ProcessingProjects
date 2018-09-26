class cam():
    
    def __init__(self, pos = PVector(0,0,0), interest = PVector(0,10,0),fov = 10):
        self.pos = pos
        self.interest = interest
        self.fov = fov
        
    def getDir(self):
        return self.pos - self.interest
    
    def reproject(self, vec):
        return (self.getDir() + vec).normalize()
