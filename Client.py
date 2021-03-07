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
turn = 0


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
                turn, currentPlayer, enemyPlayer = game.singleRound(currentPlayer, enemyPlayer)

            # sending msg to server
            sendObject = (Network.id, currentPlayer, enemyPlayer)
            Network.sendingObjToServer(sendObject)
            game.gameUpdate(currentPlayer, enemyPlayer)


    Network.clientSocket.close()
