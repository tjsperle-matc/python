#!/usr/bin/env python3

import socket

serverAddress = input('Enter Servers IPV4 Address\n')
serverPort = 5000
myServerInfo = (serverAddress, serverPort)
dataFromUser = ''

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(myServerInfo)

while dataFromUser != 'EOF':
	dataFromUser = input('What should we send to the server: ')
	dataToSend = dataFromUser.encode()
	print(f'~ Sending {dataToSend} to the server')
	clientSocket.send(dataToSend)
	dataReceived = clientSocket.recv(1024)
	print('~ We received data from the server', dataReceived.decode(), '\n')


print(f'Closing the connection to {serverAddress}: {serverPort}')
clientSocket.close

