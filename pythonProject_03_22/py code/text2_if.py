# -*- coding：uft-8 -*-
# 日期：2021/3/22 21:23
height=eval(input("请输入身高（米）"))
weight=eval(input("请输入体重(kg)"))

bmi=weight/height**2

who=""

if bmi<18.5:
    who="偏瘦"
elif bmi>=18.5 and bmi<25:
    who="ok"
elif bmi >25 and bmi<30:
    who="偏胖"
else:
    who=""

print(who)
