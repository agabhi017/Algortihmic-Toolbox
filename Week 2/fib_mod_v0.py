import os 
import numpy as np
 

def fib_array(n) :
    arr = list(np.zeros(n + 1))
    arr[0] = 0
    if n > 0 :
        arr[1] = 1
    
    for i in range(2, n + 1) :
        arr[i] = int(arr[i-1]) + int(arr[i-2])
    return arr[n]

def pisano_period(m) :
    period = []
    period.append(0)
    period.append(1)
    
    for i in range(2, m * m + 1) :
        period.append(fib_array(i) % m)
        
        if period[i - 1] == 0 and period[i] == 1:
            break
    return len(period) - 2

def fib_mod_m(n, m):
    period = pisano_period(m)
    rem = n % period
    return fib_array(rem) % m

if __name__ == "__main__" :
    n,m = map(int, input().split())
    print(fib_mod_m(n ,m))