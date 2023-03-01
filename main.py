import pygame
from app_config import AppConfig


pygame.init()


app = AppConfig(size=800)


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == '__main__':
    main()