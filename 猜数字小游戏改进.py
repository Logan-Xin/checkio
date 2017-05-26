'''
Created on 2015年10月19日

@author: Enos
'''
#coding=UTF-8

#改进我们的小游戏：当用户输入错误类型的时候，
#及时提醒用户重新输入，防止程序崩溃。

import random
times = 3
secret = random.randint(1,10)
print('------------------猜数字------------')
guess = 0
print("不妨猜一下我现在心里想的数字是哪个数字：" ,end=" ")
while (guess != secret) and (times > 0):
    temp = input()
    while not temp.isdigit():
        temp = input("抱歉，您的输入有误，请输入一个整数：")
    guess = int(temp)
    times = times - 1 #用户每输入一次，可用机会就-1
    if guess == secret:
        print("我擦，你是我肚里的蛔虫吗？！")
        print("哼，猜中了也没奖励！")
    else:
        if guess > secret:
            print("哥，大了，大了~~~~")
        else:
            print("嘿，小了，小了~~~")
        if times > 0:
            print("再试一次吧：", end = " ")
        else:
            print("机会用光咯%>_<%")
print("游戏结束，不玩啦O(∩_∩)O~")
        