# -*- coding：uft-8 -*-
# 日期：2021/4/21 10:30
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
num=eval(input("请输入一个整数："))
print(fact(abs(int(num))))