import pygame
import constants
import player
from constants import *


def main():
    dt = 0
    pygame.init()
    print(
        f"Starting asteroids!\nScreen width: {constants.SCREEN_WIDTH}\nScreen height: {constants.SCREEN_HEIGHT}"
    )
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_instance = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player_instance.update(dt)
        screen.fill(0x000000)
        player_instance.draw(screen)
        pygame.display.flip()
        Clock = pygame.time.Clock()
        dt = Clock.tick(60) / 1000


if __name__ == "__main__":
    main()
