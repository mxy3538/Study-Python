# 淘宝客服机器人
print("AI:您好，我是淘宝客服机器人小爱同学，您有什么想咨询的？")
while True:
    I = input("我:")

    if "包邮" in I:
        AI="亲，江浙沪包邮哦:)"        
        print("AI:{}".format(AI))
    elif "快递" in I:
        AI="亲，本店只发EMS哦:)"        
        print("AI:{}".format(AI))
    elif "88" in I:
        AI = "亲，记得5星好评哦:)"
        print("AI:{}".format(AI))
        break
    else:
        AI="亲，人工客服忙，稍等哦:)"
        print("AI:{}".format(AI))

