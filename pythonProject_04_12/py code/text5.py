# -*- coding：uft-8 -*-
# 日期：2021/4/12 22:03
dayup,add=1.0,0.01
for i in range(365):
    if i%7 in [6,0]:
        dayup=dayup*(1-add)
    else:
        dayup=dayup*(1+add)
print("向上5天向下2天的力量：{:.2f}".format(dayup))