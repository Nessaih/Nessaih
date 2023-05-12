import os


# 列表版本

class Load(object):

    def __init__(self, dir=None):
        self.__qss_dir = dir
        self.__qss_name = []
        self.LoadThemes()

    def LoadThemes(self, qss_file_dir=None):
        if qss_file_dir:
            path = qss_file_dir
            self.__qss_dir = path
        else:
            path = self.__qss_dir
        # print(path)
        if not path:
            return None

        for root, d, f in os.walk(path):
            for i in f:
                self.__qss_name.append(os.path.splitext(i)[0])
        # print(self.__qss_name)


    def GetThemes(self):
        return self.__qss_name

    def GetTheme(self, name):
        if name not in self.__qss_name:
            return None

        file = self.__qss_dir + name + '.qss'

        with open(file, 'r') as f:
            return f.read()

'''
# 迭代器版本

class Load(object):

    def __init__(self, dir=None):
        self.__qss_dir = dir
        self.__qss_name = []
        self.__index = -1
        self.__length = 0
        self.LoadThemes()

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < self.__length - 1:
            self.__index += 1
        else:
            raise StopIteration
        return self.__qss_name[self.__index]

    def LoadThemes(self, qss_file_dir=None):
        if qss_file_dir:
            path = qss_file_dir
            self.__qss_dir = path
        else:
            path = self.__qss_dir

        if not path:
            return None

        for root, d, f in os.walk(path):
            for i in f:
                self.__qss_name.append(os.path.splitext(i)[0])
                self.__length += 1
        # print(self.__qss_name)

    def GetTheme(self, name):
        if name not in self.__qss_name:
            return None

        file = self.__qss_dir + name + '.qss'

        with open(file, 'r') as f:
            return f.read()
'''