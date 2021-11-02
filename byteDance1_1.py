#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/27 2:21 下午
# @Author  : shaowenjie

import gc
import psutil
import os


# data = [[1, 2],
#  [5, 3],
#  [4, 6],
#  [7, 5],
#  [9, 0]]


def get_out(data):
    max_y = -1
    re = []
    while data:
        c_data = data.pop()
        if c_data[1] >= max_y:
            max_y = c_data[1]
            re.append([c_data[0], c_data[1]])
    return re

if __name__ == '__main__':

    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    data.sort()
    re = get_out(data)
    # while re:
    #     r = re.pop()
    #     print(r[0], r[1])
    print(psutil.Process(os.getpid()).memory_info().rss / 1024/ 1024)