# def int_demo():
#     aint = 1
#     print(aint)
#
#
# def add(aint, bint):
#     print(aint)
#     print(bint)
#     return aint + bint

#
# if __name__ == '__main__':
#     # int_demo()
#     # 提取变量
#     add1 = add(1, 2)
#     print(add1)
#     pass


# 声明一个 int_demo 方法
def int_demo():
    # 声明 aa 方法 并赋值 6
    aa = 6
    # 打印aa 的值
    print(aa)

# #ctrl+k commit代码
# # 声明一个sub 方法 参数有两个aa，bb
# def sub(aa, bb):
#     # 打印aa参数
#     print(aa)
#     # 打印bb参数
#     print(bb)
#     # 返回aa-bb
#     return aa * bb
#
#
# # 声明一个 int_demo 方法
# def int_demo():
#     # 声明 aa 方法 并赋值 6
#     aa = 0.6
#     # 打印aa 的值
#     print(type(aa))
#
#
#
# if __name__ == '__main__':
#     #sub1 =(0.6)
#     int_demo()
#     #print(sub1)
#     pass
#
#

# #
# # if __name__ == '__main__':
# #     # 删除方法 list.pop()
# #     print(blist.pop(4))
# #     # pop()带参数
# #     print(blist)
# #     # print(len(blist))
# #
# def pop_demo(alist):
#     alist.pop(3)
#     print(alist)
# if __name__ == '__main__':
#     alist = [1,2,3,4,5,6,7,8,9,0]
#     pop_demo(alist)
#     pass
#
#
#
# def int_demo(aint,bint):
#     print(aint)
#     print(bint)
#     return aint + bint
#
#
#
#
#
#
#
# # 局部变量
# if __name__ == '__main__':
#     # alist = [1,2,3,4,5,6,7,8,9]
#     # print(alist)
#
#     pass
# # 全局变量
blist = [1,2,3,4,5,6,7,8,9,0]

# 将列表排序的方法
def orderby_demo():
    print('调用正序的方法')
    sort_demo()
    print('调用倒叙的方法')
    reverse_demo()
    pass
# 正序方法
def sort_demo():
    blist.sort()
    print(blist)
# 倒叙方法
def reverse_demo():
    blist.reverse()
    print(blist)
if __name__ == '__main__':
    orderby_demo()


def int_demo(alist):
        print(alist)


if __name__ == '__main__':
        alist = [7, 8, 9, 5, 4, 6, 1, 2, 3]
        print(alist[-1])
        print(alist[-2])
        print(alist[-3])
        print(alist[:6])
        pass



