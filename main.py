import pygame
from pygame.locals import QUIT, KEYDOWN, K_RETURN
from document import Document
from Database import DB

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Colors
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


class Game:
    def __init__(self, character_image):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Credit Check Chronicles')
        self.font = pygame.font.Font("assets/fonts/CONSOLA.TTF", 20)
        self.clock = pygame.time.Clock()
        self.state = 'GAME_SCREEN'
        self.character_image = pygame.image.load('assets/images/upper-man.png')

    def new_character(self, character_image, character_info):
        self.character_image = pygame.image.load(character_image)
        self.id = Document(character_info, self.screen)

    def game_screen(self):
        self.screen.fill(BLACK)

        # Left top section for character image and dialogue
        self.screen.blit(pygame.transform.scale(self.character_image, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/2))), (0, 0))

        dialogue = self.font.render("Character Dialogue Here", True, WHITE)
        self.screen.blit(dialogue, (30, SCREEN_HEIGHT/4))

        # Middle top section for documents character provides
        pygame.draw.rect(self.screen, GRAY, (SCREEN_WIDTH/3, 0, SCREEN_WIDTH/3, SCREEN_HEIGHT/2))
        text = self.font.render('Documents: Transactions Character Provides', True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH/3 + 10, 20))

        # Right top section for guidebook
        pygame.draw.rect(self.screen, GRAY, (2*SCREEN_WIDTH/3, 0, SCREEN_WIDTH/3, SCREEN_HEIGHT/2))
        text = self.font.render('Documents: Guide Book', True, WHITE)
        self.screen.blit(text, (2*SCREEN_WIDTH/3 + 10, 20))

        # Left bottom section for API account info
        self.id.renderToScreen(self.screen, 0, SCREEN_HEIGHT/2, SCREEN_WIDTH/3, SCREEN_HEIGHT/2, 20)

        # Middle bottom section for API recent transactions
        pygame.draw.rect(self.screen, GRAY, (SCREEN_WIDTH/3, SCREEN_HEIGHT/2, SCREEN_WIDTH/3, SCREEN_HEIGHT/2))
        text = self.font.render('Documents: API Recent Transactions', True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH/3 + 10, SCREEN_HEIGHT/2 + 20))

        # Right bottom section for system recommendation and decision
        pygame.draw.rect(self.screen, GRAY, (2*SCREEN_WIDTH/3, SCREEN_HEIGHT/2, SCREEN_WIDTH/6, SCREEN_HEIGHT/2))
        pygame.draw.rect(self.screen, GREEN, (2*SCREEN_WIDTH/3 + SCREEN_WIDTH/6, SCREEN_HEIGHT/2, SCREEN_WIDTH/6, SCREEN_HEIGHT/2))
        text1 = self.font.render('System Recommendation', True, WHITE)
        text2 = self.font.render('Approve/Deny/Take Bribe?', True, WHITE)
        self.screen.blit(text1, (2*SCREEN_WIDTH/3 + 10, SCREEN_HEIGHT/2 + 20))
        self.screen.blit(text2, (2*SCREEN_WIDTH/3 + SCREEN_WIDTH/6 + 10, SCREEN_HEIGHT/2 + 20))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            if self.state == 'GAME_SCREEN':
                self.game_screen()

            self.clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    game = Game('assets/images/upper-man.png')
    game.new_character('assets/images/upper-man.png', {"First Name": "John", "age": 30, "city": "New York","DOB":"20/24/2124","house":"obamatown, obamingham"})
    game.run()