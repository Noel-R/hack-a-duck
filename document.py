import json
import pygame

class Document:
    jsonDict={}
    renderSurface=None
    def __init__(self,jsonDict,renderSurface):
        #converts json dictionary items to class attributes
        self.jsonDict=jsonDict
        self.renderSurface=renderSurface
        for k,v in jsonDict.items():
            setattr(self,k,v)
    def renderToScreen(self,surface,x,y,w,h):
        #renders id to screen
        dims=pygame.Rect(x,y,w,h)
        data=[]
        pygame.draw.rect(surface,(0,0,255),dims)
        font=pygame.font.Font("assets\\fonts\\CONSOLA.TTF",int(w/20))
        gap=h/len(self.jsonDict)
        textDims=[x,y]
        #insert picture here
        for k,v in self.jsonDict.items():
            text=k+" : "+str(v)           
            text=font.render(text,True,(255,255,255),None)
            textSize=(w/2,h/len(self.jsonDict)/2)
            #text=pygame.transform.scale(text,textSize)
            surface.blit(text,textDims)
            logo=pygame.image.load("assets\\images\\download.png")
            logo = pygame.transform.scale(logo, (w/2,h/2))
            surface.blit(logo,(x+w/2,y))
            textDims[1]+=gap



