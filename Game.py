from Board import Board
from Player import Player
import pygame
from Drawings import Drawings
from GlobalFunctionality import GlobalFunctionality


class Game(GlobalFunctionality):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.round = "red"
        self.board = Board()
        self.choosenPawnX = 0
        self.choosenPawnY = 0
        self.listOfMoves = []

    def mainLoop(self):

        priorityPawns = []
        running = True
        isPawnChoosed = False  # about mouse click
        redPlayer = Player((255, 0, 0))
        bluePlayer = Player((0, 0, 255))

        thisPawnList = redPlayer.getPawnList()
        otherPawnList = bluePlayer.getPawnList()
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
                    mouseXPos, mouseYPos = self.centerCoordinates(mouseXPos, mouseYPos, self.board.getMatrix())

                    if not isPawnChoosed:
                        isPawnChoosed = currentPlayer.roundChosingPawn(mouseXPos, mouseYPos, priorityPawns)
                        if isPawnChoosed:
                            self.setChoosenPawnX(mouseXPos)
                            self.setChoosenPawnY(mouseYPos)
                            self.listOfMoves = currentPlayer.getListOfMoves(self.choosenPawnX, self.choosenPawnY, self.round, otherPawnList, self.board)
                            self.listOfMoves = currentPlayer.getListOfBeatings( self.choosenPawnX, self.choosenPawnY, self.listOfMoves, otherPawnList, self.board.getMatrix())

                    elif isPawnChoosed:
                         # jesli pomiedzy ruchem i obecna pozycja jest enemy i jesli ruch jest dozwolony, usun tego wroga
                        posibleEnemyX = 0.5 * (mouseXPos - self.choosenPawnX) + self.choosenPawnX
                        posibleEnemyY = 0.5 * (mouseYPos - self.choosenPawnY) + self.choosenPawnY
                        indyjskaZmiennaPomocnicza = 0
                        if self.isMovePossible(otherPawnList, currentPlayer.getPawnList(), self.board.getMatrix(), mouseXPos, mouseYPos) and \
                            self.isEnemyThere(posibleEnemyX, posibleEnemyY, otherPawnList):
                            otherPlayer.killPawn(posibleEnemyX, posibleEnemyY)
                            indyjskaZmiennaPomocnicza = 1
                        isPawnChoosed = currentPlayer.roundMovingPawn(mouseXPos, mouseYPos, self.listOfMoves, self.choosenPawnX, self.choosenPawnY)
                        self.listOfMoves.clear()
                        if isPawnChoosed == False and indyjskaZmiennaPomocnicza == 1:
                            self.listOfMoves = currentPlayer.getListOfBeatings(mouseXPos, mouseYPos, self.listOfMoves, otherPawnList, self.board.getMatrix())
                            print(f"{self.listOfMoves}, lista mozliwych bic po biciu")


                        if isPawnChoosed == False and len(self.listOfMoves) == 0:
                            if self.round == "red":
                                self.setRound("blue")
                                currentPlayer = bluePlayer
                                otherPlayer = redPlayer
                                otherPawnList = redPlayer.getPawnList()
                                thisPawnList = bluePlayer.getPawnList()
                                print(self.getRound())
                            else:
                                self.setRound("red")
                                currentPlayer = redPlayer
                                otherPlayer = bluePlayer
                                otherPawnList = bluePlayer.getPawnList()
                                thisPawnList = redPlayer.getPawnList()
                                print(self.getRound())

                            self.listOfMoves.clear()
                            priorityPawns.clear()

            self.gameUpdate(redPlayer, bluePlayer)

    def gameUpdate(self, redPlayer, bluePlayer):
        drawings = Drawings(self.window)

        self.window.fill((255, 255, 255))
        drawings.drawBoard(self.board)
        drawings.drawPawns(redPlayer.getPawnList())
        drawings.drawPawns(bluePlayer.getPawnList())
        drawings.drawPosibleMoves(self.window, self.listOfMoves)
        pygame.display.update()

    def getWindow(self):
        return self.window

    def getChoosenPawnX(self):
        return self.choosenPawnX

    def getChoosenPawnY(self):
        return self.choosenPawnY

    def getRound(self):
        return self.round

    def setChoosenPawnX(self, newX):
        self.choosenPawnX = newX

    def setChoosenPawnY(self, newY):
        self.choosenPawnY = newY

    def setListOfMoves(self, newListOfMoves):
        self.listOfMoves = newListOfMoves

    def setRound(self, newRound):
        self.round = newRound
