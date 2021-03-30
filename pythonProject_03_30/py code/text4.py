# -*- coding：uft-8 -*-
# 日期：2021/3/30 21:15
import turtle as t
#直接到达坐标x,y的位置
def go(x,y) :
    t.penup()
    t.goto(x,y)
    t.pendown()
#设置画布大小、画笔大小、画笔粗细
def pen() :
    t.screensize(0.99, 0.99)
    t.pensize(10)
    t.speed(10)
def main() :
    pen()
    pencolor = ['blue','black','red','yellow','green']			#列表存储画笔颜色
    x = -450
    y = 0
    for i in range(5) :
        if i == 3 :
            x = -225
            y = -150
        if i < 3 :
            go(x + i * 450,y)
            t.pencolor(pencolor[i])
            t.circle(200)
        else :
            go(x + ( i - 3 ) * 450, y)
            t.pencolor(pencolor[i])
            t.circle(200)
if __name__ ==  '__main__':
    main()