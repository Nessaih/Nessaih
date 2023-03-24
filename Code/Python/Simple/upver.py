# coding:utf-8

import re
import sys
import os


def get_ver(cfile):
    ptn = re.compile(r'(PROJECT_CODE\s+"\w+")|(SOFTWARE_VER\s+"\w+")|(DEBUG_VER\s+"\w+")|(RELEASE_DATE\s+"\w+")|(HARDWARE_VER\s+"\w{2}")')
    ver = []
    with open(cfile, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
            obj = re.search(ptn, line)
            if obj : obj = re.search(r'".*"',obj.group())
            if obj : obj = re.sub(r'"','',obj.group())
            if obj : ver.append(obj)
    return '.'.join(ver)




def up_ver(vfile, ver):
    with open(vfile,'w') as file:
        file.write(ver)


if '__main__' == __name__:

    print('update foat version')

    if 1 == len(sys.argv):
        root = os.path.split(os.path.abspath(sys.argv[0]))[0]
        cfile = '\\components\\ql-application\\tbox\\inc\\tbox\\tbox_config.h'
        vfile = '\\components\\ql-config\\download\\prepack\\oemapp\\upgrade.ver'
        ver = get_ver(root+cfile)
        print(ver)
        up_ver(root+vfile,ver)
    elif 3 == len(sys.argv):
        cfile = sys.argv[1]
        vfile = sys.argv[2]
        ver = get_ver(cfile)
        print(ver)
        up_ver(vfile,ver)
    else:
        print('Parameter: ".../tbox_config.h" ".../upgrade.ver" ') 
