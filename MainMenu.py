#mainmenu.py
import pygame
from button import Button

class MainMenu:
	def startGame(self):
		print("hhhhhhh")
	def loop(self):
		self.surface.blit(self.bg,(0,0))
		if (self.logoY<0):
		   self.logoY+=1
		self.surface.blit(self.logo,(self.logoX,self.logoY))
		for button in self.clickable:
			button.render()
			button.handleClick()
			
	clickable=[]	
	bg=None
	logo=None
	surface=None
	logoY=0
	logoX=0
	logoDims=None
	logoPos=None
	def __init__(self,surface):
		self.surface=surface
		self.logo=pygame.image.load("C:\\Users\\george\\Documents\\anything\\assets\\images\\main menu\\logo.png")
		self.logoDims=[self.surface.get_width()/4,self.surface.get_height()/4]
		self.logo=pygame.transform.scale(self.logo,self.logoDims)
		self.logoY=-self.logoDims[1]
		self.logoX=self.surface.get_width()/2-self.logoDims[0]/2
		self.bg=pygame.image.load("C:\\Users\\george\\Documents\\anything\\assets\\images\\main-menu.png")
		buttonWidth=surface.get_width()/3
		buttonHeight=surface.get_height()/8
		print(buttonWidth)
		margin=buttonHeight/2
		buttonX=(self.surface.get_width()/2)-buttonWidth/2
		buttonY=surface.get_height()*0.4
		self.clickable.append(Button(surface,buttonX,buttonY,buttonWidth,buttonHeight,"Start Game",(255,255,255),"C:\\Users\\george\\Documents\\anything\\assets\\images\\button\\menuButton1.png",self.startGame))
		self.clickable.append(Button(surface,buttonX,buttonY++buttonHeight+margin,buttonWidth,buttonHeight,"PLACEHOLDER",(255,255,255),"C:\\Users\\george\\Documents\\anything\\assets\\images\\button\\menuButton1.png",self.startGame))
		
	