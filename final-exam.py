#!/usr/bin/env python3

import argparse
import sys
import requests
from bs4 import BeautifulSoup
import json
import socket

parser = argparse.ArgumentParser(description="This is Tyler Sperle's Final")

parser.add_argument('-ip', '--internetprotocol', dest='myIP', metavar='[an IP address]',
type=str, required=False, help='Enter an IP')

parser.add_argument('-f', '--integer', dest='varInteger', metavar='[an integer]',
type=int, required=False, help='Enter 1,2,3,4,5')

args = parser.parse_args()
url = (f'http://{args.myIP}/q{args.varInteger}')
ip = (f'{args.myIP}')

print('Name: Tyler Sperle')
print(url)

def get_response(url):
	res = requests.get(url)
	print(f'ANSWER: {res.text[:250]}')

def parse_string(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text, 'html.parser')
	element = soup.find_all('h3')
	h3 = str(element)
	answer = h3[7:][:-7][::3]
	print(f'ANSWER: {answer}')

def parse_header(url):
	res = requests.get(url)
	header = res.headers['MATC-HEADER']
	print(f'ANSWER: {header}')

def parse_json(url):
	jsonRes = requests.get(url)
	dictRes = json.loads(jsonRes.text)
	for key in dictRes.keys():
		author = str(dictRes[key])
		answer = author[225:][:-97]
		print(f'ANSWER: {answer}')

def socket_client(ip):
	serverAddress = ip
#	serverPortRange = range(5000,6001)
	serverPort = 5150
	myServerInfo = (serverAddress, serverPort)
	dataFromUser = ''
#	for Port in serverPortRange:
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#	try:
	clientSocket.connect(myServerInfo)

	while dataFromUser != 'EOF':
		dataFromUser = input()
		dataToSend = dataFromUser.encode()
		clientSocket.send(dataToSend)
		dataReceived = clientSocket.recv(1024)
		print('ANSWER:', dataReceived.decode(), '\n')
		return

	print(f'Closing the connection to {serverAddress}: {serverPort}')
	clientSocket.close

if args.varInteger == 1:
	get_response(url)

if args.varInteger == 2:
	parse_string(url)

if args.varInteger == 3:
	parse_header(url)

if args.varInteger == 4:
	parse_json(url)

if args.varInteger == 5:
	socket_client(ip)

if len(sys.argv) == 1:
    (parser.print_help())
    exit(0)

