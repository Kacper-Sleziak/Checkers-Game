from Board import Board
from PawnList import PawnList
from Pawn import Pawn
import pygame
from Drawings import Drawings
from Parent import Parent


class Game(Parent):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.end = False
        self.board = Board()

    def mainLoop(self):

        bluePawnList = PawnList((0, 0, 255), 30, self.getWindow())
        redPawnList = PawnList((255, 0, 0), 30, self.getWindow())
        drawings = Drawings(self.window)
        board = Board()

        redPawnList.createPawnToList(50, 50)
        redPawnList.createPawnToList(250, 50)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseXPos, mouseYPos = pygame.mouse.get_pos()
                    mouseXPos, mouseYPos = self.centerCoordinates(mouseXPos, mouseYPos, board.getMatrix())

                    for pawn in redPawnList.getList():

                        if pawn.getCordinateX() == mouseXPos and pawn.getCordinateY() == mouseYPos:
                            runningv2 = True
                            while runningv2:
                                print("True")
                                for eventv2 in pygame.event.get():
                                    if eventv2.type == pygame.QUIT:
                                        runningv2 = False

            self.window.fill((255, 255, 255))
            drawings.drawBoard(board)
            drawings.drawPawns(redPawnList)
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
