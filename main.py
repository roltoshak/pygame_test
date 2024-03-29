import pygame
from game_logic import game_logic
import consts

pygame.init()

window = pygame.display.set_mode((consts.w, consts.h))
pygame.display.set_caption("game")

clock = pygame.time.Clock()
fps = 60

def main_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        game_logic(window)
        pygame.display.update()
        clock.tick(fps)

main_loop()