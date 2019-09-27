# 定义一个列表，从键盘输入一个随机数，判断该数是否在列表中
while 1:
    numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num=int(input("请随意输入一个数："))
    if num in numlist:
        print("正确")
    else:
        print("不在")
        print("程序退出")
        break