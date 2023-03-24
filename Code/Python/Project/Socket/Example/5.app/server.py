#file upload server

import socket

sk=socket.socket()

ip_port=("127.0.0.1",8888)

sk.bind(ip_port)
sk.listen(5)#最大连接数
while True:
    conn,address=sk.accept()#等待连接
    while True:#连接成功后一直使用当前连接，直到退出
        with open("file_rec","ab") as f :
            data=conn.recv(1024)
            if data==b'quit':
                break
            f.write(data)
            conn.send("success".encode())
    print("file rec accomplish...")
conn.close()