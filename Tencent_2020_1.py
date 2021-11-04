#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/2 11:35 上午
# @Author  : shaowenjie
# @Email   : shaowenjie@datagrand.com

'''
1. 小Q想要给他的朋友发送一个神秘字符串，但是他发现字符串的过于长了，于是小Q发明了一种压缩算法对字符串中重复的部分进行了压缩，
对于字符串中连续的m个相同字符串S将会压缩为[m|S](m为一个整数且1<=m<=100)，例如字符串ABCABCABC将会被压缩为[3|ABC]，
现在小Q的同学收到了小Q发送过来的字符串，你能帮助他进行解压缩么？
'''
class Solution1:
    def compress(self, str):
        # write code here
        return self.extract(str)

    def get_string(self, string):
        if "|" not in string:
            return string
        for i, s in enumerate(string):
            if s == "|":
                num = int(string[:i])
                break
        return num * self.extract(string[i + 1 :])

    def extract(self, string):
        stack = []
        re = []
        exclude = ["[", "|", "]"]
        for i, s in enumerate(string):
            if not stack and s not in exclude:
                re.append(s)
            if s == "[":
                stack.append(i)
            elif s == "]":
                tmp = stack.pop()
                if not stack:
                    start = tmp
                    end = i
                    re.append(self.get_string(string[start + 1 : end]))
        return "".join(re)


'''
2. 小Q在周末的时候和他的小伙伴来到大城市逛街，一条步行街上有很多高楼，共有n座高楼排成一行。
小Q从第一栋一直走到了最后一栋，小Q从来都没有见到这么多的楼，所以他想知道他在每栋楼的位置处能看到多少栋楼呢？
（当前面的楼的高度大于等于后面的楼时，后面的楼将被挡住）
'''


# 解法：分为左右两边，分别用单调栈记录
class Solution2:
    def findBuilding(self, heights):
        # write code here
        re = [1] * len(heights)  # 初始为1，只能看到自己
        left_stack = []
        right_stack = []

        length = len(heights)
        for i in range(length - 1):
            while left_stack and heights[i] >= left_stack[-1]:
                left_stack.pop()
            left_stack.append(heights[i])
            re[i + 1] += len(left_stack)

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
4. 由于业绩优秀，公司给小Q放了 n 天的假，身为工作狂的小Q打算在在假期中工作、锻炼或者休息。
他有个奇怪的习惯：不会连续两天工作或锻炼。只有当公司营业时，小Q才能去工作，只有当健身房营业时，小Q才能去健身，小Q一天只能干一件事。
给出假期中公司，健身房的营业情况，求小Q最少需要休息几天。
'''

# 解法：实际上是一个有限状态机，状态之间的转换通过动态规划解决

# work = [1,1,0,0]
# exer = [0,1,1,0]
# n = 4
'''
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
'''

'''
5. 小Q在进行一场竞技游戏,这场游戏的胜负关键就在于能否能争夺一条长度为L的河道,即可以看作是[0,L]的一条数轴。
这款竞技游戏当中有n个可以提供视野的道具−真视守卫,第i个真视守卫能够覆盖区间[x_i,y_i]。现在小Q想知道至少用几个真视守卫就可以覆盖整段河道。 
'''
n, L = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
data.sort()

def test(data):
    if not data:
        return -1
    else:
        re = [data.pop(0)]
        if re[0][0] > 0:
            return -1

    last_right = 0
    while data and re[-1][1]< L:
        d = data.pop(0)
        if d[0] > re[-1][1]:
            return -1
        elif d[1] < re[-1][1]:
            continue
        elif d[0] <= last_right:
            re.pop()
        re.append(d)
        last_right = re[-2][1] if len(re) >1 else 0
    if re[-1][1] < L:
        return -1
    else:
        return len(re)
print(test(data))