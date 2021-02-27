import socket
import pickle
from _thread import *
from Player import Player
from TestClass import TestClass


def add_header(msg, headerSize):
    return bytes(f'{len(msg):<{headerSize}}', "utf-8") + msg


def recivingObjectWithHeaders(clientSocket, HEADERSIZE):
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


def client_thread(clientSocket):
    clientSocket.send(b'Welcome to server')
    sendMsg = Player((420,30,50))
    while True:
        try:
            # reciving object
            receivedMsg = recivingObjectWithHeaders(clientSocket, 10)
            #sending object
            sendMsgPicle = pickle.dumps(sendMsg)
            sendMsgPicle = add_header(sendMsgPicle, 10)
            clientSocket.sendall(sendMsgPicle)
        except:
            break
    print("Conection lost")
    clientSocket.close()

ip = "192.168.0.105"
port = 2140
address = (ip, port)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(address)
serverSocket.listen(2)





while True:
    clientSocket, clientAddress = serverSocket.accept()
    print(f"conection from {clientAddress}")
    start_new_thread(client_thread, (clientSocket,))
    # receivedMsg = clientSocket.recv(1024)
    # clientSocket.sendall(msg)
    # print(receivedMsg.decode("utf-8"))
