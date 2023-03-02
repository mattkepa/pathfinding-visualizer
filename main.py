import pygame
from app_config import AppConfig
from utils import draw, get_clicked_pos, a_star_search


pygame.init()


app = AppConfig(size=800)


def main():
    start_node = None
    end_node = None

    searching = False

    run = True
    while run:

        draw(app.window, app.grid, app.rows, app.columns, app.size)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if searching:
                continue

            if pygame.mouse.get_pressed()[0]: # LEFT MOUSE CLICK
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, app.rows, app.columns, app.size)
                clicked_node = app.grid[row][col]
                if start_node == None and clicked_node != end_node and not clicked_node.is_obstacle():
                    start_node = clicked_node
                    clicked_node.make_start()
                elif end_node == None and clicked_node != start_node and not clicked_node.is_obstacle():
                    end_node = clicked_node
                    clicked_node.make_end()
                elif clicked_node != end_node and clicked_node != start_node:
                    clicked_node.make_obstacle()

            elif pygame.mouse.get_pressed()[2]: # RIGHT MOUSE CLICK
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, app.rows, app.columns, app.size)
                clicked_node = app.grid[row][col]
                clicked_node.reset()
                if clicked_node == start_node:
                    start_node = None
                elif clicked_node == end_node:
                    end_node = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not searching: # SPACEBAR PRESS
                    for row in app.grid:
                        for node in row:
                            node.update_neighbors(app.grid)
                    searching = True
                    a_star_search(app.grid, start_node, end_node, lambda: draw(app.window, app.grid, app.rows, app.columns, app.size))
                    searching = False

    pygame.quit()


if __name__ == '__main__':
    main()