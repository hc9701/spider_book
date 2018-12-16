#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:54:52 2018

@author: hc
"""
import re, requests, random
import random

# 编译的工作可以留到循环外面进行，避免重复计算
# 用来解析最后一页
last_page = re.compile('<a href="/p/5964052167\?pn=(\d+)">尾页</a>', flags=re.S)
# 解析出所有包含楼层的信息
floor = re.compile('<span class="tail-info">(\\d+)楼</span>', flags=re.S)


def get_floor(url='https://tieba.baidu.com/p/5964052167'):
    max_floor = 1
    session = requests.session()
    while True:
        resp = session.get(url)
        # 返回页面源代码
        content = resp.text
        pn = re.search(last_page, content).group(1)
        # 访问最后一页
        resp = session.get(url + '?pn=' + pn )
        # 得到最后一个楼层信息。
        last_floor = re.findall(floor, resp.text)[-1]
        # 如果楼层增长很快，避免更新过快，来不及看。可将下面的输出注释
        print(last_floor)
        if int(last_floor) > max_floor:
            max_floor = int(last_floor)
            print('last_floor', last_floor)


if __name__ == '__main__':
    get_floor()
