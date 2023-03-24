import os
import serial
import serial.tools
import serial.tools.list_ports

port_list = serial.tools.list_ports.comports()

count = 0;
com = []
for x in port_list:
	count = count + 1
	x = list(x)
	com.append(x[0])
	print(str(count) +'.'+ x[0])
	
key = input('请按数字键选择串口：')

while(int(key)>=count):
	key = input('没有此选项，请重新输入：')
key = com[int(key)-1]
com = serial.Serial(key,115200)
com.write(str.encode('hello '))

