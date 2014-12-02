import socketserver
class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            dataReceived = self.request.recv(1024)
            if not dataReceived:
                break

            self.request.send(dataReceived)

myServer = socketserver.ThreadingTCPServer(('',8881), MyHandler)
myServer.serve_forever()
