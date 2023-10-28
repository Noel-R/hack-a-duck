import json
import pygame
class Document:
    def __init__(self,jsonDict):
        #converts json dictionary items to class attributes
        for k,v in dictData.items():
            setattr(self,k,v)
    def renderToScreen(self,screen,x,y,width,height):
        dims=pygame.rect(x,y,w,h)



        
