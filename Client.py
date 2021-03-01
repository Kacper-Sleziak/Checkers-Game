import socket
import pickle
import time
import pygame
from Game import Game
from Player import Player
from TestClass import TestClass
from Network import Network


HEIGHT = 800
WIDTH = 800
pygame.init()
window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Checkers")
icon = pygame.image.load('chess-board.png')
pygame.display.set_icon(icon)
game = Game(window, "single player")
turn = 0


Network = Network()
Network.connect()
currentPlayer = Player((255, 0, 0))
enemyPlayer = Player((0, 0, 255))


id = Network.recivingObjectWithHeaders(Network.clientSocket, Network.HEADERSIZE)
Network.id = id

if id == "not conected":
    print(f"Welcome, server i full.. you fool !")
    Network.clientSocket.close()
else:
    print(f"Welcome to server, you are -> {Network.id} player")
    while True:

        ending, currentPlayer, otherPlayer = game.singleRound(currentPlayer, enemyPlayer)

        #sendObject = (currentPlayer, otherPlayer)
        newMsg = Network.sendingAndGettingObjFromServer(currentPlayer)
        print(f"newMsg = {newMsg}")

    Network.clientSocket.close()
