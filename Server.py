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


def client_thread(clientSocket, id):
    global redPlayer
    global bluePlayer
    global turn
    id = pickle.dumps(id)
    id = add_header(id, 10)
    clientSocket.send(id)
    #sendMsg = Player((420,30,50))
    while True:

        try:
            # reciving object
            receivedMsg = recivingObjectWithHeaders(clientSocket, 10)
            id = receivedMsg[0]
            if id == turn:
                if id == 0:
                    redPlayer = receivedMsg[1]
                    #bluePlayer = receivedMsg[2]
                    print("q1")
                elif id == 1:
                    #redPlayer = receivedMsg[2]
                    bluePlayer = receivedMsg[1]
                    print("q2")
            #sending object
            if id == 0:
                sendMsg = (turn, redPlayer, bluePlayer)
                print("q3")
            elif id == 1:
                sendMsg = (turn, bluePlayer, redPlayer)
                print("q4")

            sendMsgPicle = pickle.dumps(sendMsg)
            sendMsgPicle = add_header(sendMsgPicle, 10)
            clientSocket.sendall(sendMsgPicle)
            print (turn)
            turn = changeTurn(turn)
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
        start_new_thread(client_thread, (clientSocket0, 0,))
        start_new_thread(client_thread, (clientSocket1, 1,))
    else:
        print("server is full")
        msg = pickle.dumps("not conected")
        msg = add_header(msg, 10)
        clientSocket.send(msg)


    conectedPayers +=1
