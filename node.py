import pygame
from utils import COLORS

class Node:
    """
    Represents single node in grid for A* Pathfinding

    :param row: int
    :param col: int
    :param size: int
    """
    def __init__(self, row, col, size, rows_total, columns_total):
        self.row = row
        self.col = col
        self.x = row * size
        self.y = col * size
        self.size = size
        self.color = COLORS['white']
        self.neighbors = []
        self.rows_total = rows_total
        self.columns_total = columns_total

    def get_pos(self):
        return (self.row, self.col)

    def is_open(self):
        return self.color == COLORS['green']

    def is_closed(self):
        return self.color == COLORS['red']

    def is_obstacle(self):
        return self.color == COLORS['black']

    def is_start(self):
        return self.color == COLORS['gold']

    def is_end(self):
        return self.color == COLORS['teal']

    def make_open(self):
        self.color = COLORS['green']

    def make_closed(self):
        self.color = COLORS['red']

    def make_obstacle(self):
        self.color = COLORS['black']

    def make_start(self):
        self.color = COLORS['gold']

    def make_end(self):
        self.color = COLORS['teal']

    def make_path(self):
        self.color = COLORS['purple']

    def reset(self):
        self.color = COLORS['white']

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

    def update_neighbors(self, grid):
        self.neighbors = []
        # check UP
        if self.row > 0 and not grid[self.row - 1][self.col].is_obstacle():
            self.neighbors.append(grid[self.row - 1][self.col])
        # check UP-RIGHT
        if self.row > 0 and self.col < self.columns_total - 1 and not grid[self.row - 1][self.col + 1].is_obstacle():
            self.neighbors.append(grid[self.row - 1][self.col + 1])
        # check RIGHT
        if self.col < self.columns_total - 1 and not grid[self.row][self.col + 1].is_obstacle():
            self.neighbors.append(grid[self.row][self.col + 1])
        # check BOTTOM-RIGHT
        if self.row < self.rows_total - 1 and self.col < self.columns_total - 1 and not grid[self.row + 1][self.col + 1].is_obstacle():
            self.neighbors.append(grid[self.row + 1][self.col + 1])
        # check BOTTOM
        if self.row < self.rows_total - 1 and not grid[self.row + 1][self.col].is_obstacle():
            self.neighbors.append(grid[self.row + 1][self.col])
        # check BOTTOM-LEFT
        if self.row < self.rows_total - 1 and self.col > 0 and not grid[self.row + 1][self.col - 1].is_obstacle():
            self.neighbors.append(grid[self.row + 1][self.col - 1])
        # check LEFT
        if self.col > 0 and not grid[self.row][self.col - 1].is_obstacle():
            self.neighbors.append(grid[self.row][self.col - 1])
        # check UP-LEFT
        if self.row > 0 and self.col > 0 and not grid[self.row - 1][self.col - 1].is_obstacle():
            self.neighbors.append(grid[self.row - 1][self.col - 1])
