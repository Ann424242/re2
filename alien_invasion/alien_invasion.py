import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bg_color = (230, 230, 230)
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()
run_game()