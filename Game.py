from Board import Board
from Player import Player
from Pawn import Pawn
from Drawings import Drawings
from GlobalFunctionality import GlobalFunctionality
import pygame


class Game(GlobalFunctionality):

    def __init__(self, window, gameMode):
        super().__init__()
        self.window = window
        self.round = "red"
        self.board = Board()
        self.choosenPawn = Pawn(69, 420, (21,3,7))
        self.listOfMoves = []
        self.gameMode = gameMode

    def mainLoop(self):

        priorityPawns = []
        running = True
        isPawnChoosed = False  # about mouse click
        redPlayer = Player((255, 0, 0))
        bluePlayer = Player((0, 0, 255))

        currentPlayer = redPlayer
        otherPlayer = bluePlayer

        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                priorityPawns = currentPlayer.searchingPriorityPawns(otherPlayer.pawnList, self.board)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        isPawnChoosed = False
                        self.listOfMoves.clear()
                        self.gameUpdate(redPlayer, bluePlayer)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseXPos, mouseYPos = pygame.mouse.get_pos()
                    mouseXPos, mouseYPos = self.centerCoordinates(mouseXPos, mouseYPos, self.board.matrix)

                    if not isPawnChoosed:
                        isPawnChoosed = currentPlayer.roundChosingPawn(mouseXPos, mouseYPos, priorityPawns)
                        if isPawnChoosed != False:
                            self.choosenPawn = isPawnChoosed
                            isPawnChoosed = True
                            self.listOfMoves = currentPlayer.getListOfMoves(self.choosenPawn, otherPlayer.pawnList, self.board)
                            self.listOfMoves = currentPlayer.getListOfBeatings(self.choosenPawn, self.listOfMoves, otherPlayer.pawnList, self.board)

                    elif isPawnChoosed:
                         # jesli pomiedzy ruchem i obecna pozycja jest enemy i jesli ruch jest dozwolony, usun tego wroga
                        pawnKilledEnemy = 0

                        if self.isMoveInListOfMoves(mouseXPos, mouseYPos, self.listOfMoves):
                            vector = self.checkVectorDirection(self.choosenPawn, mouseXPos, mouseYPos)
                            vectorX, vectorY = vector
                            positionX = self.choosenPawn.coordinateX
                            positionY = self.choosenPawn.coordinateY
                            while (positionX != mouseXPos and positionY != mouseYPos):
                                positionX += vectorX
                                positionY += vectorY
                                if self.isEnemyThere(positionX, positionY, otherPlayer.pawnList):
                                    otherPlayer.killPawn(positionX, positionY)
                                    pawnKilledEnemy = 1


                        isPawnChoosed = currentPlayer.roundMovingPawn(mouseXPos, mouseYPos, self.listOfMoves, self.choosenPawn)
                        self.gameUpdate(redPlayer, bluePlayer)
                        if isPawnChoosed == False:
                            self.listOfMoves.clear()
                            if pawnKilledEnemy == 1:
                                self.listOfMoves = currentPlayer.getListOfBeatings(self.choosenPawn, self.listOfMoves, otherPlayer.pawnList, self.board)

                        if isPawnChoosed == False and len(self.listOfMoves) == 0:
                            if self.round == "red":
                                self.round = "blue"
                                currentPlayer = bluePlayer
                                otherPlayer = redPlayer
                            else:
                                self.round = "red"
                                currentPlayer = redPlayer
                                otherPlayer = bluePlayer

                            self.listOfMoves.clear()
                            priorityPawns.clear()

                    print(len(currentPlayer.pawnList))
                    if len(currentPlayer.pawnList) == 0:
                        print(f"The end!")
                        running = False

            self.gameUpdate(redPlayer, bluePlayer)

    def gameUpdate(self, redPlayer, bluePlayer):
        drawings = Drawings(self.window)

        self.window.fill((255, 255, 255))
        drawings.drawBoard(self.board)
        drawings.drawPawns(redPlayer.pawnList)
        drawings.drawPawns(bluePlayer.pawnList)
        drawings.drawPosibleMoves(self.window, self.listOfMoves)
        pygame.display.update()
