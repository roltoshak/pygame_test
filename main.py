import pygame
from game_logic import game_logic, spawn_bugs
import consts

pygame.init()

window = pygame.display.set_mode((consts.w, consts.h))
pygame.display.set_caption("game")

clock = pygame.time.Clock()
fps = 60

EVspawn_bugs = pygame.USEREVENT + 0
pygame.time.set_timer(EVspawn_bugs, 1000)

def main_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == spawn_bugs:
                spawn_bugs()
        game_logic(window)
        pygame.display.update()
        clock.tick(fps)

main_loop()