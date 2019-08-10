import pygame

pygame.init()
size = width, height = 600, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Змейка")


class NotBoardCoord(Exception):
    pass


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # self.board[0][0] = -2
        self.left = 0
        self.top = 0
        self.cell_size = 20

    def reader(self, text):
        self.board = text

    def level_get(self, n):
        name = str("level" + n)
        with open(name, "r") as l:
            return l.read().split("\n")

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.board[j][i] == 0:
                    pygame.draw.rect(screen, (0, 0, 0),
                                     (self.left + i * self.cell_size, self.top + j * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                elif self.board[j][i] == -1:
                    pygame.draw.circle(screen, (255, 0, 0),
                                       (i * self.cell_size + self.cell_size // 2,
                                        j * self.cell_size + self.cell_size // 2),
                                       self.cell_size // 2)
                elif self.board[j][i] == -2:
                    pygame.draw.rect(screen, (222, 163, 100),
                                     (self.left + i * self.cell_size, self.top + j * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                    pygame.draw.line(screen, (0, 0, 0),
                                     [i * self.cell_size,
                                      j * self.cell_size],
                                     [self.cell_size + i * self.cell_size,
                                      self.cell_size + j * self.cell_size], 3)
                    pygame.draw.line(screen, (0, 0, 0),
                                     [self.cell_size + i * self.cell_size,
                                      j * self.cell_size],
                                     [i * self.cell_size,
                                      self.cell_size + j * self.cell_size], 3)
                elif self.board[j][i] == 1.3:  # скин вправо
                    pygame.draw.rect(screen, (0, 255, 0),
                                     (self.left + i * self.cell_size, self.top + j * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                    pygame.draw.rect(screen, (0, 0, 0),  # глаз верхний
                                     (self.left + i * self.cell_size + 3, self.top + j * self.cell_size + 2,
                                      5, 5), 0)
                    pygame.draw.rect(screen, (0, 0, 0),  # глаз нижний
                                     (self.left + i * self.cell_size + 3, self.top + j * self.cell_size + 13,
                                      5, 5), 0)
                elif self.board[j][i] == 1.9:  # скин влево
                    pygame.draw.rect(screen, (0, 255, 0),
                                     (self.left + i * self.cell_size, self.top + j * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                    pygame.draw.rect(screen, (0, 0, 0),  # глаз верхний
                                     (self.left + i * self.cell_size + 3, self.top + j * self.cell_size + 2,
                                      5, 5), 0)
                    pygame.draw.rect(screen, (0, 0, 0),  # глаз нижний
                                     (self.left + i * self.cell_size + 3, self.top + j * self.cell_size + 13,
                                      5, 5), 0)
                elif self.board[j][i] == 1.12:  # скин вверх
                    pygame.draw.rect(screen, (0, 255, 0),
                                     (self.left + i * self.cell_size, self.top + j * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                    pygame.draw.rect(screen, (0, 0, 0),  # глаз левый
                                     (self.left + i * self.cell_size + 2, self.top + j * self.cell_size + 12,
                                      5, 5), 0)
                    pygame.draw.rect(screen, (0, 0, 0),  # глаз правый
                                     (self.left + i * self.cell_size + 13, self.top + j * self.cell_size + 12,
                                      5, 5), 0)
                elif self.board[j][i] == 1.6:  # скин вниз
                    pygame.draw.rect(screen, (0, 255, 0),
                                     (self.left + i * self.cell_size, self.top + j * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                    pygame.draw.rect(screen, (0, 0, 0),  # глаз левый
                                     (self.left + i * self.cell_size + 2, self.top + j * self.cell_size + 3,
                                      5, 5), 0)
                    pygame.draw.rect(screen, (0, 0, 0),  # глаз правый
                                     (self.left + i * self.cell_size + 13, self.top + j * self.cell_size + 3,
                                      5, 5), 0)
                else:
                    pygame.draw.rect(screen, (0, 255, 0),
                                     (self.left + i * self.cell_size, self.top + j * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                pygame.draw.rect(screen, (255, 255, 255), (0, 600, 600, 100), 1)

    def get_cell(self, mouse_pos):
        try:
            if mouse_pos[0] < self.left or mouse_pos[0] > self.left + self.cell_size * \
                    self.width or mouse_pos[1] < self.left or mouse_pos[1] > self.top + self.cell_size * self.height:
                raise NotBoardCoord
            x = (mouse_pos[0] - self.left) // self.cell_size + 1
            y = (mouse_pos[1] - self.top) // self.cell_size + 1
            return x, y
        except NotBoardCoord:
            print("Вне поля")

    def on_click(self, cell_coords):
        try:
            if self.board[cell_coords[1] - 1][cell_coords[0] - 1] == 0:
                self.board[cell_coords[1] - 1][cell_coords[0] - 1] = 1
            elif self.board[cell_coords[1] - 1][cell_coords[0] - 1] == 1:
                self.board[cell_coords[1] - 1][cell_coords[0] - 1] = 0
        except TypeError:
            pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
