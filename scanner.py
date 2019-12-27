#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])	#Translate hostname to IPv4

else:
	print("Invalid amount of arguments.")
	print("python3 scanner.py <ip>")
	sys.exit()

print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(1,65535):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = sock.connect_ex((target,port)) #returns an error indicator 0,1
		if result == 0:
			print("Port {} is open".format(port))
		sock.close()
except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
