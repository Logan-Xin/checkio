'''
Created on 2015年12月15日

@author: Enos
'''
#coding=UTF-8
#由for循环实现指定正整数的阶乘。
def factorial(n):
    result = n
    for i in range (1,n):
        result *= i
    
    return result

number = int(input('请输入一个正整数：'))

result = factorial(number)
print("%d 的阶乘是：%d" %(number,result))

