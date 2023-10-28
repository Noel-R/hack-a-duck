import pygame

class Button:
	x=None
	surface=None
	y=None
	h=None
	w=None
	text=""
	font=None
	textColor=None
	img=None
	textScale=0.5

	
	def onLeftClick(self):
		#abstract class uno
		pass
	def onRightClick(self):
		#abstract class dos
		pass

	def isColliding(self,x,y):
		if (x>=self.x and x<self.x+self.w) and (y>=self.y and y<self.y+self.h):
			return True
		return False

	def render(self):
		dims=pygame.Rect(self.x,self.y,self.w,self.h)
		img=pygame.transform.scale(self.img,(self.w,self.h))
		self.surface.blit(img,(self.x,self.y))
		text=self.font.render(self.text,False,self.textColor)
		text=pygame.transform.scale(text,(self.w*self.textScale,self.h*self.textScale))
		textX=self.x+(self.w/2)-text.get_width()/2
		textY=self.y+(self.h/2)-text.get_height()/2
		self.surface.blit(text,(textX,textY))


		
		
		
		
	def __init__(self,surface,x,y,w,h,text,textColor,imgPath,textScale=0.5,fontPath="assets\\fonts\\CONSOLA.TTF"):
		self.x=x
		self.y=y
		self.surface=surface
		self.h=h
		self.w=w
		self.img=pygame.image.load(imgPath)
		self.text=text
		self.textScale
		self.font=pygame.font.Font(fontPath)
		self.textColor=textColor


