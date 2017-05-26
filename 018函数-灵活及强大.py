'''
Created on 2015年10月28日

@author: Enos
'''
#coding=UTF-8

def MyFirstFuction(name):
    '函数定义过程的name是叫做形参'
    #因为Ta只是一个形式，表示占据一个参数位置
    print('传递进来的'+ name + '叫实参，因为他是具体的参数值')
    
MyFirstFuction('小龙哥')

MyFirstFuction.__doc__


help(MyFirstFuction)


def MyFun(x):
    return x ** 3
y = 3
print(MyFun(y))


def mFun(*param,base=3):
    result = 0
    for each in param:
        result += each
    
    result *= base
    
    print('结果是：',result)
    
mFun(1,2,3,4,5,base=5)

mFun(1,2,3,4,5)











