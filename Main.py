from Game import Game
import pygame

HEIGHT = 800
WIDTH = 800

pygame.init()

window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Checkers")
icon = pygame.image.load('chess-board.png')
pygame.display.set_icon(icon)

game = Game(window)
game.mainLoop()

# dodaje komentarz w atom
