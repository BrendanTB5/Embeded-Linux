#!/usr/bin/env python3

import socket

HOST = '10.0.2.15'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send("Hello".encode())

from_server = client.recv(4096)

client.close()

print (from_server)