import socket
import pickle
from Player import Player
from Network import Network


Network = Network()
Network.connect()

while True:

    msg = Network.clientSocket.recv(2048)
    print(msg.decode("utf-8"))
    newMsg = Network.send_and_recive("wysylam-1")
    print(newMsg)
    newMsg = Network.send_and_recive("wysylam-klient2")
    print(newMsg)
    newMsg = Network.send_and_recive("wysylam333")
    print(newMsg)
    Network.clientSocket.close()
