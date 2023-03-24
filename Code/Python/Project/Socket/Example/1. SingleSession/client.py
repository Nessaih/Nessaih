import socket

client = socket.socket()

ip_port = ("192.168.10.3", 8888)
client.connect(ip_port)
data = client.recv(1024)
print(data.decode())