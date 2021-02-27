import socket
import pickle
from _thread import *
from Player import Player
from TestClass import TestClass


def add_header(msg, headerSize):
    return f'{len(msg):<{headerSize}}', "utf-8" + msg


def client_thread(clientSocket):
    clientSocket.send(b'Welcome to server')
    sendMsg = Player((420,30,50))
    while True:
        try:
            receivedMsg = clientSocket.recv(4096)
            print("tutaj")
            d = pickle.loads(receivedMsg)
            print(d.x)
            sendMsgPicle = pickle.dumps(sendMsg)
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
