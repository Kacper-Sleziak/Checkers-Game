import socket
import pickle
import time
import pygame
from Game import Game
from Player import Player
from Network import Network
from Menu import Menu
from HotSeat import HotSeat

# initialization
HEIGHT = 800
WIDTH = 800
pygame.init()
window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Checkers")
icon = pygame.image.load('chess-board.png')
pygame.display.set_icon(icon)

currentPlayer = Player((255, 0, 0))
enemyPlayer = Player((0, 0, 255))
turn = 0
Network = Network()
game = Game(window)
hotSeat = HotSeat(WIDTH, HEIGHT, window, currentPlayer, enemyPlayer, game)
menu = Menu(WIDTH, HEIGHT, window)

#Menu
gameType = menu.menuDisplay()

#Game
if gameType == "Hot-seat":
    hotSeat.hotSeatGame()
elif gameType == "Multi-player":
    Network.connect()
    id = Network.recivingObjectWithHeaders(Network.clientSocket, Network.HEADERSIZE)
    Network.id = id

    if Network.id == 0:
        currentPlayer = Player((255, 0, 0))
        enemyPlayer = Player((0, 0, 255))
    elif Network.id == 1:
        currentPlayer = Player((0, 0, 255))
        enemyPlayer = Player((255, 0, 0))

    if id == "not conected":
        print(f"Welcome, server i full.. you fool !")
        Network.clientSocket.close()
    else:
        print(f"Welcome to server, you are -> {Network.id} player")
        while True:

            # reciving msg from server
            if turn != id:
                newMsg = Network.recivingObjFromServer()
                print(f"turn = {newMsg[0]}")
                turn = newMsg[0]
                currentPlayer = newMsg[1]
                enemyPlayer = newMsg[2]
                game.gameUpdate(currentPlayer, enemyPlayer)

            if turn == id :
                # plaing turn
                if turn == Network.id:
                    ending, currentPlayer, enemyPlayer = game.singleRound(currentPlayer, enemyPlayer)
                    turn = (turn + 1) % 2

                # sending msg to server
                sendObject = (Network.id, currentPlayer, enemyPlayer)
                Network.sendingObjToServer(sendObject)
                game.gameUpdate(currentPlayer, enemyPlayer)


        Network.clientSocket.close()
