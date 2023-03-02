import pygame
import math
import os
from random import getrandbits
from queue import PriorityQueue


# CONSTANTS
COLORS = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'gray': (22, 22, 22),
    'gray1': (142, 142, 147),
    'gray2': (199, 199, 204),
    'gray3': (242, 242, 247),
    'green': (146, 172, 44),
    'red': (227, 6, 19),
    'gold': (248, 196, 9),
    'teal': (48, 176, 199),
    'purple': (93, 47, 136)
}

CONTROLS = {
    'KEY_R': pygame.image.load(os.path.join('assets', 'img', 'key_icon_R.png')),
    'KEY_SPACE': pygame.image.load(os.path.join('assets', 'img', 'key_icon_SPACE.png')),
    'KEY_A': pygame.image.load(os.path.join('assets', 'img', 'key_icon_A.png')),
    'KEY_D': pygame.image.load(os.path.join('assets', 'img', 'key_icon_D.png')),
    'KEY_G': pygame.image.load(os.path.join('assets', 'img', 'key_icon_G.png')),
    'MOUSE_LEFT': pygame.image.load(os.path.join('assets', 'img', 'mouse_icon_LEFT.png')),
    'MOUSE_RIGHT': pygame.image.load(os.path.join('assets', 'img', 'mouse_icon_RIGHT.png'))
}



def draw(app):
    """
    Draws grid lines and nodes on the screen and updates it

    :param app: AppConfig - app configuration object with constants and methods
    """
    app.window.fill(COLORS['white'])

    for row in app.grid:
        for node in row:
            node.draw(app.window)

    draw_grid(app.window, app.rows, app.columns, app.size)
    draw_controls(app)

    pygame.display.update()


def draw_grid(surface, rows, columns, size):
    """
    Draws grid lines on the screen

    :param surface: Surface - pygame surface object
    :param rows: int - number of rows of grid
    :param columns: int - number of columns of grid
    :param grid_size: int - size of the width and height of grid in pixels
    """
    n_size = size // rows #set size of node based on window size and number of rows/columns
    for i in range(rows):
        pygame.draw.line(surface, COLORS['gray'], (0, i*n_size), (size, i*n_size))
    for j in range(columns):
        pygame.draw.line(surface, COLORS['gray'], (j*n_size, 0), (j*n_size, size))


def draw_controls(app):
    """
    Draws instruction for control program flow on the screen

    :param app: AppConfig - app configuration object with constants and methods
    """
    start_x = app.size + app.SIDE_PADDING

    # Background
    pygame.draw.rect(app.window, COLORS['gray3'], (app.size, 0, app.WIDTH - app.size, app.HEIGHT))
    pygame.draw.line(app.window, COLORS['gray2'], (app.size, 0), (app.size, app.HEIGHT), 2)
    # Title - Algorithm Name
    title = app.FONT_TITLE.render(app.algo_name, True, COLORS['gray'])
    app.window.blit(title, (start_x, app.TOP_PADDING))
    # Control - Set A* Algorithm
    app.window.blit(CONTROLS['KEY_A'], (start_x, 115))
    control_text = app.FONT_CONTROLS.render('A* Search', True, COLORS['gray1'])
    app.window.blit(control_text, (start_x + 55, 115 + 20 - control_text.get_height() // 2))
    # Control - Set Dijkstra's Algorithm
    app.window.blit(CONTROLS['KEY_D'], (start_x, 115 + 60))
    control_text = app.FONT_CONTROLS.render('Dijkstra\'s Search', True, COLORS['gray1'])
    app.window.blit(control_text, (start_x + 55, 115 + 60 + 20 - control_text.get_height() // 2))
    # Separator
    pygame.draw.line(app.window, COLORS['gray2'], (start_x, 235), (app.WIDTH - app.SIDE_PADDING, 235), 1)
    # Control - Set Point
    app.window.blit(CONTROLS['MOUSE_LEFT'], (start_x, 255))
    control_text = app.FONT_CONTROLS.render('Set point', True, COLORS['gray1'])
    app.window.blit(control_text, (start_x + 55, 255 + 20 - control_text.get_height() // 2))
    # Control - Unset Point
    app.window.blit(CONTROLS['MOUSE_RIGHT'], (start_x, 255 + 60))
    control_text = app.FONT_CONTROLS.render('Unset point', True, COLORS['gray1'])
    app.window.blit(control_text, (start_x + 55, 255 + 60 + 20 - control_text.get_height() // 2))
    # Control - Generate Maze
    app.window.blit(CONTROLS['KEY_G'], (start_x, 255 + 120))
    control_text = app.FONT_CONTROLS.render('Generate maze', True, COLORS['gray1'])
    app.window.blit(control_text, (start_x + 55, 255 + 120 + 20 - control_text.get_height() // 2))
    # Control - Reset Grid
    app.window.blit(CONTROLS['KEY_R'], (start_x, 255 + 180))
    control_text = app.FONT_CONTROLS.render('Reset', True, COLORS['gray1'])
    app.window.blit(control_text, (start_x + 55, 255 + 180 + 20 - control_text.get_height() // 2))
    # Control - Start Searching
    app.window.blit(CONTROLS['KEY_SPACE'], (start_x, 255 + 240))
    control_text = app.FONT_CONTROLS.render('Start searching', True, COLORS['gray1'])
    app.window.blit(control_text, (start_x + 95, 255 + 240 + 20 - control_text.get_height() // 2))


def get_clicked_pos(pos, rows, columns, size):
    """
    Returns tuple of row and column clicked node's

    :param pos: tuple[int, int] - cursor position when click occured
    :param rows: int - number of rows of grid
    :param columns: int - number of columns of grid
    :param grid_size: int - size of the width and height of grid in pixels
    """
    n_size = size // rows #set size of node based on grid size and number of rows/columns
    y, x = pos

    row =  y // n_size
    col = x // n_size
    return (row, col)


def generate_maze(grid, rows, columns):
    """
    Randomly generates obstacles to create imitation of a maze

    :param grid: list[list[Node]] - two dimensional list of Nodes objects
    :param rows: int - number of rows of grid
    :param columns: int - number of columns of grid
    """
    for i in range(rows):
        for j in range(columns):
            node = grid[i][j]
            # randomly choose true or false by generating one bit: 1 - True 0 - False
            obstacle = bool(getrandbits(1))
            if obstacle:
                node.make_obstacle()



def a_star_search(grid, start, end, draw_fn):
    """
    A* Pathfinding Algorithm implementation.
    Sets g and f score maps for all nodes in grid and traverse this grid based on these scores.
    Draws every step on the screen and at the end draw path

    :param grid: list[list[Node]] - two dimensional list of Nodes objects
    :param: start: Node - start node
    :param: end: Node - end node
    :param: draw_fn: function - reference to drawing function
    """

    # init g_score map with all nodes and their g_score (how far from start node they are)
    # at the beginning all have value of infinity
    g_score = { node: float('inf') for row in grid for node in row }
    # init f_score map with all nodes and their f_score (sum of g_score and h_score - how far from end node they are)
    # at the beginning all have value of infinity
    f_score = { node: float('inf') for row in grid for node in row }

    g_score[start] = 0
    f_score[start] = h(start.get_pos(), end.get_pos())

    order = 0 # keeps track when node was added to the queue
    from_map = {} # keeps track from which node current node is reached
    open_queue = PriorityQueue()
    open_queue.put((f_score[start], order, start))
    open_set = { start } # keeps track which nodes are in open_queue


    while not open_queue.empty():
        # adds the ability to close the program while searching for a path
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        # get node with the lowest f_score from the queue
        current = open_queue.get()[2]
        open_set.remove(current)

        # if current node is end node reconstruct and draw a path
        if current == end:
            reconstruct_path(from_map, current, draw_fn)
            start.make_start()
            end.make_end()
            return True

        for neighbor in current.neighbors:
            # d(current,neighbor) is distance from current to neighbor
            # tentative_g_score is the distance from start to the neighbor through current
            tentative_g_score = g_score[current] + d(current.get_pos(), neighbor.get_pos())
            if tentative_g_score < g_score[neighbor]:
                # this path to neighbor is so far the best so update it
                from_map[neighbor] = current
                # update f and g scores for neighbor node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor.get_pos(), end.get_pos())
                # add neighbor to open_queue if is not in it
                if neighbor not in open_set:
                    order += 1
                    open_queue.put((f_score[neighbor], order, neighbor))
                    open_set.add(neighbor)
                    neighbor.make_open()

        # draw nodes and after it change current node state for next drawing
        draw_fn()
        if current != start:
            current.make_closed()

    # open_queue is empty but end node was never reached
    return False


def reconstruct_path(from_map, current, draw_fn):
    """
    Traverse from_map created by pathfinding algorithm and draws path of nodes on the screen

    :param from_map: dict(Node: Node)
    :param current: Node - last reached node
    :param draw_fn: function - reference to drawing function
    """
    while current in from_map:
        current = from_map[current]
        current.make_path()
        draw_fn()


def h(curr_pos, end_pos):
    """
    Heuristic function to help find out which node reach next.
    Returns distance between current node and end node

    :param curr_pos: tuple[int, int] - row and column of current node
    :param end_pos: tuple[int, int] - row and column of end node
    """
    x1, y1 = curr_pos
    x2, y2 = end_pos
    return math.sqrt((x2 - x1)**2 + (y2-y1)**2)


def d(n1_pos, n2_pos):
    """
    Returns distance between two nodes in grid

    :param n1_pos: tuple[int, int] - row and column of first node
    :param n2_pos: tuple[int, int] - row and column of second node
    """
    x1, y1 = n1_pos
    x2, y2 = n2_pos
    return math.sqrt((x2 - x1)**2 + (y2-y1)**2)