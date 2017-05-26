'''
Created on 2015年12月8日

@author: Enos
'''
#coding=UTF-8


def discounts(price,rate):
    final_price = price * rate
    return final_price

old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price,rate)
print('打折后的价格：',new_price)
