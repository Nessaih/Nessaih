import socket

sk = socket.socket()
ip_port = ("192.168.10.3", 8888)
sk.bind(ip_port)
sk.listen(5)
print("正在进行等待接受数据...")
conn, address = sk.accept()
msg = "hello world!"
conn.send(msg.encode())
conn.close()

