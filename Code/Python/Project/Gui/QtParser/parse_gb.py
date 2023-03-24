# coding: utf-8

import re
import wcwidth


def lpad(s, n, c=' '):
    return (n - wcwidth.wcswidth(s)) * c + s


def rpad(s, n, c=' '):
    return s + (n - wcwidth.wcswidth(s)) * c

class Filter(object):

    def __init__(self):
        pass

    def filter_file(self, file_path):
        ptn = re.compile(
            r'(\[[0-9:.]*\]0x[0-9a-fA-F]+\s+(\s[0-9a-fA-F]{2})+\s?\n?)+')
        with open(file_path, 'r') as f:
            str_log = f.read()
            iter = re.finditer(ptn, str_log)
        return iter

    def filter_data(self, str_memhex):
        ptn = re.compile(r'\[(\d{2}:?){3}\.\d{3}\]0x[0-9a-fA-F]{8}\s+')
        msg_str = re.sub(ptn, '', str_memhex)
        msg_list = msg_str.split()
        return msg_list


class Parser(object):

    def __init__(self, msg_list):
        # master protocol name
        self.mpn = ('起始符', '命令单元', '车辆识别码', '终端软件版本', '数据加密方式', '数据单元长度',
                    '数据单元', '校验码')
        self.msg_list = msg_list
        self.msg_list_hex = [int(i, 16) for i in msg_list]
        self.parsed_head = []
        self.parsed_body = []
        self.parsed_tail = []

    def check_ok(self):
        c = 0
        for i in self.msg_list_hex[2:-1]:
            c = c ^ i
        if c == self.msg_list_hex[-1]:
            return True
        return False

    def parser_head(self):
        s = ('%s | %02X %02X') % (lpad(self.mpn[0],
                                       20), self.msg_list_hex[0], self.msg_list_hex[1])
        self.parsed_head.append(s)
        s = ('%s | %02X') % (lpad(self.mpn[1], 20), self.msg_list_hex[2])
        self.parsed_head.append(s)

    def parser_body(self):
        pass

    def parser_tail(self):
        pass


if '__main__' == __name__:
    filter = Filter()
    it = filter.filter_file('./Parser/MPU_2023-02-23 15.16.27.log')
    for i in it:
        s1 = i.group()
        # print(s, end='\n\n')
        s1 = filter.filter_data(s1)
        # print(s, end='\n\n')

        parser = Parser(s1)
        if parser.check_ok():
            # print('OK', end='\n\n')

            parser.parser_head()
            for i in parser.parsed_head:
                print(i)

        else:
            print('ERROR', end='\n\n')

        break
