#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 钢条切割问题自底向上 返回收益和最优解
# 原理：Rn = max(Pi+R(n-1))

def EXTENDED_BOTTOM_UP_CUT_ROD(price,n):
    result = [-float('-inf') for x in range(n+1)]
    result[0] = 0
    solution = [x for x in range(n+1)]
    
    for j in range(1,n+1):
        cResult = -float('inf')
        for i in range(1,j+1):
            if cResult < price[i]+result[j-i]:
                cResult = price[i]+result[j-i]
                solution[j] = i
        result[j] = cResult
    return (result,solution)
    
def PRINT_CUT_ROD_SOLUTION(price,n):
    optimalSolution = EXTENDED_BOTTOM_UP_CUT_ROD(price,n)
    #optimalSolution = (result,solution)
    
    print('最大收益',optimalSolution[0][n])
    while n > 0:
        print(optimalSolution[1][n])
        n = n-optimalSolution[1][n]
        
        
if __name__ == '__main__':
    # price = [0,1,5,8,9,10,17,17,20,24,30]
    # n = 10
    price = [0,1,5,8,9]
    n = 4
    print('价格表:',price)
    PRINT_CUT_ROD_SOLUTION(price,n)