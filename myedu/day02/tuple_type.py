# 元组类型 与 list 一样 的访问方式；元组中的元素不可以被更改
# 元组只可以被读取；只读

# 声明一个元组类型的全局变量
atuple = (1,6,58,4,5,74,46)
if __name__ == '__main__':
    # 元组不可以被修改
    print(atuple[3])
    atuple[3] = 1