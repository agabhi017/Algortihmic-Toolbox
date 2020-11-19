import os
import numpy as np

def knapsack_basic(W, weights, value_unit) :
    value = 0
    while W > 0 and len(weights) > 0:
        index = np.argmax(value_unit)
        weight = min(weights[index], W)
        value += value_unit[index] * weight
        W -= weight
        weights[index] -= weight
        if weights[index] == 0 :
            weights = np.delete(weights, index)
            value_unit = np.delete(value_unit, index)

    return np.round(value, 4)

if __name__ == "__main__" :
    n, W = map(int, input().split())
    weights = np.zeros(n)
    value_unit = np.zeros(n)
    for i in range (0, n) :
        v, w = map(int, input().split())
        weights[i] = w
        value_unit[i] = v/w
        
    print(knapsack_basic(W, weights, value_unit))