# coding: utf-8
'''
自动计算统一文件夹中所有*.asc文件中CAN报文的条数。
注意：
    1.  文件夹下只能有asc文件;
'''

import os
import timeit
import threading

TEST_DIR = 'C:\\Users\\Administrator\\Desktop\\TEMP\\can_asc\\'


def get_files(dir_path: str):
    for root, d, f in os.walk(dir_path):
        return f
    #         files.append(f)
    # return files


def get_lines(file_path: str):
    count = 0
    with open(file_path) as f:
        for index, line in enumerate(f):
            count += 1
    return count


def get_lines_ext(file_list: list):
    s = 0
    for f in file_list:
        s += get_lines(TEST_DIR + f) - 7
    return s


def get_lines_ext2(file_list: list, ret: list):
    ret.clear()
    for f in file_list:
        ret.append(get_lines(TEST_DIR + f) - 7)


def add_test1():
    fs = get_files(TEST_DIR)
    c = get_lines_ext(fs)
    print('\n接收CAN条数: {}\n'.format(c))


def add_test2():
    '''
    使用线程加速
    '''
    # nums =
    fs = get_files(TEST_DIR)
    fc = len(fs)
    tc = 5
    step = int(fc / tc + 0.5)
    pa = [fs[i:i + step] for i in range(0, fc, step)]

    # print(pa)

    ret = []
    # 线程池列表
    threads = []

    #添加线程
    for i in range(len(pa)):
        ret.append([])
        th_name = 'th' + str(i)
        th = threading.Thread(target=get_lines_ext2,
                              args=[pa[i], ret[i]],
                              name=th_name)
        threads.append(th)

    # 启动线程
    for t in threads:
        t.start()

    #等待所有线程结束
    for t in threads:
        t.join()

    s = 0
    for l in ret:
        s += sum(l)
    print('\n接收CAN条数: {}\n'.format(s))



if '__main__' == __name__:
    run_time = timeit.timeit('add_test1()',
                             'from __main__ import add_test1',
                             number=1)
    
    print('程序运行时间:%f s' %run_time)


    # add_test2()