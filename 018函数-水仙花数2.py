'''
Created on 2015年10月28日

@author: Enos
'''
#coding=UTF-8

def main():
    for i in range(100,1000):
        a = i%10
        b = (int(i/10))%10
        c = int(i/100)
        if i == a**3+b**3+c**3:
            print (i,end='\t')
print("所有水仙花数分别是：",end='')

main()