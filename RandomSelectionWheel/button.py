import datetime


class button():
    
    def __init__(self,function=lambda: False,word = '',x=0,y=0,w=0,h=0,btype = 'button'):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hover = False
        self.hoverStart = 0
        self.tooltipDisplayed = False
        self.function = function
        self.type = btype
        self.drawn = False
        self.word = word
        
    def debugDraw(self,layer):
        layer.beginDraw()
        layer.fill(color(255,255,255,100))
        layer.rect(self.x,self.y,self.w,self.h)
        layer.endDraw()
        
    def over(self):
        if (mouseX >= self.x and mouseX <= self.x+self.w and mouseY >= self.y and mouseY <= self.y+self.h):
            self.hover = True
            return True
        else:
            self.hover = False
        return False

    def onClick(self):
        self.function()

    def onDoubleClick(self):
        self.function()
        
            