import pygame
import json
from document import Document
pygame.init()

surface=pygame.display.set_mode((500,500),0,32)
jsonDict = {"First Name": "John", "age": 30, "city": "New York","DOB":"20/24/2124","house":"obamatown, obamingham"}
d=Document(jsonDict,surface)
while 1:
    #surface.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    d.renderToScreen(surface,40,0,300,100)
    pygame.display.update()
