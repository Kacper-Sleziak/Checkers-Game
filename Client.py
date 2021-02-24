import socket
import pickle
from Player import Player
from Network import Network


Network = Network()
Network.connect()

while True:

    Network.sendingToServer()
    receivedObject = Network.gettingObjFromServer()
    print(receivedObject.xd)
    
