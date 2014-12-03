import socket
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',10000)
#This is not a bug
print('starting up on %s port %d' % server_address,file=sys.stderr)
sock.bind(server_address)
sock.listen(3)

content=b'''HTTP/1.x 200 OK
Content-Type:text/html

'''
f = open('index.html','rb')
t_content = content + f.read()
f.close()

content=b'''HTTP/1.x 200 OK
Content-Type:image/jpg

'''
f = open('arch.jpg','rb')
p_content = content + f.read()
f.close

while True:
    connection,client_address = sock.accept()
    request = connection.recv(1024).decode('UTF-8')
    method = request.split(' ')[0]
    src = request.split(' ')[1]

    if method == 'GET':
        print('Connected by',client_address)
        print('Request is',request)

        if src == '/arch.jpg':
            outputcontent=p_content

        else:
            outputcontent=t_content

        connection.sendall(outputcontent)

    connection.close()
