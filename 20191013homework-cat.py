__author__ = 'Sunky'
#  -*-coding:utf8 -*-
#打印小猫爱吃鱼，小猫要喝水
class Animal():
    def __init__(self,name,food,drink):
        self.name=name
        self.food=food
        self.drink=drink
    def cat(self):
        print(self.name+'爱吃'+self.food+','+self.name+'爱喝'+self.drink)
a =Animal('小猫','鱼','水')
a.cat()