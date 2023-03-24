
import socket
import threading

CLIENT_IP = ("192.168.10.3", 8888)
SERVER_IP = ("192.168.10.3", 8888)
TRANSMIT_LEN = 1024


class Client:
    def __init__(self, ip=CLIENT_IP):
        self.ip = ip
        self.sk = socket.socket()

    def recv(self):
        self.sk.connect(self.ip)
        data = self.sk.recv(TRANSMIT_LEN)
        self.sk.close()
        self.recv_callback(data.decode)

    def send(self, text):
        data = text.encode()
        self.sk.connect(self.ip)
        self.sk.send(data)
        self.sk.close()

    def recv_callback(self, text):
        print(text)

    def ip_set(self):
        pass


class Server:
    def __init__(self, ip=SERVER_IP):
        self.ip = ip
        self.sk = socket.socket()
        self.sk.bind(self.ip)
        self.sk.listen(5)

    def recv(self):
        threading.Thread(target=self.recv_callback,)

    def send(self):
        pass
    
    def recv_callback(self, text):
        print(text)

    def ip_set(self):
        pass



if '__main__' == __name__:
    pass
