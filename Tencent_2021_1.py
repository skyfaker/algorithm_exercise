#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 3:50 下午
# @Author  : shaowenjie

import time
import random
random.seed(1)

'''
1. 现在有 105 个用户，编号为 1- 105，现在已知有 m 对关系，每一对关系给你两个数 x 和 y ，代表编号为 x 的用户和编号为 y 的用户是在一个圈子中，
例如： A 和 B 在一个圈子中， B 和 C 在一个圈子中，那么 A , B , C 就在一个圈子中。现在想知道最多的一个圈子内有多少个用户。
'''
# NOTE: 数组实现, 比字典更快
class UFS(object):
    def __init__(self, maxNum) -> None:
        self.parent = [i for i in range(maxNum + 1)]
        self.num = [1] * (maxNum + 1)

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def merge(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x == p_y:
            return
        elif p_x > p_y:
            self.parent[p_x] = p_y
            self.parent[x] = p_y
            self.num[p_y] += self.num[p_x]
        else:
            self.parent[p_y] = p_x
            self.parent[y] = p_x
            self.num[p_x] += self.num[p_y]

# T = int(input())
# for i in range(T):
#     n = int(input())
#     u = UFS(maxNum=10**5)
#     for j in range(n):
#         x, y = map(int, input().split())
#         u.merge(x, y)
#     print(max(u.num))


# 测试：
# max_num = 10**5
# # epoch = max_num * 1
# epoch = 10**6
# test_data = [random.sample(range(1,max_num), 2) for _ in range(epoch)]
# # print(test_data)
#
# s = time.time()
# u = UFS(maxNum=max_num)
# for x, y in test_data:
#     u.merge(x, y)
# print(max(u.num))
# print(time.time() - s)


'''
2. 输入一个字符串 s，s 由小写英文字母组成，保证 s 长度小于等于 5000 并且大于等于 1。在 s 的所有不同的子串中，输出字典序第 k 小的字符串。
字符串中任意个连续的字符组成的子序列称为该字符串的子串。
字母序表示英文单词在字典中的先后顺序，即先比较第一个字母，若第一个字母相同，则比较第二个字母的字典序，依次类推，则可比较出该字符串的字典序大小
'''
def get_k(string, k):
    re = []
    index = []
    m = min(string)
    length = len(string)
    re.append(m)
    for i, v in enumerate(string):  # 遍历，记录最小值出现的位置
        if v == m:
            index.append(i)
    for l in range(1, k + 1):  # 查找从最小值处开始，长度在k以内的子串
        for s in index:
            if s + l <= length:
                sub_s = string[s:s + l]
                if sub_s not in re:
                    re.append(sub_s)
    return re

def del_min(string):  # 删除字符串中的所有最小值
    s = min(string)
    tmp = []
    for i in string:
        if i != s:
            tmp.append(i)
    return ''.join(tmp)


# string = input()
# k = int(input())
# re = []
# while len(re) < k:
#     re.extend(get_k(string, k))
#     k -= 1
#     string = del_min(string)
# re.sort()
# print(re[k])