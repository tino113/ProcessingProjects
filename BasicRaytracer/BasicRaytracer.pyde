# A basic raytracer

# STEP 1: Get spheres drawing as flat objects (no shading)
# STEP 2: Depth shading
# STEP 3: Basic shading
# STEP 4: Reflectivity and materials
from scene import scene
from RTSphere import RTSphere
from cam import cam
from material import material
from raytracer import raytracer
from light import light
    
def setup():
    size(100,100)
    noLoop()
    scn = scene()
    scn.setCamera(cam(PVector(0,-5,0),PVector(0,0,0)))
    
    w = material(color(255))
    gr = material(color(150),opacity = 0.5)
    r = material(color(255,0,0))
    g = material(color(0,255,0))
    b = material(color(0,0,255))
    c = material(color(0,255,255))
    y = material(color(255,255,0))
    m = material(color(255,0,255))
    scn.addObject(RTSphere(PVector(0,0,-1000010),1000000,r))
    scn.addObject(RTSphere(PVector(0,0,1000010),1000000,g))
    scn.addObject(RTSphere(PVector(-1000010,0,0),1000000,b))
    scn.addObject(RTSphere(PVector(1000010,0,0),1000000,c))
    scn.addObject(RTSphere(PVector(0,1000010,0),1000000,m))
    scn.addObject(RTSphere(PVector(0,0,0),2,gr))
    scn.addObject(RTSphere(PVector(-2,2,-4),3,w))
    scn.addLight(light(PVector(0,5,8),color(255,255,255),1.0))
    rt = raytracer()
    rt.raytrace(scn)
    #rt.bucketRaytrace(scn,10)
    
    