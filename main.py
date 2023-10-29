#main.py
import pygame
from pygame.locals import *
import json
import time
from Button import Button
from document import Document
from theactualgameforrealthistime import ThePartWhereWeScamPoorPeople


# Initialize pygame
pygame.init()

# global state
global GAME_STATE
GAME_STATE = 'MAIN_MENU'

# Constants
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700

class GuideBook:
    clickable = []
    bg = None
    surface = None
    backButton = None
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.Font("assets/fonts/CONSOLA.TTF", 15)
        self.bg = pygame.image.load("assets\\images\\ccc-guidebook-bckg.png")
        self.bg = pygame.transform.scale(self.bg, (self.surface.get_width(), self.surface.get_height()))
        self.backButton = Button(surface, surface.get_width() / 2 - 100, surface.get_height() - 100, 200, 100, "Back", (255, 255, 255), "assets\\images\\button\\menubutton1.png", self.back)

    def back(self):
        global GAME_STATE
        GAME_STATE = 'MAIN_MENU'

    def text(self, text, x, y):
        self.surface.blit(self.font.render(text, True, (15, 15, 15)), (x, y))

    def loop(self):
        self.surface.blit(self.bg, (0, 0))
        self.text("Welcome to Credit Check Chronicles!", self.surface.get_width()/2 - 180, self.surface.get_height()/4 - 30)
        self.text("As an officer at Capital One, your role is to approve or deny credit loans based on credit scores, risk scores, and transaction histories.", 85, self.surface.get_height()/4)
        self.text("To play:", 85, self.surface.get_height()/4 + 30)
        self.text("Each character will approach with a story or dialogue. Use this information along with their provided documents to make informed decisions.", 85, self.surface.get_height()/4 + 60)
        self.text("At the end of each day, you'll be presented with statistics on your performance, decisions, and any potential consequences of your actions.", 85, self.surface.get_height()/4 + 90)
        self.text("If you make too many wrong decisions, the game ends. Aim to make accurate decisions and maintain your integrity for the best outcome.", 85, self.surface.get_height()/4 + 120)
        self.text("Example discrepancy is if the character tells you their email is haha@gmail.com but it's actually hahaha@gmail.com", 85, self.surface.get_height()/4 + 150)
        self.backButton.render()
        self.backButton.handleClick()
        for button in self.clickable:
            button.render()
            button.handleClick()

class MainMenu:
    clickable = []
    bg = None
    logo = None
    surface = None
    logoY = 0
    logoX = 0
    logoDims = None
    logoPos = None


    def startGame(self):
        global GAME_STATE
        GAME_STATE = 'GAME_SCREEN'

    def openGuidebook(self):
        global GAME_STATE
        GAME_STATE = 'GUIDEBOOK'

    def loop(self):
        self.surface.blit(self.bg, (0, 0))
        if (self.logoY < 0):
            self.logoY += 1
        self.surface.blit(self.logo, (self.logoX, self.logoY))
        for button in self.clickable:
            button.render()
            button.handleClick()

    def __init__(self, surface):
        mus=pygame.mixer_music.load("assets\\music\\epic.mp3")
        pygame.mixer_music.play(-1)
        self.surface = surface
        self.logo = pygame.image.load("assets\\images\\main menu\\logo.png")
        self.logoDims = [self.surface.get_width() / 4, self.surface.get_height() / 4]
        self.logo = pygame.transform.scale(self.logo, self.logoDims)
        self.logoY = -self.logoDims[1]
        self.logoX = self.surface.get_width() / 2 - self.logoDims[0] / 2
        self.bg = pygame.image.load("assets\\images\\main-menu.png")

        buttonWidth = surface.get_width() / 3
        buttonHeight = surface.get_height() / 8
        margin = buttonHeight / 2
        buttonX = (self.surface.get_width() / 2) - buttonWidth / 2
        buttonY = surface.get_height() * 0.4
        self.clickable.append(Button(surface, buttonX, buttonY, buttonWidth, buttonHeight, "Start Game", (255, 255, 255), "assets\\images\\button\\menuButton1.png", self.startGame))
        self.clickable.append(Button(surface, buttonX, buttonY + buttonHeight + margin, buttonWidth, buttonHeight, "Guidebook", (255, 255, 255), "assets\\images\\button\\menuButton1.png", self.openGuidebook))

class Game:
    clickables=[]
    menu=None
    game = None
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Credit Check Chronicles')
        self.clock = pygame.time.Clock()
        self.menu=MainMenu(self.screen)

    def game_screen(self):
        self.game = ThePartWhereWeScamPoorPeople(self.screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        with open("assets/character_info.json") as json_file:
            char_info = json.load(json_file)
        self.game.new_character("assets/images/upper-man.png", char_info, "assets/character_prov_docs.json")
        
        self.game.game_screen()
        
        self.game.loop()

    def approved_screen(self):
        timer = 0
        self.clock.tick(60)
        while True:
            self.screen.fill((255,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == self.TICK_SECOND:
                    timer += 1
                    if timer == 5:
                        global GAME_STATE
                        GAME_STATE = 'GAME_SCREEN'
            
            pygame.display.update()

    def guidebook(self):
        guidebook = GuideBook(self.screen)
        guidebook.loop()

    def run(self):
        running = True
        while running:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            if GAME_STATE == 'GAME_SCREEN':
                self.game_screen()
            if GAME_STATE == 'APPROVED_SCREEN':
                self.approved_screen()
            if GAME_STATE == 'DENIED_SCREEN':
                self.denied_screen()
            if GAME_STATE == 'MAIN_MENU':
                self.menu.loop()
            if GAME_STATE == 'GUIDEBOOK':
                self.guidebook()

            self.clock.tick(60)
            pygame.display.update()
        
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()