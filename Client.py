import socket
import pickle
from Player import Player
from Network import Network


Network = Network()
Network.connect()


receivedObject = Network.gettingObjFromServer()
print(receivedObject.xd)
