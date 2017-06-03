'''
Created on 2015年12月15日

@author: Enos
'''
#coding=UTF-8

'''
假设兔子出生后2个月就可以生一对小兔子，那么20个月后，总共有多少对小兔子？
'''

def F(n):
    n1=1
    n2=1
    n3=1
    
    if n <1:
        print('输入有误！')
        return -1
    while (n-2)>0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
          
    return n3


print(F(20))

