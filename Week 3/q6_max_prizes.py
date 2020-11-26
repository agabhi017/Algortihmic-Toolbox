import os
import numpy as np

def kids(n) :
    max_k = int(np.floor(np.sqrt(n * 2)))
    while max_k * (max_k + 1) / 2 > n:
        max_k -=1
    candies = []
    for i in range(max_k - 1):
        candies.append(i + 1)
    
    last_candy = n - sum(candies)
    candies.append(last_candy)
    return candies

if __name__ == "__main__" :
    n = int(input())
    candies = kids(n)
    print(len(candies))
    print(*candies, sep = ' ')