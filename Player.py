from Pawn import Pawn


class Player:
    def __init__(self, color):
        self.color = color
        self.pawnList = self.createPawnList()

    def createPawn(self, coordinateX, coordinateY):
        pawn = Pawn(coordinateX, coordinateY, self.color)
        return pawn

    def createPawnList(self):
        pawnList = []

        if self.color == (255, 0, 0):
            pawnList.append(self.createPawn(50, 50))
            pawnList.append(self.createPawn(250, 50))
            pawnList.append(self.createPawn(450, 50))
            pawnList.append(self.createPawn(650, 50))

        elif self.color == (0, 0, 255):
            pawnList.append(self.createPawn(150, 750))
            pawnList.append(self.createPawn(350, 750))
            pawnList.append(self.createPawn(550, 750))
            pawnList.append(self.createPawn(750, 750))

        return pawnList

    def getPawnList(self):
        return self.pawnList

    def movingPawn(self):
        pass

    def choosingPawn(self):
        pass
