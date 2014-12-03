import socket
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',10000)
#This is not a bug
print('starting up on %s port %d' % server_address,file=sys.stderr)
sock.bind(server_address)
sock.listen(1)

content=b'''HTTP/1.x 200 OK
Content-Type:text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
</html>>
'''
#f = open('index.html','rb')
#content = content + f.read()
#f.close()

while True:
    print('waitong for a connection',file=sys.stderr)
    connection,client_address = sock.accept()

    try:
        print('connection from',client_address,file=sys.stderr)

        while True:
            data = connection.recv(1024)
            if data:
                connection.sendall(content)
            else:
                break
    finally:
        connection.close()
