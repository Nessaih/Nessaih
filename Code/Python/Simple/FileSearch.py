import json
import os


class FileSeach(object):
    def __init__(self, filter) -> None:
        self.__filter_ext = filter

    def collect(self, path) -> dict:
        ddir = {}
        ldir = []
        dirs = self.__subdir(path)

        for dir in dirs:
            if self.__filter(os.path.join(path,dir)):
                ldir.append(dir)
            dict = self.collect(os.path.join(path, dir))
            if dict:
                ldir.append(dict)
        if ldir:
            ddir[os.path.split(path)[1]] = ldir

        return ddir

    def __subdir(self, path) -> list:
        dirs_and_files = os.listdir(path)
        dirs = []
        for d in dirs_and_files:
            dpath = os.path.join(path, d)
            if os.path.isdir(dpath):
                dirs.append(d)
        return dirs

    def __filter(self, path) -> bool:
        dirs_and_files = os.listdir(path)
        for f in dirs_and_files:
            fpath = os.path.join(path, f)
            if os.path.isfile(fpath):
                ext = os.path.split(fpath)[1]
                if ext in self.__filter_ext:
                    return True
        return False


if "__main__" == __name__:
    fs = FileSeach(['CMakeLists.txt'])
    dict = fs.collect('D:\\Code\\Work\\CAT1_HPM\\MPU\\LTE01R02A09_C_SDK_U')
    # print(dict)
    print(json.dumps(dict))
