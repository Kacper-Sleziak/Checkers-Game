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
            pawnList.append(self.__createPawn(50, 50))
            pawnList.append(self.__createPawn(250, 50))
            pawnList.append(self.__createPawn(450, 50))
            pawnList.append(self.__createPawn(650, 50))

        elif self.__color == (0, 0, 255):
            pawnList.append(self.__createPawn(150, 750))
            pawnList.append(self.__createPawn(350, 750))
            pawnList.append(self.__createPawn(550, 750))
            pawnList.append(self.__createPawn(750, 750))

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
                if pawn.getCordinateX() == mouseXPos and pawn.getCordinateY() == mouseYPos:
                    return True
        else:
            for pawn in priorityPawns:
                if pawn.getCordinateX() == mouseXPos and pawn.getCordinateY() == mouseYPos:
                    return True

        return False

    def roundMovingPawn(self, mouseXPos, mouseYPos, listOfMoves, choosenPawnX, choosenPawnY):
        for pawn in self.pawnList:
            if pawn.getCordinateX() == choosenPawnX and pawn.getCordinateY() == choosenPawnY:
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

        pawnX = pawn.getCordinateX()
        pawnY = pawn.getCordinateY()

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
            if not self.isMovePossible(enemyPawnList, self.pawnList, board.getMatrix(), moveCordsX, moveCordsY): #Global
                listOfPossibleMoves.remove(rectangle)
                #rectangleToCheckX
        return listOfPossibleMoves

    def getListOfQueenMoves(self, pawn, enemyPawnList, board):

        listOfPossibleMoves = []

        pawnX = pawn.getCordinateX()
        pawnY = pawn.getCordinateY()
        print(f"pawnX = {pawnX}, pawnY = {pawnY},")
        listOfVectors= [(100, 100), (100, -100), (-100, -100), (-100, -100)]
        for vector in listOfVectors:
            i = 0
            enemy = 0
            vectorX, vectorY = vector

            while True:
                pawnX = pawnX + vectorX
                pawnY = pawnY + vectorY
                print(f"{pawnX}, {pawnY}")
                if not board.isRecInMatrix(pawnX, pawnY):
                    print("blad boarda")
                    break
                if self.isPawnInList(pawnX, pawnY, self.pawnList):
                    print("blad ally pawn")
                    break
                if self.isPawnInList(pawnX, pawnY, enemyPawnList):
                    enemy += 1
                    print("enemy pawn1")
                    if enemy >= 2:
                        print("enemy pawn2")
                        break

                enemy = 0
                print("bezbledu")
                listOfPossibleMoves.append((pawnX, pawnY))

        return listOfPossibleMoves


    def searchingPriorityPawns(self, enemyPawnList, board):
        priorityPawns = []

        for pawn in self.pawnList:
            x = pawn.getCordinateX()
            y = pawn.getCordinateY()

            listOfNearEnemyPawns = self.isEnemyNear(x, y, enemyPawnList)

            if listOfNearEnemyPawns != []:
                for enemyPawn in listOfNearEnemyPawns:
                    enemyX = enemyPawn.getCordinateX()
                    enemyY = enemyPawn.getCordinateY()
                    deltaX = enemyX - x
                    deltaY = enemyY - y
                    #print(f"{enemyX + deltaX},{enemyY + deltaY}")
                    if self.isRectangleEmpty(enemyX + deltaX, enemyY + deltaY, self.pawnList, enemyPawnList, board):
                        priorityPawns.append(pawn)

        return priorityPawns

    def isEnemyNear(self, x, y, listOfEnemyPawns):
        listOfNearEnemyPawns = []
        for pawn in listOfEnemyPawns:

            if pawn.getCordinateX() == (x + 100) and pawn.getCordinateY() == (y + 100):
                listOfNearEnemyPawns.append(pawn)

            elif pawn.getCordinateX() == (x + 100) and pawn.getCordinateY() == (y - 100):
                listOfNearEnemyPawns.append(pawn)

            elif pawn.getCordinateX() == (x - 100) and pawn.getCordinateY() == (y + 100):
                listOfNearEnemyPawns.append(pawn)

            elif pawn.getCordinateX() == (x - 100) and pawn.getCordinateY() == (y - 100):
                listOfNearEnemyPawns.append(pawn)

        return listOfNearEnemyPawns

    def getListOfBeatings(self, choosenPawnX, choosenPawnY, listOfPossibleMoves, listOfEnemyPawns, matrix):

        listOfBeatings = []
        listOfNearEnemyPawns = self.isEnemyNear(choosenPawnX, choosenPawnY, listOfEnemyPawns)

        if not len(listOfNearEnemyPawns) == 0:
            for enemyPawn in listOfNearEnemyPawns:

                enemyPawnX = enemyPawn.getCordinateX()
                enemyPawnY = enemyPawn.getCordinateY()
                deltaX = enemyPawnX - choosenPawnX
                deltaY = enemyPawnY - choosenPawnY
                if self.isMovePossible(self.pawnList, listOfEnemyPawns, matrix, enemyPawnX + deltaX, enemyPawnY + deltaY):
                    listOfBeatings.append((enemyPawnX + deltaX,  enemyPawnY + deltaY))

            if not len(listOfBeatings) == 0:
                listOfPossibleMoves.clear()
                listOfPossibleMoves = listOfBeatings

        return listOfPossibleMoves

    def returnPawnFromCords(self, cordX, cordY):
        for pawn in self.pawnList:
            if pawn.getCordinateX() == cordX and pawn.getCordinateY() == cordY:
                return pawn

        return False

    def getPawnList(self):
        return self.pawnList

    def movingPawn(self):
        pass

    def choosingPawn(self):
        pass

    def killPawn(self, x, y):

        for pawn in self.pawnList:
            if pawn.getCordinateX() == x and pawn. getCordinateY() == y:
                self.pawnList.remove(pawn)

    def isPawnInList(self, x, y, pawnList):
        for pawn in pawnList:
            if x == pawn.getCordinateX() and y == pawn.getCordinateY():
                return True
        return False
