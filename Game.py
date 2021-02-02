from Board import Board
from PawnList import PawnList
import pygame
from Drawings import Drawings
from GlobalFunctionality import GlobalFunctionality


class Game(GlobalFunctionality):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.redPawnList = PawnList((255, 0, 0), 30, self.getWindow())
        self.bluePawnList = PawnList((0, 0, 255), 30, self.getWindow())
        self.end = False
        self.round = "red"
        self.board = Board()
        self.choosenPawnX = 0
        self.choosenPawnY = 0

    def mainLoop(self):

        drawings = Drawings(self.window)
        board = Board()

        self.redPawnList.createPawnToList(50, 50)
        self.redPawnList.createPawnToList(250, 50)
        self.redPawnList.createPawnToList(450, 50)
        self.redPawnList.createPawnToList(650, 50)

        self.bluePawnList.createPawnToList(150, 750)
        self.bluePawnList.createPawnToList(350, 750)
        self.bluePawnList.createPawnToList(550, 750)
        self.bluePawnList.createPawnToList(750, 750)

        running = True
        isPawnChoosed = False  # about mouse click
        thisPawnList = self.getRedPawnList()
        otherPawnList = self.getBluePawnList()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseXPos, mouseYPos = pygame.mouse.get_pos()
                    mouseXPos, mouseYPos = self.centerCoordinates(mouseXPos, mouseYPos, board.getMatrix())

                    if not isPawnChoosed:
                        isPawnChoosed = self.roundChosingPawn(thisPawnList, mouseXPos, mouseYPos)
                        print("Pawn is Choosed")
                        print(f"{self.getChoosenPawnX()}, {self.getChoosenPawnY()}")

                    elif isPawnChoosed:
                        print("Pawn is moving1")
                        isPawnChoosed = self.roundMovingPawn(otherPawnList, thisPawnList, mouseXPos, mouseYPos)
                        print(f"Pawn is moving2,{isPawnChoosed}")
                        if not isPawnChoosed:
                            if self.round == "red":
                                self.setRound("blue")
                                otherPawnList = self.getRedPawnList()
                                thisPawnList = self.getBluePawnList()
                                print(self.getRound())
                            else:
                                self.setRound("red")
                                otherPawnList = self.getBluePawnList()
                                thisPawnList = self.getRedPawnList()
                                print(self.getRound())

            self.window.fill((255, 255, 255))
            drawings.drawBoard(board)
            drawings.drawPawns(self.getRedPawnList())
            drawings.drawPawns(self.getBluePawnList())
            pygame.display.update()

    def roundChosingPawn(self, pawnList, mouseXPos, mouseYPos):

        for pawn in pawnList.getList():
            if pawn.getCordinateX() == mouseXPos and pawn.getCordinateY() == mouseYPos:
                self.setChoosenPawnX(pawn.getCordinateX())
                self.setChoosenPawnY(pawn.getCordinateY())
                return True

        return False

    def roundMovingPawn(self, otherPawnList, thisPawnList, mouseXPos, mouseYPos):

        for pawn in thisPawnList.getList():
            if pawn.getCordinateX() == self.getChoosenPawnX() and pawn.getCordinateY() == self.getChoosenPawnY():
                if pawn.isMovePossible(otherPawnList, thisPawnList, mouseXPos, mouseYPos):
                    pawn.setCordinateX(mouseXPos)
                    pawn.setCordinateY(mouseYPos)
                    return False
        return True

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

    def getChoosenPawnX(self):
        return self.choosenPawnX

    def getChoosenPawnY(self):
        return self.choosenPawnY

    def getRound(self):
        return self.round

    def getRedPawnList(self):
        return self.redPawnList

    def getBluePawnList(self):
        return self.bluePawnList

    def setChoosenPawnX(self, newX):
        self.choosenPawnX = newX

    def setChoosenPawnY(self, newY):
        self.choosenPawnY = newY

    def setRound(self, newRound):
        self.round = newRound
