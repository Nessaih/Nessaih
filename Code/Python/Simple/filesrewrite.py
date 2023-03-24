import os
import sys
import tkinter,tkinter.filedialog

filter=['.doc','.docx','.pdf','.xlsx','.py','.txt','.c','.h','.copy'] #设置过滤后的文件类型 当然可以设置多个类型

class FilesRewrite(object):
    def __init__(self,mdir = None):
        if mdir == None:
            self.maindir = 'D://cszx'
        else:
            self.maindir = mdir
        self.files =  []

    def all_path(self):
        for maindir, subdir, file_name_list in os.walk(self.maindir):
            # print("1:",maindir) #当前主目录
            # print("2:",subdir) #当前主目录下的所有目录
            # print("3:",file_name_list)  #当前主目录下的所有文件
            for filename in file_name_list:
                apath = os.path.join(maindir, filename)#合并成一个完整路径
                ext = os.path.splitext(apath)[1]        # 获取文件后缀 [0]获取的是除了文件名以外的内容
                if ext in filter:
                    self.files.append(apath)
        return self.files

    # def resourcepath():
    #     if hasattr(sys,'_MEIPASS'):
    #         return sys._MEIPASS
    #     return None

    def rewrite(self,files,num = 0):
        if num != 0:
            fp = files
            file = open(fp,'rb')
            lines = file.readlines()
            file.close()
            os.remove(fp)
            file = open(fp+'.copy','wb')
            for line in lines:
                file.write(line)
            file.close()
        else:
            for fp in files:
                #file = open(fp,encoding='utf-8')
                file = open(fp,'rb')
                lines = file.readlines()
                file.close()
                os.remove(fp)
                file = open(fp+'.copy','wb')
                for line in lines:
                    file.write(line)
                file.close()
                #os.rename(fp+'.copy',fp)

    def rename(self,files,num = 0):
        if num != 0:
            fp = files
            newfp = fp[:-5]
            # newfp = fp.rstrip('.cpoy')
            os.rename(fp,newfp)
        else:
            for fp in files:
                newfp = fp[:-5]
                # newfp = fp.rstrip('.cpoy')
                os.rename(fp,newfp)

class Window(tkinter.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master

        self.tSpath = tkinter.StringVar()
        self.tIoperation = tkinter.IntVar()
        self.grid()
        # self.pack()
        self.cratewindow()
        
    def cratewindow(self):
        self.master.geometry('200x100')
        self.master.title('Files decode')
        #布局：
        #[rb]:b1,b2
        #[btm]:b3,b4

        #创建一个容器
        self.rb = tkinter.Frame(self)
        #将两个Radiobutton按钮放置在此容器上
        self.b1 = tkinter.Radiobutton(self.rb,text = 'Encode',variable = self.tIoperation, value = 0)
        self.b1.grid(row = 0,column = 0,padx = 7,sticky = tkinter.N,ipadx = 5, pady = 2)
        self.b2 = tkinter.Radiobutton(self.rb,text = 'Decode',variable = self.tIoperation, value = 1)
        self.b2.grid(row = 0,column = 1,padx = 7,sticky = tkinter.N,ipadx = 5, pady = 2)
        self.rb.grid(row = 0,column = 0,padx = 16,sticky = tkinter.E + tkinter.W,ipadx = 5, pady = 2)
        #直接将按键放置主容器

        self.btm = tkinter.Frame(self)
        self.b3 = tkinter.Button(self.btm, text ="选择路径", command = self.SelectDirectoryCallback)
        self.b3.grid(row = 0,column = 0,padx = 2,sticky = tkinter.E + tkinter.W,ipadx = 10, pady = 2)
        self.b4 = tkinter.Button(self.btm, text ="选择文件", command = self.SelectFileCallback)
        self.b4.grid(row = 0,column = 1,padx = 2,sticky = tkinter.E + tkinter.W,ipadx = 10, pady = 2)
        self.btm.grid(row = 1,column = 0,padx = 16,sticky = tkinter.E + tkinter.W,ipadx = 5, pady = 2)


    #选择文件夹回调函数
    def SelectDirectoryCallback(self):
        self.path = tkinter.filedialog.askdirectory()
        f = FilesRewrite(self.path)
        f.all_path()
        if 0 == self.operation:
            f.rewrite(f.files)
        else:
            f.rename(f.files)

    #选择文件回调函数
    def SelectFileCallback(self):
        self.path = tkinter.filedialog.askopenfilename()
        f = FilesRewrite(self.path)
        if 0 == self.operation:
            f.rewrite(self.path,1)
        else:
            f.rename(self.path,1)

    #访问器
    @property
    def path(self):
        return self.tSpath.get()
    #访问器
    @property
    def operation(self):
        return self.tIoperation.get()
    #修改器
    @path.setter
    def path(self,path):
        self.tSpath.set(path)

r = tkinter.Tk()  
w = Window(r)
w.mainloop()
