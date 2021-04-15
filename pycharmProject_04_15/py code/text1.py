# -*- coding：uft-8 -*-
# 日期：2021/4/15 16:38
n = eval(input())
for i in range(1,n+1,2):
    print("{0:^{1}}".format('*'*i, n))