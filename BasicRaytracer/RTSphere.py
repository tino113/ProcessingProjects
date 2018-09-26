from material import material

class RTSphere():
    
    def __init__(self, cen = PVector(0,0,0), r = 1, mat = material()):
        self.centre = cen
        self.radius = r
        self.mat = mat
        
    def inside(self,pos):
        dVec = pos - self.centre
        if abs(dVec.mag()) < self.radius:
            return True
        return False
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return "Centre: " + str(self.centre) + " radius: " + str(self.radius)
        
