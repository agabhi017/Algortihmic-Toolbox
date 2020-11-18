import os
import numpy as np


def change_greedy(amount) :
    changes = 0
    
    while amount > 0 :
        if amount >= 10 :
            amount -= 10
            changes += 1
        elif amount >= 5 and amount < 10 :
            amount -= 5
            changes += 1
        else:
            amount -= 1
            changes += 1
    
    return changes

def change_simple(amount) :
    change_10 = int(np.floor(amount/10))
    change_5 = int(np.floor((amount % 10) /5))
    change_1 = int((amount % 10) % 5)
    return change_10 + change_5 + change_1

if __name__ == "__main__" :
    n = int(input())
    print(change_simple(n))