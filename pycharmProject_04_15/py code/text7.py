# -*- coding：uft-8 -*-
# 日期：2021/4/15 17:31
def hello_world():
    print('ST',end="*")
def three_hellos():
    for i in range(3):
        hello_world()
three_hellos()