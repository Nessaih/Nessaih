import os
import re


filter=['.c','.h'] #设置过滤后的文件类型 当然可以设置多个类型

class FilesRewrite(object):
    def __init__(self,mdir = None):
        if mdir == None:
            self.maindir = 'D://Code//Work//SG//MPU//tzs100//apps//tzlink//app//kbc'
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

    def rename(self):
        for fp in self.files:
            new = re.sub('kobelco','kbc',fp)
            #print(new)
            os.rename(fp,new)

    def showfiles(self):
        print(self.files)
    
f = FilesRewrite(None)
f.all_path()
f.rename()
