import socket
import pickle
from Player import Player
from TestClass import TestClass

class Network():
    def __init__(self):
        self.address = ("192.168.0.2", 2140)
        self.HEADERSIZE = 10
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.id = 0

    def connect(self):
        self.clientSocket.connect(self.address)

    def sendingAndGettingObjFromServer(self, sendObject):
        try:
            #sending object
            sendMsg = pickle.dumps(sendObject)
            sendMsg = self.add_header(sendMsg, 10)
            self.clientSocket.send(sendMsg)
            #getting object
            receivedObject = self.recivingObjectWithHeaders(self.clientSocket, 10)
            return receivedObject
        except:
            pass


    def recivingObjectWithHeaders(self, clientSocket, HEADERSIZE):
        fullMsg = b''
        newMsg = True
        running = True
        while running:
            msg = clientSocket.recv(16)
            if newMsg:
                newMsg = False
                msgLen = int(msg[:HEADERSIZE])

            fullMsg +=msg

            if len(fullMsg) == msgLen + HEADERSIZE:
                receivedObject = pickle.loads(fullMsg[HEADERSIZE:])
                running = False

        return receivedObject

    def add_header(self, msg, headerSize):
        return bytes(f'{len(msg):<10}', "utf-8") + msg
