# coding: utf-8

import requests
import re
import os
import html


def url_get(url: str) -> str:
    '''
    读取网页
    '''
    head = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26',
        'Connection':'close'
    }
    # connect_timeout = 30
    # read_timeout = 30
    # page = requests.get(url,
    #                     headers=head,
    #                     stream=True,
    #                     verify=True,
    #                     timeout=(connect_timeout, read_timeout))
    page = requests.get(url, headers=head)
    page.close()
    return page.text


def text_filter(text: str) -> str:
    '''
    读取文本
    '''
    ptn = {
        'rsv': r'<div\x20class="highlight">[\s\S]*?</div>',  # resever 
        'dlt': r'</?[(span)(a)(div)].*?>'  # delete
    }

    text = re.search(ptn['rsv'], text).group()
    if None != text:
        text = re.sub(ptn['dlt'], '', text)
        text = html.unescape(text)  # escape character
    return text


def node_filter(text: str) -> tuple:
    '''
    读取超链接
    '''
    ptn = {
        'rsv': r'<td><a\x20class="tree-icon.*">[\s\S]*?</a></td>',  # resever
        'dlt': r'</?[(td)(a)].*?>',  # delete
        'dir':
        r'<td><a\x20class=".*tree"\x20href=".*">[\s\S]*?</a></td>',  # diretoris
        'fil':
        r'<td><a\x20class=".*blob"\x20href=".*">[\s\S]*?</a></td>'  # file
    }
    node = {'dirs': [], 'files': []}

    res = re.findall(ptn['rsv'], text)
    for i in range(len(res)):
        node_type = -1
        if re.match(ptn['dir'], res[i]):
            node_type = 0
        elif re.match(ptn['fil'], res[i]):
            node_type = 1

        res[i] = re.sub(ptn['dlt'], '', res[i])

        if 0 == node_type:
            node['dirs'].append(res[i])
        elif 1 == node_type:
            node['files'].append(res[i])

    return node


def download(path: str, url: str) -> None:
    '''
    递归下载文件
    '''
    print(path)
    page = url_get(url)
    node = node_filter(page)

    for i in node['dirs']:
        os.mkdir(path + '\\' + i)
        download(path + '\\' + i, url + i + '/')
    for i in node['files']:
        fpath = path + '\\' + i
        if not os.path.exists(fpath):
            fpage = url_get(url + i)
            text = text_filter(fpage)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(text)


def test_get_file():
    url = 'https://elixir.bootlin.com/linux/0.01/source/boot/boot.s'
    t = url_get(url)
    t = text_filter(t)
    print(t)


def test_get_node():
    url = 'https://elixir.bootlin.com/linux/0.01/source/'
    t = url_get(url)
    t = node_filter(t)
    print(t)


def test_download():
    '''
    输入网址开始下载文件
    '''
    path = 'D:\\Code\\Python\\BatchDownload\\Linux\\6.28'
    url = 'https://elixir.bootlin.com/linux/v6.2.8/source/'

    if not os.path.exists(path): os.mkdir(path)
    download(path, url)


if '__main__' == __name__:
    test_download()
