import pygame
from pygame.locals import QUIT, KEYDOWN, K_RETURN
import json
import time
from document import Document
from Database import DB

# Colors
WHITE = (255, 255, 255)
RED = (157, 41, 51)    # Muted, dark red
BLACK = (15, 15, 15)   # Almost-black, off-black
GREEN = (89, 139, 39)  # Muted green
GRAY = (120, 120, 120) # Neutral gray
BROWN = (103, 58, 43)  # Earthy brown for potential other elements
TAN = (211, 186, 141)  # Light beige/tan for backgrounds or text
DARK_GREEN = (32, 50, 36)  # Darker green, potential for other UI elements

dbContext = DB("./Game.db")

class ThePartWhereWeScamPoorPeople:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.Font("assets/fonts/CONSOLA.TTF", 20)
        self.dialogues = []
        self.last_dialogue_time = time.time()
        self.dialogue_interval = 3  # seconds between dialogues
        self.max_dialogues_on_screen = 4  # adjust as needed

    def add_dialogue(self, dialogue):
        self.dialogues.append(dialogue)
        # Trim dialogues list if it's too long
        while len(self.dialogues) > self.max_dialogues_on_screen:
            self.dialogues.pop(0)

    def new_character(self, character_image, character_info, char_prov_docs):
        self.character_image = pygame.image.load(character_image)
        self.id = Document(character_info, self.screen)
        #self.char_prov_docs = Document(char_prov_docs, self.screen)
        #self.recent_transactions = Document(dbContext.getRecentTransactions(), self.screen)

    def get_guidebook(self):
        with open("assets/guidebook.json") as json_file:
            guide_info = json.load(json_file)
        self.guidebook = Document(guide_info, self.screen)

    def game_screen(self):
        self.screen.fill(BLACK)

        # Left top section for character image and dialogue
        self.screen.blit(pygame.transform.scale(self.character_image, (int(self.screen_width/3), int(self.screen_height/2))), (0, 0))

        dialogue = self.font.render("Character Dialogue Here", True, WHITE)
        self.screen.blit(dialogue, (30, self.screen_height/4))

        # Left bottom section for API account info
        self.id.renderToScreen(self.screen, 0, self.screen_height/2, self.screen_width/3, self.screen_height/2, 20, "assets\\images\\capitol-one.png", BLACK, TAN)

        # Place the desk.png image in the rest of the screen space
        desk = pygame.image.load("assets/images/desk.png")
        desk = pygame.transform.scale(desk, (int(self.screen_width*2/3), int(self.screen_height)))
        self.screen.blit(desk, (int(self.screen_width/3), 0))

        # Check if it's time for a new dialogue
        current_time = time.time()
        if current_time - self.last_dialogue_time > self.dialogue_interval:
            self.add_dialogue("Random dialogue")  # replace with your dialogue logic
            self.last_dialogue_time = current_time

        # Render dialogues
        for idx, dialogue in enumerate(self.dialogues[-self.max_dialogues_on_screen:]):
            dialogue_surface = self.font.render(dialogue, True, WHITE)
            y_position = self.screen_height/2 - (self.max_dialogues_on_screen - idx) * self.font.get_height()
            self.screen.blit(dialogue_surface, (0, y_position))

        pygame.display.flip()