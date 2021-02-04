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
        self.listOfMoves = []

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
                        if isPawnChoosed:
                            self.listOfMoves = self.getListOfMoves(self.choosenPawnX, self.choosenPawnY, self.round, self.getRedPawnList(), self.getBluePawnList())
                            self.listOfMoves = self.appendListOfPossiblesBeatings(self.listOfMoves, self.choosenPawnX, self.choosenPawnY, self.getRedPawnList(), self.getBluePawnList(), self.round)
                            print("posible moves")
                            print(self.listOfMoves)


                    elif isPawnChoosed:
                        #listofmoves wrzuc do inita? tak samo otherPawnList i thisPawnList

                        isPawnChoosed = self.roundMovingPawn(thisPawnList, mouseXPos, mouseYPos, self.listOfMoves)

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

                        self.listOfMoves.clear()

            self.gameUpdate()

    def roundChosingPawn(self, pawnList, mouseXPos, mouseYPos):

        for pawn in pawnList.getList():
            if pawn.getCordinateX() == mouseXPos and pawn.getCordinateY() == mouseYPos:
                self.setChoosenPawnX(pawn.getCordinateX())
                self.setChoosenPawnY(pawn.getCordinateY())
                return True

        return False

    def roundMovingPawn(self, thisPawnList, mouseXPos, mouseYPos, listOfMoves):
        for pawn in thisPawnList.getList():
            if pawn.getCordinateX() == self.getChoosenPawnX() and pawn.getCordinateY() == self.getChoosenPawnY():
                for move in listOfMoves:
                    x, y = move
                    if x == mouseXPos and y == mouseYPos:
                        pawn.setCordinateX(mouseXPos)
                        pawn.setCordinateY(mouseYPos)
                        self.listOfMoves.clear
                        return False
        return True

    def getListOfMoves(self, pawnX, pawnY, color, redPawnList, bluePawnList):

        listOfPossibleMoves = []
        leftRectangleCords = (0, 0)
        rightRectangleCords = (0, 0)
        pawnList = bluePawnList
        listOfThisPawn = redPawnList

        if color == "red":
            leftRectangleCords = (pawnX + 100, pawnY + 100)
            rightRectangleCords = (pawnX - 100, pawnY + 100)
            pawnList = bluePawnList
            listOfThisPawn = redPawnList

        elif color == "blue":
            leftRectangleCords = (pawnX + 100, pawnY - 100)
            rightRectangleCords = (pawnX - 100, pawnY - 100)
            pawnList = redPawnList
            listOfThisPawn = bluePawnList

        listOfPossibleMoves.append(leftRectangleCords)
        listOfPossibleMoves.append(rightRectangleCords)

        for rectangle in listOfPossibleMoves:
            moveCordsX, moveCordsY = rectangle
            if not self.isMovePossible(pawnList, listOfThisPawn, self.board.getMatrix(), moveCordsX, moveCordsY):
                listOfPossibleMoves.remove(rectangle)
                #rectangleToCheckX
        return listOfPossibleMoves

    def appendListOfPossiblesBeatings(self, listOfPossibleMoves, choosenPawnX, choosenPawnY, redPawnList, bluePawnList, round):

        leftRectangleCords = (0, 0)
        rightRectangleCords = (0, 0)
        pawnList = bluePawnList
        listOfThisPawn = redPawnList

        if round == "red":
            pawnList = bluePawnList
            listOfThisPawn = redPawnList

        elif round == "blue":
            pawnList = redPawnList
            listOfThisPawn = bluePawnList

        moveCordsX = choosenPawnX +  200
        moveCordsY = choosenPawnY +  200

        if self.isMovePossible(pawnList, listOfThisPawn, self.board.getMatrix(), moveCordsX, moveCordsY):
            listOfPossibleMoves.append((moveCordsX, moveCordsY))
            self.appendListOfPossiblesBeatings(listOfPossibleMoves, moveCordsX, moveCordsY, redPawnList, bluePawnList, round)

        moveCordsX = choosenPawnX +  200
        moveCordsY = choosenPawnY -  200

        if self.isMovePossible(pawnList, listOfThisPawn, self.board.getMatrix(), moveCordsX, moveCordsY):
            listOfPossibleMoves.append((moveCordsX, moveCordsY))
            self.appendListOfPossiblesBeatings(listOfPossibleMoves, moveCordsX, moveCordsY, redPawnList, bluePawnList, round)



        # for i in range(7):
        #     moveCordsX = choosenPawnX + i * direction * 100
        #     moveCordsY = choosenPawnY + i * direction * 100
        #
        #     if self.isMovePossible(pawnList, listOfThisPawn, self.board.getMatrix(), moveCordsX, moveCordsY):
        #         listOfPossibleMoves.append((moveCordsX, moveCordsY))
        #
        #     moveCordsX = choosenPawnX + i * direction * -100
        #
        #     if self.isMovePossible(pawnList, listOfThisPawn, self.board.getMatrix(), moveCordsX, moveCordsY):
        #         listOfPossibleMoves.append((moveCordsX, moveCordsY))


        return listOfPossibleMoves

    def gameUpdate(self):
        drawings = Drawings(self.window)

        self.window.fill((255, 255, 255))
        drawings.drawBoard(self.board)
        drawings.drawPawns(self.getRedPawnList())
        drawings.drawPawns(self.getBluePawnList())
        drawings.drawPosibleMoves(self.window, self.listOfMoves)
        pygame.display.update()

    def getWindow(self):
        return self.window

    def click(self, event):  # After clicking black rectangle this funcion is printis coordinates of black rectangle's middle
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

