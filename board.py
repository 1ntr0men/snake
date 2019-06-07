import pygame

pygame.init()
size = width, height = 900, 900
screen = pygame.display.set_mode(size)


class NotBoardCoord(Exception):
    pass


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]

        self.left = 0
        self.top = 0
        self.cell_size = 30

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
                    pygame.draw.rect(screen, (255, 0, 0),
                                     (self.left + i * self.cell_size, self.top + j * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                else:
                    pygame.draw.rect(screen, (0, 255, 0),
                                     (self.left + i * self.cell_size, self.top + j * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                # pygame.draw.rect(screen, (255, 255, 255),
                #                  (self.left + i * self.cell_size, self.top + j * self.cell_size,
                #                   self.cell_size, self.cell_size), 1)

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
