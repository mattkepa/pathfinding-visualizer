import pygame
from app_config import AppConfig
from utils import draw, get_clicked_pos


pygame.init()


app = AppConfig(size=800)


def main():
    start_node = None
    end_node = None

    run = True
    while run:

        draw(app.window, app.grid, app.rows, app.columns, app.size)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

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

    pygame.quit()


if __name__ == '__main__':
    main()