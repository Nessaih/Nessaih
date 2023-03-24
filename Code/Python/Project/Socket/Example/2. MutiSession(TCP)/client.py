import socket

client = socket.socket()

ip_port = ("127.0.0.1", 8888)
client.connect(ip_port)

while True:
    data = client.recv(1024)
    print(data.decode())
    msg_input=input("please input mesage to send...")
    client.send(msg_input.encode())
    if msg_input== b'exit':
        break
    data = client.recv(1024)
    print(data.decode())