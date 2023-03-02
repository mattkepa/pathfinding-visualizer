import pygame
from node import Node


class AppConfig:
    """
    Configuration of app's information and constants

    :param algo_name: str - name of searching algorithm
    :param algo_fn: function - pathfinder function implementation
    """

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 800
    ROWS = 50
    COLUMNS = 50

    def __init__(self, algo_name, algo_fn):
        self.size = self.HEIGHT
        self.rows = self.ROWS
        self.columns = self.COLUMNS
        self.set_grid(self.ROWS, self.COLUMNS, self.size)
        self.set_algorithm(algo_name, algo_fn)
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Pathfinding Algorithms Visualizer')

    def set_grid(self, rows, columns, size):
        grid = []
        n_size = size // rows
        for i in range(rows):
            grid.append([])
            for j in range(columns):
                node = Node(i, j, n_size, self.rows, self.columns)
                grid[i].append(node)
        self.grid = grid

    def set_algorithm(self, name, algo_fn):
        self.algo_name = name
        self.algorithm = algo_fn
