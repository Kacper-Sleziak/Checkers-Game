from abc import ABC

class GlobalFunctionality(ABC):

    def __init__(self):
        pass

    @staticmethod
    def centerCoordinates(posX, posY, rectangleMatrix):

        for row in rectangleMatrix:
            for rectangle in row:
                recMidX, recMidY = rectangle
                if abs(recMidX - posX) <= 50 and abs(recMidY - posY) <= 50:
                    centerPosX = recMidX
                    centerPosY = recMidY
                    return centerPosX, centerPosY
        return posX, posY

    def isMovePossible(self, pawnList, listOfThisPawn, rectangleMatrix, moveCordsX, moveCordsY):

        for row in rectangleMatrix:
            for rectangle in row:
                rectangleX, rectangleY = rectangle

                if rectangleX == moveCordsX and rectangleY == moveCordsY:

                    for pawn in pawnList:
                        if (pawn.coordinateX == moveCordsX) and (pawn.coordinateY == moveCordsY):
                            return False

                    for pawn in listOfThisPawn:
                        if (pawn.coordinateX == moveCordsX) and (pawn.coordinateY == moveCordsY) and pawn != self:
                            return False

                    return True
        return False

    def isRectangleEmpty(self, x, y, pawnList, enemyPawnList, board):

        for row in board.matrix:
            for rec in row:
                recX, recY = rec

                if x == recX and y == recY:

                    for pawn in pawnList:
                        if pawn.coordinateX == x and pawn.coordinateY == y:
                            return False

                    for pawn in enemyPawnList:
                        if pawn.coordinateX == x and pawn.coordinateY == y:
                            return False

                    return True

        return False

    def isEnemyThere(self, x, y, enemyPawnList):

        for pawn in enemyPawnList:
            pawnX = pawn.coordinateX
            pawnY = pawn.coordinateY
            if pawnX == x and pawnY == y:
                return True

        return False

    def isMoveInListOfMoves(self, moveX, moveY, listOfMoves):
        for move in listOfMoves:
            x, y = move
            if x == moveX and y == moveY:
                return True
        return False

    def checkVectorDirection(self, pawn, mouseX, mouseY):
        x = pawn.coordinateX
        y = pawn.coordinateY
        vectorX = 0
        vectorY = 0

        if mouseX - x > 0:
            vectorX = 100
        else:
            vectorX = -100

        if mouseY - y > 0:
            vectorY = 100
        else:
            vectorY = -100

        return (vectorX, vectorY)
