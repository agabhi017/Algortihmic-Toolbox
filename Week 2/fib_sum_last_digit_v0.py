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

def fib_sum(n):
    
    if n <= 1:
        return fib_array(n)
    
    return fib_sum(n - 1) + fib_sum(n - 2) + 1

if __name__ == "__main__" :
    n = int(input())
    print(fib_sum(n))