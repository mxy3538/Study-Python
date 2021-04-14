# -*- coding：uft-8 -*-
# 日期：2021/4/13 23:53
monthstr="一月二月三月四月五月六月七月八月九月十月十一月十二月"
monthid=eval(input("请输入月份数字(1-12): "))
pos=(monthid-1)*2
if monthid==11:
    print(monthstr[pos:pos+3])
elif monthid<=10:
    print(monthstr[pos:pos + 2])
else:
    print(monthstr[pos+1:])