from Board import Board
from PawnList import PawnList
from Pawn import Pawn
import pygame


class Game:

    def __init__(self, window):
        self.window = window
        self.end = False
        self.board = Board()

    def mainLoop(self):

        bluePawnList = PawnList((0, 0, 255), 30, self.getWindow())
        redPawnList = PawnList((255, 0, 0), 30, self.getWindow())

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.window.fill((255, 255, 255))
            self.board.draw(self.getWindow())
            redPawnList.createPawnToList(50, 50)
            pygame.display.update()

        bluePawnList = PawnList((), 30, self.getWindow())
        redPawnList = PawnList((255, 0, 0), 30, self.getWindow())

    def gameUpdate(self):
        pass

    def getWindow(self):
        return self.window

    def click(self,
              event):  # After clicking black rectangle this funcion is printis coordinates of black rectangle's middle
        x = event.x
        y = event.y

        for row in self.board.getMatrix():
            for coordinates in row:

                [boardX, boardY] = coordinates
                leftCornerX = boardX - 50  # coordinates of
                leftCornerY = boardY - 50

                if (x >= leftCornerX and x <= (leftCornerX + 100)) and (y >= leftCornerY and y <= (leftCornerY + 100)):
                    return coordinates
