import os
import numpy as np

def fib_array(n) :
    arr = list(np.zeros(n + 1))
    
    arr[0] = 0
    if n > 0 :
        arr[1] = 1
    
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    
    return arr[n]

def fib_sum_squared(n) :
    rem1 = n % 60
    rem2 = (n + 1) % 60
    return (fib_array(rem1) * fib_array(rem2)) % 10

if __name__ == "__main__" :
    n = int(input())
    print(fib_sum_squared(n))