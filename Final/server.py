#!/usr/bin/env python3

import socket

HOST = socket.gethostname()
PORT = 8080

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	serv.bind((HOST, PORT))

except socket.error as msg:
	print ('Bind failed. Error Code: ' + str(msg[0] + ' Message ' + msg[1]))
	sys.exit()

print ('Successfully bound to ' + str(HOST) + ' on port ' + str(PORT))

serv.listen(5)
print('Now listening...')


while True:
    conn, addr = serv.accept()
    print('Connected to ' + addr[0] + ':' + str(addr[1]))
    from_client = ''

    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data.decode()
        print (from_client)

        conn.send("I am SERVER\n".encode())

    conn.close()
    print ('client disconnected')
