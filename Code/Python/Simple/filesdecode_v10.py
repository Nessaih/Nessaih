import os
import sys

filter=['.txt','.c','.h','.copy','.xlsx'] #设置过滤后的文件类型 当然可以设置多个类型
class FilesRewrite(object):
    def __init__(self,mdir = None):
        if mdir == None:
            self.maindir = 'F://cszx'
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

    def rewrite(self):
        for fp in self.files:
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

    def rename(self):
        for fp in self.files:
            newfp = fp.rstrip('.cpoy')
            os.rename(fp,newfp)

f = FilesRewrite(None)
f.all_path()
f.rewrite()
#f.rename()
