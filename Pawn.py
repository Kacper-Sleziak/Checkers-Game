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
