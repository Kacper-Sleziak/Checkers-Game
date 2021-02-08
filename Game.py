from Board import Board
from Player import Player
from Pawn import Pawn
from Drawings import Drawings
from GlobalFunctionality import GlobalFunctionality
import pygame


class Game(GlobalFunctionality):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.round = "red"
        self.board = Board()
        self.choosenPawn = Pawn(69, 420, (21,3,7))
        self.listOfMoves = []

    def mainLoop(self):

        priorityPawns = []
        running = True
        isPawnChoosed = False  # about mouse click
        redPlayer = Player((255, 0, 0))
        bluePlayer = Player((0, 0, 255))

        thisPawnList = redPlayer.pawnList
        otherPawnList = bluePlayer.pawnList
        currentPlayer = redPlayer
        otherPlayer = bluePlayer

        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                priorityPawns = currentPlayer.searchingPriorityPawns(otherPawnList, self.board)

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
                            self.listOfMoves = currentPlayer.getListOfMoves(self.choosenPawn, otherPawnList, self.board)
                            self.listOfMoves = currentPlayer.getListOfBeatings(self.choosenPawn, self.listOfMoves, otherPawnList, self.board.matrix)

                    elif isPawnChoosed:
                         # jesli pomiedzy ruchem i obecna pozycja jest enemy i jesli ruch jest dozwolony, usun tego wroga
                        posibleEnemyX = 0.5 * (mouseXPos - self.choosenPawn.coordinateX) + self.choosenPawn.coordinateX
                        posibleEnemyY = 0.5 * (mouseYPos - self.choosenPawn.coordinateY) + self.choosenPawn.coordinateY
                        pawnKilledEnemy = 0
                        if self.isMovePossible(otherPawnList, currentPlayer.pawnList, self.board.matrix, mouseXPos, mouseYPos) and \
                            self.isEnemyThere(posibleEnemyX, posibleEnemyY, otherPawnList):
                            otherPlayer.killPawn(posibleEnemyX, posibleEnemyY)
                            pawnKilledEnemy = 1
                        isPawnChoosed = currentPlayer.roundMovingPawn(mouseXPos, mouseYPos, self.listOfMoves, self.choosenPawn)

                        if isPawnChoosed == False:
                            self.listOfMoves.clear()
                            if pawnKilledEnemy == 1:
                                self.listOfMoves = currentPlayer.getListOfBeatings(self.choosenPawn, self.listOfMoves, otherPawnList, self.board.matrix)

                        if isPawnChoosed == False and len(self.listOfMoves) == 0:
                            if self.round == "red":
                                self.round = "blue"
                                currentPlayer = bluePlayer
                                otherPlayer = redPlayer
                                otherPawnList = redPlayer.pawnList
                                thisPawnList = bluePlayer.pawnList
                                print(self.round)
                            else:
                                self.round = "red"
                                currentPlayer = redPlayer
                                otherPlayer = bluePlayer
                                otherPawnList = bluePlayer.pawnList
                                thisPawnList = redPlayer.pawnList
                                print(self.round)

                            self.listOfMoves.clear()
                            priorityPawns.clear()

            self.gameUpdate(redPlayer, bluePlayer)

    def gameUpdate(self, redPlayer, bluePlayer):
        drawings = Drawings(self.window)

        self.window.fill((255, 255, 255))
        drawings.drawBoard(self.board)
        drawings.drawPawns(redPlayer.pawnList)
        drawings.drawPawns(bluePlayer.pawnList)
        drawings.drawPosibleMoves(self.window, self.listOfMoves)
        pygame.display.update()
