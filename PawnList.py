from Pawn import *


class PawnList:
    def __init__(self, color, radius, canvas, window):
        self.radius = radius
        self.canvas = canvas
        self.window = window
        self.color = color
        self.list = []

    def createPawnToList(self, cordinateX, cordinateY):
        self.list.append(
            Pawn(cordinateX, cordinateY, self.getRadius(), self.getColor(), self.getCanvas(), self.getWindow()))

    def getColor(self):
        return self.color

    def getPawnById(self, id):
        return self.list[id]

    def getList(self):
        return self.list

    def getListLength(self):
        return len(self.getList())

    def getRadius(self):
        return self.radius

    def getCanvas(self):
        return self.canvas

    def getWindow(self):
        return self.window
