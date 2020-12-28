import numpy as np

def check_knapsack(items) :
    w = sum(items)
    n_items = len(items) 
    array = np.zeros((n_items + 1, w + 1), dtype = int)
    for i in range(1, n_items + 1) :
        for j in range(1, w + 1) :
            if items[i - 1] <= j :
                array[i][j] = max(array[i - 1][j - items[i - 1]] + items[i - 1], array[i - 1][j])
            else :
                array[i][j] = array[i - 1][j]
    if w % 3 != 0 :
        return 0
    elif array[n_items][int(w/3)] == int(w/3) and array[n_items][int(2 * w/3)] == int(2*w/3):
        return 1
    else :
        return 0


if __name__ == "__main__" :
    n = int(input())
    items = list(map(int, input().split()))
    print(check_knapsack(items))