from Game import Game
from Player import Player
import pygame

HEIGHT = 800
WIDTH = 800

pygame.init()

window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Checkers")
icon = pygame.image.load('chess-board.png')
pygame.display.set_icon(icon)

redPlayer = Player((255, 0, 0))
bluePlayer = Player((0, 0, 255))

game = Game(window, "single player")
turn = 0
running = True
while running:
    if turn % 2 == 0:
        running = game.singleRound(redPlayer, bluePlayer)[0]
    elif turn % 2 == 1:
        running = game.singleRound(bluePlayer, redPlayer)[0]

    turn += 1

print(f"turn = {turn}")
