#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 3:50 下午
# @Author  : shaowenjie

import time
import random
random.seed(1)

def get_k(string, k):
    re = []
    index = []
    m = min(string)
    length = len(string)
    re.append(m)
    for i, v in enumerate(string):
        if v == m:
            index.append(i)
    for l in range(1, k + 1):
        for s in index:
            if s + l <= length:
                sub_s = string[s:s + l]
                if sub_s not in re:
                    re.append(sub_s)
    return re

def del_s(string, s):
    tmp = []
    for i in string:
        if i != s:
            tmp.append(i)
    return ''.join(tmp)

# string= input()
# k = int(input())

string = 'aabb'
k = 3

re = []
while len(re)>=k:


print(re[k])