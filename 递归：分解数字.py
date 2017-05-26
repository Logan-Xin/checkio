'''
Created on 2015年12月16日

@author: Enos
'''
#coding=UTF-8
result = []
def get_digits(n):

    if n > 0:
        result.insert(0,n%10)
        get_digits(n//10)
    
get_digits(13254)
print(result)
        
    