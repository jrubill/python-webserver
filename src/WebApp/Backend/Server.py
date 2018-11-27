import socket
import WebApp.Config as Config
import threading
from WebApp.Backend import request_handler as rh
import signal

class Server(object):
    def __init__(self, IP_ADDR='localhost', PORT=5000):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.IP_ADDR, self.PORT = IP_ADDR, PORT
        self.socket.bind((IP_ADDR, PORT))
        self.threads = list()
        signal.signal(signal.SIGTERM, self.die)

    def run(self):
        self.socket.listen(1)
        while True:
            conn, addr = self.socket.accept()
            print("Connected by", addr)
            new_client = threading.Thread(target=Server.handle_client, args=(self,conn,))
            self.threads.append(new_client)
            new_client.start()

    def handle_client(self, conn):
        data = conn.recv(1024)
        response = rh.handle_request(data.decode('US-ASCII'))
        try:
            conn.send(response.encode()) 
        except:
            print("Error sending response")
        conn.close()

    def die(self):
        for thread in self.threads:
            thread.exit()
        self.socket.close()
