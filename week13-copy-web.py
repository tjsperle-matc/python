#!/usr/bin/env python3

import requests

res = requests.get('https://notpurple.com')
res.raise_for_status()
playFile = open('my_web_file.html', 'wb')
for chunk in res.iter_content(100000):
	playFile.write(chunk)

playFile.close()
