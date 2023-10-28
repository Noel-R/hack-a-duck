import pygame
import json
from document import Document
from button import Button
pygame.init()

def func():
    print("ahh")

surface=pygame.display.set_mode((500,500),0,32)
b=Button(surface,50,50,200,200,"button",(255,255,0),imgPath="C:\\Users\\george\\Documents\\anything\\assets\\images\\button\\button1.png",leftclickFunc=func)

while 1:
    #surface.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    b.render()
    x,y=pygame.mouse.get_pos()
    btn=pygame.mouse.get_pressed()
    pygame.display.update()

    

