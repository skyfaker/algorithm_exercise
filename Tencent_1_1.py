#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 3:50 下午
# @Author  : shaowenjie

import time
import random
random.seed(1)


# NOTE: 数组实现, 更快
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

# NOTE：字典实现
class UFS_dict(object):
    def __init__(self) -> None:
        self.parent = {}
        self.num = {}

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
#     u2 = UFS_dict()
#     n = int(input())
#     data = []
#     max_num = 0
#     for j in range(n):
#         x, y = map(int, input().split())
#         data.append([x, y])
#
#         u2.parent[x] = x
#         u2.num[x] = 1
#         u2.parent[y] = y
#         u2.num[y] = 1
#
#     for x, y in data:
#         u2.merge(x, y)
#
#     print(max(u2.num.values()))


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
#
#
# s = time.time()
# u2 = UFS_dict()
# for x, y in test_data:
#     if x not in u2.parent:
#         u2.parent[x] = x
#         u2.num[x] = 1
#     if y not in u2.parent:
#         u2.parent[y] = y
#         u2.num[y] = 1
#
#     u2.merge(x, y)
#
# m = max(u2.num.values())
# print(m)
# print(time.time() - s)

if __name__ == "__main__":
    test_data = [random.sample(range(1, 100), 1) for _ in range(10 ** 5)]
    s = time.time()
    while test_data:
        test_data.pop(0)
    print(time.time() - s)

    test_data = [random.sample(range(1, 100), 1) for _ in range(10 ** 5)]
    s = time.time()
    while test_data:
        test_data.pop()
    print(time.time() - s)