# coding: utf-8



if "__main__" == __name__:
    while True:
        str = input("请输入字符：")
        bts = str.encode('UTF-8')
        print('\r\n八进制编码：',end=' ')
        for b in bts:
            print('\\{:o}'.format(b), end='')
        print('\r\n')
