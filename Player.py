from Pawn import Pawn
from GlobalFunctionality import GlobalFunctionality


class Player(GlobalFunctionality):

    def __init__(self, color):
        self.__color = color
        self.specialRec = self.__createSpecialRec()
        self.pawnList = self.__createPawnList()


    def __createPawn(self, coordinateX, coordinateY):
        pawn = Pawn(coordinateX, coordinateY, self.__color)
        return pawn


    def __createPawnList(self):
        pawnList = []

        if self.__color == (255, 0, 0):
            for i in range(3):
                for j in range (4):
                    if i%2 != 0:
                        pawnList.append(self.__createPawn(150 + j * 200, 50 + i *100))
                    else:
                        pawnList.append(self.__createPawn(50 + j * 200, 50 + i *100))

        elif self.__color == (0, 0, 255):
            for i in range(3):
                for j in range (4):
                    if i%2 != 0:
                        pawnList.append(self.__createPawn(50 + j * 200, 750 - i *100))
                    else:
                        pawnList.append(self.__createPawn(150 + j * 200, 750 - i *100))

        return pawnList


    def __createSpecialRec(self):
        specialRecList = []
        if self.__color == (255, 0, 0):
            specialRecList.append((150,750))
            specialRecList.append((350,750))
            specialRecList.append((550,750))
            specialRecList.append((750,750))

        elif self.__color == (0, 0, 255):
            specialRecList.append((50,50))
            specialRecList.append((250,50))
            specialRecList.append((450,50))
            specialRecList.append((650,50))

        return specialRecList


    def roundChosingPawn(self, mouseXPos, mouseYPos, priorityPawns):

        if priorityPawns == []:
            for pawn in self.pawnList:
                if pawn.coordinateX == mouseXPos and pawn.coordinateY == mouseYPos:
                    return pawn
        else:
            for pawn in priorityPawns:
                if pawn.coordinateX == mouseXPos and pawn.coordinateY == mouseYPos:
                    return pawn

        return False


    def roundMovingPawn(self, mouseXPos, mouseYPos, listOfMoves, choosenPawn):
        for pawn in self.pawnList:
            if pawn.coordinateX == choosenPawn.coordinateX and pawn.coordinateY == choosenPawn.coordinateY:
                for move in listOfMoves:
                    x, y = move
                    if x == mouseXPos and y == mouseYPos:
                        pawn.movePawn(mouseXPos, mouseYPos)
                        pawn.evolvePawnToQuen(self.specialRec)
                        return False
        return True


    def getListOfMoves(self, pawn, enemyPawnList, board):

        listOfPossibleMoves = []
        if pawn.isQueen == False:
            listOfPossibleMoves = self.getListOfPawnMoves(pawn, enemyPawnList, board)

        elif pawn.isQueen == True:
            listOfPossibleMoves = self.getListOfQueenMoves(pawn, enemyPawnList, board)

        return listOfPossibleMoves


    def getListOfPawnMoves(self, pawn, enemyPawnList, board):
        listOfPossibleMoves = []
        leftRectangleCords = (0, 0)
        rightRectangleCords = (0, 0)

        pawnX = pawn.coordinateX
        pawnY = pawn.coordinateY

        if self.__color == (255, 0, 0):
            leftRectangleCords = (pawnX + 100, pawnY + 100)
            rightRectangleCords = (pawnX - 100, pawnY + 100)

        elif self.__color == (0, 0, 255):
            leftRectangleCords = (pawnX + 100, pawnY - 100)
            rightRectangleCords = (pawnX - 100, pawnY - 100)

        listOfPossibleMoves.append(leftRectangleCords)
        listOfPossibleMoves.append(rightRectangleCords)

        for rectangle in listOfPossibleMoves:
            moveCordsX, moveCordsY = rectangle
            if not self.isMovePossible(enemyPawnList, self.pawnList, board.matrix, moveCordsX, moveCordsY): #Global
                listOfPossibleMoves.remove(rectangle)
                #rectangleToCheckX
        return listOfPossibleMoves


    def getListOfQueenMoves(self, pawn, enemyPawnList, board):

        listOfPossibleMoves = []

        listOfVectors= [(100, 100), (100, -100), (-100, 100), (-100, -100)]
        for vector in listOfVectors:
            vectorX, vectorY = vector

            pawnX = pawn.coordinateX
            pawnY = pawn.coordinateY

            while True:
                pawnX += vectorX
                pawnY += vectorY
                if not board.isRecInMatrix(pawnX, pawnY):
                    break
                if self.isPawnInList(pawnX, pawnY, self.pawnList):
                    break
                if self.isPawnInList(pawnX, pawnY, enemyPawnList):
                    break
                else:
                    listOfPossibleMoves.append((pawnX, pawnY))



        return listOfPossibleMoves


    def searchingPriorityPawns(self, enemyPawnList, board):
        priorityPawns = []

        for pawn in self.pawnList:
            x = pawn.coordinateX
            y = pawn.coordinateY

            listOfNearEnemyPawns = self.isEnemyNear(x, y, enemyPawnList)
            listOfVectors = [(100, 100), (100, -100), (-100, 100), (-100, -100)]

            if pawn.isQueen == False:
                if listOfNearEnemyPawns != []:
                    for enemyPawn in listOfNearEnemyPawns:
                        enemyX = enemyPawn.coordinateX
                        enemyY = enemyPawn.coordinateY
                        deltaX = enemyX - x
                        deltaY = enemyY - y
                        if self.isRectangleEmpty(enemyX + deltaX, enemyY + deltaY, self.pawnList, enemyPawnList, board):
                            priorityPawns.append(pawn)
            elif pawn.isQueen == True:

                for vector in listOfVectors:
                    vectorX, vectorY = vector

                    pawnX = x
                    pawnY = y
                    enemy = 0

                    while True:
                        pawnX += vectorX
                        pawnY += vectorY
                        if not board.isRecInMatrix(pawnX, pawnY):
                            break
                        if self.isPawnInList(pawnX, pawnY, self.pawnList):
                            break
                        if enemy == 1 and self.isMovePossible(enemyPawnList, self.pawnList, board.matrix, pawnX,
                                                              pawnY):
                            priorityPawns.append(pawn)
                        if self.isPawnInList(pawnX, pawnY, enemyPawnList):
                            enemy += 1
                        if enemy >= 2:
                            break

        return priorityPawns


    def isEnemyNear(self, x, y, listOfEnemyPawns):
        listOfNearEnemyPawns = []
        for pawn in listOfEnemyPawns:

            if pawn.coordinateX == (x + 100) and pawn.coordinateY == (y + 100):
                listOfNearEnemyPawns.append(pawn)

            elif pawn.coordinateX == (x + 100) and pawn.coordinateY == (y - 100):
                listOfNearEnemyPawns.append(pawn)

            elif pawn.coordinateX == (x - 100) and pawn.coordinateY == (y + 100):
                listOfNearEnemyPawns.append(pawn)

            elif pawn.coordinateX == (x - 100) and pawn.coordinateY == (y - 100):
                listOfNearEnemyPawns.append(pawn)

        return listOfNearEnemyPawns


    def getListOfBeatings(self, choosenPawn, listOfPossibleMoves, listOfEnemyPawns, board):

        listOfBeatings = []
        if choosenPawn.isQueen == False:
            listOfBeatings = self.getListOfPawnBeatings(choosenPawn, listOfPossibleMoves, listOfEnemyPawns, board)

        elif choosenPawn.isQueen == True:
            listOfBeatings = self.getListOfQueenBeatings(choosenPawn, listOfPossibleMoves, listOfEnemyPawns, board)

        return listOfBeatings


    def getListOfPawnBeatings(self, choosenPawn, listOfPossibleMoves, listOfEnemyPawns, board):
        listOfBeatings = []
        listOfNearEnemyPawns = self.isEnemyNear(choosenPawn.coordinateX, choosenPawn.coordinateY, listOfEnemyPawns)

        if len(listOfNearEnemyPawns) != 0:
            for enemyPawn in listOfNearEnemyPawns:

                enemyPawnX = enemyPawn.coordinateX
                enemyPawnY = enemyPawn.coordinateY
                deltaX = enemyPawnX - choosenPawn.coordinateX
                deltaY = enemyPawnY - choosenPawn.coordinateY
                if self.isMovePossible(self.pawnList, listOfEnemyPawns, board.matrix, enemyPawnX + deltaX, enemyPawnY + deltaY):
                    listOfBeatings.append((enemyPawnX + deltaX,  enemyPawnY + deltaY))

            if len(listOfBeatings) != 0:
                listOfPossibleMoves.clear()
                listOfPossibleMoves = listOfBeatings

        return listOfPossibleMoves


    def getListOfQueenBeatings(self, choosenPawn, listOfPossibleMoves, listOfEnemyPawns, board):

        listOfPossibleBeatings = []
        listOfVectors= [(100, 100), (100, -100), (-100, 100), (-100, -100)]
        for vector in listOfVectors:
            vectorX, vectorY = vector

            pawnX = choosenPawn.coordinateX
            pawnY = choosenPawn.coordinateY
            enemy = 0

            while True:
                pawnX += vectorX
                pawnY += vectorY
                if not board.isRecInMatrix(pawnX, pawnY):
                    break
                if self.isPawnInList(pawnX, pawnY, self.pawnList):
                    break
                if enemy == 1 and self.isMovePossible(listOfEnemyPawns ,self.pawnList, board.matrix, pawnX, pawnY):
                    listOfPossibleBeatings.append((pawnX, pawnY))
                if self.isPawnInList(pawnX, pawnY, listOfEnemyPawns):
                    enemy += 1
                if enemy >= 2:
                    break
        if len(listOfPossibleBeatings) == 0:
            listOfPossibleBeatings = listOfPossibleMoves

        return listOfPossibleBeatings


    def killPawn(self, x, y):

        for pawn in self.pawnList:
            if pawn.coordinateX == x and pawn.coordinateY == y:
                self.pawnList.remove(pawn)


    def isPawnInList(self, x, y, pawnList):
        for pawn in pawnList:
            if x == pawn.coordinateX and y == pawn.coordinateY:
                return True
        return False
