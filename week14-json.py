#!/usr/bin/env python3

import argparse
import json
import requests
import sys

parser = argparse.ArgumentParser(description='idk')

parser.add_argument('-ip', '--internetprotocol', dest='myIP', metavar='[an IP address]', type=str, required=False, help='Enter an IP')

args = parser.parse_args()
url = 'http://ipinfo.io/172.217.8.206/json'
jsonResp = requests.get(url)
dictResp = json.loads(jsonResp.text)

for key in dictResp.keys():
	print(f'{key: <10}:{dictResp[key]: <10}')
