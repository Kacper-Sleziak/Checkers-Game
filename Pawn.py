import pygame
from GlobalFunctionality import GlobalFunctionality


class Pawn(GlobalFunctionality):

    def __init__(self, coordinateX, coordinateY, color):
        super().__init__()
        self.coordinateX = coordinateX
        self.coordinateY = coordinateY
        self.color = color
        self.alive = True
        self.radius = 30

    def movePawn(self, newPosX, newPosY, rectangleMatrix, pawnList, listOfThisPawn):

        newPosX, newPosY = self.centerCoordinates(newPosX, newPosY, rectangleMatrix)
        if self.isMovePossible(pawnList, listOfThisPawn, newPosX, newPosY):
            self.setCordinateX(newPosX)
            self.setCordinateY(newPosY)

    def pawnDestroy(self):
        self.alive = False

    def getCordinateX(self):
        return self.coordinateX

    def getCordinateY(self):
        return self.coordinateY

    def getRadius(self):
        return self.radius

    def getColor(self):
        return self.color

    def setCordinateY(self, newCoordinateY):
        self.coordinateY = newCoordinateY

    def setCordinateX(self, newCoordinateX):
        self.coordinateX = newCoordinateX

    # def movePawn(self, newPosX, newPosY):
    #
    #     print("move")
    #     pawn = self.drawing
    #     moving = True
    #     startingX = self.getCordinateX()
    #     startingY = self.getCordinateY()
    #     speedX = 4
    #     speedY = 4
    #     positionCorrection = self.getRadius() * -1
    #
    #     self.setCordinateX(newPosX)
    #     self.setCordinateY(newPosY)
    #
    #     if self.getColor() == "red":
    #         if startingX > newPosX:
    #             speedX *= -1
    #
    #     elif self.getColor() == "blue":
    #         speedY *= -1
    #         if startingX > newPosX:
    #             speedX *= -1
    #
    #     while moving:
    #         pawn_pos = self.getCanvas().coords(pawn)
    #         self.getCanvas().move(pawn, speedX, speedY)
    #         self.getWindow().update()
    #         time.sleep(0.01)
    #         x, y, r, r = pawn_pos
    #         print(x, y)
    #         if x == newPosX + positionCorrection and y == newPosY + positionCorrection:
    #             moving = False
