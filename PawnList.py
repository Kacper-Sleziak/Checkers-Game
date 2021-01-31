from Pawn import Pawn


class PawnList:
    def __init__(self, color, radius, window):
        self.radius = radius
        self.window = window
        self.color = color
        self.list = []

    def createPawnToList(self, cordinateX, cordinateY):
        self.list.append(
            Pawn(cordinateX, cordinateY, self.getRadius(), (self.getColor()), self.getWindow()))

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

    def getWindow(self):
        return self.window
