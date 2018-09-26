import cam

class scene():
    
    def __init__(self):
        self.cam = cam.cam()
        self.objects = []
        self.lights = []
        
    def setCamera(self, cam):
        self.cam = cam
        
    def addObject(self, obj):
        self.objects.append(obj)
        
    def addLight(self, light):
        self.lights.append(light)
        
        
