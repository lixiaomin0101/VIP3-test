__author__ = 'Sunky'
#  -*-coding:utf8 -*-
#小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤

class Person():
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def  xweight(self):
        print(self.name+'体重是'+self.weight+'公斤')

a = Person('小明','75.0')
a.xweight()

class Motion(Person):
    def run(self):
        self.weight = int(input('请输入小明体重：'))
        runing =int(input('请输入跑的公里数：'))
        if runing>0:
           self.weight=self.weight -1
           print(self.name+'跑步：',runing,'公里。体重为:',self.weight)
        eat = int(input("请输入吃的东西："))
        if eat>0:
            self.weight=self.weight +1

            print(self.name+'吃馒头',eat,'个。体重为', self.weight)
b =Motion('张三',68)
b.run()











