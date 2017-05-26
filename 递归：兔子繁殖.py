'''
Created on 2015年12月15日

@author: Enos
'''
#coding=UTF-8

'''
假设兔子出生后2个月就可以生一对小兔子，那么20个月后，总共有多少对小兔子？
'''

def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return F(n-1)+F(n-2)
   
   
print(F(35))