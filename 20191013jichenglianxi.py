#定义一个Teacher类，继承Person类，拥有自身的属性工号：gh，自身的方法：teach教课（课程）；
#1、实现gh为xx的老师，教xx课 名字，课程，工号，地点，工资
#2、实现gh为xx老师，在xx上班，一月工资xx
#3、名字是xx，工号为xx的老师，吃饭

class Person():
    def __init__(self,name,gh,didian,kecheng,gz):
        self.name=name
        self.gh=gh
        self.kecheng=kecheng
        self.gz=gz
        self.didian=didian


class Teacher(Person):
    def teach(self):
        print('名字为：'+self.name,'工号为:'+self.gh +'的老师,在'+ self.didian +'教'+self.kecheng)
    def teach1(self):
        print('工号为：'+self.gh+'老师,在'+self.didian+'上班，'+'工资为：'+self.gz)
    def teach2(self):
        print('名字是'+self.name +'。工号为'+self.gh+'的老师，吃饭')

a =Teacher('王帅','001','希望中学','英语','6000')
a.teach()
a.teach1()
a.teach2()
