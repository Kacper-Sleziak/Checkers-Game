import pygame


class Board:

    def __init__(self):
        self.size = 100  # size mean height and width of single black rectangle on the board
        self.matrix = self.__createRecMatrix()

    def __createRecMatrix(self):

        matrix = []
        rows = 8

        for i in range(rows):

            row = []  # single row of black rectangles in matrix
            rowIndex = 0

            jump = 200  # distance between rectangles
            coordinateY = i * 100

            if i % 2 == 0:
                lastRectangle = 700  # CoordinatesX of first and last Rectangle in board row
                firstRectangle = 0  # When board row is starting with black rectangle
            else:
                lastRectangle = 800  # CoordinatesX of first and last lRectangle in board row
                firstRectangle = 100  # When board row is starting with white rectangle

            for coordinateX in range(firstRectangle, lastRectangle, jump):

                middleCoordinates = [coordinateX + 50,
                                     coordinateY + 50]  # Saving coordinates of the middle of single rectangle

                row.append(middleCoordinates)

                rowIndex += 1

            matrix.append(row)  # Adding 4 items row to matrix

        return matrix

    def isRecInMatrix(self, recX, recY):
        for row in self.matrix:
            for rec in row:
                x,y = rec
                if recX == x and recY == y:
                    return True
        return False


    def getSize(self):
        return self.size

    def getMatrix(self):
        return self.matrix
