# -*- coding：uft-8 -*-
# 日期：2021/4/15 17:29
def exchange(a,b):
    a,b=b,a
    return (a,b)
x=10
y=20
x,y=exchange(x,y)
print(x,y)