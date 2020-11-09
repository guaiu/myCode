#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 算法6.3 MERGESORT 非降序排序序列

from random import randint

def  MERGESORT(myList):
    def MERGE(low,mid,high):
        resultList = []
        iLeft = low
        iRight = mid+1
        while iLeft <= mid and iRight <= high:
            if myList[iLeft] < myList[iRight]:
                resultList.append(myList[iLeft])
                iLeft += 1
            else:
                resultList.append(myList[iRight])
                iRight += 1
        else:
            if iLeft <= mid:
                resultList.extend(myList[iLeft:mid+1])
            else:
                resultList.extend(myList[iRight:high+1])
        myList[low:high+1] = resultList[:]

    def mergeSort(low,high):
        if low < high:
            mid = (low+high)//2
            mergeSort(low, mid)
            mergeSort(mid+1, high)
            MERGE(low,mid,high)
    
    mergeSort(0, len(myList)-1)
            
if __name__ == '__main__':
    myList = [randint(1,100) for i in range(10)]
    print('排序前：',myList)
    MERGESORT(myList)
    print('排序后：',myList)