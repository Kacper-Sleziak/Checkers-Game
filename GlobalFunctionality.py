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
                        if (pawn.getCordinateX() == moveCordsX) and (pawn.getCordinateY() == moveCordsY):
                            return False

                    for pawn in listOfThisPawn:
                        if (pawn.getCordinateX() == moveCordsX) and (pawn.getCordinateY() == moveCordsY) and pawn != self:
                            return False

                    return True
        return False

    def isRectangleEmpty(self, x, y, pawnList, enemyPawnList, board):

        for row in board.getMatrix():
            for rec in row:
                recX, recY = rec

                if x == recX and y == recY:

                    for pawn in pawnList:
                        if pawn.getCordinateX() == x and pawn.getCordinateY() == y:
                            return False

                    for pawn in enemyPawnList:
                        if pawn.getCordinateX() == x and pawn.getCordinateY() == y:
                            return False

                    return True

        return False

    def isEnemyThere(self, x, y, enemyPawnList):

        for pawn in enemyPawnList:
            pawnX = pawn.getCordinateX()
            pawnY = pawn.getCordinateY()
            if pawnX == x and pawnY == y:
                return True

        return False
