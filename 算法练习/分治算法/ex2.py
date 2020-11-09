#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 算法6.2 BINARYSEARCHREC 找到元素x的逻辑下标

from random import randint

def  BINARYSEARCHREC(myList,x):
    def binarySearchRec(low,high):
        if low > high:
            return 0
        else:
            mid = (low+high)//2
            if x == myList[mid]:
                return mid+1
                #返回逻辑下标
            elif x < myList[mid]:
                return binarySearchRec(low,mid-1)
            else:
                return binarySearchRec(mid+1,high)

    return binarySearchRec(0, len(myList)-1)

if __name__ == '__main__':
    myList = [randint(1,100) for i in range(10)]
    myList.sort()
    print(myList)
    for i in range(5):
        if i == 3:
            x = randint(-10,0)
        elif i == 4:
            x = randint(101,110)
        else:
            x = myList[randint(0,9)]

        print('搜索',x)
        resultIndex = BINARYSEARCHREC(myList,x)
        if resultIndex != 0:
            print('{}的逻辑下标是{}'.format(x,resultIndex))
        else:
            print('序列中没有{}元素，返回下标0'.format(x))