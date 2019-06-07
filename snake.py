from board import *
from random import randint
import sys

pygame.init()
size = width, height = 900, 900
screen = pygame.display.set_mode(size)


class Snake(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.length = 4
        self.x_start = 15
        self.y_start = 16
        self.spawn()
        self.direction = 3  # вправо-3 вниз-6 влево-9 вверх-12

    def spawn(self):
        for i in range(self.length):
            self.board[self.y_start][self.x_start - i] = i + 1
        self.board[3][3] = -1

    def drtn(self, direction):
        if direction + self.direction != 12 and direction + self.direction != 18:
            self.direction = direction

    def eat(self):
        self.board[randint(1, 29)][randint(1, 29)] = -1

    def death(self):
        sys.exit()

    def move(self):
        head = [15, 15]
        tail = [0, 0]
        l = False
        for i in range(len(self.board)):
            if 1 in self.board[i]:
                head[0] = self.board[i].index(1)
                head[1] = i
            if self.length in self.board[i]:
                tail[0] = self.board[i].index(self.length) - 1
                tail[1] = i
            for j in range(len(self.board[i])):
                if self.board[i][j] > 0:
                    self.board[i][j] += 1
        if self.direction == 3:
            if self.board[head[1] % 30][(head[0] + 1) % 30] == -1:
                self.eat()
                self.length += 1
                l = True
            elif self.board[(head[1]) % 30][(head[0] + 1) % 30] != 0:
                self.death()
            self.board[head[1] % 30][(head[0] + 1) % 30] = 1
        elif self.direction == 6:
            if self.board[(head[1] - 1) % 30][head[0] % 30] == -1:
                self.eat()
                self.length += 1
                l = True
            elif self.board[(head[1] - 1) % 30][head[0] % 30] != 0:
                self.death()
            self.board[(head[1] - 1) % 30][head[0] % 30] = 1
        elif self.direction == 9:
            if self.board[head[1] % 30][(head[0] - 1) % 30] == -1:
                self.eat()
                self.length += 1
                l = True
            elif self.board[head[1] % 30][(head[0] - 1) % 30] != 0:
                self.death()
            self.board[head[1] % 30][(head[0] - 1) % 30] = 1
        elif self.direction == 12:
            if self.board[(head[1] + 1) % 30][head[0] % 30] == -1:
                self.eat()
                self.length += 1
                l = True
            elif self.board[(head[1] + 1) % 30][head[0] % 30] != 0:
                self.death()
            self.board[(head[1] + 1) % 30][head[0] % 30] = 1
        if not l:
            self.board[tail[1]][tail[0] + 1] = 0


snk = Snake(30, 30)
running = True
fps = 10
r = False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 275:
                snk.drtn(3)
            elif event.key == 274:
                snk.drtn(12)
            elif event.key == 273:
                snk.drtn(6)
            elif event.key == 276:
                snk.drtn(9)
    screen.fill((0, 0, 0))
    snk.render()
    snk.move()
    clock.tick(fps)
    pygame.display.flip()
