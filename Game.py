from Board import Board
from Player import Player
import pygame
from Drawings import Drawings
from GlobalFunctionality import GlobalFunctionality


class Game(GlobalFunctionality):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.round = "red"
        self.board = Board()
        self.choosenPawnX = 0
        self.choosenPawnY = 0
        self.listOfMoves = []

    def mainLoop(self):

        priorityPawns = []
        running = True
        isPawnChoosed = False  # about mouse click
        redPlayer = Player((255, 0, 0))
        bluePlayer = Player((0, 0, 255))

        thisPawnList = redPlayer.getPawnList()
        otherPawnList = bluePlayer.getPawnList()

        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                priorityPawns = self.searchingPriorityPawns(thisPawnList, otherPawnList)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        isPawnChoosed = False
                        self.listOfMoves.clear()
                        self.gameUpdate(redPlayer, bluePlayer)
                        print("escape")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseXPos, mouseYPos = pygame.mouse.get_pos()
                    mouseXPos, mouseYPos = self.centerCoordinates(mouseXPos, mouseYPos, self.board.getMatrix())

                    if not isPawnChoosed:
                        isPawnChoosed = self.roundChosingPawn(thisPawnList, mouseXPos, mouseYPos, priorityPawns)
                        if isPawnChoosed:
                            self.listOfMoves = self.getListOfMoves(self.choosenPawnX, self.choosenPawnY, self.round, redPlayer.getPawnList(), bluePlayer.getPawnList())
                            self.listOfMoves = self.appendListOfPossiblesBeatings(self.listOfMoves, self.choosenPawnX, self.choosenPawnY, redPlayer.getPawnList(), bluePlayer.getPawnList(), self.round, 0)
                            print("posible moves")
                            print(self.listOfMoves)


                    elif isPawnChoosed:
                        isPawnChoosed = self.roundMovingPawn(thisPawnList, mouseXPos, mouseYPos, self.listOfMoves)

                        if not isPawnChoosed:
                            if self.round == "red":
                                self.setRound("blue")
                                otherPawnList = redPlayer.getPawnList()
                                thisPawnList = bluePlayer.getPawnList()
                                print(self.getRound())
                            else:
                                self.setRound("red")
                                otherPawnList = bluePlayer.getPawnList()
                                thisPawnList = redPlayer.getPawnList()
                                print(self.getRound())

                            self.listOfMoves.clear()
                            priorityPawns.clear()

            self.gameUpdate(redPlayer, bluePlayer)

    def roundChosingPawn(self, pawnList, mouseXPos, mouseYPos, priorityPawns):

        if priorityPawns == []:
            for pawn in pawnList:
                if pawn.getCordinateX() == mouseXPos and pawn.getCordinateY() == mouseYPos:
                    self.setChoosenPawnX(pawn.getCordinateX())
                    self.setChoosenPawnY(pawn.getCordinateY())
                    return True
        else:
            for pawn in priorityPawns:
                if pawn.getCordinateX() == mouseXPos and pawn.getCordinateY() == mouseYPos:
                    self.setChoosenPawnX(pawn.getCordinateX())
                    self.setChoosenPawnY(pawn.getCordinateY())
                    return True

        return False

    def roundMovingPawn(self, thisPawnList, mouseXPos, mouseYPos, listOfMoves):
        for pawn in thisPawnList:
            if pawn.getCordinateX() == self.getChoosenPawnX() and pawn.getCordinateY() == self.getChoosenPawnY():
                for move in listOfMoves:
                    x, y = move
                    if x == mouseXPos and y == mouseYPos:
                        pawn.setCordinateX(mouseXPos)
                        pawn.setCordinateY(mouseYPos)
                        self.listOfMoves.clear()
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

    def isEnemyNear(self, x, y, listOfEnemyPawns):
        for pawn in listOfEnemyPawns:
            if pawn.getCordinateX() == (x + 100) and pawn.getCordinateY() == (y + 100):
                return (1,1)
            if pawn.getCordinateX() == (x + 100) and pawn.getCordinateY() == (y - 100):
                return (1,-1)
            if pawn.getCordinateX() == (x - 100) and pawn.getCordinateY() == (y + 100):
                return (-1,1)
            if pawn.getCordinateX() == (x - 100) and pawn.getCordinateY() == (y - 100):
                return (-1,-1)


    def appendListOfPossiblesBeatings(self, listOfPossibleMoves, choosenPawnX, choosenPawnY, redPawnList, bluePawnList, round, counter):

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

        def recurency(xDirection, yDirection):
            nonlocal counter
            moveCordsX = choosenPawnX +  200 * xDirection
            moveCordsY = choosenPawnY +  200 * yDirection

            if self.isMovePossible(pawnList, listOfThisPawn, self.board.getMatrix(), moveCordsX, moveCordsY) and counter  < 9 and \
            self.isEnemyNear(choosenPawnX, choosenPawnY, pawnList) == (xDirection, yDirection):
                print("im in")
                counter = counter + 1
                listOfPossibleMoves.append((moveCordsX, moveCordsY))
                self.appendListOfPossiblesBeatings(listOfPossibleMoves, moveCordsX, moveCordsY, redPawnList, bluePawnList, round, counter)


        recurency(1,1)
        recurency(1,-1)
        recurency(-1,1)
        recurency(-1,-1)
        # moveCordsX = choosenPawnX -  200
        # moveCordsY = choosenPawnY +  200
        #
        # if self.isMovePossible(pawnList, listOfThisPawn, self.board.getMatrix(), moveCordsX, moveCordsY) and counter < 5 and \
        # self.isEnemyNear(choosenPawnX, choosenPawnY, pawnList) == (-1,1):
        #
        #     counter = counter + 1
        #     listOfPossibleMoves.append((moveCordsX, moveCordsY))
        #     self.appendListOfPossiblesBeatings(listOfPossibleMoves, moveCordsX, moveCordsY, redPawnList, bluePawnList, round, counter)
        #
        # moveCordsX = choosenPawnX +  200
        # moveCordsY = choosenPawnY -  200
        #
        # if self.isMovePossible(pawnList, listOfThisPawn, self.board.getMatrix(), moveCordsX, moveCordsY) and counter < 5 and \
        # self.isEnemyNear(choosenPawnX, choosenPawnY, pawnList) == (1,-1):
        #
        #     counter = counter + 1
        #     listOfPossibleMoves.append((moveCordsX, moveCordsY))
        #     self.appendListOfPossiblesBeatings(listOfPossibleMoves, moveCordsX, moveCordsY, redPawnList, bluePawnList, round, counter)
        #
        # moveCordsX = choosenPawnX -  200
        # moveCordsY = choosenPawnY -  200
        #
        # if self.isMovePossible(pawnList, listOfThisPawn, self.board.getMatrix(), moveCordsX, moveCordsY) and counter < 5 and \
        # self.isEnemyNear(choosenPawnX, choosenPawnY, pawnList) == (-1,-1):
        #
        #     counter = counter + 1
        #     listOfPossibleMoves.append((moveCordsX, moveCordsY))
        #     self.appendListOfPossiblesBeatings(listOfPossibleMoves, moveCordsX, moveCordsY, redPawnList, bluePawnList, round, counter)




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

    def gameUpdate(self, redPlayer, bluePlayer):
        drawings = Drawings(self.window)

        self.window.fill((255, 255, 255))
        drawings.drawBoard(self.board)
        drawings.drawPawns(redPlayer.getPawnList())
        drawings.drawPawns(bluePlayer.getPawnList())
        drawings.drawPosibleMoves(self.window, self.listOfMoves)
        pygame.display.update()

    def searchingPriorityPawns(self, listOfThisPawn, pawnList):
        priorityPawns = []

        for pawn in listOfThisPawn:
            x = pawn.getCordinateX()
            y = pawn.getCordinateY()
            nearRectangles = []

            nearRectangle1 = (x + 100, y - 100)
            nearRectangle2 = (x + 100, y + 100)
            nearRectangle3 = (x - 100, y + 100)
            nearRectangle4 = (x - 100, y + 100)

            nearRectangles.append(nearRectangle1)
            nearRectangles.append(nearRectangle2)
            nearRectangles.append(nearRectangle3)
            nearRectangles.append(nearRectangle4)

            for nearRectangle in nearRectangles:
                nearX, nearY = nearRectangle
                for row in self.board.getMatrix():
                    for rectangle in row:
                        recX, recY = rectangle
                        if nearX == recX and nearY == recY:
                            for enemyPawn in pawnList:
                                if nearX == enemyPawn.getCordinateX() and nearY == enemyPawn.getCordinateY():
                                    priorityPawns.append(pawn)
        return priorityPawns

    def getWindow(self):
        return self.window

    def getChoosenPawnX(self):
        return self.choosenPawnX

    def getChoosenPawnY(self):
        return self.choosenPawnY

    def getRound(self):
        return self.round

    def setChoosenPawnX(self, newX):
        self.choosenPawnX = newX

    def setChoosenPawnY(self, newY):
        self.choosenPawnY = newY

    def setRound(self, newRound):
        self.round = newRound
