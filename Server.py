import socket
import pickle
from Player import Player


def add_header(msg, headerSize):
    return bytes(f'{len(msg):<{headerSize}}', "utf-8") + msg


ip = "192.168.0.2"
port = 2140
address = (ip, port)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(address)
serverSocket.listen()

msg = pickle.dumps(Player((255, 0, 0)))
msg = add_header(msg, 10)

while True:
    clientSocket, clientAddress = serverSocket.accept()
    print(f"conection from {clientAddress}")
    while True:

        receivedMsg = clientSocket.recv(1024)
        clientSocket.sendall(msg)
        print(receivedMsg.decode("utf-8"))
        
