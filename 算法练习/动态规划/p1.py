#!/usr/bin/env python
# -*- coding: utf-8 -*-

# p1 钢条切割问题自顶向下递归实现(仅返回收益)
# 原理：Rn = max(Pi+R(n-1))


def CUT_ROD(price,n):
    if n == 0:
        return 0
    result = -float('inf')
    for i in range(1,n+1):
        result = max(result,price[i]+CUT_ROD(price,n-i))
    return result


if __name__ == '__main__':
    # price = [0,1,5,8,9,10,17,17,20,24,30]
    # n = 10
    price = [0,1,5,8,9]
    n = 4
    result = CUT_ROD(price,n)
    print('价格表:',price)
    print('最大收益',result)