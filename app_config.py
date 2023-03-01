import pygame


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
        self.window = pygame.display.set_mode((size, size))
        pygame.display.set_caption('A* Pathfinding Algorithm Visualizer')
