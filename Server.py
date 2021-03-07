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


def changeTurn(turn):
    turn = (turn + 1) % 2
    return turn


def client_thread(clientSocket, enemySocket, id):
    global redPlayer
    global bluePlayer
    global turn
    idSend = pickle.dumps(id)
    idSend = add_header(idSend, 10)
    clientSocket.send(idSend)
    while True:

        try:
            if id == turn:
                # reciving object
                receivedMsg = recivingObjectWithHeaders(clientSocket, 10)
                # change current player position
                if id == 0:
                    redPlayer = receivedMsg[1]
                    print("send red")
                    bluePlayer = receivedMsg[2]
                elif id == 1:
                    redPlayer = receivedMsg[2]
                    bluePlayer = receivedMsg[1]
                    print("send blue")
                # change turn
                print(f'turn = {turn}, id = {id}')
                turn = changeTurn(turn)
                #sending object
                if id == 0:
                    ToMe = (turn, redPlayer, bluePlayer)
                    ToEnemy = (turn, bluePlayer, redPlayer)
                elif id == 1:
                    ToMe = (turn, bluePlayer, redPlayer)
                    ToEnemy = (turn, redPlayer, bluePlayer)
                # sending to my client
                picleToMe = pickle.dumps(ToMe)
                picleToMe = add_header(picleToMe, 10)
                #clientSocket.sendall(picleToMe)
                # sending to enemy client
                picleToEnemy = pickle.dumps(ToEnemy)
                picleToEnemy = add_header(picleToEnemy, 10)
                enemySocket.sendall(picleToEnemy)

            # else:
            #
            #     # reciving object
            #     receivedMsg = recivingObjectWithHeaders(clientSocket, 10)
            #
            #     if id == 0:
            #         #redPlayer = receivedMsg[1]
            #         bluePlayer = receivedMsg[2]
            #     elif id == 1:
            #         redPlayer = receivedMsg[2]
            #         #bluePlayer = receivedMsg[1]
        except:
            pass

    print("Conection lost")
    clientSocket.close()


ip = "192.168.0.2"
port = 2140
address = (ip, port)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(address)
serverSocket.listen(2)
conectedPayers = 0 # id
redPlayer = Player((255,0,0))
bluePlayer = Player((0,0,255))
turn = 0


while True:

    clientSocket, clientAddress = serverSocket.accept()
    print(f"conection from {clientAddress}")
    if conectedPayers == 0:
        print("waiting for enemy...")
        clientSocket0 = clientSocket
    elif conectedPayers == 1:
        clientSocket1 = clientSocket
        start_new_thread(client_thread, (clientSocket0, clientSocket1, 0,))
        start_new_thread(client_thread, (clientSocket1, clientSocket0, 1,))
    else:
        print("server is full")
        msg = pickle.dumps("not conected")
        msg = add_header(msg, 10)
        clientSocket.send(msg)


    conectedPayers +=1
