from Board import Board
from PawnList import PawnList
from Pawn import Pawn


class Game:

    def __init__(self, window, canvas):
        self.window = window
        self.canvas = canvas
        self.end = False

    def mainLoop(self):
        board = Board()
        board.draw(self.getWindow(), self.getCanvas())

        bluePawnList = PawnList("blue", 30, self.getCanvas(), self.getWindow())
        redPawnList = PawnList("red", 30, self.getCanvas(), self.getWindow())

    def gameUpdate(self):
        pass

    def click(self, event, boardMatrix):  # After clicking black rectangle this funcion is printis coordinates of black rectangle's middle
        x = event.x
        y = event.y

        for row in boardMatrix.getMatrix():
            for coordinates in row:
                [boardX, boardY] = coordinates
                leftCornerX = boardX - 50  # coordinates of
                leftCornerY = boardY - 50

                if (x >= leftCornerX and x <= (leftCornerX + 100)) and (y >= leftCornerY and y <= (leftCornerY + 100)):
                    print(coordinates)

    def getWindow(self):
        return self.window

    def getCanvas(self):
        return self.canvas
