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
    def renderToScreen(self,surface,x,y,w,h,font_size,img,font_color=(255,255,255),bg_color=(0,0,0),font="assets/fonts/CONSOLA.TTF"):
        #renders id to screen
        dims=pygame.Rect(x,y,w,h)
        data=[]
        pygame.draw.rect(surface,bg_color,dims)
        font=pygame.font.Font(font,font_size)
        gap=h/len(self.jsonDict)-font_size
        textDims=[x,y]
        #insert picture here
        for k,v in self.jsonDict.items():
            text=k+": "+str(v)           
            text=font.render(text,True,font_color,None)
            textSize=(w/2,h/len(self.jsonDict)/2)
            #text=pygame.transform.scale(text,textSize)
            surface.blit(text,textDims)
            if not img==None:
                logo=pygame.image.load(img)
                logo = pygame.transform.scale(logo, (w/2,h/2))
                surface.blit(logo,(x+w/2,y))
            textDims[1]+=gap