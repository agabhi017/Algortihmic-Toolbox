import os
import numpy as np

def ad_optimize(profit, clicks, n) :
    value = 0
    profit2 = sorted(profit)[::-1]
    clicks2 = sorted(clicks)[::-1]
    for i in range(0, n) :
        value += profit2[i] * clicks2[i]
        
    return value

if __name__ == "__main__" :
    n = int(input())
    profit = list(map(int, input().split()))
    n_clicks = list(map(int, input().split()))
    print(ad_optimize(profit, n_clicks, n))
      