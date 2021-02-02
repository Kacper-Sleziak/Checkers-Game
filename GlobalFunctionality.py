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
