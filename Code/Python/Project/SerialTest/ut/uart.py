# coding: utf-8


import time
import serial
import serial.tools.list_ports

import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import PyQt5.QtWidgets as QW

# from PyQt5.QtCore import pyqtSignal, QThread, QObject
# from PyQt5.QtWidgets import QMessageBox



class UartThread(QC.QThread):

    received = QC.pyqtSignal(dict)

    def __init__(self, run):
        super(UartThread, self).__init__()
        self.runfun = run

    def run(self):
        self.runfun()


class Uart(QC.QObject):

    def __init__(self):
        super(Uart, self).__init__()
        self.receiver = UartThread(self.Receive)
        self.ser = serial.Serial()

    def GetPorts(self) -> list:
        ports = serial.tools.list_ports.comports()
        if len(ports):
            self.ports = [{'port': p[0], 'name': p[1]} for p in ports]
        else:
            self.ports = None
        return self.ports

    def GetPortState(self):
        pass

    def OpenPort(self, port=None, rate=115200, bits=8, parity='N', stopbit=1):
        self.ser.port = port
        self.ser.baudrate = rate
        self.ser.bytesize = bits
        self.ser.parity = parity
        self.ser.stopbits = stopbit

        try:
            self.ser.open()
        except:
            return False

        if not self.receiver.isRunning():
            self.receiver.start()
        print('open port')
        return True

    def ClosePort(self, port=None):
        self.ser.port = port

        try:
            self.ser.close()
        except:
            return False

        if self.receiver.isRunning():
            self.receiver.quit()

        print('close port')
        return True

    def SendBytes(self, data: bytes):
        self.ser.write(data)

    def SendStr(self, data: str):
        self.ser.write(data)

    def Receive(self):
        while True:
            data = {}
            try:
                num = self.ser.inWaiting()
            except:
                self.ser.close()
                data['valid'] = False
                data['data'] = None

            if num > 0 and self.ser.isOpen():
                buf = self.ser.read(num)
                data['valid'] = True
                data['data'] = buf
                self.receiver.received.emit(data)
            time.sleep(0.1)


if __name__ == '__main__':
    ut = Uart()
    ports = ut.GetPorts()
    print(('%-6s    %-30s') % ('Port', 'Name'))
    print('------------------------------------')
    for p in ports:
        print(('%-6s    %-30s') % (p['port'], p['name']))
