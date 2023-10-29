import json
import pygame
from button import Button
import plswork

class Document:
    jsonDict={}
    renderSurface=None
    colliders=[]
    def press(self,button):
        print(button.data)
        button.data[2]=not button.data[2]
    def __init__(self,jsonDict,renderSurface,bgPath="assets\\images\\ccc-id-card.png"):
        #converts json dictionary items to class attributes
        self.jsonDict=jsonDict
        self.surface=renderSurface
        self.bgPath=bgPath
        count=0
        jsonDict.pop("developerId")
        for k,v in jsonDict.items():
            if count==10:
               break
               setattr(self,k,v)
            
    def renderToScreen(self,surface,x,y,w,h,font_size,img,font_color=(255,255,255),font="assets/fonts/CONSOLA.TTF"):
        #renders id to screen
        dims=pygame.Rect(x,y,w,h)
        data=[]
        bg=pygame.image.load(self.bgPath)
        bg=pygame.transform.scale(bg,(dims[2],dims[3]))
        surface.blit(bg,dims)
        font=pygame.font.Font(font,font_size)
        gap=h/len(self.jsonDict)-25
        textDims=[x+50,y+30]
        #insert picture here
        count=0
        for k,v in self.jsonDict.items():
            text=k+": "+str(v)           
            text=font.render(text,True,font_color,None)
            textSize=(w/2,h/len(self.jsonDict)/2)
            # if len(self.colliders)<len(self.jsonDict):
            #     b=Button(surface,textDims[0],textDims[1],textSize[0],textSize[1],"",(0,0,0),None,self.press,doRender=False,data=[k,v,False])
            #     b.lcArgs=b;
            #     self.colliders.append(b)
            #text=pygame.transform.scale(text,textSize)
            surface.blit(text,textDims)
            
            if not img==None:
                logo=pygame.image.load(img)
                logo = pygame.transform.scale(logo, (w/2,h/2))
                surface.blit(logo,(x+w/2,y+15))
        
            textDims[1]+=gap
            count+=1

        for b in self.colliders:
           # b.debugRender()
            b.handleClick()

    