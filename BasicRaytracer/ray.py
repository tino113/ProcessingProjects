from RTSphere import RTSphere

class ray():
    
    def __init__(self,origin = PVector(0,0,0), dir = PVector(0,-1,0)):
        self.origin = origin
        self.dir = dir.normalize()
    
    def hit(self, object):
        self.obj = object
        if isinstance(object,RTSphere):
            return self.hitSphere()
        return False
    
    def hitSphere(self):
        dotp = self.dir.dot(self.origin - self.obj.centre)
        if dotp > 0:
            opD = self.dir * -1
            cpVect = (dotp*opD)
            closestPoint = cpVect + self.origin
            dVec = self.obj.centre - closestPoint
            d = dVec.mag()
            if d < self.obj.radius:
                dVecHit = PVector(0,0,0)
                if self.obj.inside(self.origin):
                    dVecHit = cpVect.mag() + sqrt(self.obj.radius*self.obj.radius - d * d)
                else:
                    dVecHit = cpVect.mag() - sqrt(self.obj.radius*self.obj.radius - d * d)
                self.hitPos = self.origin + self.dir * dVecHit
                self.hitDist = self.hitPos.mag()
                self.hitNorm = (self.obj.centre - self.hitPos).normalize()
                return True
        return False
