#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 算法6.4 找第i小元素 快速排序原理

from random import randint

def RANDOMIZED_SPLIT(myList,low,high):
    def split():
        i = low
        x = myList[low]
        for j in range(low+1, high+1):
            if myList[j] < x:
                i += 1
                if i != j:
                    myList[i],myList[j] = myList[j],myList[i]
        myList[low],myList[i] = myList[i],myList[low]
        divisionIndex = i
        return divisionIndex
        
    randomIndex = randint(low,high)
    if randomIndex != low:
        myList[randomIndex],myList[low] = myList[low],myList[randomIndex]
    return split()

def RANDOMIZED_SELECT(myList,low,high,i):
    if low == high:
        return myList[low]
        
    splitIndex = RANDOMIZED_SPLIT(myList,low,high)
    key = splitIndex-low+1
    if i == key:
        return myList[splitIndex]
    elif i < key:
        return RANDOMIZED_SELECT(myList,low,splitIndex-1,i)
    else:
        return RANDOMIZED_SELECT(myList,splitIndex+1,high,i-key)
        
if __name__ == '__main__':
    myList = [randint(1,100) for i in range(10)]
    i = randint(1,10)
    print(myList)
    print('寻找第{}小的元素'.format(i))
    
    result = RANDOMIZED_SELECT(myList[:],0,len(myList)-1,i)
    print('第{}小的元素是{}'.format(i,result))
    