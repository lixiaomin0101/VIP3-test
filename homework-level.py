# 输入一个数，判断该数的范围：90-100：等级为A，60以下，等级为E
while 1 :
    num = float(input("请输入数值："))

    if num >= 90 and num <= 100:
        print("数值等级为:A")
    elif num >= 80 and num <= 85:
        print("数值等级为：B")
    elif num >= 60 and num < 80:
        print("数值等级为：C")
    elif num < 60:
        print("数值等级为：E")
    else:
        print("语句结束")
        break

