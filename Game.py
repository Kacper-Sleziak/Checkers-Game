from Board import Board
from PawnList import PawnList
from Pawn import Pawn
import pygame
from Drawings import Drawings
from GlobalFunctionality import GlobalFunctionality


class Game(GlobalFunctionality):

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
        redPawnList.createPawnToList(450, 50)
        redPawnList.createPawnToList(650, 50)

        bluePawnList.createPawnToList(150, 750)
        bluePawnList.createPawnToList(350, 750)
        bluePawnList.createPawnToList(550, 750)
        bluePawnList.createPawnToList(750, 750)

        running = True
        isPawnChoosed = False #about mouse click

        global pawnChoosenCordinateX
        global pawnChoosenCordinateY

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseXPos, mouseYPos = pygame.mouse.get_pos()
                    mouseXPos, mouseYPos = self.centerCoordinates(mouseXPos, mouseYPos, board.getMatrix())

                    if isPawnChoosed == False:
                        for pawn in redPawnList.getList():
                            if pawn.getCordinateX() == mouseXPos and pawn.getCordinateY() == mouseYPos:
                                print("first click")
                                isPawnChoosed = True

                                pawnChoosenCordinateX = pawn.getCordinateX()
                                pawnChoosenCordinateY = pawn.getCordinateY()

                    elif isPawnChoosed == True:
                        for pawn in redPawnList.getList():
                            if pawn.getCordinateX() == pawnChoosenCordinateX and pawn.getCordinateY() == pawnChoosenCordinateY:
                                if pawn.isMovePossible(bluePawnList, redPawnList, mouseXPos, mouseYPos):
                                    print("move")
                                    pawn.setCordinateX(mouseXPos)
                                    pawn.setCordinateY(mouseYPos)
                                    print(f"{pawn.getCordinateX()}, {pawn.getCordinateY()}")
                                    isPawnChoosed = False
                            


            self.window.fill((255, 255, 255))
            drawings.drawBoard(board)
            drawings.drawPawns(redPawnList)
            drawings.drawPawns(bluePawnList)
            pygame.display.update()

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

                if x >= leftCornerX and x <= (leftCornerX + 100) and y >= leftCornerY and y <= (leftCornerY + 100):
                    return coordinates
