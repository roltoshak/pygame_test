import pygame
import cv2
import numpy as np

pygame.init()

w = 640
h = 480
sizeW = 100
sizeH = 80

pygame.display.set_mode((w, h))

bugs = []

for i in range(4):
    a = pygame.image.load(f"./images/{i}.jpg").convert_alpha()
    a = pygame.transform.scale(a, (sizeW, sizeH))
    bugs.append(a)


pygame.quit()