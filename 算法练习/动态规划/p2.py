#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 钢条切割问题自顶向下，带备忘(仅返回收益)
# 原理：Rn = max(Pi+R(n-1))

def MEMOIZED_CUT_ROD(price,n):
    result = [-float('inf') for x in range(n+1)]
    return MEMOIZED_CUT_ROD_AUX(price,n,result)
    
def MEMOIZED_CUT_ROD_AUX(price,n,result):
    if result[n] >= 0:
        return result[n]
    if n == 0:
        cResult = 0
    else:
        cResult = -float('inf')
        for i in range(1,n+1):
            cResult = max(cResult, price[i]+MEMOIZED_CUT_ROD_AUX(price,n-i,result))
    result[n] = cResult
    return cResult


if __name__ == '__main__':
    # price = [0,1,5,8,9,10,17,17,20,24,30]
    # n = 10
    price = [0,1,5,8,9]
    n = 4
    result = MEMOIZED_CUT_ROD(price,n)
    print('价格表:',price)
    print('最大收益',result)