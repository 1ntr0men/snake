import pygame
from random import randint
from board import *
import sys

r = 0
g = 0
b = 0
clock = pygame.time.Clock()
fps = 30


def terminate():
    sys.exit()


class Button:
    def __init__(self, x, y, h, w, text):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.text = text

    def draw(self):
        font_size = 60
        pygame.draw.rect(screen, (255, 255, 255), ((self.x, self.y), (self.w, self.h)), 1)
        font = pygame.font.Font(None, font_size)
        text = font.render(self.text, False, (0, 0, 0))
        # screen.blit(text, [self.x + abs((self.w - font_size * len(self.text)) // 2),
        #                    self.y + (self.h - font_size) // 2])
        # screen.blit(text, [self.x, self.y])
        screen.blit(text, [self.x + font_size, self.y + (self.h - font_size) // 2])

    def click(self, coordinats):
        if self.x <= coordinats[0] <= self.x + self.w and self.y + self.h >= coordinats[1] >= self.y:
            return True
        return False


def color_drift():
    global r, g, b
    if r == 255:
        r -= randint(1, 51) * 5
    elif g == 255:
        g -= randint(1, 51) * 5
    elif b == 255:
        b -= randint(1, 51) * 5
    else:
        random = randint(0, 3)
        if random == 0:
            r += 5
        elif random == 1:
            g += 5
        else:
            b += 5


def start_menu():
    play = Button(200, 150, 120, 200, "play")
    levels = Button(200, 290, 120, 200, "levels")
    exit = Button(200, 430, 120, 200, "exit")
    global r, g, b
    while True:
        play.draw()
        levels.draw()
        exit.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play.click(event.pos):
                    return
                elif levels.click(event.pos):
                    pass
                elif exit.click(event.pos):
                    terminate()
        pygame.display.flip()
        screen.fill((r, g, b))
        color_drift()
        clock.tick(fps)
