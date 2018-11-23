import socket
import WebApp.Config as Config
import threading
import WebApp.request_handler as rh


class Server(object):
    def __init__(self, IP_ADDR='localhost', PORT=5000):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.IP_ADDR, self.PORT = IP_ADDR, PORT
        self.socket.bind((IP_ADDR, PORT))
        self.threads = list()

    def run(self):
        self.socket.listen(1)
        while True:
            conn, addr = self.socket.accept()
            print("Connected by", addr)
            new_client = threading.Thread(target=Server.handle_client, args=(self,conn,))
            self.threads.append(new_client)
            new_client.start()

    def handle_client(self, conn):
        response = rh.handle_request(conn.recv(4096).decode())
        conn.send(response.encode()) 
        conn.close()
