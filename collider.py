import pygame

class collider:
    data=None
    def __int__(self,x,y,w,h,onCollision):
        self.x=x
        self.y=y
        self.h=h
        self.w=w
        self.data=data
        self.Collision=onCollision

    def checkCollision(self,x,y):
        if (x>self.x and y>self.y and x<self.x+self.w and y<self.y+self.h):
            return True
        return False

    def onCollision(self,data=None):
        self.Collision()
        
