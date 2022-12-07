import socket
import platform
import psutil
import sys
import os
import random

# Create a TCP/IP socket in order to grab server's IP address
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("8.8.8.8", 80))
IP = sock.getsockname()[0]
sock.close()

# Get the server's hostname
hostname = socket.gethostname()

# Get the server's OS
OperatinSystem = platform.system()

# Create the server's socket
serversocket = socket.socket()
host = IP
port = random.randint(1000, 9999)
try :
    serversocket.bind((host, port))
except socket.error as e:
    print(str(e))

# Listen for connections
serversocket.listen(5)
print(f"Server is listening on {host}:{port}")

