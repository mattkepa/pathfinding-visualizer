import pygame


# CONSTANTS
COLORS = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'gray': (22, 22, 22),
    'green': (146, 172, 44),
    'red': (227, 6, 19),
    'gold': (248, 196, 9),
    'teal': (48, 176, 199),
    'purple': (93, 47, 136)
}



def draw(surface, grid, rows, columns, size):
    """
    Draws grid lines and nodes on the screen and updates it

    :param surface: Surface - pygame surface object
    :param rows: int - number of rows of grid
    :param columns: int - number of columns of grid
    :param size: int - size of the width and height of screen in pixels
    """
    surface.fill(COLORS['white'])

    for row in grid:
        for node in row:
            node.draw(surface)

    draw_grid(surface, rows, columns, size)

    pygame.display.update()


def draw_grid(surface, rows, columns, size):
    """
    Draws grid lines on the screen

    :param surface: Surface - pygame surface object
    :param rows: int - number of rows of grid
    :param columns: int - number of columns of grid
    :param size: int - size of the width and height of screen in pixels
    """
    n_size = size // rows #set size of node based on window size and number of rows/columns
    for i in range(rows):
        pygame.draw.line(surface, COLORS['gray'], (0, i*n_size), (size, i*n_size))
    for j in range(columns):
        pygame.draw.line(surface, COLORS['gray'], (j*n_size, 0), (j*n_size, size))


def get_clicked_pos(pos, rows, columns, size):
    """
    Returns tuple of row and column clicked node's

    :param pos: tuple[int, int] - cursor position when click occured
    :param rows: int - number of rows of grid
    :param columns: int - number of columns of grid
    :param size: int - size of the width and height of screen in pixels
    """
    n_size = size // rows #set size of node based on window size and number of rows/columns
    y, x = pos

    row =  y // n_size
    col = x // n_size
    return (row, col)