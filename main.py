import pygame


pygame.init()


def main():
    pygame.display.set_mode((800, 800))
    pygame.display.set_caption('A* Pathfinding Algorithm Visualizer')

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == '__main__':
    main()