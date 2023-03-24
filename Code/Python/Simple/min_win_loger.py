import tkinter
import tkinter.messagebox as messagebox
import os,datetime

class Checkin(tkinter.Frame):
    def __init__(self,master = None):
        tkinter.Frame.__init__(self,master)
        self.time = ''
        self.msg = tkinter.StringVar()
        self.master.overrideredirect(True)  #去除外框
        self.master.attributes("-alpha", 0.8)#设置透明度0.7
        self.grid()
        self.creat_widget()

        
        
    def creat_widget(self):
        self.master.geometry('100x50+70+790')
        self.master.title('借用登记')
        #frm1
        self.e1 = tkinter.Entry(self,width = 15,textvariable = self.msg)
        self.e1.grid(column = 0,row = 0,sticky = tkinter.N)
        #frm2
        self.buttom_frame = tkinter.Frame(self)
        self.b1 = tkinter.Button(self.buttom_frame, text ="确定", command = self.checkinCallback)
        self.b2 = tkinter.Button(self.buttom_frame, text ="退出", command = self.master.quit)
        self.b1.grid(column = 0,row = 1,ipadx = 8,padx = 1,sticky = tkinter.E + tkinter.W)
        self.b2.grid(column = 1,row = 1,ipadx = 8,padx = 1,sticky = tkinter.E + tkinter.W)
        self.buttom_frame.grid(column = 0,row = 1,padx = 1,sticky = tkinter.E + tkinter.W)
        self.e1.bind('<Return>',func = self.keyenter_checkinCallback)#绑定回车键触发

    def checkinCallback(self):
        self.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        path = os.getcwd() + '\\log.txt'
        line = self.time + '    ' + self.msg.get() + '\n'
        file = open(path,'a+',encoding='utf-8')
        file.write(line)
        file.close()
        messagebox.showinfo('成功记录', '%s' % line)

    #定义一个参数会出错，提示为有两个参数，详见印象笔记“TypeError: xxx takes 1 positional argument but 2 were given解决方法”
    def keyenter_checkinCallback(self,myself):
        self.checkinCallback()

#root = tkinter.Tk()
app = Checkin()
app.mainloop()
