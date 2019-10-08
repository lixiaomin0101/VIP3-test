__author__ = 'Sunky'
#  -*-coding:utf8 -*-
#3.求10的阶乘
# def factorial(n):
#     res=1
#     for i in  range(1,n+1):
#         res *= i
#         return res
#         print(i)

#4.求100以内能被3整除的数，并将作为列表输出
# num =1
# for i in range(100):
#     if i % 3 == 0:
#         print(i)
#         num +=1

#5.列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
# orgList =[1,2,3,4,3,4,2,5,5,8,9,7]
# formatList = list(set(orgList))
# print(formatList)

#6.求斐波那契数列 1 2 3 5 8 13 ……

#7.求10000以内的质数
primeNum =2
for i in range(10000):
    if i % 2 !=0:
        print(i)
        primeNum +=1