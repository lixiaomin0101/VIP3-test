def fun1():
    print('fun1')


def fun2():
    print('fun2')

print('mymodule文件的name的属性', __name__)


if __name__ == '__main__':
    fun1()
    fun2()