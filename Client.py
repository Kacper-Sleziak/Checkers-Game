import socket
import pickle
import time
from Player import Player
from TestClass import TestClass
from Network import Network


Network = Network()
Network.connect()
currentPlayer = Player((255,0,0))
enemyPlayer = Player((0, 0, 255))
while True:

    msg = Network.clientSocket.recv(2048)
    print(msg.decode("utf-8"))

    running = True
    while running:
            running, currentPlayer, otherPlayer = game.singleRound(currentPlayer, enemyPlayer)

    sendObject = (currentPlayer, otherPlayer)
    newMsg = Network.sendingAndGettingObjFromServer(sendObject)
    # time.sleep(4)
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
