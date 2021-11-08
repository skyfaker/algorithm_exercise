#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/4 4:56 下午
# @Author  : shaowenjie
# @Email   : shaowenjie@datagrand.com

'''
1. 给定一个队列q，小美会按照以下规则进行游戏：
每次从队列中取出一个数，如果这个数是当前队列中最小的值，那么小美就会丢掉这个数。否则小美就会把这个数重新加入队列。
小美会一直进行游戏直到队列变空为止，她想知道她最多需要进行多少次操作才能结束游戏。
'''


'''
2. 
'''
def quick_sort(data):
    def partition(left, right):
        if left>=right: return
        tmp = data[left]
        p = left
        for i in range(left+1, right+1):
            if data[i] < tmp:
                p+=1
                if p!=i:
                    data[p], data[i] = data[i], data[p]
        data[p], data[left] = data[left], data[p]
        return p

    def sort(left, right):
        if left<right:
            p = partition(left, right)
            sort(left, p-1)
            sort(p+1, right)

    sort(0, len(data)-1)
    return data
def s3():
    n, p = map(int, input().split())
    data = list(map(int, input().split()))
    data = quick_sort(data)
    # print(data)
    t = 0
    re = 0
    for d in data:
        if t+d<p:
            re+=1
            t +=d
        else:
            break
    print(re)

'''
4. 
'''