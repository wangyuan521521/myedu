def int_demo():
    aint = 1
    print(aint)


def add(aint, bint):
    print(aint)
    print(bint)
    return aint + bint


if __name__ == '__main__':
    # int_demo()
    # 提取变量
    add1 = add(1, 2)
    print(add1)
    pass


# 声明一个 int_demo 方法
def int_demo():
    # 声明 aa 方法 并赋值 6
    aa = 6
    # 打印aa 的值
    print(aa)


# 声明一个sub 方法 参数有两个aa，bb
def sub(aa, bb):
    # 打印aa参数
    print(aa)
    # 打印bb参数
    print(bb)
    # 返回aa-bb
    return aa * bb


# 声明一个 int_demo 方法
def int_demo():
    # 声明 aa 方法 并赋值 6
    aa = 0.6
    # 打印aa 的值
    print(type(aa))



if __name__ == '__main__':
    #sub1 =(0.6)
    int_demo()
    #print(sub1)
    pass
