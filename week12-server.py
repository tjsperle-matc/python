#!/usr/bin/env python3

import socket

myServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

myIP = ('172.20.1.1')
myPort = 5000
myServerInfo = (myIP, myPort)

print('Server Port:', myPort)

myServerSocket.bind(myServerInfo)

myServerSocket.listen(1)

while True:
	print(f'Waiting for a connection on {myIP}:{myPort}')
	myConnection, clientAddress = myServerSocket.accept()
	try:
		print(f'Connection established to {clientAddress}')
		while True:
			incomingData = myConnection.recv(1024)
			print(f'Received data: {incomingData}')
			if incomingData:
				print('Sending data back to the client')
				myConnection.sendall(incomingData)
			else:
				print(f'End of client data {clientAddress}')
				myConnection.close()
	except socket.error as mySocketError:
		print(f'Connection state: {myPort}::{mySocketError}')
		myConnection.close()
