from board import *
from menu import *
from random import randint
import sys

pygame.init()
size = width, height = 600, 700
fps = 10
score = 0

with open("Cookie.txt", "r") as cookie:
    record = "".join(list(cookie.read().split("\n")[0])[7:])


def terminate():
    sys.exit()


def get_record():
    global score, record
    record_text = ["Рекорд", str(record)]
    score_text = ["Счет", str(score)]

    font = pygame.font.Font(None, 32)

    for i in range(2):
        string_rendered = font.render(record_text[i], 1, pygame.Color('White'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 610
        intro_rect.x = 100 * i + 10
        screen.blit(string_rendered, intro_rect)

    for i in range(2):
        string_rendered = font.render(score_text[i], 1, pygame.Color('White'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 640
        intro_rect.x = 100 * i + 10
        screen.blit(string_rendered, intro_rect)


class Snake(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.length = 4
        self.x_start = 15
        self.y_start = 16
        self.spawn()
        self.direction = 3  # вправо-3 вниз-6 влево-9 вверх-12

    def spawn(self):
        for i in range(1, self.length):
            self.board[self.y_start][self.x_start - i] = i + 1
        self.board[self.y_start][self.x_start] = 1.1
        self.spawn_eat()

    def drtn(self, direction):  # проверка направления
        if direction + self.direction != 12 and direction + self.direction != 18:
            self.direction = direction

    def spawn_eat(self):
        l1 = randint(1, 29)
        l2 = randint(1, 29)
        while self.board[l1][l2] != 0:
            l1 = randint(1, 29)
            l2 = randint(1, 29)
        self.board[l1][l2] = -1

    def move(self):
        head = [15, 15]
        tail = [0, 0]
        l = False  # переменная отвечает за разрешение на удаление последней клетки змейки
        global score

        for i in range(len(self.board)):  # создание головы и хвоста как переменных
            if 1.1 in self.board[i]:
                head[0] = self.board[i].index(1.1)
                head[1] = i
            elif 1.2 in self.board[i]:
                head[0] = self.board[i].index(1.2)
                head[1] = i
            if self.length in self.board[i]:  # удлиннение змейки
                tail[0] = self.board[i].index(self.length) - 1
                tail[1] = i
            for j in range(len(self.board[i])):
                if self.board[i][j] > 0:
                    self.board[i][j] += 1
                    self.board[i][j] = int(self.board[i][j])

        if self.direction == 3:  # вправо
            if self.board[head[1] % 30][(head[0] + 1) % 30] == -1:
                self.spawn_eat()
                self.length += 1
                score += 10
                self.check_score(score)
                self.check_record()
                l = True
            elif self.board[(head[1]) % 30][(head[0] + 1) % 30] != 0:
                terminate()
            self.board[head[1] % 30][(head[0] + 1) % 30] = 1.1

        elif self.direction == 6:  # вниз
            if self.board[(head[1] - 1) % 30][head[0] % 30] == -1:
                self.spawn_eat()
                self.length += 1
                score += 10
                self.check_score(score)
                self.check_record()
                l = True
            elif self.board[(head[1] - 1) % 30][head[0] % 30] != 0:
                terminate()
            self.board[(head[1] - 1) % 30][head[0] % 30] = 1.2

        elif self.direction == 9:  # влево
            if self.board[head[1] % 30][(head[0] - 1) % 30] == -1:
                self.spawn_eat()
                self.length += 1
                score += 10
                self.check_score(score)
                self.check_record()
                l = True
            elif self.board[head[1] % 30][(head[0] - 1) % 30] != 0:
                terminate()
            self.board[head[1] % 30][(head[0] - 1) % 30] = 1.1

        elif self.direction == 12:  # вверх
            if self.board[(head[1] + 1) % 30][head[0] % 30] == -1:
                self.spawn_eat()
                self.length += 1
                score += 10
                self.check_score(score)
                self.check_record()
                l = True
            elif self.board[(head[1] + 1) % 30][head[0] % 30] != 0:
                terminate()
            self.board[(head[1] + 1) % 30][head[0] % 30] = 1.2
        if not l:
            self.board[tail[1]][tail[0] + 1] = 0

    def check_score(self, n):
        global fps
        if n % 100 == 0:
            fps += 1
        self.check_record()

    def check_record(self):
        global score, record
        if int(score) >= int(record):
            with open("cookie.txt", "w") as cookie:
                cookie.write("Record " + str(score))
            record = score


snk = Snake(30, 30)
running = True
# r = False
clock = pygame.time.Clock()
start_menu()
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
    snk.move()
    get_record()
    snk.render()
    clock.tick(fps)
    pygame.display.flip()
