'''
Created on 2015年12月15日

@author: Enos
'''
#coding=UTF-8

def Dec2Bin(dec):
    result = ''
    
    if dec:
       result = Dec2Bin(dec//2)
       return result + str(dec%2)
    else:
       return result
   
   
print(Dec2Bin(62))
    