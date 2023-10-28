import pygame

class Button:
	x=None
	y=None
	h=None
	w=None
	text=""

	def render(self):
		rect=pygame.Rect(self.x,self.y,self.w,self.h)
		
	def __init__(self,x,y,w,h,text):
		self.x=x
		self.y=y
		self.h=h
		self.w=w
		self.text=text

