import socket
import pickle
from Player import Player
from TestClass import TestClass

class Network():
    def __init__(self):
        self.address = ("192.168.0.105", 2140)
        self.HEADERSIZE = 10
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.serverSocket

    def connect(self):
        self.clientSocket.connect(self.address)

    def sendingAndGettingObjFromServer(self, sendObject):

        try:

            sendMsg = pickle.dumps(sendObject)
            self.clientSocket.send(sendMsg)
            #getting object

            msg = self.clientSocket.recv(4096)

            receivedObject = pickle.loads(msg)
            print("tutaj")

        except:
            pass

    return receivedObject

    def sendingToServer(self):
        self.clientSocket.sendall(b'hello')

    def send_and_recive(self, data):
        try:
            self.clientSocket.send(str.encode(data))
            reply = self.clientSocket.recv(2048)
            reply = reply.decode("utf-8")
            return reply
        except:
            return 1
            pass
