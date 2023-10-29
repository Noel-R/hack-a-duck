import pygame
from pygame.locals import QUIT, KEYDOWN, K_RETURN
import json
import time
from button import Button
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
        print("Starting game")

    def loop(self):
        self.surface.blit(self.bg, (0, 0))
        if (self.logoY < 0):
            self.logoY += 1
        self.surface.blit(self.logo, (self.logoX, self.logoY))
        for button in self.clickable:
            button.render()
            button.handleClick()

    def __init__(self, surface):
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
        self.clickable.append(Button(surface, buttonX, buttonY + buttonHeight + margin, buttonWidth, buttonHeight, "PLACEHOLDER", (255, 255, 255), "assets\\images\\button\\menuButton1.png", self.startGame))

class Game:
    clickables=[]
    menu=None
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Credit Check Chronicles')
        self.clock = pygame.time.Clock()
        self.menu=MainMenu(self.screen)

    def game_screen(self):
        game = ThePartWhereWeScamPoorPeople(self.screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        with open("assets/character_info.json") as json_file:
            char_info = json.load(json_file)
        game.new_character("assets/images/upper-man.png", char_info, "assets/character_prov_docs.json")
        game.get_guidebook()
        game.game_screen()

    def run(self):
        running = True
        while running:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            if GAME_STATE == 'GAME_SCREEN':
                self.game_screen()
            if GAME_STATE == 'MAIN_MENU':
                self.menu.loop()

            self.clock.tick(60)
            pygame.display.update()
        
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()