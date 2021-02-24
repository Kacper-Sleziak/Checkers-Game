import socket
import pickle
from Player import Player


class Client():
    def __init__(self):
        self.address = ("192.168.0.2", 2140)
        self.HEADERSIZE = 10
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.clientSocket.connect(self.address)

    def gettingMsgFromServer(self):
        fullMsg = b''
        isNewMsg = True
        msgLen = 0

        while True:

            msg = self.clientSocket.recv(16)
            if isNewMsg:
                msgLen = int(msg[:self.HEADERSIZE])
                print(f"len = {msgLen}")
                isNewMsg = False

            fullMsg += msg

            if len(fullMsg) == msgLen + self.HEADERSIZE:
                print(f"recive: {fullMsg[self.HEADERSIZE:]}")
                receivedObject = pickle.loads(fullMsg[self.HEADERSIZE:])
                print(f"xd = {receivedObject.xd}")
                isNewMsg = True
                fullMsg = b''

        return receivedObject
Client = Client()
Client.connect()
receivedObject = Client.gettingMsgFromServer()
print(receivedObject.xd)
