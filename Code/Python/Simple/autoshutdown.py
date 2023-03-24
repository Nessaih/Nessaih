import os
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.master.geometry('100x50')
        self.master.title('定时关机')
        self.entry = tk.Entry(self,show = None)
        self.entry.pack()
        self.button = tk.Button(self, text = '请输入数字',command = self.shutdow)
        self.button.pack()
    
    def shutdow(self):
        cmd = 'shutdown /s /t ' + str(int(float(self.entry.get())*3600))
        print(cmd)
        os.system(cmd)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
