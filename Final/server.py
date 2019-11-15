#!/usr/bin/env python3

import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(('137.112.234.99', 8000))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    from_client = ''

    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data
        print (from_client)

        conn.send("I am SERVER\n")

    conn.close()
    print ('client disconnected')
