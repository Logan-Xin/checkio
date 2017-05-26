'''
Created on 2015年12月10日

@author: Enos
'''
#coding=UTF-8


print(list(filter(lambda x:x %2,range(10))))

def outside():
    var = 5
    def inside():
        nonlocal var
        
        var *= var
        print(var)
        
    inside()
    
outside()

