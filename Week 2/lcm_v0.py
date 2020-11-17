import os
import numpy as np

def lcm_naive(a,b):
    lcm = a * b
    for i in range(max(a,b), a*b) :
        if i % a == 0 and i % b == 0:
            lcm = i
            break
            
    return lcm

def gcd_euclid(a,b) :
    if a == 0 or b == 0 :
        return a + b
    
    rem = max(a,b) % min(a,b)
    return gcd_euclid(min(a,b), rem)

def lcm_gcd_euclid(a, b):
    gcd = gcd_euclid(a,b)
    rem1 = int(a / gcd)
    rem2 = int(b / gcd)
    return gcd * rem1 * rem2
        
if __name__ == "__main__" :
    a,b = map(int, input().split())
    print(lcm_gcd_euclid(a,b))