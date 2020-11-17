import os
#os.chdir('E:\Coursera\Algo Toolbox\Assignment')

import numpy as np

def fib_recurisve(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recusrive(n-2)

def fib_array(n):
    arr = list(np.zeros(n + 1, dtype = np.int64))
    arr[0] = 0
    if n > 0: 
        arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = (int(arr[i - 1]) % 10 + int(arr[i - 2]) % 10) % 10
    
    return arr[n]

def last_digit(n) :
    return fib_array(n) % 10

if __name__ == "__main__":
    n = int(input())
    print(last_digit(n))