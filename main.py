import pygame
import constants
from constants import *


def main():
    pygame.init()
    print(
        f"Starting asteroids!\nScreen width: {constants.SCREEN_WIDTH}\nScreen height: {constants.SCREEN_HEIGHT}"
    )
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0x000000)
        pygame.display.flip()


if __name__ == "__main__":
    main()
