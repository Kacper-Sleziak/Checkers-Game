from Pawn import Pawn
from GlobalFunctionality import GlobalFunctionality


class Player(GlobalFunctionality):

    def __init__(self, color):
        self.__color = color
        self.pawnList = self.__createPawnList()

    def __createPawn(self, coordinateX, coordinateY):
        pawn = Pawn(coordinateX, coordinateY, self.__color)
        return pawn

    def __createPawnList(self):
        pawnList = []

        if self.__color == (255, 0, 0):
            pawnList.append(self.__createPawn(50, 50))
            pawnList.append(self.__createPawn(250, 50))
            pawnList.append(self.__createPawn(450, 450))
            pawnList.append(self.__createPawn(450, 650))

        elif self.__color == (0, 0, 255):
            pawnList.append(self.__createPawn(150, 750))
            pawnList.append(self.__createPawn(350, 750))
            pawnList.append(self.__createPawn(550, 750))
            pawnList.append(self.__createPawn(750, 750))

        return pawnList

    def roundChosingPawn(self, mouseXPos, mouseYPos, priorityPawns):

        if priorityPawns == []:
            for pawn in self.pawnList:
                if pawn.getCordinateX() == mouseXPos and pawn.getCordinateY() == mouseYPos:
                    return True
        else:
            for pawn in priorityPawns:
                if pawn.getCordinateX() == mouseXPos and pawn.getCordinateY() == mouseYPos:
                    return True

        return False

    def roundMovingPawn(self, mouseXPos, mouseYPos, listOfMoves, choosenPawnX, choosenPawnY):
        for pawn in self.pawnList:
            if pawn.getCordinateX() == choosenPawnX and pawn.getCordinateY() == choosenPawnY:
                for move in listOfMoves:
                    x, y = move
                    if x == mouseXPos and y == mouseYPos:
                        pawn.setCordinateX(mouseXPos)
                        pawn.setCordinateY(mouseYPos)
                        return False
        return True

    def getListOfMoves(self, pawnX, pawnY, color, enemyPawnList, board):

        listOfPossibleMoves = []
        leftRectangleCords = (0, 0)
        rightRectangleCords = (0, 0)

        if self.__color == (255, 0, 0):
            leftRectangleCords = (pawnX + 100, pawnY + 100)
            rightRectangleCords = (pawnX - 100, pawnY + 100)

        elif self.__color == (0, 0, 255):
            leftRectangleCords = (pawnX + 100, pawnY - 100)
            rightRectangleCords = (pawnX - 100, pawnY - 100)

        listOfPossibleMoves.append(leftRectangleCords)
        listOfPossibleMoves.append(rightRectangleCords)

        for rectangle in listOfPossibleMoves:
            moveCordsX, moveCordsY = rectangle
            if not self.isMovePossible(enemyPawnList, self.pawnList, board.getMatrix(), moveCordsX, moveCordsY): #Global
                listOfPossibleMoves.remove(rectangle)
                #rectangleToCheckX
        return listOfPossibleMoves

    def searchingPriorityPawns(self, enemyPawnList, board):
        priorityPawns = []

        for pawn in self.pawnList:
            x = pawn.getCordinateX()
            y = pawn.getCordinateY()

            listOfNearEnemyPawns = self.isEnemyNear(x, y, enemyPawnList)

            if listOfNearEnemyPawns != []:
                for enemyPawn in listOfNearEnemyPawns:
                    enemyX = enemyPawn.getCordinateX()
                    enemyY = enemyPawn.getCordinateY()
                    deltaX = enemyX - x
                    deltaY = enemyY - y
                    if self.isRectangleEmpty(enemyX + deltaX, enemyY + deltaY, self.pawnList, enemyPawnList):
                        priorityPawns.append(pawn)

        return priorityPawns

    def isEnemyNear(self, x, y, listOfEnemyPawns):
        listOfNearEnemyPawns = []
        for pawn in listOfEnemyPawns:
            if pawn.getCordinateX() == (x + 100) and pawn.getCordinateY() == (y + 100):
                listOfNearEnemyPawns.append(pawn)
            if pawn.getCordinateX() == (x + 100) and pawn.getCordinateY() == (y - 100):
                listOfNearEnemyPawns.append(pawn)
            if pawn.getCordinateX() == (x - 100) and pawn.getCordinateY() == (y + 100):
                listOfNearEnemyPawns.append(pawn)
            if pawn.getCordinateX() == (x - 100) and pawn.getCordinateY() == (y - 100):
                listOfNearEnemyPawns.append(pawn)
        return listOfNearEnemyPawns

    def getListOfBeatings(self, choosenPawnX, choosenPawnY, listOfPossibleMoves, listOfEnemyPawns, matrix):

        listOfBeatings = []
        listOfNearEnemyPawns = self.isEnemyNear(choosenPawnX, choosenPawnY, listOfEnemyPawns)

        if not len(listOfNearEnemyPawns) == 0:
            for enemyPawn in listOfNearEnemyPawns:

                enemyPawnX = enemyPawn.getCordinateX()
                enemyPawnY = enemyPawn.getCordinateY()
                deltaX = enemyPawnX - choosenPawnX
                deltaY = enemyPawnY - choosenPawnY
                if self.isMovePossible(self.pawnList, listOfEnemyPawns, matrix, enemyPawnX + deltaX, enemyPawnY + deltaY):
                    listOfBeatings.append((enemyPawnX + deltaX,  enemyPawnY + deltaY))

            if not len(listOfBeatings) == 0:
                listOfPossibleMoves.clear()
                listOfPossibleMoves = listOfBeatings

        return listOfPossibleMoves

    def getPawnList(self):
        return self.pawnList

    def movingPawn(self):
        pass

    def choosingPawn(self):
        pass

    def killPawn(self, x, y):

        for pawn in self.pawnList:
            if pawn.getCordinateX() == x and pawn. getCordinateY() == y:
                self.pawnList.remove(pawn)
