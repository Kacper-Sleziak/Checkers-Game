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
