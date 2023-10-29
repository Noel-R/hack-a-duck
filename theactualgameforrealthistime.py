import pygame
from pygame.locals import *
import json
import time
from document import Document
from plswork import apiGenData

# Colors
WHITE = (255, 255, 255)
RED = (157, 41, 51)    # Muted, dark red
BLACK = (15, 15, 15)   # Almost-black, off-black
GREEN = (89, 139, 39)  # Muted green
GRAY = (120, 120, 120) # Neutral gray
BROWN = (103, 58, 43)  # Earthy brown for potential other elements
TAN = (211, 186, 141)  # Light beige/tan for backgrounds or text
DARK_GREEN = (32, 50, 36)  # Darker green, potential for other UI elements

class ThePartWhereWeScamPoorPeople:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.Font("assets/fonts/CONSOLA.TTF", 20)
        self.dialogues = []
        self.line_num = 0
        with open("assets/example-dialogue.txt") as f: self.total_dialogues = f.readlines()
        self.last_dialogue_time = time.time()
        self.dialogue_interval = 1.5
        self.max_dialogues_on_screen = 10
        self.timer = 0
        self.max_time = 120
        self.TICK_SECOND = pygame.USEREVENT + 1
        pygame.time.set_timer(self.TICK_SECOND, 1000)

    def add_dialogue(self, dialogue):
        self.dialogues.append(dialogue)
        self.line_num += 1
        # Trim dialogues list if it's too long
        while len(self.dialogues) > self.max_dialogues_on_screen:
            self.dialogues.pop(0)

    def check_dialogue(self):
        # Check if it's time for a new dialogue
        current_time = time.time()
        if current_time - self.last_dialogue_time > self.dialogue_interval:
            if not self.line_num >= len(self.total_dialogues): self.add_dialogue(self.total_dialogues[self.line_num])
            self.last_dialogue_time = current_time

    def render_dialogue(self):
        for idx, dialogue in enumerate(self.dialogues[-self.max_dialogues_on_screen:]):
            dialogue_surface = self.font.render(dialogue, True, WHITE)
            y_position = self.screen_height/2 - 100 - (self.max_dialogues_on_screen - idx) * self.font.get_height()
            if dialogue.startswith("You:"):
                self.screen.blit(dialogue_surface, (40, y_position))
            else:
                self.screen.blit(dialogue_surface, (0, y_position))

    def new_character(self, character_image, character_info, char_prov_docs):
        self.character_image = pygame.image.load(character_image)
        self.id = Document(apiGenData(), self.screen)
        self.compare= Document(apiGenData(),self.screen)
        #self.char_prov_docs = Document(char_prov_docs, self.screen)
        #self.recent_transactions = Document(dbContext.getRecentTransactions(), self.screen)

    def game_screen(self):
        self.screen.fill(BLACK)

        # Left top section for character image and dialogue
        self.screen.blit(pygame.transform.scale(self.character_image, (int(self.screen_width/3), int(self.screen_height/2))), (0, 0))

        # Place the desk.png image in the rest of the screen space
        desk = pygame.image.load("assets/images/desk.png")
        desk = pygame.transform.scale(desk, (int(self.screen_width*2/3), int(self.screen_height)))
        self.screen.blit(desk, (int(self.screen_width/3), 0))

        # Write dialogue
        dialogue = self.font.render("", True, WHITE)
        self.screen.blit(dialogue, (30, self.screen_height/4))

        # Left bottom section for API account info
        self.id.renderToScreen(self.screen, 0, self.screen_height/2, self.screen_width/3, self.screen_height/2, 20, "assets\\images\\capitol-one.png", BLACK)
        #self.compare.renderToScreen(self.screen, self.screen_width/2, self.screen_height/2, self.screen_width/3, self.screen_height/2, 20, "assets\\images\\capitol-one.png", BLACK)
        
        timer_font = pygame.font.Font("assets/fonts/CONSOLA.TTF", 80)
        timer_text = timer_font.render(str(self.timer + "/" + self.max_time), True, (0, 0, 0))
        self.screen.blit(timer_text, (self.screen_width - 100, 10))

        self.check_dialogue()
        self.render_dialogue()

        pygame.display.flip()

    def loop(self):
        running = True
        while running:
            self.game_screen()
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == self.TICK_SECOND:
                    self.timer += 1
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        running = False

        pygame.quit()