#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 算法6.6 QUICKSORT 快速排序
# 改进：RANDOMIZED_QUICKSORT 快速排序的随机化版本

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
    

def RANDOMIZED_QUICKSORT(myList,low,high):
    if low < high:
        divisionIndex = RANDOMIZED_SPLIT(myList,low,high)
        RANDOMIZED_QUICKSORT(myList, low, divisionIndex)
        RANDOMIZED_QUICKSORT(myList, divisionIndex+1, high)
        
if __name__ == '__main__':
    myList = [randint(1,100) for i in range(10)]
    print('排序前：',myList)
    RANDOMIZED_QUICKSORT(myList,0,len(myList)-1)
    print('排序后：',myList)  