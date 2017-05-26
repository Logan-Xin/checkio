'''
Created on 2015年12月15日

@author: Enos
'''
#coding=UTF-8
#由递归实现求正整数的阶乘。
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input('请输入一个正整数：'))

result = factorial(number)
print("%d 的阶乘是：%d" %(number,result))