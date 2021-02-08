import pygame

class Drawings:

    def __init__(self, window):
        self.window = window
        self.recSize = 100
        pass

    def drawBoard(self, board):
        matrix = board.matrix
        for row in matrix:
            for rectangle in row:
                x, y = rectangle
                coordinateX = x - 50
                coordinateY = y - 50

                pygame.draw.rect(self.window, (0, 0, 0), ((coordinateX, coordinateY), (self.recSize, self.recSize)))

    def drawPawns(self, pawnList):
        for pawn in pawnList:
            r, g, b = pawn.color
            pygame.draw.circle(self.window, (r, g, b),
                               (pawn.coordinateX, pawn.coordinateY), pawn.radius)

    def drawPosibleMoves(self, window, listOfMoves):
        for move in listOfMoves:
            x, y = move
            pygame.draw.circle(window, (200, 200, 0), (x, y), 10)
