#!/usr/bin/env python3

# Dictionary containing FQDN to IP address mappings
FQDNtoIP = {'server1.testlab.com':'192.168.1.10', 'server2.testlab.com':'192.168.1.11', 'server3.testlab.com':'192.168.1.12',
'server4.testlab.com':'192.168.1.13', 'server5.testlab.com':'192.168.1.14', 'server6.testlab.com':'192.168.1.15'}

# List all of the FQDN's in the dictionary
print(FQDNtoIP.keys())

print("")

# List all of the IP's in the dictionsary
print(FQDNtoIP.values())

print("")

# List all of the full records (key/value pairs)
print(FQDNtoIP.items())

# Add server7 and server8
FQDNtoIP['server7.testlab.com'] = '192.168.1.16'

FQDNtoIP['server8.testlab.com'] = '192.168.1.17'

print("")

# Check for server2.testlab.com in dictionary
print('server2.testlab.com' in FQDNtoIP)

print("")

# Check for server10.testlab.com in dictionary
print('server10.testlab.com' in FQDNtoIP)
