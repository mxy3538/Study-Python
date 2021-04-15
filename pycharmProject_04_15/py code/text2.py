# -*- coding：uft-8 -*-
# 日期：2021/4/15 16:40
template = "零一二三四五六七八九"
s = input()
for c in s:
    print(template[eval(c)], end="")

