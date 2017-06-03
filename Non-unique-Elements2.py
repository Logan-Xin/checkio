'''
Created on 2017年5月26日

@author: Logan
'''




def checkio(data):
    return (a for a in data if data.count(a) > 1)





data = input("请输入一个数组（0 < |X| < 1000）：")
print([checkio(data)])