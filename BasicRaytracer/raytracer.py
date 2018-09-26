from ray import ray
import thread
import threading
import time

queueLock = threading.Lock()

def getHitDist(e):
    return e.hitDist

def clampCol(col):
    return color(constrain(red(col),0,255),constrain(green(col),0,255),constrain(blue(col),0,255),constrain(alpha(col),0,255))
    

class raytracer():
    
    def __init__(self, redrawRate = 100):
        self.redrawRate = redrawRate
    
    def raytrace(self, scene, samplesPerPixel = 1, method = 'random', xStart = 0, yStart = 0, xEnd = -1, yEnd = -1):
        if xEnd == -1:
            xEnd = width
        if yEnd == -1:
            yEnd = height
    
        lightWeight = 1.0/len(scene.lights)
        sampleWeight = 1.0/samplesPerPixel
        for y in range(yStart,yEnd):
            yMult = (y-float(height)/2)/(float(height)/2)
            pixelLocY = scene.cam.fov * yMult
            
            for x in range(xStart,xEnd):
                xMult = (x-float(width)/2)/(float(width)/2)
                pixelLocX = scene.cam.fov * xMult
               
                c = ab = la = color(0)
                
                hits = {}
                for i in range(samplesPerPixel):
                    pixLoc = PVector(pixelLocX,0,pixelLocY)
                    if samplesPerPixel > 1:
                        if method == 'random':
                            pixLoc += PVector(random(-1,1),0,random(-1,1))
                    reprj = scene.cam.reproject(pixLoc)
                    for obj in scene.objects:
                        r = ray(scene.cam.pos,reprj)
                        if r.hit(obj):
                            hits[r.hitDist] = r
                   
                    for key in sorted(hits.keys()):
                        #Albedo Shading
                        ab += hits[key].obj.mat.col
                        ab = clampCol(ab)
                        #Depth shading
                        #c += color(key*10)
                        #Lambert
                        for l in scene.lights:
                            ld = (l.pos-hits[key].hitPos).normalize()
                            la += color(ld.dot(hits[key].hitNorm) * 255) # * l.col * l.intensity
                        la *= lightWeight
                        la = clampCol(la)
                        if hits[key].obj.mat.opacity >= 1.0:
                            break;
                    c += ab + la
                c *=  sampleWeight
                c = clampCol(c)
                #set(x,y,c)
                pixels[width * y + x] = c
        
        queueLock.acquire()
        print(".")
        '''
        for y in range(yStart,yEnd):
            for x in range(xStart,xEnd):
                pixels[width * y + x] = c
        '''
        updatePixels()  
        redraw()      
        queueLock.release()
    
    def bucketRaytrace(self,scene, bucketSize = 50, samplesPerPixel = 1, method = 'random' ):
        loadPixels()
        for ybukt in range(ceil(height/bucketSize)):
            yStart = ybukt * bucketSize
            yEnd = (ybukt+1) * bucketSize
            if yEnd > height:
                yEnd = height
                
            for xbukt in range(ceil(width/bucketSize)):
                xStart = xbukt * bucketSize
                xEnd = (xbukt+1) * bucketSize
                if xEnd > width:
                    xEnd = width
                    
                #self.raytrace(scene,samplesPerPixel,method,xStart,yStart,xEnd,yEnd)
                try:
                    print("thread: ", xStart,yStart,xEnd,yEnd)
                    thread.start_new_thread( self.raytrace, (scene,samplesPerPixel,method,xStart,yStart,xEnd,yEnd) )
                except:
                    print ("Error: unable to start thread")
        print(threading.activeCount())
        while threading.activeCount() > 2:
            time.sleep(1)
            print(threading.activeCount())
            
        print("All buckets complete!")
        point(0,0)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        
