#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 钢条切割问题自底向上(仅返回收益)
# 原理：Rn = max(Pi+R(n-1))

def BOTTOM_UP_CUT_ROD(price,n):
    result = [-float('-inf') for x in range(n+1)]
    result[0] = 0
    for j in range(1,n+1):
        cResult = -float('inf')
        for i in range(1,j+1):
            cResult = max(cResult,price[i]+result[j-i])
        result[j] = cResult
    return result[n]

if __name__ == '__main__':
    # price = [0,1,5,8,9,10,17,17,20,24,30]
    # n = 10
    price = [0,1,5,8,9]
    n = 4
    result = BOTTOM_UP_CUT_ROD(price,n)
    print('价格表:',price)
    print('最大收益',result)