import os
import numpy as np

def money_change_1(n) :
    change = np.zeros(n + 1, dtype = int)
    for i in range(n + 1) :
        change_1 = -1
        change_3 = -1
        change_4 = -1
        
        if i - 1 >= 0:
            change_1 = change[i - 1] + 1
        if i - 3 >= 0:
            change_3 = change[i - 3] + 1
        if i - 4 >= 0:
            change_4 = change[i - 4] + 1
        
        lst = [change_1, change_3, change_4]
        lst = [x for x in lst if x != -1]
        if len(lst) == 0 :
            change[i] = 0
        else :
            change[i] = min(lst)
    return change[n]

def money_change_2(n) :
    change = np.zeros(n + 1, dtype = int) 
    for i in range(n + 1) :
        lst = [i - 1, i - 3, i - 4]
        lst = [x for x in lst if x >= 0]
        if len(lst) == 0 :
            change[i] = 0
        else :
            change[i] = min([change[x] for x in lst]) + 1
    return change[n]

if __name__ == "__main__" :
    n = int(input()) 
    print(money_change_2(n))