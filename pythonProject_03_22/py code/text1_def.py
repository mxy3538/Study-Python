# -*- coding：uft-8 -*-
# 日期：2021/3/22 16:26
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
x=0
y=5
z1=fact(x)
z2=fact(y)
print(z1,z2)
