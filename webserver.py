import socketserver

class EchoRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data=self.request.recv(1024)
        self.request.send(data)
        return

if __name__ == '__main__':
    import socket
    import threading

    address=('localhost',0)
    server=socketserver.TCPServer(address,EchoRequestHandler)
    ip,port=server.server_address

    t=threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#    s.connect((ip,port))
    s.bind((ip,port))
    s.listen(1)
    message=b'Hello World'
#    print('sending:"%s"'%message)
#    len_sent=s.send(message)

    response=s.recv(16)
    print('Received: "%s"'%response)

    server.shutdown()
    s.close()
    server.socket.close()
