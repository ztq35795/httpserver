import socketserver

server_address = ('localhost',10000)

class MYTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):

        tool=CreateAndJudge()
        request = self.request.recv(1024).decode('UTF-8')

        print('Connected by',self.client_address)
        print('Request is',request)

        method = request.split(' ')[0]
        src = request.split(' ')[1]

        if method == 'GET':
            if tool.isImageRequested(src):
                OutPutConcent = tool.GetImage()

            elif tool.isIndexRequested(src):
                OutPutConcent = tool.GetIndex()

            else:
                OutPutConcent = tool.Get404Page()

            self.request.sendall(OutPutConcent)

class CreateAndJudge():
    def __init__(self):
        self.t_content = b'''HTTP/1.x 200 OK
        Content-Type:text/html

        '''

        self.p_content = b'''HTTP/1.x 200 OK
        Content-Type:image/jpg

        '''

        self.NotFoundContent = b'''HTTP/1.x 404 Not Found
        Content-Type:text/html

        '''

    def GetIndex(self):
        f = open('index.html','rb')
        t_content = self.t_content + f.read()
        f.close()

        return t_content

    def GetImage(self):
        f = open('arch.jpg','rb')
        p_content = self.p_content + f.read()
        f.close()

        return p_content

    def Get404Page(self):
        f = open('404page.html','rb')
        NotFoundContent= self.NotFoundContent + f.read()
        f.close()
        return NotFoundContent

    def isIndexRequested(self,src):
        if src == '/' or src == '/index.html':
            return True

        else:
            return False

    def isImageRequested(self,src):
        if src == '/arch.jpg':
            return True

        else:
            return False



server = socketserver.TCPServer(server_address,MYTCPHandler)

server.serve_forever()
