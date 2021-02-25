import socket
import pickle
from _thread import *
from Player import Player


def add_header(msg, headerSize):
    return bytes(f'{len(msg):<{headerSize}}', "utf-8") + msg


def client_thread(clientSocket):
    clientSocket.send(b'Welcome to server')
    while True:
        try:
            receivedMsg = clientSocket.recv(2048).decode('utf-8')
            print("Recived:" + receivedMsg)
            sendMsg = b'send-server'
            clientSocket.sendall(sendMsg)
        except:
            break
    print("Conection lost")
    clientSocket.close()

ip = "192.168.0.2"
port = 2140
address = (ip, port)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(address)
serverSocket.listen(1)

msg = pickle.dumps(Player((255, 0, 0)))
msg = add_header(msg, 10)


while True:
    clientSocket, clientAddress = serverSocket.accept()
    print(f"conection from {clientAddress}")
    start_new_thread(client_thread, (clientSocket,))
    # receivedMsg = clientSocket.recv(1024)
    # clientSocket.sendall(msg)
    # print(receivedMsg.decode("utf-8"))
