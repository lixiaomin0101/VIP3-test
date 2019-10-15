__author__ = 'Sunky'
#  -*-coding:utf8 -*-
#1）.房子有户型，总面积和家具名称列表,新房子没有任何的家具
#2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
#3）.将以上三件家具添加到房子中
#4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

class Furniture():
    def __init__(self,aparment,totalarea):
        self.aparment=aparment
        self.totalarea=totalarea

    def jiaju(self):
        bed = 4
        yigui = 2
        canzhuo =1.5
        jiaju1 = bed + yigui + canzhuo
        surplusarea = self.totalarea-jiaju1
        print('户型为：',self.aparment,'总面积为：',self.totalarea,'。剩余面积为：',surplusarea)
    def jiajuname(self,bed,yigui,canzhuo):
        print('家具名称列表：'+bed,yigui,canzhuo)
a =Furniture('南北通透', 90)
a.jiaju()
a.jiajuname('床','衣柜','餐桌')
