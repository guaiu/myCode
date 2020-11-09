#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 算法6.1 MINMAX 同时找出序列中的最大值和最小值(的位置下标)
# 注：myList[1...2^n]， n={1,2,3...}

from random import randint

def MINMAX(myList):
    def minmax(low,high):
        if high-low == 1:   
            if myList[low] < myList[high]:
                return (low,high)
            else:
                return (high,low)
        else:
            mid = (low+high)//2
            resultLeft = minmax(low,mid)
            resultRight = minmax(mid+1,high)
            minIndex = min(resultLeft[0], resultRight[0])
            maxIndex = max(resultLeft[1], resultRight[1])
            return (minIndex, maxIndex)
            
    return minmax(0, len(myList)-1)
    
if __name__ == '__main__':
    myList = [randint(1,100) for i in range(8)]
    result = MINMAX(myList)
    print(myList)
    print('最大元素为{}，最小元素为{}'.format(myList[result[0]], myList[result[1]]))