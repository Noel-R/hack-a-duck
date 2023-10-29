#document.py
import json
import pygame
from Button import Button
import plswork
import copy
import random
class Document:
    jsonDict={}
    renderSurface=None
    buttons=[]
    
    def toggleButtons(self, button):
        for b in self.buttons:
            if b.data[0]==button.data[0]:
                b.data[2]= True
            else:
                b.data[2]= False
            
    def press(self,button):
        self.toggleButtons(button)
        
    def __init__(self,jsonDict,surface,x,y,w,h,font_size,img,font_color=(255,255,255),bgPath="assets\\images\\documents\\documents.jpg",font="assets/fonts/CONSOLA.TTF",hasButtons=True):
        #converts json dictionary items to class attributes
        self.jsonDict=jsonDict
        self.surface=surface
        self.bgPath=bgPath
        self.x=x
        self.y=y
        self.hasButtons=hasButtons
        self.h=h
        self.w=w
        self.font_size=font_size
        self.img=img
        self.font_color=font_color
        self.font=font
        self.dims=pygame.Rect(x,y,w,h)
        self.gap=self.h/10
   
        if hasButtons:
            self.genButtons()



    def genButtons(self):
        if self.hasButtons:
            buttonDims=copy.copy(self.dims)
            for i in range(10):
                b=Button(self.surface,buttonDims.x,buttonDims.y,buttonDims.w,10,leftClickFunc=self.press,data=[None,None,False], )
                b.lcArgs=b
                buttonDims.y+=self.gap
                self.buttons.append(b)
            self.updateButtons()

    def renderToScreen(self):
        #renders id to screen
        bg=pygame.image.load(self.bgPath)
        bg=pygame.transform.scale(bg,(self.dims[2],self.dims[3]))
        self.surface.blit(bg,self.dims)
        font=pygame.font.Font(self.font,self.font_size)
   
        for button in self.buttons:
            if button.data[2]:
                button.background = (255, 0, 0)  # red
            else:
                button.background = (0, 255, 0)  # green

            button.docrender()
            button.handleClick()
   
   
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

class Id(Document):    
    def __init__(self, jsonDict, surface, x, y, w, h, font_size, img, font_color=(0, 0, 0), bgPath="assets\images\documents\documents.jpg", font="assets/fonts/CONSOLA.TTF",toBeApproved=True,hasButtons=True):
        super().__init__(jsonDict, surface, x, y, w, h, font_size, img, font_color, bgPath, font,hasButtons)
        self.jsonDict=jsonDict
   
        invalidReason=None
        self.approved = toBeApproved
    def makeInvalid(self,reason):
        self.invalidReason=reason
        match reason:
            case "DOCUMENT_MISMATCH":
                randKey=self.buttons[random.randint(0,9)].data[0]
                secondJsonDict=plswork.apiGenData()
                print(randKey,self.jsonDict[randKey])
                print(randKey,secondJsonDict[randKey])
                self.jsonDict[randKey]=secondJsonDict[randKey]
                self.updateButtons()
                print(self.jsonDict)


    def updateButtons(self):
        i=0
        for k,v in self.jsonDict.items():
            if i <= 9:
                self.buttons[i].data=[k,v, False]
                i += 1
            else:
                return

    async def regen(self):
        self.buttons = []
        self.jsonDict = await plswork.apiGenData()
        self.genButtons()
        self.updateButtons()
        i = 0        

    
    def approve(self):
        self.approved = True
        global GAME_STATE
        GAME_STATE = 'APPROVED_SCREEN'
        if self.approved:
            sound=pygame.mixer.Sound("assets\\music\\ding.mp3")
            sound.play()
            GAME_STATE="MAIN_MENU"
        

    
    def deny(self):
        self.approved = False
        
    def renderToScreen(self):
        #renders id to screen
        
        textDims=[self.x,self.y]
        
        bg=pygame.image.load(self.bgPath)
        bg=pygame.transform.scale(bg,(self.dims[2],self.dims[3]))
        self.surface.blit(bg,self.dims)
        font=pygame.font.Font(self.font,self.font_size)
   
        for button in self.buttons:
            if button.data[2]:
                fontColor = (255, 0, 0)
            else:
                fontColor= (0,0, 0)
            
            #button.docrender()
            text=str(button.data[0])+": "+str(button.data[1])         
            text=font.render(text,True,fontColor,None)
            textSize=(self.w/2,self.h/len(self.jsonDict)/2)

            text=pygame.transform.scale(text,textSize)
            self.surface.blit(text,textDims)
            textDims[1]+=self.gap
            
            button.handleClick()