'''
Created on 2017年5月26日

@author: Logan
'''

#Your optional code here
#You can import some modules or create additional functions


def checkio(data):
    result = []
    #init empty list
    for item in data:
        if data.count(item) >1:
            result.append(item)
            #add the current item to the new list you initialized before
    # return the list 
    
    #replace this for solution
    return result

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


data = input("请输入一个数组（0 < |X| < 1000）：")

print(checkio(data))
