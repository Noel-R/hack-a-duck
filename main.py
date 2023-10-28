import pygame
from pygame.locals import QUIT, KEYDOWN, K_RETURN

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# hgjuhhyh

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Credit Check Chronicles Lite')
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
        self.state = 'MAIN_MENU'

    def main_menu(self):
        self.screen.fill(BLACK)
        text = self.font.render('Main Menu - Press Enter to Start', True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        pygame.display.flip()

    def game_screen(self):
        self.screen.fill(BLACK)
        text = self.font.render('Main Game Screen', True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        pygame.display.flip()

    def stats_screen(self):
        self.screen.fill(BLACK)
        text = self.font.render('Day End Stats', True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        pygame.display.flip()

    def game_over(self):
        self.screen.fill(BLACK)
        text = self.font.render('Game Over', True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2))
        pygame.display.flip()

    def game_win(self):
        self.screen.fill(BLACK)
        text = self.font.render('You Win!', True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2))
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN and event.key == K_RETURN:
                    if self.state == 'MAIN_MENU':
                        self.state = 'GAME_SCREEN'
                    elif self.state == 'GAME_SCREEN':
                        self.state = 'STATS_SCREEN'
                    elif self.state == 'STATS_SCREEN':
                        self.state = 'GAME_OVER'
                    elif self.state == 'GAME_OVER':
                        self.state = 'GAME_WIN'
                    elif self.state == 'GAME_WIN':
                        running = False

            if self.state == 'MAIN_MENU':
                self.main_menu()
            elif self.state == 'GAME_SCREEN':
                self.game_screen()
            elif self.state == 'STATS_SCREEN':
                self.stats_screen()
            elif self.state == 'GAME_OVER':
                self.game_over()
            elif self.state == 'GAME_WIN':
                self.game_win()

            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()