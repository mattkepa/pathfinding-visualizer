import pygame
from node import Node


class AppConfig:
    """
    Configuration of app's information and constants

    :param size: int - width and height of program's window in pixels
    """

    # CONSTANTS
    ROWS = 50
    COLUMNS = 50

    def __init__(self, size):
        self.size = size
        self.rows = self.ROWS
        self.columns = self.COLUMNS
        self.set_grid(self.ROWS, self.COLUMNS, size)
        self.window = pygame.display.set_mode((size, size))
        pygame.display.set_caption('A* Pathfinding Algorithm Visualizer')

    def set_grid(self, rows, columns, size):
        grid = []
        n_size = size // rows
        for i in range(rows):
            grid.append([])
            for j in range(columns):
                node = Node(i, j, n_size, self.rows, self.columns)
                grid[i].append(node)
        self.grid = grid
