import pygame
import sys

# initialise
pygame.init()


class Settings:
    WIDTH = 600
    HEIGHT = 500

# create screen
screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))

game_over = False

while not game_over:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()




