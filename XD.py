from Pawn import Pawn
import pygame
from Board import Board

pygame.init()

board = Board()

window = pygame.display.set_mode((100, 100))
pawn = Pawn(1, 2, 10, 2, window)
pawn.centerCoordinates(10, 20, pawn.getMatrix())
