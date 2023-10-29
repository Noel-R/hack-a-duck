import json
import pygame
from Button import Button
import plswork
import copy
class Document:
    jsonDict={}
    renderSurface=None
    buttons=[]
    def press(self,button):
        print(button.data)
        button.data[2]=not button.data[2]
    def __init__(self,jsonDict,surface,x,y,w,h,font_size,img,font_color=(255,255,255),bgPath="assets\\images\\documents\\documents.jpg",font="assets/fonts/CONSOLA.TTF"):
        #converts json dictionary items to class attributes
        self.jsonDict=jsonDict
        self.surface=surface
        self.bgPath=bgPath
        self.x=x
        self.y=y
        self.h=h
        self.w=w
        self.font_size=font_size
        self.img=img
        self.font_color=font_color
        self.font=font
        self.dims=pygame.Rect(x,y,w,h)
        self.gap=self.h/10
        count=0
        jsonDict.pop("developerId")
        self.genButtons()
        for k,v in jsonDict.items():
            if count==10:
               break
            self.buttons[count].data=[k,v,False]
            setattr(self,k,v)
            print(k,v)
        

    def genButtons(self):
        buttonDims=copy.copy(self.dims)
        for i in range(10):
            b=Button(self.surface,buttonDims.x,buttonDims.y,buttonDims.w,buttonDims.h,leftClickFunc=self.press,data=[None,None,False])
            b.lcArgs=b
            buttonDims.y+=self.gap
            self.buttons.append(b)
        print("s;",self.dims)

    def renderToScreen(self):
        #renders id to screen
        bg=pygame.image.load(self.bgPath)
        bg=pygame.transform.scale(bg,(self.dims[2],self.dims[3]))
        self.surface.blit(bg,self.dims)
        font=pygame.font.Font(self.font,self.font_size)
   
        textDims=[self.x,self.y]
        #insert picture here
        count=0
        for k,v in self.jsonDict.items():
            text=k+": "+str(v)           
            text=font.render(text,True,self.font_color,None)
            textSize=(self.w/2,self.h/len(self.jsonDict)/2)
#            if len(self.colliders)<len(self.jsonDict):
#                b=Button(self.surface,textDims[0],textDims[1],textSize[0],textSize[1],"",(0,0,0),None,self.press,doRender=False,data=[k,v,False])
#                b.lcArgs=b;
#                self.colliders.append(b)
            text=pygame.transform.scale(text,textSize)
            self.surface.blit(text,textDims)
            
            if not self.img==None:
                logo=pygame.image.load(self.img)
                logo = pygame.transform.scale(logo, (self.w/2,self.h/2))
                self.surface.blit(logo,(self.x+self.w/2,self.y))
        
            textDims[1]+=self.gap
            count+=1

        for b in self.buttons:
            #b.debugRender()
            b.handleClick()

    