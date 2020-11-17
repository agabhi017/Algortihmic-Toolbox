import os
import numpy as np

def fib_array(n) :
    array = list(np.zeros(n + 1))
    
    array[0] = 0
    if n > 0 :
        array[1] = 1
    
    for i in range(2, n + 1):
        array[i] = array[i - 1] + array[i - 2]
    
    return array[n]

def fib_sum_recurse(n):
    
    if n <= 1:
        return fib_array(n)
    
    return fib_sum_recurse(n - 1) + fib_sum_recurse(n - 2) + 1

'''
(F0 + F1 + F2 + .... + Fn) % 10 = F0 % 10 + F1 % 10 + .... + Fn % 10

Using pisano period, Fn % 10 = F(n % 60) as 60 is the pisano period of 10
'''

def fib_sum_pisano(n) :
    rem1 = n % 60
    rem2 = (n + 1) % 60
    return (fib_array(rem1) + fib_array(rem2) - 1) % 10

if __name__ == "__main__" :
    n = int(input())
    print(fib_sum_pisano(n))