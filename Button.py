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
	rightClickFunc=None
	leftClickFunc=None
	data=None
	lcArgs=None
	rcArgs=None

	def handleClick(self):
		x,y=pygame.mouse.get_pos()
		btn=pygame.mouse.get_pressed()
		if self.isColliding(x,y):
			if btn[0]:
				self.onLeftClick()
			if btn[1]:
				self.onRightClick()
	def onLeftClick(self):
		if self.leftClickFunc!=None:
			if self.lcArgs==None:
				self.leftClickFunc()
			else:
				self.leftClickFunc(self.lcArgs)
	def onRightClick(self):
		if self.rightClickFunc!=None:
			if self.rcArgs==None:
				self.rightClickFunc()
			else:
				self.rightClickFunc(self.rcArgs)

	def isColliding(self,x,y):
		#checks for collision, use before calling onleftclick/onrightclick
		if (x>=self.x and x<self.x+self.w) and (y>=self.y and y<self.y+self.h):
			return True
		return False
	def debugRender(self):
		
		rect=pygame.draw.rect(self.surface,(0,0,0),(self.x,self.y,self.w,self.h))
		#self.surface.blit(rect,(dims.x,dims.y))
		

	def render(self):
		if self.doRender:
			dims=pygame.Rect(self.x,self.y,self.w,self.h)
			img=pygame.transform.scale(self.img,(self.w,self.h))
			self.surface.blit(img,(self.x,self.y))
			text=self.font.render(self.text,False,self.textColor)
			text=pygame.transform.scale(text,(self.w*self.textScale,self.h*self.textScale))
			textX=self.x+(self.w/2)-text.get_width()/2
			textY=self.y+(self.h/2)-text.get_height()/2
			self.surface.blit(text,(textX,textY))
		
		
	def __init__(self,surface,x,y,w,h,text,textColor,imgPath,leftclickFunc=None,rightClickFunc=None,textScale=0.5,fontPath="assets\\fonts\\CONSOLA.TTF",doRender=True,data=None,lcArgs=None,rcArgs=None):
		self.x=x
		self.y=y
		self.lcArgs=lcArgs
		self.rcArgs=rcArgs
		self.doRender=doRender
		self.surface=surface
		self.h=h
		self.w=w
		self.data=data
		if imgPath!=None:
			self.img=pygame.image.load(imgPath)
		self.text=text
		self.textScale
		self.font=pygame.font.Font(fontPath)
		self.textColor=textColor
		self.rightClickFunc=rightClickFunc
		self.leftClickFunc=leftclickFunc


