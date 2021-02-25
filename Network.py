import socket
import pickle
from Player import Player

class Network():
    def __init__(self):
        self.address = ("192.168.0.2", 2140)
        self.HEADERSIZE = 10
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.serverSocket

    def connect(self):
        self.clientSocket.connect(self.address)

    def gettingObjFromServer(self):
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
                receivedObject = pickle.loads(fullMsg[self.HEADERSIZE:])
                isNewMsg = True
                fullMsg = b''

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
