import socketserver
from babywatcher_server.daemon import Daemon
from babywatcher_server.stream import Stream

# server constant
HOST = '0.0.0.0'
PORT = 5050
ADDR = (HOST, PORT)
BUFSIZE = 4096


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        if self.data == "getStreamUrl":
            stream_url = Stream.getStream()
            self.request.sendall(stream_url)
        elif self.data == "stopStream":
            Stream.stopStream()
            self.request.sendall("StreamClosed")


class BabyWatcherServer(Daemon):
    def run(self):
        serv = socketserver.TCPServer((HOST, PORT), TCPHandler)
        serv.serve_forever()
