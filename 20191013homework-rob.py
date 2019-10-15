__author__ = 'Sunky'
#  -*-coding:utf8 -*-
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
#
class Rob():
    def __init__(self,bullet):
        self.bullet=bullet
    def addBullet(self,num1):
         print('士兵瑞恩有一把AK47抢，原有子弹为：',self.bullet,'添加子弹为：',num1,'个，剩余子弹为：',self.bullet+num1)
         self.bullet= self.bullet+ num1
    def launchBullet(self,num):
         print('士兵瑞恩有一把AK47抢，原有子弹为：', self.bullet, '发射子弹：', num, '个，剩余子弹为', self.bullet-num)
         self.bullet=self.bullet -num

rob =Rob(20)
rob.addBullet(2)
rob.launchBullet(1)