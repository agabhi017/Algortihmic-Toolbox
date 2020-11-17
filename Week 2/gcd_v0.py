import os
import numpy as np

#os.chdir('E:\Coursera\Algo Toolbox\Assignment')

def gcd_naive(a, b):
    gcd = 1
    if a == 0 or b == 0:
        return (a != 0)*a + (b != 0)*b
    
    for i in range(1, min(a,b) + 1):
        if a % i == 0 and b % i == 0 and i > gcd:
            gcd = i
    
    return gcd

def gcd_euclid(a,b) :
    if a == 0 or b == 0 :
        return (a != 0)*a + (b != 0)*b
    
    rem = max(a,b) % min(a,b)
    return gcd_euclid(min(a,b), rem)

if __name__ == "__main__" :
    a,b = map(int, input().split())
    print(gcd_euclid(a,b))