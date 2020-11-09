#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 算法6.5 SPLIT 划分算法

from random import randint

def SPLIT(myList):
    def split(low,high):
        i = low
        x = myList[low]
        for j in range(low+1, high+1):
            if myList[j] <= x:
                i += 1
                if i != j:
                    myList[i],myList[j] = myList[j],myList[i]
        myList[low],myList[i] = myList[i],myList[low]
        w = i #返回位置下标
        return w
    
    return split(0,len(myList)-1)
    
if __name__ == '__main__':
    myList = [randint(1,100) for i in range(10)]
    print('划分前：',myList)
    w = SPLIT(myList)
    print('划分后：',myList)
    print('主元位置下标为：',w)
    
                