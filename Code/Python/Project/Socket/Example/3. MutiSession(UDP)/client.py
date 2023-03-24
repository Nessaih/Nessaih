#udp
import  socket

sk=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port=("127.0.0.1",8888)
while True:
    msg_input=input("please input message to send...")
    if msg_input==b'exit':
        break
    sk.sendto(msg_input.encode(),ip_port)
sk.close()