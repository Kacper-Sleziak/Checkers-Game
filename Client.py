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


msg = Network.clientSocket.recv(2048)
print(msg.decode("utf-8"))
while True:

    ending, currentPlayer, otherPlayer = game.singleRound(currentPlayer, enemyPlayer)

    #sendObject = (currentPlayer, otherPlayer)
    newMsg = Network.sendingAndGettingObjFromServer(currentPlayer)
    print(f"newMsg = {newMsg}")

    # newMsg = Network.sendingAndGettingObjFromServer(sendObject)
    # print(newMsg.x)
    # time.sleep(4)
    # newMsg = Network.sendingAndGettingObjFromServer(sendObject)
    # print(newMsg.x)
    # time.sleep(4)
    # newMsg = Network.sendingAndGettingObjFromServer(sendObject)
    # print(newMsg.x)
    # time.sleep(10)
    Network.clientSocket.close()
