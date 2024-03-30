import pygame
import cv2
import numpy as np
import consts
import random
import math
import asyncio

cam = cv2.VideoCapture(0)

w, h = consts.w, consts.h
speed = 2
radX = consts.sizeW / 2
radY = consts.sizeH / 2

bugs_list = pygame.sprite.Group()
zone = pygame.Rect(0, 0, w, h)

class Bug(pygame.sprite.Sprite):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.is_rotate = False
        self.x = random.randint(0, w)
        self.y = random.randint(0, h)
        self.angle = math.radians(random.randint(0, 360))
        self.image = pygame.transform.rotate(consts.bugs[self.id], self.angle)
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def rotate(self):
        self.steps -= 1
        if self.steps == 0:
            self.is_rotate = False
            self.angle = math.radians(self.angle)
            return
        self.angle = (self.angle + 30 * self.turn)%360
        if self.angle < 0:
            self.angle = 360 - self.angle
        self.image = pygame.transform.rotate(consts.bugs[self.id], self.angle)
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def update(self):
        if self.is_rotate:
            self.rotate()
            return
        x = self.x + math.cos(self.angle) * 7
        y = self.y - math.sin(self.angle) * 7
        if not self.is_rotate and not zone.collidepoint(x, y):
            self.is_rotate = True
            self.steps = random.randint(1, 9)
            self.turn = random.choice((-1, 1))
            self.angle = math.degrees(self.angle)
            return
        self.x = x
        self.y = y
        
        self.rect.center = (self.x, self.y)

b = Bug(random.randint(0, 3))
bugs_list.add(b)

def spawn_bugs():
    global bugs_list
    b = Bug(random.randint(0, 3))
    bugs_list.add(b)

def killing_bugs():
    (x, y) = pygame.mouse.get_pos()
    for bug in bugs_list:
        if bug.rect.collidepoint(x, y):
            bug.kill()
            return


def game_logic(window):
    global bugs_list
    try:
        _, frame = cam.read()
    except: print('cam error')

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = np.rot90(img)
    img = pygame.surfarray.blit_array(window, img)

    bugs_list.update()
    bugs_list.draw(window)
