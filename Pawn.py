import pygame
from GlobalFunctionality import GlobalFunctionality


class Pawn(GlobalFunctionality):

    def __init__(self, coordinateX, coordinateY, color):
        super().__init__()
        self.coordinateX = coordinateX
        self.coordinateY = coordinateY
        self.color = color
        self.radius = 30
        self.isQueen = False

    def movePawn(self, newX, newY):
        self.coordinateX = newX
        self.coordinateY = newY

    def evolvePawnToQuen(self, listOfSpecialRect):
        for rec in listOfSpecialRect:
            recX, recY = rec
            
            if self.coordinateX == recX and self.coordinateY == recY:
                print("we are here")
                self.setQueen()




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

    def setQueen(self):
        self.isQueen = True
