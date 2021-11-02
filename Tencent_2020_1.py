#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/2 11:35 上午
# @Author  : shaowenjie
# @Email   : shaowenjie@datagrand.com

''''''

'''
2. 小Q在周末的时候和他的小伙伴来到大城市逛街，一条步行街上有很多高楼，共有n座高楼排成一行。
小Q从第一栋一直走到了最后一栋，小Q从来都没有见到这么多的楼，所以他想知道他在每栋楼的位置处能看到多少栋楼呢？
（当前面的楼的高度大于等于后面的楼时，后面的楼将被挡住）
'''
#
# @param heights int整型一维数组
# @return int整型一维数组
#
class Solution:
    def findBuilding(self, heights):
        # write code here
        re = [1] * len(heights)
        left_stack = []
        right_stack = []

        length = len(heights)
        for i in range(length-1):
            while left_stack and heights[i] >= left_stack[-1]:
                left_stack.pop()
            left_stack.append(heights[i])
            re[i+1] += len(left_stack)

            while right_stack and heights[length - i - 1] >= right_stack[-1]:
                right_stack.pop()
            right_stack.append(heights[length - i - 1])
            re[length - i - 2] += len(right_stack)

        return re

# heights = [5,3,8,3,2,5]
# # [3,3,5,4,4,4]
# s = Solution()
# print(s.findBuilding(heights))

'''
3. 由于业绩优秀，公司给小Q放了 n 天的假，身为工作狂的小Q打算在在假期中工作、锻炼或者休息。
他有个奇怪的习惯：不会连续两天工作或锻炼。只有当公司营业时，小Q才能去工作，只有当健身房营业时，小Q才能去健身，小Q一天只能干一件事。
给出假期中公司，健身房的营业情况，求小Q最少需要休息几天。
'''
# work = [1,1,0,0]
# exer = [0,1,1,0]
# n = 4
n = int(input())
work = list(map(int, input().split()))
exer = list(map(int, input().split()))

# re[n][0,1,2]分别表示第n天工作、锻炼和休息的情况下休息的总天数，re[0]第0天均为0
re = [[n for i in range(3)] for _ in range(n+1)] # 工作0 锻炼1 休息2
re[0] = [0,0,0]
for i in range(1,n+1):
    if work[i-1]: #第i天工作，第i天是否可以工作为work[i-1]
        re[i][0] = min(re[i-1][1], re[i-1][2])
    if exer[i-1]:
        re[i][1] = min(re[i - 1][0], re[i - 1][2])
    re[i][2] = min(re[i - 1][0], re[i-1][1], re[i-1][2]) + 1
print(min(re[n]))