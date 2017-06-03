'''
Created on 2015年8月18日

@author: Enos
'''
#coding=UTF-8

print('------我的第一个程序---------')
temp = input("不妨猜一下哥现在心里想的是哪个数字：")
guess = int(temp)
if guess == 8:
    print("卧槽，你是哥肚子里的蛔虫啊！")
    print("猜中了，也没奖~~O(∩_∩)O哈哈~")
else:
    print("猜错了，你真笨！")
print("游戏结束！")
