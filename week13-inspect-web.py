#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

res = requests.get('https://notpurple.com')

print(f'Status Code: {res.status_code}')
soup = BeautifulSoup(res.text, 'html.parser')
for link in soup.find_all('a'):
	print(link.get('href'))
